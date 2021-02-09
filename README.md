## 2D to 3D lifting of sign language body poses


The goal of this project is to predict the depth of skeleton poses extracted from American Sign Language videos. That means going from 2D skeletons to 3D skeletons.

This project also tackles the reconstruction of 3D skeleton keypoints from videos. In the folder _preprocessing_ we can find a method that reconstructs missing points and corrects misplaced keypoints.


### Content:

- **Train_net_*.ipynb**: (M and J are have the same code, the only think that changes is the data loaded). Notebook to prepare the data and train the model stored in the folder _Model_ using the parameters and functions stored in _Train_.

- **Evaluation.ipynb**: Loads the models trained with the other notebook and stored in _Output_ and evaluates them using test data. The method used is PCK [(explanation)](https://github.com/cbsudux/Human-Pose-Estimation-101#percentage-of-correct-key-points---pck).

- **Model/**: Implementation of a LSTM neural network in pytorch.

- **Train/**: Train and test function for the LSTM neural network as well as the hyperparameters configuration. It implements _stateful training_: the hidden states of the network are not reseted between consecutive batches, keeping the information along the whole video. It also accounts for videos ending in the middle of a batch, reseting the hidden state in these cases. 

- **Output/**: Stores the trained models and the train and validation losses.

- **Preprocessing/**: Folder that contains the code needed to load, preprocess and transform the data in order to train it. There is a separate README.md file in this folder that better explains the steps taken.


#### Acknowledgments:


The codes in the folder Models and Train have been adapted from previous work done by [Mireia Hernández](https://github.com/mireiahernandez) [(github repo)](https://github.com/imatge-upc/3D_skeleton_conversion)


The codes in _Preprocessing/pipeline_demo_01_json2h5.ipynb_ and _Preprocessing/pipeline_demo_02_filter.ipynb_ have been adapted to deal with 3D skeletons instead of 2D skeletons but are originally written by Jan Zelinka and presented at WACV2020 conference. The associated paper is located here: https://openaccess.thecvf.com/content_WACV_2020/html/Zelinka_Neural_Sign_Language_Synthesis_Words_Are_Our_Glosses_WACV_2020_paper.html

When using the codes in your work, please cite the paper as:

@InProceedings{Zelinka_2020_WACV,  
  author = {Zelinka, Jan and Kanis, Jakub},  
  title = {Neural Sign Language Synthesis: Words Are Our Glosses},  
  booktitle = {The IEEE Winter Conference on Applications of Computer Vision (WACV)},  
  month = {March},  
  year = {2020}  
}




