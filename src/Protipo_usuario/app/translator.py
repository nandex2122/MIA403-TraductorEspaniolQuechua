from transformers import BartForConditionalGeneration, BartTokenizer
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

# --- Paso 1: Cargar BART fine-tuned ---
model_path = r"D:\Jose\UNI\Maestria IA\Cursos\03_Tercer_ciclo\03_Proyecto_Tesis\Proyecto\Modelo\Protipo_usuario\bart_traducido_final"
tokenizer = BartTokenizer.from_pretrained(model_path)
bart_model = BartForConditionalGeneration.from_pretrained(model_path)

# --- Paso 2: Cargar modelo de embeddings ---
embed_model = SentenceTransformer(
    r"D:\Jose\UNI\Maestria IA\Cursos\03_Tercer_ciclo\03_Proyecto_Tesis\Proyecto\Modelo\Prototipo_usuario_all-MiniLM-L6-v2\models"
)

# --- Paso 3: Cargar corpus de referencia ---
with open(
    r"D:\Jose\UNI\Maestria IA\Cursos\03_Tercer_ciclo\03_Proyecto_Tesis\Proyecto\Modelo\Prototipo_usuario_all-MiniLM-L6-v2\oraciones_separadas.txt",
    "r",
    encoding="utf-8",
) as f:
    corpus = [line.strip() for line in f.readlines()]

corpus_embeddings = embed_model.encode(corpus)

# --- Paso 4: Función de traducción con recuperación (sin FAISS) ---
def translate_text(text, top_k=1):
    # 4a: calcular similitud coseno entre la consulta y el corpus
    query_emb = embed_model.encode([text])
    similarities = cosine_similarity(query_emb, corpus_embeddings)[0]

    # 4b: recuperar las frases más similares
    top_indices = np.argsort(similarities)[::-1][:top_k]
    retrieved_context = " ".join([corpus[i] for i in top_indices])

    # 4c: combinar texto original + contexto
    ##input_text = f"{text} Contexto: {retrieved_context}"  ## Inventa contexto con : puntos
    ##input_text = f"{text} [CONTEXT] {retrieved_context}"  ## Inventa contexto sin ":"
    input_text = text

    # 4d: generar traducción con BART fine-tuned
    inputs = tokenizer([input_text], max_length=1024, return_tensors="pt", truncation=True)
    output_ids = bart_model.generate(
        inputs["input_ids"], num_beams=4, max_length=100, early_stopping=True
    )
    return tokenizer.decode(output_ids[0], skip_special_tokens=True)
