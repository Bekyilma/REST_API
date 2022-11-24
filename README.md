# Webdev-II exercise: A Simple Deep learning REST API (Flask)
  A simple image classifier using pretrained Neural Network [ResNet50](https://keras.io/applications/#resnet50). More details about the model [here](https://blog.keras.io/building-a-simple-keras-deep-learning-rest-api.html).

## Credits
[Building a simple Keras + deep learning REST API](https://blog.keras.io/building-a-simple-keras-deep-learning-rest-api.html)

## Getting started
- Clone the repository.

### Install Miniconda


```sh
~$ curl https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh -o Miniconda3-latest-Linux-x86_64.sh
~$ bash Miniconda3-latest-Linux-x86_64.sh
```

### Create a conda environment
```sh
~$ conda create --name yourenvname python=3.9
```
```sh
~$ conda activate yourenvname
```

### Install requirements
```sh
~$ pip3 install -r requirements.txt
```
For those who use different CPU architecture such as Apple Silicon M1/M2, you may encounter an issue with tensorflow. You can install requirements separately using conda, such as: 

```sh
~$ conda install -c conda-forge tensorflow
~$ conda install -c anaconda flask
~$ conda install -c anaconda pillow
```

### Run

```
~$ python3 app.py
```
Open up browser and go to:
```
http://127.0.0.1:5000.
```

* Upload a picture and click submit.

![2022-11-25](static/demo.png)


