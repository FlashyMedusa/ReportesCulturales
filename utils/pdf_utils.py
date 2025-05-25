import os
from reportlab.lib.pagesizes import LETTER
from reportlab.pdfgen import canvas

def generar_pdf_info(datos, output_path):
    c = canvas.Canvas(output_path, pagesize=LETTER)
    c.setFont("Helvetica", 12)
    y = 750

    info = [
        f"📄 Reporte: {datos[1]}",
        f"👤 Persona: {datos[0]}",
        f"📝 Descripción: {datos[2]}",
        f"🗂 Categoría: {datos[3]}",
        f"📍 CAO: {datos[4]}",
        f"📅 Mes: {datos[5]}",
        f"🕒 Horas Programadas: {datos[6]}",
        f"👥 Personas Inscritas: {datos[7]}",
        f"📆 Fecha Entrega: {datos[8]}",
    ]

    for linea in info:
        c.drawString(50, y, linea)
        y -= 25

    c.save()
