import os
import json
from labelme import utils
import numpy as np
from PIL import Image

input_dir = "."
output_dir = "./mask"
os.makedirs(output_dir, exist_ok=True)

json_files = [f for f in os.listdir(input_dir) if f.endswith(".json")]

for json_file in json_files:
    json_path = os.path.join(input_dir, json_file)
    with open(json_path, "r") as f:
        data = json.load(f)

    imageData = data.get("imageData")
    if not imageData:
        # Cargar desde archivo si no está embebida
        img_path = os.path.join(input_dir, data["imagePath"])
        with open(img_path, "rb") as img_f:
            imageData = utils.img_arr_to_b64(np.array(Image.open(img_f)))
            data["imageData"] = imageData

    img = utils.img_b64_to_arr(data["imageData"])

    label_name_to_value = {"_background_": 0}
    for shape in data["shapes"]:
        label_name = shape["label"]
        if label_name not in label_name_to_value:
            label_name_to_value[label_name] = len(label_name_to_value)

    lbl, _ = utils.shapes_to_label(img.shape, data["shapes"], label_name_to_value)

    mask = Image.fromarray((lbl == 1).astype(np.uint8) * 255)
    base = os.path.splitext(json_file)[0]
    mask.save(os.path.join(output_dir, f"{base}_mask.png"))

print("✅ Conversion terminada. Máscaras guardadas en 'mascaras/'.")
