import torch
from classify import classify_image

model = torch.load("model.pth")
model.eval()

test_imgs = ['1.png','2.png','3.png','4.png','5.png']


for img in test_imgs:
    test_img_path = 'testimages/'+ img
    print(classify_image(test_img_path, model))
