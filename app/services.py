import keras
from keras_retinanet import models
from keras_retinanet.utils.image import read_image_bgr, preprocess_image, resize_image

import tensorflow as tf
import numpy as np

from tensorflow.python.client import device_lib

class Retinanet:

    def __init__(self, weigths, classes, backbone_name='resnet50'):
        self.model = models.load_model(weigths)
        
        self.graph = tf.get_default_graph()
        self.classes = classes

    def get_predictions(self, img, threshold=0.5):
        image = read_image_bgr(img)
        image = preprocess_image(image)
        image, scale = resize_image(image)
        
        with self.graph.as_default():
            boxes, scores, labels = self.model.predict_on_batch(
                np.expand_dims(image, axis=0)
            )
        
        boxes /= scale

        result = []

        for box, score, label in zip(boxes[0], scores[0], labels[0]):
            if score <= threshold:
                break
            
            b = box.astype(int)
            
            result.append({
                "bbox" : b.tolist(),
                "label" : self.classes[label],
                "score" : float(score)
            })

        return result