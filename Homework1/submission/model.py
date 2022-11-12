import os
import tensorflow as tf

class model:
    def __init__(self, path):
        self.model = tfk.load_model(os.path.join(path, 'ANN_Homework1_Model'))

    def predict(X, Y):

        # Preprocessing

        out = self.model.predict(X)
        out = tf.argmax(out, axis=-1)

        return out