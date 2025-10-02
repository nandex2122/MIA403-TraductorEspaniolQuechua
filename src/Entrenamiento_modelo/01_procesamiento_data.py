import os
from datasets import load_dataset

# 1. Ruta de guardado
ruta_base = "D:/Jose/UNI/Maestria IA/Cursos/03_Tercer_ciclo/03_Proyecto_Tesis/Proyecto/Diccionarios/huggingface/somosnlp-hackathon-2022/Dataset"
os.makedirs(ruta_base, exist_ok=True)

# 2. Cargar dataset
dataset = load_dataset("somosnlp-hackathon-2022/spanish-to-quechua")

# 3. Guardar cada división con el formato solicitado
def guardar_con_codigos(data_split, nombre_archivo):
    with open(nombre_archivo, "w", encoding="utf-8") as f:
        for i, ejemplo in enumerate(data_split, 1):
            codigo = f"{i:06d}"
            esp = ejemplo["es"].strip().replace("\n", " ")
            que = ejemplo["qu"].strip().replace("\n", " ")
            f.write(f"{codigo} {esp} {codigo} {que}\n")

# 4. Guardar los splits
guardar_con_codigos(dataset["train"], os.path.join(ruta_base, "train.txt"))
guardar_con_codigos(dataset["validation"], os.path.join(ruta_base, "validation.txt"))
guardar_con_codigos(dataset["test"], os.path.join(ruta_base, "test.txt"))

print(" ¡Listo! Los archivos fueron guardados correctamente.")


import os
import re

ruta_base = "D:/Jose/UNI/Maestria IA/Cursos/03_Tercer_ciclo/03_Proyecto_Tesis/Proyecto/Diccionarios/huggingface/somosnlp-hackathon-2022/Dataset"
archivos_entrada = ["train.txt", "validation.txt", "test.txt"]
archivo_salida = "corpus_total.txt"

contador = 1

# Expresión regular para capturar:
# código + texto español + código + texto quechua
patron = re.compile(r"(\d{6}) (.+?) (\d{6}) (.+)")

with open(os.path.join(ruta_base, archivo_salida), "w", encoding="utf-8") as fout:
    for archivo in archivos_entrada:
        path_archivo = os.path.join(ruta_base, archivo)
        with open(path_archivo, "r", encoding="utf-8") as fin:
            for linea in fin:
                linea = linea.strip()
                m = patron.match(linea)
                if m:
                    # Extraemos solo los textos, ignorando los códigos originales
                    esp = m.group(2)
                    que = m.group(4)
                    codigo = f"{contador:06d}"
                    fout.write(f"{codigo} {esp} {codigo} {que}\n")
                    contador += 1
                else:
                    print(f" Línea ignorada (no cumple formato esperado): {linea}")

print(" Archivo corpus_total.txt generado correctamente con códigos únicos.")


import hashlib

archivo_salida = "D:/Jose/UNI/Maestria IA/Cursos/03_Tercer_ciclo/03_Proyecto_Tesis/Proyecto/Diccionarios/huggingface/somosnlp-hackathon-2022/Dataset/01_corpus_total.txt"
archivo_salida = "data/corpus_total_combinado.txt"


def generar_hash_sha256(ruta_archivo):
    sha256 = hashlib.sha256()
    with open(ruta_archivo, "rb") as f:
        for bloque in iter(lambda: f.read(4096), b""):
            sha256.update(bloque)
    return sha256.hexdigest()

# Ejemplo de uso
archivo = archivo_salida
hash_resultado = generar_hash_sha256(archivo)
print(f"Hash SHA-256 del archivo '{archivo}':\n{hash_resultado}")

import os
from datasets import load_dataset
import re

ruta_base = "D:/Jose/UNI/Maestria IA/Cursos/03_Tercer_ciclo/03_Proyecto_Tesis/Proyecto/Diccionarios/huggingface/pollitoconpapass/Dataset"
os.makedirs(ruta_base, exist_ok=True)

dataset = load_dataset("pollitoconpapass/cuzco-quechua-translation-spanish")

print("Splits disponibles:", dataset.keys())

def guardar_con_codigos(data_split, nombre_archivo, start_index=1):
    with open(nombre_archivo, "w", encoding="utf-8") as f:
        for i, ejemplo in enumerate(data_split, start_index):
            codigo = f"{i:06d}"
            esp = ejemplo["spa"].strip().replace("\n", " ")
            que = ejemplo["quz"].strip().replace("\n", " ")
            f.write(f"{codigo} {esp} {codigo} {que}\n")
    return i + 1

indice = 1
indice = guardar_con_codigos(dataset["train"], os.path.join(ruta_base, "train.txt"), start_index=indice)
indice = guardar_con_codigos(dataset["validate"], os.path.join(ruta_base, "validate.txt"), start_index=indice)
indice = guardar_con_codigos(dataset["test"], os.path.join(ruta_base, "test.txt"), start_index=indice)

print(" Archivos guardados correctamente.")


ruta_base = "D:/Jose/UNI/Maestria IA/Cursos/03_Tercer_ciclo/03_Proyecto_Tesis/Proyecto/Diccionarios/huggingface/pollitoconpapass/Dataset"
archivos_entrada = ["train.txt", "validate.txt", "test.txt"]
archivo_salida = "corpus_total.txt"
contador = 1
patron = re.compile(r"(\d{6}) (.+?) (\d{6}) (.+)")

with open(os.path.join(ruta_base, archivo_salida), "w", encoding="utf-8") as fout:
    for archivo in archivos_entrada:
        path_archivo = os.path.join(ruta_base, archivo)
        with open(path_archivo, "r", encoding="utf-8") as fin:
            for linea in fin:
                linea = linea.strip()
                m = patron.match(linea)
                if m:
                    esp = m.group(2)
                    que = m.group(4)
                    codigo = f"{contador:06d}"
                    fout.write(f"{codigo} {esp} {codigo} {que}\n")
                    contador += 1
                else:
                    print(f" Línea ignorada (formato inesperado): {linea}")

print(f" Archivo combinado {archivo_salida} creado correctamente.")

import os
import re

# Ruta donde están los corpus generados
ruta_base = "D:/Jose/UNI/Maestria IA/Cursos/03_Tercer_ciclo/03_Proyecto_Tesis/Proyecto/Diccionarios/huggingface"

# Archivos a combinar (ajusta nombres y rutas)
archivos_entrada = [
    os.path.join(ruta_base, "somosnlp-hackathon-2022", "Dataset", "corpus_total.txt"),  # ejemplo somosnlp
    os.path.join(ruta_base, "pollitoconpapass","Dataset", "corpus_total.txt")        # ejemplo pollito
]

archivo_salida = os.path.join(ruta_base, "corpus_total_combinado.txt")

contador = 1
patron = re.compile(r"(\d{6}) (.+?) (\d{6}) (.+)")

with open(archivo_salida, "w", encoding="utf-8") as fout:
    for archivo in archivos_entrada:
        with open(archivo, "r", encoding="utf-8") as fin:
            for linea in fin:
                linea = linea.strip()
                m = patron.match(linea)
                if m:
                    esp = m.group(2)
                    que = m.group(4)
                    codigo = f"{contador:06d}"
                    fout.write(f"{codigo} {esp} {codigo} {que}\n")
                    contador += 1
                else:
                    print(f" Línea ignorada (formato inesperado): {linea}")

print(f" Corpus combinado creado en:\n{archivo_salida}")



