# DeepLearning-StainTransfer
Replication and extension of GAN-based virtual H&amp;E staining of skin tissues. Includes model training, evaluation, and exploratory analysis.


### Running KID-FID-SSIM
To run the KID, FID, SSIM metrics, make sure you have installed the following packages:
```
numpy
torch
torchmetrics
torchvision
```

Also, you should arrange the directories of test directories, and dataset itself including the unstained and H&E stained images. 
```
directories = {"DCLGAN":"DCL_TEST_DIR", 
               "CycleGAN": "Cycle_TEST_DIR",
               "CutGAN": "CUT_TEST_DIR"}

generated_image_path =  directories[model]
stained_image_path = '../data/stained/'
unstained_image_path = '../data/unstained/'
```

After putting the correct directories, you could run by ```python fid_kid_ssim.py --variation stained-vstained --model DCLGAN --metric fid```.
You could see the other options with ```python fid_kid_ssim.py --help```.



