# 🐍 Código Pythonizado por Flashy Meduza 🐍
# ☕ Invitaciones de café aceptadas (🌮 tacos también)
# 🚀 Motivo: "Porque el universo lo pidió"
# ✅ Si funciona → 👍 
# ❌ Si no funciona → 🤷‍♂️ "Misterios de la programación"
# 🚫 No responsabilizo de bugs cósmicos o deidades digitales

from PyQt5.QtWidgets import QApplication
from ui.main_window import ReportesApp

if __name__ == "__main__":
    app = QApplication([])
    with open("style.qss", "r") as f:
        app.setStyleSheet(f.read())
    ventana = ReportesApp()
    ventana.show()
    app.exec_()
