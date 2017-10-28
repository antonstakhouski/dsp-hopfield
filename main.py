#!/usr/bin/env python3

import numpy as np
import os
import matplotlib.image as mpimg


class HopfieldNetwok:
    def __init__(self):
        self.n = 100
        self.entry_layer = np.zeros(self.n)
        self.neurons = np.zeros(self.n)
        self.weights = np.zeros((self.n, self.n))
        self.m = 3
        self.test_images = np.zeros((self.m, 10, 10))
        self.test_dir = "original/"

    def load_test_images(self):
        for _, _, files in os.walk(self.test_dir):
            i = 0
            for _file in files:
                f = mpimg.imread(self.test_dir + _file)[:, :, 0]
                self.test_images[i] = f
                for y in range(0, 10):
                    for x in range(0, 10):
                        if self.test_images[i, y, x] == 0:
                            self.test_images[i, y, x] = -1
                i += 1

    def train(self):
        for i in range(0, self.n):
            for j in range(i + 1, self.n):
                s = 0

                if i != j:
                    for k in range(0, self.m):
                        s += self.test_images[k].ravel()[i] * self.test_images[k].ravel()[j]
                self.weights[i, j] = s
                self.weights[j, i] = self.weights[i, j]

    def run(self):
        self.load_test_images()
        self.train()
        print(self.weights)


net = HopfieldNetwok()
net.run()
