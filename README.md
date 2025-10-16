# 🛡️ Traductor Automático de Español a Quechua

Este proyecto implementa el entrenamiento de un modelo BART de arquitectura de 

Transformers con el fine tuning con un Corpus y el prototipo visual de utilización del modelo.

Este repositorio forma parte del curso **Proyecto de Investigación II (MIA 403)**.

---

## 👥 Autores
- Fernado Andrés Herrera Cubas – [@nandex2122](https://github.com/nandex2122)
- José Carlos Ramos Maldonado – [@joseramos135](https://github.com/joseramos135)

---

## 📊 Dataset
- **Fuente**: [Hugging Face – Spanish to Quechua translation](https://huggingface.co/somosnlp-hackathon-2022/)  
- **Registros**: 128.5K párrafos traducidos, 78.5MB.  
- **Versión usada**: descargada el 28/10/2022  
- **Hash** (SHA256): `3b7e7fed69aeeabb5eb3802c4dd74e6166ddb0c5341f9ee7161068fbc821bc77`  

### Fuentes Adicionales

#### 1. Literatura - Paco Yunque
- **Fuente**: [Centro de Recursos - Paco Yunque Edición Multilingüe](https://centroderecursos.cultura.pe/es/registrobibliografico/paco-yunque-edici%C3%B3n-multiling%C3%BCe)
- **Registros**: 142 pares de oraciones
- **Tamaño**: 16 KB
- **Año**: 2023
- **Tipo**: Literatura peruana (César Vallejo)

#### 2. Material Educativo - MINEDU
- **Fuente**: [Repositorio MINEDU](https://repositorio.minedu.gob.pe/handle/20.500.12799/10380)
- **Registros**: 471 pares de oraciones
- **Tamaño**: 35 KB
- **Año**: 2014
- **Tipo**: Material educativo oficial

#### 3. Manual Médico
- **Fuente**: [Manual de Semiología en Quechua](https://www.cmp.org.pe/wp-content/uploads/2020/07/ManualSemiologiaQuechua-2020.pdf)
- **Registros**: 310 pares de oraciones
- **Tamaño**: 24 KB
- **Tipo**: Terminología médica y de salud

#### 4. Literatura - El Vencedor
- **Fuente**: [Centro de Recursos - El Vencedor Edición Multilingüe](https://centroderecursos.cultura.pe/es/registrobibliografico/el-vencedor-edici%C3%B3n-multiling%C3%BCe)
- **Registros**: 150 pares de oraciones
- **Tamaño**: 25 KB
- **Año**: 2024
- **Tipo**: Literatura contemporánea

#### 5. Corpus Médico RAG - Español
- **Fuente**: Oraciones médicas en idioma Español generadas por GPT-4 para entrenamiento RAG
- **Registros**: 20,000 oraciones segmentadas
- **Tamaño**: 1,977 KB
- **Año**: 2025
- **Especialidad**: Terminología médica, síntomas, diagnósticos usados en centros de salud

---

## 🗂️ Estructura del repositorio (Pendiente)
```
data/
 ├── raw/          # dataset original
 ├── interim/      # dataset procesado y unido
 ├── processed/    # dataset formato de Corpus paralelo
notebooks/
	 ├── EDA         
	 │   ├── Evaluacion_KFold_BART.ipynb            # Notebook para la ejecucion del EDA realizado
	 ├── Entrenamiento         
	 │   ├── 01_Generacion_Corpus.ipynb            # Notebook para la generación de corpus
	 │   ├── 02_Entrenamiento_modelo_BART.ipynb    # Notebook para ejecutar BART en un servidor (para Quechua)
	 ├── Metrica         
	 │   ├── Evaluacion_KFold_BART.ipynb            # Notebook para la ejecucion dde metricas BLEU y OUGE-L
src/               
 ├── Entrenamiento_modelo/               
 ├   ├── 01_procesamiento_data.py       		# script para la generación de corpus
 ├   └── 02_entrenamiento_modelo_baseline.py    # script para ejecutar BART en un servidor (para Quechua)
 └───Prototipo_usuario/               
	 ├── app/                              # Carpeta principal de la aplicación Flask
	 │   ├── __pycache__/            	   # Archivos compilados automáticamente por Python
	 │   ├── static/               		   # Archivos estáticos (imágenes, CSS, JS)  
	 │   │   └── Logo_UNI.png			   # Imagen usada en la aplicación        
	 │   ├── templates/    				   # Plantillas HTML de Flask          
	 │   │   └── index.html     		   # Página principal con el formulario     
	 │   ├── app.py              	       # Archivo principal Flask (servidor web)          
	 │   ├── run_with_ngrok.py             # Script para ejecutar Flask + Ngrok
	 │   └── translator.py                 # Script que carga el modelo y hace la traducción
	 └── bart_traducido_final/             # Carpeta con el modelo fine-tuned de BART          

logs/              # archivos de logging y métricas
slides/            # presentaciones de resultados
README.md
pyproject.toml
poetry.lock / requirements.txt
.gitignore
```

---

## ⚙️ Requisitos
Instalar dependencias usando [Poetry](https://python-poetry.org/):  
```bash
poetry install
```
O con `pip`:  
```bash
pip install -r requirements.txt
```

---

## 🚀 Cómo ejecutar el pipeline
1. **Procesamiento Corpus**
   - Opción A (script): 
   ```bash
   python src/Entrenamiento_modelo/01_procesamiento_data.py
   ```  
   - Opción B (notebook): 
	- Abrir y ejecutar `notebooks/Entrenamiento_modelo/01_Generacion_Corpus.ipynb`
	
   - Ambos realizan la lectura de los diccionarios, limpieza, generación de traducciones en paralelo.  
   - Guardado en `data/processed/corpus_total_formateado.txt`.

2. **Entrenamiento baseline y Fine tuning**
   - Opción A (script): 
   ```bash
   python src/Entrenamiento_modelo/02_entrenamiento_modelo_baseline.py
   ```
   - Opción B (notebook):  
     - Abrir y ejecutar `notebooks/Entrenamiento_modelo/02_Entrenamiento_modelo_BART.ipynb`  
   - Ambos generan resultados en `logs/log_baseline.txt`

3. **Prototipo**
   
   Probar Prototipo Online [Click Aquí](https://0704e13dcc33.ngrok-free.app)

   ```bash
   ngrok config add-authtoken
   python src/Protipo_usuario/app/app.py
   src/Protipo_usuario/app/ngrok http 5000

   ```
   - Genera el servicio para levantar la url pública del prototipo
   - Generan resultados en `logs/log_baseline.txt`  

---
# 🔍 Feature Engineering y Configuración del Modelo de Traducción Español–Quechua

Este documento describe el proceso de **fine-tuning del modelo BART** para la tarea de **traducción automático Español–Quechua**, desarrollado en Jupyter Notebook.  
Se presentan dos versiones del modelo: una entrenada con **2 épocas** (para validación inicial) y otra con **50 épocas** (para convergencia completa y evaluación final).

---

## 📄 1. Configuración General

| Parámetro | Modelo 2 Épocas | Modelo 50 Épocas |
|------------|----------------|------------------|
| Modelo base | `facebook/bart-base` | `facebook/bart-base` |
| Tokenizer | `BartTokenizer` | `BartTokenizer` |
| Longitud máxima (`max_length`) | 128 | 128 |
| Tamaño de batch | 8 | 8 |
| Learning rate | 5e-5 | 5e-5 |
| Épocas | 2 | 50 |
| Tiempo estimado de entrenamiento | ~3.5 min | ~1.5 h |
| Métricas registradas | No registradas | No registradas |

---

## ⚙️ 2. Feature Engineering (FE) para Texto

El **preprocesamiento textual** aplicado antes del entrenamiento incluye:

1. **Tokenización** con `BartTokenizer`, aplicando segmentación sub-palabra (Byte-Pair Encoding).  
2. **Conversión** de los pares Español–Quechua a tensores (`input_ids`, `attention_mask`, `labels`).  
3. **Padding y truncado** hasta una longitud fija de 128 tokens.  
4. No se aplica limpieza adicional (stopwords, lematización, etc.), ya que BART maneja ruido textual de forma eficiente.

> 🧩 Este pipeline representa un **FE estándar para modelos seq2seq**, optimizado para tareas de traducción.

---

## 🔍 3. Recuperación de Información (RAG)

El modelo actual **no implementa un módulo de recuperación** (Retriever o RAG).

- **TF-IDF / BM25:** No aplican.  
- **Posición del pasaje:** No aplica.  
- **Señales del retriever:** (score, overlap, top-k) No implementadas.

> 💡 En futuras versiones se planea integrar un **módulo RAG** que utilice búsqueda semántica (TF-IDF o embeddings) para seleccionar pasajes relevantes antes de traducir.

---

## 🧩 4. Longitud de Contexto

- Longitud máxima: **128 tokens** por entrada.  
- Este valor equilibra costo computacional y capacidad de generalización.  
- En escenarios de chatbot o RAG, se puede ampliar a **256–512 tokens** para mejorar cobertura contextual (a costa de mayor latencia).

---

## 🧠 5. Embeddings

- Los **embeddings son generados internamente** por el modelo BART durante el entrenamiento.  
- No se utilizan embeddings externos como Word2Vec o Sentence-BERT.  
- Esta decisión reduce **latencia** y simplifica el **despliegue en producción**.

---

## ⏱️ 6. Estimación de Costo y Latencia

| Configuración | Tiempo estimado de entrenamiento | Uso esperado |
|----------------|----------------------------------|---------------|
| 2 épocas | ~3.5 minutos | Validación funcional / test rápido |
| 50 épocas | ~1.5 horas | Modelo final / despliegue |

*(Tiempos estimados en GPU NVIDIA T4 o RTX 3060, dataset de tamaño medio).*

---

## 📊 7. Conclusiones

- El modelo de **2 épocas** permite validar el pipeline y estructura de datos.  
- El modelo de **50 épocas** logra una mejor convergencia y coherencia en la traducción.  
- No se aplican técnicas RAG ni embeddings externos.  
- La longitud de contexto de 128 tokens garantiza **eficiencia y bajo costo**.

---

## 🚀 8. Próximos Pasos

- Incorporar métricas de evaluación (BLEU, ROUGE, chrF).  
- Registrar tiempos reales de entrenamiento e inferencia.  
- Implementar módulo RAG con recuperación semántica.  

---
 
📅 **Versión:** Octubre 2025  

---
## 📜 Licencia
Uso académico – Universidad Nacional de Ingeniería (UNI).
