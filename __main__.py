from simplennet.neural_network import NeuralNetwork
import numpy as np

input_train_scaled = np.load('data/input_train_scaled.npy')
output_train_scaled = np.load('data/output_train_scaled.npy')
input_test_scaled = np.load('data/input_test_scaled.npy')
output_test_scaled = np.load('data/output_test_scaled.npy')
input_pred = np.load('data/input_pred.npy')

nn = NeuralNetwork()
nn.train(input_train_scaled, output_train_scaled, 200)
nn.predict(input_pred)
nn.view_error_development()
nn.test_evaluation(input_test_scaled, output_test_scaled)