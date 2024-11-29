import sys
from cx_Freeze import setup, Executable

build_exe_options = {
    "packages": ["tkinter", "json"],
    "include_files": ["categories.json", "questions.json"]
}

base = None
if sys.platform == "win32":
    base = "Win32GUI"

setup(
    name="Quiz System",
    version="1.0",
    description="Sistema de Quiz con Categorías",
    options={"build_exe": build_exe_options},
    executables=[Executable("tercia.py", base=base, icon="icon.ico")]
)