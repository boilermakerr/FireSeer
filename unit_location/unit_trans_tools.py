
def find_row_in_list(cell,floors):
    for i,floor in enumerate(floors):
        if cell in floor:
            return i
def is_same_column(cell1, cell2,threshold=0.5):
    x1_diff = abs(cell1[0] - cell2[0])
    thres=threshold*max(abs(cell1[2]-cell1[0]),abs(cell2[2]-cell2[0]))
    return x1_diff < thres


