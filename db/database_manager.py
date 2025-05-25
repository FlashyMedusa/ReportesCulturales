# 🐍 Código Pythonizado por Flashy Meduza 🐍

import sqlite3
from pathlib import Path

DB_PATH = Path("database/reportes.db")

def setup_db():
    DB_PATH.parent.mkdir(exist_ok=True)
    with sqlite3.connect(DB_PATH) as conn:
        conn.execute("""
            CREATE TABLE IF NOT EXISTS reportes (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nombrePersona TEXT NOT NULL,
                taller TEXT NOT NULL,
                descripcion TEXT,
                categoria TEXT NOT NULL,
                cao TEXT NOT NULL,
                mes_reporte TEXT NOT NULL,
                horas_programadas INTEGER NOT NULL,
                personas_inscritas INTEGER NOT NULL,
                fecha_entrega TEXT NOT NULL,
                ruta_archivo TEXT NOT NULL UNIQUE
            )
        """)

def insert_reporte(data, ruta_archivo):
    with sqlite3.connect(DB_PATH) as conn:
        conn.execute("""
            INSERT INTO reportes (nombrePersona, taller, descripcion, categoria, cao, mes_reporte,
            horas_programadas, personas_inscritas, fecha_entrega, ruta_archivo)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)""",
            (data.nombre.text(), data.taller.text(), data.descripcion.text(), data.categoria.currentText(),
             data.cao.currentText(), data.mes.currentText(), data.horas.value(), data.personas.value(),
             data.fecha_entrega.dateTime().toString("yyyy-MM-dd HH:mm:ss"), ruta_archivo))

def delete_reporte(rid):
    with sqlite3.connect(DB_PATH) as conn:
        conn.execute("DELETE FROM reportes WHERE id = ?", (rid,))

def get_ruta_archivo(rid):
    with sqlite3.connect(DB_PATH) as conn:
        row = conn.execute("SELECT ruta_archivo FROM reportes WHERE id = ?", (rid,)).fetchone()
        return row[0] if row else None

def get_filtered_reportes(cat, cao, mes):
    query = "SELECT id, nombrePersona, taller, categoria, cao, mes_reporte, fecha_entrega FROM reportes"
    filters = []
    params = []
    if cat != "Todas":
        filters.append("categoria = ?")
        params.append(cat)
    if cao != "Todos":
        filters.append("cao = ?")
        params.append(cao)
    if mes != "Todos":
        filters.append("mes_reporte = ?")
        params.append(mes)
    if filters:
        query += " WHERE " + " AND ".join(filters)
    with sqlite3.connect(DB_PATH) as conn:
        return conn.execute(query, params).fetchall()
