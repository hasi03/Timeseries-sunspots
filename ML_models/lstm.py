import tensorflow as tf

class LSTMModel:
    def __init__(self, input_shape, units, output_size, number_epochs, loss_function):
        self.input_shape = input_shape
        self.units = units
        self.output_size = output_size
        self.number_epochs = number_epochs
        self.loss_function = loss_function
        self.model = self.build_model()

    def build_model(self):
        model = tf.keras.Sequential([
            tf.keras.layers.LSTM(self.units, input_shape=self.input_shape),
            tf.keras.layers.Dense(self.output_size)
        ])
        model.compile(optimizer='adam', loss=self.loss_function)
        return model

    def train(self, x_train, y_train):
        self.model.fit(x_train, y_train, epochs=self.number_epochs)

    def predict(self, x_test):
        return self.model.predict(x_test)