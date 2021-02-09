## Preprocessing

This folder contains all the scripts needed to load transform and prepare the data in order to train it. The folder Data is not included in this repository. All the files ending in .py are auxiliary scripts used by the notebooks (ending in .ipynb).


- **pipeline_demo_01_json2h5.ipynb**: loads and converts the original files (json) into .npy (numpy) files.

- **pipeline_demo_02_filter.ipynb**: corrects the joint locations in the .npy files. It smooths the trajectories and inserts missing joints.

- **pipeline_rotate.ipynb**: centers the skeleton in the origin of coordinates and rotates it so that its column (Mid-Hip to Neck vector) is in the Y axis and it is facing forwards (which means that the Nose to Neck vector is in the YZ plane so that the z coordinate contains the depth of the skeleton).

- **pipeline_scale.ipynb**:  Computes the 2D-length of the skeleton's column and scales the 3 axes with this length so that the skeleton's column length is 1. This normalization is inspired in the paper _Can 3D Pose be Learned from 2D Projections Alone, Dylan Drover, Rohith MV, Ching-Hang Chen, ECCVW 2018_


#### Acknowledgments:

The codes _pipeline_demo_01_json2h5.ipynb_ and _pipeline_demo_02_filter.ipynb_ have been modified to deal with 3D skeletons instead of 2D skeletons, but are originally written by Jan Zelinka and presented at WACV2020 conference. The associated paper is located here: https://openaccess.thecvf.com/content_WACV_2020/html/Zelinka_Neural_Sign_Language_Synthesis_Words_Are_Our_Glosses_WACV_2020_paper.html

When using the codes in your work, please cite the paper as:

@InProceedings{Zelinka_2020_WACV,  
  author = {Zelinka, Jan and Kanis, Jakub},  
  title = {Neural Sign Language Synthesis: Words Are Our Glosses},  
  booktitle = {The IEEE Winter Conference on Applications of Computer Vision (WACV)},  
  month = {March},  
  year = {2020}  
}


The codes _pipeline_rotate.ipynb_ and _pipeline_scale.ipynb_ have been adapted from previous work done by Mireia Hernández [(github repo)](https://github.com/imatge-upc/3D_skeleton_conversion)




