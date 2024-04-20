### Commands used

- Clone the CUTGAN repo:
```bash
git clone https://github.com/JunlinHan/DCLGAN.git
```

- Install PyTorch 1.1 and other dependencies (e.g., torchvision, visdom, dominate, gputil).

  For pip users, please type the command `pip install -r requirements.txt`.

  For Conda users,  you can create a new Conda environment using `conda env create -f environment.yml`.
  
Split the dataset downloaded from official resource provided in homework description using split.py


- Train the CUT model:
```bash
!python contrastive-unpaired-translation/train.py --dataroot dataset_directory --n_epochs 50 --n_epochs_decay 15 --name stain_CUTGAN --CUT_mode CUT
```
The checkpoints will be stored at `./checkpoints/`.

- Test the CUT model:
```bash
!python contrastive-unpaired-translation/test.py --dataroot dataset_directory --name stain_CUTGAN --CUT_mode CUT --phase test --num_test 268
```
