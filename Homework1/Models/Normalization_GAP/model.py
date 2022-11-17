import os
import tensorflow as tf
import numpy as np

class model:
    def __init__(self, path):
        self.model = tf.keras.models.load_model(os.path.join(path, 'ANN_Homework1_Model'))

    def predict(self, X):

        # Preprocessing
        mean = [87.67739, 95.358444, 88.99623]
        devstd = [54.538552, 55.0427897, 53.839036]
        X_normalized = (X - mean)/devstd
        X_scaled = X_normalized/255

        out = self.model.predict(X_scaled)
        out = tf.argmax(out, axis=-1)

        return out
