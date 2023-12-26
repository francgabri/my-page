import csv
with open("archivos\\dato.csv") as archivo:
    reader=csv.reader(archivo)
    for row in reader :
        print(row)