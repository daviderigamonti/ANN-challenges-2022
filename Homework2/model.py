import os
import tensorflow as tf
import numpy as np

class model:
    def __init__(self, path):
        self.model = tf.keras.models.load_model(os.path.join(path, 'ANN_Homework2_Model'))

    def predict(self, X):

        # Preprocessing 

        out = self.model.predict(X)
        out = tf.argmax(out, axis=-1)

        return out
