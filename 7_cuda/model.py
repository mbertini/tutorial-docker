import torch
from torchvision import models, transforms
from PIL import Image

model = models.resnet18(weights='IMAGENET1K_V1')
model.eval().cuda()

transform = transforms.Compose([
    transforms.Resize(256),
    transforms.CenterCrop(224),
    transforms.ToTensor(),
])

def classify_image(image_file):
    image = Image.open(image_file).convert("RGB")
    input_tensor = transform(image).unsqueeze(0).cuda()
    with torch.no_grad():
        outputs = model(input_tensor)
    predicted = outputs.argmax(1).item()
    return f"Class ID: {predicted}"
