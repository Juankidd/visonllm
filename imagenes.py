import openai
import base64

# Configurar la clave de API
client = openai.OpenAI(api_key="")

# Leer y codificar la imagen en base64
with open("grafica2.png", "rb") as image_file:
    base64_image = base64.b64encode(image_file.read()).decode("utf-8")

# Llamar al modelo GPT-4 con visión
response = client.chat.completions.create(
    model="gpt-4-turbo",
    messages=[
        {
            "role": "user",
            "content": [
                {"type": "text", "text": "¿Qué ves en esta imagen?"},
                {
                    "type": "image_url",
                    "image_url": {
                        "url": f"data:image/jpeg;base64,{base64_image}",
                    },
                },
            ],
        }
    ],
    max_tokens=500,
)

# Mostrar la respuesta
print(response.choices[0].message.content)

