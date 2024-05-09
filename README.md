## MeshMAE: Masked Autoencoders for 3D Mesh Data Analysis, ECCV 2022
This is the PyTorch implementation of our MeshMAE.
## Requirements

* python 3.9+
* CUDA 11.1+
* torch 1.11+

To install python requirements:
```setup
pip install -r requirements.txt
```


To install PyGem, please refer to [Pygem](https://github.com/mathLab/PyGeM).


## Fetch Data
### Datasets
Here, we provide the download links of the datasets for pre-train, classification and segmentation. 

- ModelNet40 [here](https://drive.google.com/file/d/1Cf5zQqN-kAXF7OiZZ0hNNPT59J-Ijy-i/view?usp=sharing)
- Humanbody [here](https://drive.google.com/file/d/1XaqMC8UrIZ_N77gN83PI3VK03G5IJskt/view?usp=sharing)
- COSEG-aliens [here](https://drive.google.com/file/d/12QCv2IUySoSzxeuvERGzgmE7YY3QzjfW/view?usp=sharing)
- ShapeNet [here](https://shapenet.org)（we also provide the processed ShapeNet dataset as [here](https://pan.baidu.com/s/1w044bIgiCMY0WXD9QviUJg?pwd=ufb9)）




Please create a new folder 'datasets' in the main root, and put the downloaded datasets in this folder. And '--dataroot' in the 'xxx.sh' refers to the root of datasets. 

For example, the root of ModelNet40 should be:

```
--dataroot ./dataset/Manifold40-MAPS-96-3/ 
```


To process the raw data, please use data_preprocess/manifold.py, which can transform non-manifold mesh data into manifold and simplify it to 500 faces.

To remesh the meshes, you can refer to the datagen_maps.py of [SubdivNet](https://github.com/lzhengning/SubdivNet), which can generate hierarchical structures.


## Pretrain


* To pretrain on the ShapeNet dataset, run this command:
```
sh scripts/pretrain/train_pretrain.sh
```
 


## Downstream Tasks

### Classification

* To train the classification model from scratch, run this command:

```
sh scripts/classification/train.sh
```

* To finetune the classification model, run this command:
```
sh scripts/classification/train_finetune.sh
```


### Segmentation

* To train the segmentation model from scratch, run this command:

```
sh scripts/segmentation/<...>/train.sh
```

* To finetune the segmentation model, run this command:

```
sh scripts/segmentation/<...>/train_finetune.sh
```


## Reference
```
@inproceedings{meshmae2022,
  title={MeshMAE: Masked Autoencoders for 3D Mesh Data Analysis},
  author={Liang, Yaqian and Zhao, Shanshan and Yu, Baosheng and Zhang, Jing and He, Fazhi},
  booktitle={European Conference on Computer Vision},
  year={2022},
}
```


