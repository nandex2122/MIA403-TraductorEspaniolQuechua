from transformers import BartForConditionalGeneration, BartTokenizer

# Ruta local al modelo fine-tuned
model_path = "D:/Jose/UNI/Maestria IA/Cursos/03_Tercer_ciclo/03_Proyecto_Tesis/Proyecto/Modelo/Protipo_usuario/bart_traducido_final"

# Cargar tokenizer y modelo desde carpeta local
tokenizer = BartTokenizer.from_pretrained(model_path)
model = BartForConditionalGeneration.from_pretrained(model_path)

def translate_text(text):
    inputs = tokenizer([text], max_length=1024, return_tensors='pt', truncation=True)
    output_ids = model.generate(inputs['input_ids'], num_beams=4, max_length=100, early_stopping=True)
    return tokenizer.decode(output_ids[0], skip_special_tokens=True)