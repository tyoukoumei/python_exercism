def slices(series, length):
    slice_list = []
    if length <= 0 or length > len(series):
        raise ValueError("The length does not meet the requirements")
    else:
        for i in range(len(series) - length + 1):
            slice_list.append([int(j) for j in series[i:i+length]])
    return slice_list

