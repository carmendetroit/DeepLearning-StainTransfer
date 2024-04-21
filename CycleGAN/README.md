### Installation and Train

- Clone the CycleGAN repo:
We used the pytorch implementation.
```bash
git clone https://github.com/junyanz/pytorch-CycleGAN-and-pix2pix
```
- Train the model:
```bash
python train.py --dataroot ../Stained-Unstained/ --name UnstainedToStained --batch_size 16 --model cycle_gan --gpu_ids 0
```
However, in some cases training process is distrupted, so you can continue to train from a checkpoint. 
```
python train.py --dataroot ../Stained-Unstained/ --name UnstainedToStained --batch_size 16 --model cycle_gan --gpu_ids 0 --continue_train --epoch N --epoch_count N+1
```
### Test
- Test the model:
```bash
  python test.py --dataroot ../Stained-Unstained-Test --name UnstainedToStained  --model test --no_dropout --gpu_ids --num_test 1398
```
The test results will be saved to an HTML file here: `./results/UnstainedToStained/latest_test/index.html`.
