import os
import shutil
import pandas as pd

dia = "01"
mes = "11"
fecha = f"{dia}{mes}2021"
dest_folder = 'Sin tomar lectura'
excel_name = f"LECTURA INDUSTRIAL ENRUTA {dia}-{mes}-2021.xlsx"

act_folder = 'Sin nombrar'
path = 'D:\Documentos\Enruta\Lecturas Industriales\\' + fecha
df = pd.ExcelFile(f'{path}\{excel_name}').parse("RECORRIDO")

os.chdir(f'{path}\{act_folder}')

for file in os.listdir():
    try:
        nombreDeLaEmpresa = ""
        imagenRepetida = ""
        nombreImagen = file.split(".")[0].split(" ")
        caseta = int(nombreImagen[0])

        if(len(nombreImagen) == 2):
            imagenRepetida = " " + nombreImagen[1]

        for index, data in enumerate(df["Unnamed: 2"]):
            if(data == caseta):
                print("se hizo nombre de la empresa: " +
                      df["Unnamed: 4"][index])
                nombreDeLaEmpresa = df["Unnamed: 4"][index].replace(
                    "\n", "").replace("/", "")

        if(nombreDeLaEmpresa == ""):
            nombreDeLaEmpresa == "AAA"

        newName = str(caseta) + " " + nombreDeLaEmpresa + \
            " " + fecha + imagenRepetida + ".jpg"
        shutil.move(f"{path}\{act_folder}\{file}",
                    f"{path}\{dest_folder}\{newName}")

    except(ValueError):
        print("La caseta '" + file.split(".")
              [0] + "' deberia ser solo digitos")
