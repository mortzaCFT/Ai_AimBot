# The main idea of this aim bot is using image procesing to analyze the video source real time,
# And when the object detected, then program simulate a mouse click at the center of the object or other part of the object.
# So, we need train ai, to create an pre trained weights using yolov5 to detect objets from source( i mean games.)

import torch

model = torch.hup.load("ultralytics/yolov5", 'yolov5s', pretrained = True)

# You should use your own images.
# In this cheat, database is really valuble thing.
# the database images also should have labels,and other matter stuff...
images = ['','',''...]

results = model(images)

results.print()
results.show()

results.xyxy[0]

# Also for train those images , you should know how to specifying dataset.
# I used COCO128 train. example of coco128.yaml(this file should be on your dataset):

# path : ../.../<the path of dataset root>
# train: <name of your group images(like class)>
# val: <name your value images.>

# nc: <number of classes>
# names: [ "<name of your objects>",...]



# For training, you should run this commend on your device:
# python train.py --img 640 --batch 16 --epochs 5 --data <name of your cocotrain.yaml file> --weights yolov5s.pt
