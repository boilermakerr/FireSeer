import numpy as np

def find_median_minimizing_sum_of_absolute_deviations(numbers):
    sorted_numbers = sorted(numbers)
    n = len(sorted_numbers)

    if n % 2 == 1:
        median = sorted_numbers[n // 2]
    else:
        mid1 = sorted_numbers[n // 2 - 1]
        mid2 = sorted_numbers[n // 2]
        median = (mid1 + mid2) / 2

    return median

def remove_outliers(data,std_coefficent=2):
    data=np.array(data)
    mean = np.mean(data)
    std_dev = np.std(data)

    threshold_low = mean - std_coefficent * std_dev
    threshold_high = mean + std_coefficent * std_dev

    filtered_data = [x for x in data if threshold_low <= x <= threshold_high]
    return filtered_data