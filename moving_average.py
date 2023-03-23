def moving_average(vals: list):
    total_sum = 0
    for x in vals:
        total_sum += x
    return total_sum/len(vals)