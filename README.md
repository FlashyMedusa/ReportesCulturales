# 📊 Gestión de Reportes Culturales

Aplicación de escritorio en Python para la **gestión, filtrado, almacenamiento y descarga de reportes culturales**, desarrollada con **PyQt5** y **SQLite**.

---

## 🚀 Características principales

- 📁 Carga de nuevos reportes con formulario completo (persona, taller, descripción, horas, inscritos, etc.)
- 🔍 Filtros por categoría, CAO y mes.
- 🗃️ Almacenamiento en base de datos SQLite local.
- 📥 Descarga de reportes:
  - Incluye el archivo original cargado.
  - Genera automáticamente un PDF con los datos del formulario.
- 🗑️ Eliminación de reportes con manejo seguro de archivos.
- 🌙 Interfaz oscura moderna con estilo personalizado (`.qss`).
- 🔒 Funciona completamente **offline**.

---

## 🛠️ Tecnologías utilizadas

- [Python 3](https://www.python.org/)
- [PyQt5](https://pypi.org/project/PyQt5/) – GUI
- [SQLite3](https://www.sqlite.org/index.html) – Base de datos embebida
- [ReportLab](https://www.reportlab.com/) – Generación de PDFs
- [PyInstaller](https://pyinstaller.org/) – Opcional, para generar ejecutable

---

## 📦 Estructura del proyecto

ReportesCulturales/
├── main.py
├── style.qss
├── ui/
│ ├── main_window.py
│ └── nuevo_reporte_dialog.py
├── db/
│ └── database_manager.py
├── utils/
│ └── pdf_utils.py
├── assets/
│ └── reportes/ # Archivos cargados
└── database/
└── reportes.db # Se genera automáticamente

---

## ▶️ Cómo ejecutar

1. Instala las dependencias:
   pip install -r requirements.txt

📤 Empaquetar como ejecutable .exe
pyinstaller --noconfirm --windowed --add-data "style.qss;." --add-data "assets/reportes;assets/reportes" --add-data "database;database" main.py

🧑‍💻 Contribuciones
🐍 Código Pythonizado por Flashy Meduza 🐍
☕ Invitaciones de café aceptadas (🌮 tacos también)
🚀 Motivo: "Porque el universo lo pidió"
✅ Si funciona → 👍
❌ Si no funciona → 🤷‍♂️ "Misterios de la programación"
🚫 No responsabilizo de bugs cósmicos o deidades digitales

REPORTE CULTURAL APP

Cómo ejecutar:

1. Abre la carpeta.
2. Haz doble clic en 'main.exe'.
3. Si Windows muestra advertencia, haz clic en "Más información" y luego "Ejecutar de todas formas".

Requisitos:

- Solo copiar la carpeta. No necesita instalación ni conexión a Internet.

dist/
└── main/
├── main.exe ← ESTE ES TU PROGRAMA, HACER DOBLE CLIC PARA EJECUTAR
├── style.qss
├── database/
├── assets/
└── ...

Comando para generar el ejecutable
pyinstaller --noconfirm --windowed --add-data "style.qss;." --add-data "assets/reportes;assets/reportes" --add-data "database;database" main.py
