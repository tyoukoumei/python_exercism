def sieve(limit):
    limit_list = []
    if limit == 1:
        return limit_list
    elif limit == 2:
        limit_list.append(2)
        return limit_list
    else:
        for i in range(2,limit+1):
            a = 0
            for j in range(2,i-1):
                if i % j == 0:
                    a = 1
                    break
            if a == 0:
                limit_list.append(i)
        return limit_list
