import replicate
import os
from dotenv import load_dotenv

load_dotenv()

replicate_client = replicate.Client(
    api_token=os.getenv("REPLICATE_API_KEY")
)

def generate_img_replicate(prompt:str):
    output = replicate_client.run(
        "black-forest-labs/flux-schnell",
        input={
            "prompt": prompt,
            "width": 1024,
            "height": 1024
        }
    )

    print(output)
    return output[0]