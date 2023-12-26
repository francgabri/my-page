with open("archivos\\texto de franco.txt","a",encoding="UTF-8") as archivo:
    #agregando el archivo
    archivo.write("jajajaja te la re teclee\n")
    #usando un bucle para agregar varias lineas
    for i in range(5):
        archivo.write(f"linea {i+1} agregada\n")