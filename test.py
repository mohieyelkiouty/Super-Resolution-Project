import torch
from PIL import Image
import torchvision.transforms.functional as TF
import os

MODEL_PATH = "model.pt"
INPUT_IMAGE = r"input_lr_image.jpg"
OUTPUT_IMAGE = r"output_sr_image.jpg"

device = torch.device("cpu")
model = torch.jit.load(MODEL_PATH, map_location=device)
model.eval()

img = Image.open(INPUT_IMAGE).convert("RGB")
lr_tensor = TF.to_tensor(img).unsqueeze(0).to(device)

with torch.no_grad():
    sr_tensor = model(lr_tensor)

sr_tensor = sr_tensor.clamp(0, 1)
sr_img = TF.to_pil_image(sr_tensor.squeeze(0))

sr_img.save(OUTPUT_IMAGE)
print("Super Resolution image saved:", OUTPUT_IMAGE)
