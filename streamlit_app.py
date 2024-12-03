import streamlit as st
import os
import shutil
from pathlib import Path
import base64
import vertexai
from vertexai.generative_models import GenerativeModel, Part, SafetySetting

# Configurações adicionais usadas no processamento do vídeo
textsi_1 = """(Aqui vão as instruções que você já definiu)"""

generation_config = {
    "max_output_tokens": 8192,
    "temperature": 0.5,
    "top_p": 0.95,
}

safety_settings = [
    SafetySetting(
        category=SafetySetting.HarmCategory.HARM_CATEGORY_HATE_SPEECH,
        threshold=SafetySetting.HarmBlockThreshold.OFF
    ),
    SafetySetting(
        category=SafetySetting.HarmCategory.HARM_CATEGORY_DANGEROUS_CONTENT,
        threshold=SafetySetting.HarmBlockThreshold.OFF
    ),
    SafetySetting(
        category=SafetySetting.HarmCategory.HARM_CATEGORY_SEXUALLY_EXPLICIT,
        threshold=SafetySetting.HarmBlockThreshold.OFF
    ),
    SafetySetting(
        category=SafetySetting.HarmCategory.HARM_CATEGORY_HARASSMENT,
        threshold=SafetySetting.HarmBlockThreshold.OFF
    ),
]

# Diretório onde o vídeo será salvo
VIDEO_DIR = "vídeos"

# Criar o diretório, caso não exista
Path(VIDEO_DIR).mkdir(parents=True, exist_ok=True)

def generate(video_file):
    vertexai.init(project="deft-racer-433513-t8", location="us-central1")
    model = GenerativeModel(
        "gemini-1.5-pro-001",
        system_instruction=[textsi_1]
    )
    responses = model.generate_content(
        [video_file, """Analise detalhadamente este arquivo conforme instruções do sistema."""],
        generation_config=generation_config,
        safety_settings=safety_settings,
        stream=True,
    )
    for response in responses:
        print(response.text, end="")
        st.write(response.text, end="")

# Frontend com Streamlit
st.title("Processador de Vídeos Médicos")

# Upload do vídeo
uploaded_file = st.file_uploader("Envie o vídeo para análise", type=["mp4"])

if uploaded_file is not None:
    # Definir o caminho para salvar o vídeo
    video_path = os.path.join(VIDEO_DIR, uploaded_file.name)
    # Salvar o vídeo na pasta 'vídeos'
    with open(video_path, "wb") as f:
        shutil.copyfileobj(uploaded_file, f)
    st.success(f"Vídeo {uploaded_file.name} carregado com sucesso!")

# Botão para processar o vídeo
if st.button("Processar"):
    st.write("Processando o vídeo...")
    # Chama a função que processa o vídeo (adapte conforme sua necessidade)
    generate(video_path)
    st.write("Processamento concluído.")
