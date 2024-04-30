# Versions  
fiftyone: 0.22.3

# Input
Update the following variables in `main.py`
```
# COCO ground truth
data_path = 'DataSet1/coco_format/images'
labels_path = 'DataSet1/coco_format/annotations/instances_val.json'

# COCO predictions - make sure you added predictions json in same format as ground truth COCO JSON (with categories, images, and annotations tag)
pred_filepath = "DataSet1/coco_format/predictions/predictions.json"

classes = ['void', 'person', 'car', 'truck', 'motorcycle', 'bicycle']
```
Refer to COCO Format - https://cocodataset.org/#format-data

# Prerequisites  
```
sudo apt-get install python3-pip python3-venv
python3 -m venv venv
source venv/bin/activate
python3 -m pip install fiftyone
```
# Run
```
python3 main.py
```
Tested in Ubuntu 20.04 with Python 3.8.10  

# Credits 
*Voxel51* team - Thanks for developing such a great tool and contributing to open source world (https://voxel51.com/fiftyone/)  
