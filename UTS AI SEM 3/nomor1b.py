# -*- coding: utf-8 -*-
"""nomor1b.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1B027-ydCMDchI76RfgsWHRzEy8QzOG_A
"""

# Rafie Mirza Ramadhan - 21091397037
# No. 1B

#multi neuron, multi perceptron

##memulai numpy
import numpy as np

#memasukkan variabel yang diinginkan
inputs = [1.5, 3.5, 2.5, 1.2, 3.3, 3.8, 4.1, 4.0, 5.1, 6.4]

weights = [[-0.25, 2.3, 4.3, 2.2, -2.1, 8.0, 4.5, 5.3, 2.9, 4.4],
           [-1.5, 2.6, 4.8, -1.2, 9.0, 2.4, 1.3, 0.5, 1.9, 2.7],
           [9.5, -0.3, 0.65, -7.3, 6.1, 2.0, 7.0, -6.0, -2.6, -1.0],
           [-0.2, 1.1, 2.1, 3.9, 1.8, -8.6, 4.6, -9.0, 3.1, 0.35],
           [-4.5, 4.2, 3.0, -8.1, 6.4, 9.7, 7.3, 4.5, 6.2, -0.32]]

#penggunaan bias untuk neuronnya
biases = [9.6, 0.3, 0.2, 8.8, 8.4]

#proses perhitungan output
output = np.dot(weights, inputs) + biases

#pemanggilan output
print(output)