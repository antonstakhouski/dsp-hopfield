#!/usr/bin/env python3

import matplotlib.image as mpimg
import os
import random


class Noizer:
    def __init__(self):
        self.src_dir = "original/"
        self.dst_dir = "noized/"
        self.noize_levels = [10, 20, 30, 35, 40, 45, 50, 60, 70, 80, 90, 100]
        self.orig_images = []

    def open_images(self):
        for root, dirs, files in os.walk(self.src_dir):
            for _file in files:
                f = mpimg.imread(self.src_dir + _file)
                self.orig_images.append((f, _file))

    def add_noize(self, pic):
        for lvl in self.noize_levels:
            self.add_noize_lvl(pic, lvl)

    def add_noize_lvl(self, pic, level):
        image = pic[0].copy()
        name = pic[1]
        name.replace(".png", str(level) + ".png")
        width, height, _ = image.shape
        for y in range(0, height):
            for x in range(0, width):
                val = random.uniform(0.0, 1.0)
                if val <= level / 100:
                    image[y][x] = 1.0
        mpimg.imsave(self.dst_dir + name, image)

    def run(self):
        self.open_images()
        for pic in self.orig_images:
            self.add_noize(pic)
        #  print(self.orig_images[0][0])
        pass


noizer = Noizer()
noizer.run()
