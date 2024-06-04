#!/bin/bash

# Exit script if any command fails
set -e

# Base x2 re
CUDA_VISIBLE_DEVICES=1 python3 basicsr/train.py -opt /workspace/LMLT/options/train/LMLT/train_large_DF2K_X2.yml

# base x3 re
CUDA_VISIBLE_DEVICES=1 python3 basicsr/train.py -opt /workspace/LMLT/options/train/LMLT/train_large_DF2K_X3.yml

# base x4 re
CUDA_VISIBLE_DEVICES=1 python3 basicsr/train.py -opt /workspace/LMLT/options/train/LMLT/train_large_DF2K_X4.yml