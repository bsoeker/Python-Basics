from zipfile import ZipFile
from pathlib import Path


# zip_file = ZipFile("./files.zip", "w")
# for path in Path("./").iterdir():
#     zip_file.write(path)
# zip_file.close()


with ZipFile("./files.zip") as zip_file:
    print(zip_file.namelist())
