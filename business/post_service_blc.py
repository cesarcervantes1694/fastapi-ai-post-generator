from service.stabilityia_client import generate_img
from service.replicateira_client import generate_img_replicate

# Generar imagen con Stability
def generate_post_stability(req):
    prompt = f"""
        Instagram marketing post for a {req.business},
        promotion: {req.promotion},
        style: {req.tone},
        modern design,
        clean background,
        vibrant colors,
        professional advertising,
        social media ready,
        square format,
        space for text
    """
    img_base64 = generate_img(prompt= prompt)

    return {
        "message": "Post generado correctamente",
        "prompt": prompt
    }

# Generar imagen con Replicate IA
def generate_post_replicate(req):
    prompt = f"""
    Instagram marketing post for a {req.business},
    promotion: {req.promotion},
    style: {req.tone},
    modern design,
    clean background,
    vibrant colors,
    professional advertising,
    social media ready,
    square format,
    space for text
    """

    image_url = generate_img_replicate(prompt)

    return {
        "message": "Post generado correctamente",
        "image_url": image_url,
        "prompt": prompt
    }