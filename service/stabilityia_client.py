import requests
from settings.config import STABILITY_API_KEY

def generate_img(prompt:str):
    print(prompt)

    url = "https://api.stability.ai/v2beta/stable-image/generate/core"

    headers = {
        "Authorization": f"Bearer {STABILITY_API_KEY}",
        "Accept": "application/json"
    }

    files = {
        "prompt": (None, prompt),
        "output_format": (None, "png"),
        "aspect_ratio": (None, "1:1")
    }

    response = requests.post(url, headers=headers, files=files)
     
    data = response.json()
    return data["image"] #file as stringBase64