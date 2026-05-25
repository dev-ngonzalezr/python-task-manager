import os
from dotenv import load_dotenv
from openai import OpenAI

from task import Task

load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def create_simple_tasks(task_description):
    if client.api_key is None:
        raise Exception("API key not set")

    prompt = f"""Desglosa la siguiente tarea compleja en 3 a 5 tareas simples y accionables.
    
    Tarea: {task_description}
    
    Formato de respuesta:
    - subtarea 1
    - subtarea 2
    - subtarea 3
    - etc
    
    Responde solo con una lista de tareas, una por linea, empezando cada linea con un guion.
    """

    params = {
        "model": "gpt-5",
        "messages": [
            {"role": "system", "content": "Eres un asistente de gestion de tareas que ayuda a dividir en tareas mas sencillas y accionables."},
            {"role": "user", "content": prompt},
        ],
        "max_completion_tokens": 300,
        "verbosity": "medium",
        "reasoning_effort": "minimal"
    }

    try:
        response = client.chat.completions.create(**params)
        content = response.choices[0].message.content.strip()

        subtareas = []

        for line in content.split("\n"):
            if line.startswith("-"):
                subtareas.append(line[1:].strip())

        return subtareas
    except Exception as e:
        print(e)
        raise Exception("Error conectando con OpenAI")
