import csv

annotations = {}

with open("/home/grajebhosle/Documents/IPML/Projects/Tracking/Annotation_For3Class.csv") as csvfile:
    reader = csv.reader(csvfile)
    next(reader)  # Skip header row
    for row in reader:
        image_path, x1, x2, y1, y2, class_id = row
        if class_id =="ADVISORY SPEED MPH":
            class_id=0
            
        if class_id =="DIRECTIONAL ARROW AUXILIARY":
            class_id=1
        if class_id =="DO NOT ENTER":
            class_id=2         
        
        
        # convert the bounding box coordinates into YOLO format
        x_center = (float(x1) + float(x2)) / 2
        x_center=x_center/1920
        y_center = (float(y1) + float(y2)) / 2
        y_center=y_center/1080
        width = float(x2) - float(x1)
        width=width/1920
        height = float(y2) - float(y1)
        height=height/1080
        if image_path not in annotations:
            annotations[image_path] = []
        annotations[image_path].append([class_id,(x_center),(y_center),(width),(height)])

for image_path, annots in annotations.items():
    with open("/home/grajebhosle/Documents/IPML/Projects/Tracking/data/{}.txt".format(image_path), "w") as annotfile:
        for annot in annots:
            annotfile.write(" ".join(str(x) for x in annot) + "\n")

