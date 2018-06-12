def sum_of_multiples(limit, multiples):
    sum_list = []
    for i in range(limit):
        for j in multiples:
            if i%j == 0:
                sum_list.append(i)
                break
    return sum(sum_list)
