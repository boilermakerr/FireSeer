from unit_localization_tools import find_row_in_list,is_same_column

def unit_localization(floors,limit_number=0):
    result_containers = []
    col_num=0
    floors_bk=floors.copy()
    while floors:
        col_num+=1
        current_cols_containers = {}
        min_x1_cell = None
        min_x1_layer = -1
        for layer_idx, layer in enumerate(floors):
            if layer:
                cell = layer[0]
                if min_x1_cell is None or cell[0] < min_x1_cell[0]:
                    min_x1_cell = cell
                    min_x1_layer = layer_idx
        base_layer_d = min_x1_layer
        min_x1_layer=find_row_in_list(min_x1_cell,floors_bk)
        base_cell = min_x1_cell
        base_layer = min_x1_layer
        column_cells = {base_layer_d: [base_cell]}
        current_cols_containers["{}-{}".format(base_layer+1,col_num)] = [base_cell]
        for layer_idx_d, layer in enumerate(floors):
            layer_idx=find_row_in_list(layer[0],floors_bk)
            if layer_idx == base_layer:
                continue
            layer_column_cells = []
            for cell in layer:
                if is_same_column(base_cell, cell):
                    layer_column_cells.append(cell)
                    break
            if layer_column_cells:
                column_cells[layer_idx_d] = layer_column_cells
                current_cols_containers["{}-{}".format(layer_idx+1,col_num)] = layer_column_cells


        new_floors = []
        for layer_idx, layer in enumerate(floors):
            if layer_idx in column_cells:
                new_layer = [cell for cell in layer if cell not in column_cells[layer_idx]]
            else:
                new_layer = layer
            if new_layer:
                new_floors.append(new_layer)
        floors = new_floors
        if len(current_cols_containers)<= limit_number:
            col_num-=1
            continue

        result_containers.append(current_cols_containers)

    return result_containers

