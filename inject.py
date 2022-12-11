import os
from shutil import copyfile
copyfile(
    "main.pyw",
    f"C:/Users/{os.getlogin()}/AppData/Roaming/Microsoft/Windows/Start Menu/Programs/Startup/main.pyw"
)