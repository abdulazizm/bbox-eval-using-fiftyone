# ValueError: Dataset name 'xxxxx' is not available
# In case of above error, just try again. Hope 51 team will fix this soon
import fiftyone as fo
import fiftyone.utils.coco as fouc

# Tested bbox detections with fiftyone : 0.22.3
# Format - https://cocodataset.org/#format-data

# COCO ground truth
data_path = 'DataSet1/coco_format/images'
labels_path = 'DataSet1/coco_format/annotations/instances_val.json'

# COCO predictions - make sure you added predictions json with labels and image id - same format as ground truth COCO json
pred_filepath = "DataSet1/coco_format/predictions/predictions.json"

classes = ['void', 'person', 'car', 'truck', 'motorcycle', 'bicycle']

dataset = fo.Dataset.from_dir(
    data_path=data_path,
    labels_path=labels_path,
    dataset_type=fo.types.COCODetectionDataset,
    label_field="ground_truth",
    label_types="detections",
    name="DataSet1",
)

# Predictions' image_id should be indexed from 1, 2, 3, 4, ... [not MS COCO's restriction, but from Voxel51], so better edit Ground truth dataset as well to start image_id from index=1
fouc.add_coco_labels(
    dataset,
    labels_or_path=pred_filepath,
    label_field="pred",
    classes=classes,
    label_type="detections",
)

results = dataset.evaluate_detections(
    "pred",
    gt_field="ground_truth",
    eval_key=f"eval_pred",
)

eval_patches = dataset.to_evaluation_patches(f"eval_pred") # calculate confusion matrix
print(eval_patches.count_values("type")) # this will print {'fp': x, 'tp': y, 'fn': z}

# for visualization
session = fo.launch_app(dataset, desktop=True)
session.view = eval_patches
session.wait()
