# LMLT(Low-to-high Multi-Level Vision Transformer)

Jeongsoo Kim, Jongho Nang, Junsuk Choe<sup>*</sup>

<sup>*</sup> : Corresponding author

### Requirements
```
# Install Packages
pip install -r requirements.txt
pip install matplotlib

# Install BasicSR
python3 setup.py develop
```


### Dataset
We use DIV2K, Flickr2K as Training dataset.
You can download two datasets at https://github.com/dslisleedh/Download_df2k/blob/main/download_df2k.sh
and prepare other test datasets at https://github.com/XPixelGroup/BasicSR/blob/master/docs/DatasetPreparation.md#Common-Image-SR-Datasets

And also, you'd better extract subimages using 
```
python3 scripts/data_preparation/extract_subimages.py
```
By running the code above, you may get subimages of training datasets.



### Training
You can train LMLT following commands below 
```
python3 basicsr/train.py -opt options/train/LMLT/train_tiny(base, large)_DF2K_X2(3, 4).yml
```
And also, we set `torch.backends.cudnn.benchmark` to `True` to accelerate training process so that results can be fluctuated a little. If you want to get fixed output, you should set it to `False` and set `torch.backends.cudnn.deterministic` to `True`.


### Test
You can test LMLT following commands below
```
python3 basicsr/test.py -opt options/test/LMLT/test_tiny(base, large)_benchmark_X2(3, 4).yml
```


### Results
We will provide visual results of LMLT_Base x4 scale soon. 
If you want to see only architecture, refer to `LMLT.py`.
