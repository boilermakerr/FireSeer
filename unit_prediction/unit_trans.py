from unit_trans_tools import find_median_minimizing_sum_of_absolute_deviations,remove_outliers


def unit_prediction(data):
    max_rows=0
    max_cols=len(data)
    for col in data:
        for key, value in col.items():

            row_num,c = key.split('-')
            max_rows =max(max_rows,int(row_num))
    empty_list = [[[] for _ in range(max_cols)] for _ in range(max_rows)]
    rc_info=(max_rows,max_cols)
    for col in data:
        for key,value in col.items():
            row,col=key.split('-')
            row,col=int(row)-1,int(col)-1
            empty_list[row][col]=value

    hang_dian_jihe = []
    temp_list2 = []
    for i, row in enumerate(empty_list):

        if i == 0:
            temp_list = []
            for j in row:
                for k in j:
                    temp_list.append(k[3])
                    temp_list2.append(k[1])
            temp_list = remove_outliers(temp_list)
            median = find_median_minimizing_sum_of_absolute_deviations(temp_list)
            hang_dian_jihe.append(median)

        elif i == len(empty_list) - 1:
            temp_list = []
            for j in row:
                for k in j:
                    temp_list.append(k[1])
                    temp_list2.append(k[3])
            temp_list2 = remove_outliers(temp_list2)
            median = find_median_minimizing_sum_of_absolute_deviations(temp_list2)
            hang_dian_jihe.append(median)
            temp_list = remove_outliers(temp_list)
            median = find_median_minimizing_sum_of_absolute_deviations(temp_list)
            hang_dian_jihe.append(median)

        else:
            temp_list = temp_list2.copy()
            temp_list2 = []
            for j in row:
                for k in j:
                    temp_list.append(k[3])
                    temp_list2.append(k[1])

            temp_list = remove_outliers(temp_list)
            median = find_median_minimizing_sum_of_absolute_deviations(temp_list)
            hang_dian_jihe.append(median)
    lie_dian_jihe = []
    temp_list2 = []

    for i in range(max_cols):

        if i == 0:
            temp_list = []
            for j in range(max_rows):
                for k in empty_list[j][i]:
                    temp_list.append(k[0])
                    temp_list2.append(k[2])
            temp_list = remove_outliers(temp_list)
            median = find_median_minimizing_sum_of_absolute_deviations(temp_list)
            lie_dian_jihe.append(median)
        elif i == max_cols - 1:
            temp_list = []
            for j in range(max_rows):
                for k in empty_list[j][i]:
                    temp_list.append(k[2])
                    temp_list2.append(k[0])
            temp_list2 = remove_outliers(temp_list2)
            median = find_median_minimizing_sum_of_absolute_deviations(temp_list2)
            lie_dian_jihe.append(median)
            temp_list = remove_outliers(temp_list)
            temp_list = remove_outliers(temp_list)
            median = find_median_minimizing_sum_of_absolute_deviations(temp_list)
            lie_dian_jihe.append(median)

        else:
            temp_list = temp_list2.copy()
            temp_list2 = []
            for j in range(max_rows):
                for k in empty_list[j][i]:
                    temp_list.append(k[0])
                    temp_list2.append(k[2])
            temp_list = remove_outliers(temp_list)
            median = find_median_minimizing_sum_of_absolute_deviations(temp_list)
            lie_dian_jihe.append(median)
    return (hang_dian_jihe,lie_dian_jihe),rc_info


