### Commands used4

- Clone the DCLGAN repo:
```bash
git clone https://github.com/JunlinHan/DCLGAN.git
```

- Install PyTorch 1.1 and other dependencies (e.g., torchvision, visdom, dominate, gputil).

  For pip users, please type the command `pip install -r requirements.txt`.

  For Conda users,  you can create a new Conda environment using `conda env create -f environment.yml`.
  
curl the dataset
```bash
curl -o dataset.zip https://dataset-49t.s3.amazonaws.com/dir.zip
```
unzip the dataset
```bash
unzip dataset.zip -d /path/to/destination
```

- Train the DCL model:
```bash
python train.py --dataroot ./path/to/dataset --name HEstain_DCL 
```
The checkpoints will be stored at `./checkpoints/`.

- Test the DCL model:
```bash
python test.py --dataroot ./path/to/datasets --name HEstain_DCL
```
