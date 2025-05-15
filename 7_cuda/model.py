import torch
from torchvision import models, transforms
from PIL import Image
import torch.nn.functional as F
import json

model = models.resnet18(weights='IMAGENET1K_V1')
model.eval().cuda()

# Load ImageNet class labels
with open('imagenet_class_index.json') as labels_file:
    labels = json.load(labels_file)

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
        probabilities = F.softmax(outputs, dim=1)
        predicted_idx = probabilities.argmax(1).item()
        predicted_class = labels[str(predicted_idx)][1]
        predicted_prob = probabilities[0, predicted_idx].item()
    return f"Class idx: {predicted_idx}, Class: {predicted_class}, Probability: {predicted_prob:.4f}"