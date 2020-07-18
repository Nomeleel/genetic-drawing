import cv2
import os
import time
from IPython.display import clear_output
from genetic_drawing import *

#load the example image and set the generator for 100 stages with 20 generations each
gen = GeneticDrawing('example.jpg', seed=time.time())
out = gen.generate(100, 20)

#load a custom mask and set a smaller brush size for finer details
gen.sampling_mask = cv2.cvtColor(cv2.imread("mask.jpg"), cv2.COLOR_BGR2GRAY)
gen.brushesRange = [[0.05, 0.1], [0.1, 0.2]]
#keep drawing on top of our previous result
out = gen.generate(40, 30)

#save all the images from the image buffer
if not os.path.exists('out'):
    os.mkdir("out")
for i in range(len(gen.imgBuffer)):
    cv2.imwrite(os.path.join("out", f"{i:06d}.png"), gen.imgBuffer[i])
#if you want to save only last image, run below
# cv2.imwrite("out/final.png', out)