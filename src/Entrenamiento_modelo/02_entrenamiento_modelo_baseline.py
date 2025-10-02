import zipfile
import os

ruta_zip = '01_corpus_total.zip'           # Ruta del archivo zip
carpeta_destino = './'  # Carpeta donde quieres extraer el contenido

# Crear la carpeta destino si no existe
os.makedirs(carpeta_destino, exist_ok=True)

# Abrir el archivo zip y extraer todo
with zipfile.ZipFile(ruta_zip, 'r') as zip_ref:
    zip_ref.extractall(carpeta_destino)

print(f'Contenido extraído en {carpeta_destino}')

import re

archivo_original = 'corpus_total_combinado.txt'
archivo_salida = 'corpus_total_formateado.txt'

with open(archivo_original, 'r', encoding='utf-8') as f_in, \
     open(archivo_salida, 'w', encoding='utf-8') as f_out:

    for linea in f_in:
        linea = linea.strip()
        # Buscar los dos IDs y textos intermedios con regex
        # Patrón: ID (6 dígitos) + texto + ID (6 dígitos) + texto
        match = re.match(r'^(\d{6})\s(.+)\s(\d{6})\s(.+)$', linea)
        if match:
            id_esp = match.group(1)
            texto_esp = match.group(2)
            id_que = match.group(3)
            texto_que = match.group(4)

            # Escribir con tabuladores
            f_out.write(f"{id_esp}\t{texto_esp}\t{id_que}\t{texto_que}\n")
        else:
            print(f"Línea no coincide con el patrón esperado:\n{linea}")

print("Archivo formateado guardado en", archivo_salida)

import csv
import os
os.environ["TRANSFORMERS_NO_TF"] = "1"

# Ruta de Archivo
carpeta = "./"
os.makedirs(carpeta, exist_ok=True)

#nombre_archivo = "esp_ingles - 2024-11-02.txt"
nombre_archivo = "corpus_total_formateado.txt"
nombre_corpus = "corpus_trad.csv"

path_1 = os.path.join(carpeta, nombre_archivo)
path_2 = os.path.join(carpeta, nombre_corpus)

with open(nombre_archivo, "r", encoding="utf-8") as infile, \
     open(nombre_corpus, "w", newline='', encoding="utf-8") as outfile:

    writer = csv.writer(outfile)
    writer.writerow(["source", "target"])  # encabezado

    for line in infile:
        parts = line.strip().split("\t")
        if len(parts) == 4:
            _, source, _, target = parts
            writer.writerow([source, target])

import torch
print("CUDA available:", torch.cuda.is_available())
print("CUDA device count:", torch.cuda.device_count())
print("Current CUDA device:", torch.cuda.current_device())
print("Device name:", torch.cuda.get_device_name(torch.cuda.current_device()))

import os
os.environ["TRANSFORMERS_NO_TF"] = "1"

from transformers import BartTokenizer, BartForConditionalGeneration, Seq2SeqTrainingArguments, Seq2SeqTrainer
from datasets import load_dataset

# 1. Cargar tokenizer y modelo preentrenado
model_name = "facebook/bart-base"
tokenizer = BartTokenizer.from_pretrained(model_name)
model = BartForConditionalGeneration.from_pretrained(model_name)

# Mover modelo a GPU si está disponible
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
model.to(device)

# 2. Cargar dataset desde el CSV generado
dataset = load_dataset("csv", data_files={"train": "corpus_trad.csv"}, split="train")

# 3. Preprocesamiento: tokenizar entradas y salidas
def preprocess(example):
    inputs = tokenizer(example["source"], max_length=128, truncation=True, padding="max_length")
    targets = tokenizer(example["target"], max_length=128, truncation=True, padding="max_length")
    inputs["labels"] = targets["input_ids"]
    return inputs

tokenized_dataset = dataset.map(preprocess, remove_columns=dataset.column_names)

# 4. Definir parámetros de entrenamiento
training_args = Seq2SeqTrainingArguments(
    output_dir="./bart_traducido",
    learning_rate=5e-5,
    per_device_train_batch_size=8,
    num_train_epochs=2,
    weight_decay=0.01,
    save_total_limit=1,
    predict_with_generate=True,
)

# 5. Crear trainer
trainer = Seq2SeqTrainer(
    model=model,
    args=training_args,
    train_dataset=tokenized_dataset,
    tokenizer=tokenizer,
)

# 6. Entrenar
trainer.train()


## Guardar el modelo entrenado
# Después de trainer.train()
trainer.save_model("./bart_traducido_final")
tokenizer.save_pretrained("./bart_traducido_final")

## Luego para cargar
from transformers import BartTokenizer, BartForConditionalGeneration

model_path = "D:/Jose/UNI\Maestria IA\Cursos\03_Tercer_ciclo\03_Proyecto_Tesis\Proyecto\Modelo\Local/bart_traducido_final"

tokenizer = BartTokenizer.from_pretrained(model_path)
model = BartForConditionalGeneration.from_pretrained(model_path)

