def get_average_box_area_delect_default_box(detections,threshold=0.3):

    if len(detections) == 0:
        return 0.0
    total_box_area = 0.0
    temp_box_area =[]
    for box in detections:
        box_area = abs(box[2] - box[0]) * abs(box[3] - box[1])
        total_box_area += box_area
        temp_box_area.append(box_area)
    avg_area=total_box_area / len(detections)
    x=avg_area*threshold
    new_detections = [row for i, row in enumerate(detections) if temp_box_area[i] >= x]
    return avg_area, new_detections


def is_same_row(cell1, cell2,threshold=0.5):
    y1_diff = abs(cell1[1] - cell2[1])
    thres=threshold*max(abs(cell1[3]-cell1[1]),abs(cell2[3]-cell2[1]))
    return y1_diff < thres
