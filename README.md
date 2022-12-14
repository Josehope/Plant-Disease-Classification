
# Plant Disease Classification

This model is aimed at predicting plant disease from the following selected plants

[Corn', 'Pepper', 'Potato', 'Tomato').

 The dataset which was titled "PlantVillage" was gotten from kaggle

 The model was trained on #14650 images belonging to 16 classes, after the training process the model was evaluated on the test data set to test the accuracy of the model and the model score was 93% accuracy.

 The model was able to classify plant disease accurately, and the few times the model was not able to predict correctly the right plant disease, was when we have similar images for different diseases.

The frontend of this model for demonstration purpose was done using streamlit.
## Badges

Add badges from somewhere like: [shields.io](https://shields.io/)

[![MIT License](https://img.shields.io/badge/License-MIT-green.svg)](https://choosealicense.com/licenses/mit/)
[![GPLv3 License](https://img.shields.io/badge/License-GPL%20v3-yellow.svg)](https://opensource.org/licenses/)
[![AGPL License](https://img.shields.io/badge/license-AGPL-blue.svg)](http://www.gnu.org/licenses/agpl-3.0)


## Demo

This is a demo of how the model performes when hosted and run using streamlit

![](https://github.com/Josehope/Plant-Disease-Classification/blob/master/Screenshot/plant-disease-1.gif?raw=true)



Below is another demo of how the model performes

![](https://github.com/Josehope/Plant-Disease-Classification/blob/master/Screenshot/plant-disease-2.gif)


## Deployment

To deploy this project run

```bash
  pip install -r requirements.txt

  streamlit run streamlit_host.py
```

