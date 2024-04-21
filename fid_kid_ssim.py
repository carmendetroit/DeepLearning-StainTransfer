import torch 
from torchmetrics.image.fid import FrechetInceptionDistance
from torchmetrics.image.kid import KernelInceptionDistance
from torchvision.io import read_image
import os
from torchvision import transforms
import argparse
from SSIM import ssim
import numpy as np


BATCH_SIZE = 300
parser = argparse.ArgumentParser()
parser.add_argument('--variation', '-v', type=str, default='stained-vstained', help='[stained-vstained, unstained-vstained, unstained-stained]')
parser.add_argument('--model', '-m', type=str, default='DCLGAN', help='[DCLGAN, CycleGAN, CutGAN]')
parser.add_argument('--metric', type=str, default='fid', help='[fid, kid, ssim]')

args = parser.parse_args()
variation = args.variation
model = args.model
metric = args.metric

measure_model = None
if metric == 'fid':
    measure_model = FrechetInceptionDistance(feature=2048)
elif metric == 'kid':
    measure_model = KernelInceptionDistance(subset_size=20)

directories = {"DCLGAN":"DCL_TEST_DIR", 
               "CycleGAN": "Cycle_TEST_DIR",
               "CutGAN": "CUT_TEST_DIR"}



generated_image_path =  directories[model]
stained_image_path = '../data/stained/'
unstained_image_path = '../data/unstained/'

images = os.listdir(generated_image_path)
path1 = generated_image_path
if variation == 'stained-vstained':
    path2 = stained_image_path
elif variation == 'unstained-vstained':
    path2 = unstained_image_path
elif variation == 'unstained-stained':
    path1 = stained_image_path
    path2 = unstained_image_path
else:
    print("Invalid variation")
    exit()


if model == 'CycleGAN':
    images = [image for image in images if 'fake' in image and image.endswith('.png')]
else:
    images = [image for image in images if image.endswith('.png')]

    

transform  = transforms.Resize((299, 299))

ssim_scores = []
for i in range(0, len(images), BATCH_SIZE):
    batch_images = images[i:i+BATCH_SIZE]
    generated_tensors = []
    real_tensors = []

    for image in batch_images:
        image2 = image
        image1 = image

        # CycleGAN has a different naming convention
        if model == 'CycleGAN' :
            image2 = image.replace('_fake', '')
            if variation == 'unstained-stained':
                image1 = image2
       
        img1 = read_image(path1 + image1)
        img2 = read_image(path2 + image2)
        img1 = transform(img1)
        img2 = transform(img2)

        if (metric == 'ssim'):
            img1 = img1.float()/255.0
            img2 = img2.float()/255.0

           

            true_vs_false = ssim(img1, img2, val_range=255)
            ssim_scores.append(true_vs_false.item())
            continue
        
       

        generated_tensors.append(img1)
        real_tensors.append(img2)

    if metric == 'ssim':
        continue
    generated_tensors = torch.stack(generated_tensors)
    real_tensors = torch.stack(real_tensors)
    
    measure_model.update(generated_tensors, real=False)
    measure_model.update(real_tensors, real=True)





with open(f'results.txt', 'a') as f:
    if metric == 'fid':
        f.write(f"{variation} {model} FID Score: {measure_model.compute()}\n")
    elif metric == 'kid':
        mean, std = measure_model.compute()
        f.write(f"{variation} {model} KID Mean: {mean}\n")
    elif metric == 'ssim':
        f.write(f"{variation} {model} SSIM Mean: {np.mean(ssim_scores)}\n")


