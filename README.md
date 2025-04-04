# ULGP

## Dataset 
Dataset is ready to download at Baidu netdisk:

We can download it easily from this link: https://pan.baidu.com/s/1XRejqwCEgX4r-UMy5R9XlA?pwd=n3fh  pwd: n3fh

## Code
Now the floor classifacation, unit location and grid prediction code is ready !!!

## The deployment method of Nvidia Orin Nano

Model can be deployed by tensorRT_Pro-YOLOv8 framework https://github.com/Melody-Zhou/tensorRT_Pro-YOLOv8


1. Install environmental dependency tensorRT_Pro.
2. Convert the pytorch pt into onnx and deploy follow the repo tutorial.

### We import wrong manuscript version code when make the grid prediction video, so there is one line left out. 
By changing the column threshold from 0.5 to 0.3, the grid prediction lines can function properly.
