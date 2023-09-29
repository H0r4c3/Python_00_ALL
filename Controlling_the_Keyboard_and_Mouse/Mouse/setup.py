from cx_Freeze import setup, Executable

setup(
    name="mouse_left_click",
    version="1.0",
    description="Left click mouse",
    executables=[Executable("mouse_left_click.py")]
)