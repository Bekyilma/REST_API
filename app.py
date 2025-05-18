#!/usr/bin/env python3
# coding: utf-8

from keras.applications import ResNet50
from tensorflow.keras.utils import img_to_array
from keras.applications import imagenet_utils
from PIL import Image
import numpy as np
import flask
from flask import render_template, request
import io
import os

# Ignore AVX AVX2 warning
os.environ["TF_CPP_MIN_LOG_LEVEL"] = "2"

# Initialize Flask app and global model
app = flask.Flask(__name__)
model = None

UPLOAD_FOLDER = os.path.join(app.root_path, "static", "img")
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER


def load_model():
    global model
    model = ResNet50(weights="imagenet")


def prepare_image(image, target):
    if image.mode != "RGB":
        image = image.convert("RGB")

    image = image.resize(target)
    image = img_to_array(image)
    image = np.expand_dims(image, axis=0)
    image = imagenet_utils.preprocess_input(image)
    return image


@app.route("/", methods=["POST", "GET"])
def predict():
    data = {"success": False}
    title = "Upload an image"
    name = "default.png"

    if request.method == "POST":
        if request.files.get("image"):
            image_file = request.files["image"]
            image_path = os.path.join(app.config["UPLOAD_FOLDER"], image_file.filename)
            image_file.save(image_path)

            with open(image_path, "rb") as f:
                image = Image.open(io.BytesIO(f.read()))

            processed_image = prepare_image(image, target=(224, 224))

            # Run prediction
            preds = model.predict(processed_image)
            results = imagenet_utils.decode_predictions(preds)
            data["predictions"] = []

            for (imagenetID, label, prob) in results[0]:
                r = {"label": label, "probability": float(prob)}
                data["predictions"].append(r)

            data["success"] = "Uploaded"
            title = "Prediction Results"
            name = image_file.filename

            return render_template("index.html", data=data, title=title, name=name)

    return render_template("index.html", data=data, title=title, name=name)


if __name__ == "__main__":
    print("* Loading Keras model and Flask starting server...please wait until server has fully started.")
    load_model()
    app.run(debug=True)

