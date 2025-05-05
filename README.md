# Análisis de Imágenes con GPT-4 Vision en Raspberry Pi 5 / Jetson Nano

Este proyecto permite analizar el contenido de una imagen utilizando el modelo **GPT-4 Turbo con capacidades de visión** de OpenAI. Se ejecuta en dispositivos de computación en el borde como **Raspberry Pi 5** o **NVIDIA Jetson Nano**.

## 📌 Descripción

El script carga una imagen local (`grafica2.png`), la codifica en base64 y la envía al modelo de OpenAI junto con una pregunta. Luego imprime la descripción generada por GPT-4 Turbo sobre el contenido visual.

## 🚀 Requisitos

- Python 3.8 o superior
- Conexión a Internet
- Dispositivo: Raspberry Pi 5 o Jetson Nano (o cualquier sistema Linux con Python)
- Clave API de OpenAI (con acceso habilitado a modelos con visión)

## 🛠 Instalación

1. **Clonar este repositorio o copiar el archivo**
2. **Instalar las dependencias necesarias**:

```bash
pip install openai
