import os
import tensorflow as tf
import numpy as np

class model:
    def __init__(self, path):
        self.model = tf.keras.models.load_model(os.path.join(path, 'ANN_Homework1_Model'))

    def predict(self, X):

        # Preprocessing 
        X_scaled = X/255

        out = self.model.predict(X_scaled)
        out = tf.argmax(out, axis=-1)

        return out
