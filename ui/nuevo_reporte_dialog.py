# 🐍 Código Pythonizado por Flashy Meduza 🐍

from PyQt5.QtWidgets import QDialog, QFormLayout, QLineEdit, QComboBox, QSpinBox, QPushButton, QFileDialog, QDateTimeEdit
from PyQt5.QtCore import QDateTime

class NuevoReporteDialog(QDialog):
    def __init__(self, parent):
        super().__init__(parent)
        self.setWindowTitle("Nuevo Reporte")
        self.setMinimumWidth(400)
        self.file_path = ""

        layout = QFormLayout()
        self.nombre = QLineEdit()
        self.taller = QLineEdit()
        self.descripcion = QLineEdit()

        self.categoria = QComboBox()
        self.categoria.addItems(["Admin Cultural", "Gestor Cultural", "Coord Cultural", "Detonador Cultural", "Activador cultural"])

        self.cao = QComboBox()
        self.cao.addItems(["PUEBLOS", "AJUSCO MEDIO", "MESA HORNOS", "TIEMPO NUEVO"])

        self.mes = QComboBox()
        self.mes.addItems(["Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio", "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre"])

        self.horas = QSpinBox()
        self.horas.setRange(0, 1000)

        self.personas = QSpinBox()
        self.personas.setRange(0, 1000)

        self.fecha_entrega = QDateTimeEdit()
        self.fecha_entrega.setCalendarPopup(True)
        self.fecha_entrega.setDateTime(QDateTime.currentDateTime())

        self.archivo_btn = QPushButton("Seleccionar Archivo")
        self.archivo_btn.clicked.connect(self.select_file)

        layout.addRow("Nombre:", self.nombre)
        layout.addRow("Taller:", self.taller)
        layout.addRow("Descripción:", self.descripcion)
        layout.addRow("Categoría:", self.categoria)
        layout.addRow("CAO:", self.cao)
        layout.addRow("Mes:", self.mes)
        layout.addRow("Horas:", self.horas)
        layout.addRow("Personas:", self.personas)
        layout.addRow("Archivo:", self.archivo_btn)
        layout.addRow("Fecha de Entrega:", self.fecha_entrega)

        self.save_btn = QPushButton("Guardar")
        self.save_btn.clicked.connect(self.accept)
        layout.addRow(self.save_btn)

        self.setLayout(layout)

    def select_file(self):
        path, _ = QFileDialog.getOpenFileName(self, "Seleccionar archivo")
        if path:
            self.file_path = path
