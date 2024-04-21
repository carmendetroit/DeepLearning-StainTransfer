### Installation
* Install torch and dependencies from https://github.com/torch/distro
* Install torch packages nngraph, class, display
```bash
luarocks install nngraph
luarocks install class
luarocks install https://raw.githubusercontent.com/szym/display/master/display-scm-0.rockspec
```
- Clone the CycleGAN repo:
```bash
git clone https://github.com/junyanz/CycleGAN
cd CycleGAN
```
- Train the model:
```bash
DATA_ROOT=./path/to/dataset name=Stain_model th train.lua
```
### Test
- Test the model:
```bash
  DATA_ROOT=./path/to/dataset name=Stain_model phase=test th test.lua
```
The test results will be saved to an HTML file here: `./results/Stain_model/latest_test/index.html`.
