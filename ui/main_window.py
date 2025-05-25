# 🐍 Código Pythonizado por Flashy Meduza 🐍
import shutil
import sqlite3
from utils.pdf_utils import generar_pdf_info
import tempfile

from PyQt5.QtWidgets import (
    QMainWindow, QWidget, QVBoxLayout, QHBoxLayout,
    QLabel, QComboBox, QPushButton, QTableWidget, QTableWidgetItem,
    QMessageBox, QFileDialog
)
import os
from db.database_manager import setup_db, insert_reporte, delete_reporte, get_filtered_reportes, get_ruta_archivo
from utils.file_manager import safe_copy_file, delete_file
from ui.nuevo_reporte_dialog import NuevoReporteDialog

REPORTES_DIR = "assets/reportes"

class ReportesApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Gestión de Reportes Culturales")
        self.resize(1000, 700)
        setup_db()

        central = QWidget()
        layout = QVBoxLayout()
        filters = QHBoxLayout()

        self.cat_cb = QComboBox()
        self.cat_cb.addItems(["Todas", "Admin Cultural", "Gestor Cultural", "Coord Cultural", "Detonador Cultural", "Activador cultural"])
        self.cao_cb = QComboBox()
        self.cao_cb.addItems(["Todos", "PUEBLOS", "AJUSCO MEDIO", "MESA HORNOS", "TIEMPO NUEVO"])
        self.mes_cb = QComboBox()
        self.mes_cb.addItems(["Todos", "Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio", "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre"])

        for cb in (self.cat_cb, self.cao_cb, self.mes_cb):
            cb.currentTextChanged.connect(self.load_data)

        filters.addWidget(QLabel("Categoría:"))
        filters.addWidget(self.cat_cb)
        filters.addWidget(QLabel("CAO:"))
        filters.addWidget(self.cao_cb)
        filters.addWidget(QLabel("Mes:"))
        filters.addWidget(self.mes_cb)

        btns = QHBoxLayout()
        self.nuevo_btn = QPushButton("Nuevo Reporte")
        self.nuevo_btn.clicked.connect(self.nuevo_reporte)

        self.del_btn = QPushButton("Eliminar Seleccionado")
        self.del_btn.clicked.connect(self.eliminar_reporte)

        self.down_sel_btn = QPushButton("Descargar Seleccionado")
        self.down_sel_btn.clicked.connect(lambda: self.descargar_reportes(True))

        self.down_all_btn = QPushButton("Descargar Todos (Filtrados)")
        self.down_all_btn.clicked.connect(lambda: self.descargar_reportes(False))

        for b in [self.nuevo_btn, self.down_sel_btn, self.down_all_btn, self.del_btn]:
            btns.addWidget(b)

        self.table = QTableWidget(0, 7)
        self.table.setHorizontalHeaderLabels(["ID", "Persona", "Taller", "Categoría", "CAO", "Mes", "Fecha de Entrega"])
        self.table.setSelectionBehavior(self.table.SelectRows)
        self.table.setEditTriggers(self.table.NoEditTriggers)

        layout.addLayout(filters)
        layout.addLayout(btns)
        layout.addWidget(self.table)

        central.setLayout(layout)
        self.setCentralWidget(central)
        self.load_data()

    def load_data(self):
        self.table.setRowCount(0)
        cat, cao, mes = self.cat_cb.currentText(), self.cao_cb.currentText(), self.mes_cb.currentText()
        reportes = get_filtered_reportes(cat, cao, mes)
        for row in reportes:
            row_pos = self.table.rowCount()
            self.table.insertRow(row_pos)
            for i, val in enumerate(row):
                self.table.setItem(row_pos, i, QTableWidgetItem(str(val)))

    def nuevo_reporte(self):
        dlg = NuevoReporteDialog(self)
        if dlg.exec():
            if not dlg.file_path:
                QMessageBox.warning(self, "Error", "Debe seleccionar un archivo")
                return
            dest = safe_copy_file(dlg.file_path, REPORTES_DIR)
            insert_reporte(dlg, dest)
            self.load_data()

    def eliminar_reporte(self):
        rows = self.table.selectionModel().selectedRows()
        if not rows:
            QMessageBox.warning(self, "Aviso", "Seleccione un reporte")
            return
        if QMessageBox.question(self, "Confirmar", f"Eliminar {len(rows)} reporte(s)?") != QMessageBox.Yes:
            return
        for row in rows:
            rid = int(self.table.item(row.row(), 0).text())
            ruta = get_ruta_archivo(rid)
            if ruta:
                delete_file(ruta)
            delete_reporte(rid)
        self.load_data()

    def descargar_reportes(self, seleccionados=True):
        rows = self.table.selectionModel().selectedRows() if seleccionados else range(self.table.rowCount())
        if not rows:
            QMessageBox.warning(self, "Aviso", "No hay reportes para descargar")
            return

        dest_dir = QFileDialog.getExistingDirectory(self, "Seleccionar carpeta destino")
        if not dest_dir:
            return

        with sqlite3.connect("database/reportes.db") as conn:
            for row in rows:
                rid = int(self.table.item(row.row(), 0).text()) if seleccionados else int(self.table.item(row, 0).text())
                
                ruta = conn.execute("SELECT ruta_archivo FROM reportes WHERE id = ?", (rid,)).fetchone()
                if ruta and os.path.exists(ruta[0]):
                    nombre_archivo = os.path.basename(ruta[0])
                    nombre_sin_ext, ext = os.path.splitext(nombre_archivo)
                    destino_pdf = os.path.join(dest_dir, nombre_archivo)

                    # Obtener datos del reporte
                    datos = conn.execute("""
                        SELECT nombrePersona, taller, descripcion, categoria, cao, mes_reporte,
                            horas_programadas, personas_inscritas, fecha_entrega
                        FROM reportes WHERE id = ?
                    """, (rid,)).fetchone()

                    # Crear PDF con los datos
                    pdf_info_path = os.path.join(dest_dir, f"{nombre_sin_ext}_info.pdf")
                    generar_pdf_info(datos, pdf_info_path)

                    # Copiar archivo original
                    shutil.copy2(ruta[0], destino_pdf)

        QMessageBox.information(self, "Éxito", f"Se descargaron {len(rows)} archivo(s)")




