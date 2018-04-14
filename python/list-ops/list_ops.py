def append(xs, ys):
    for y in ys:
        xs.append(y)
    return xs


def concat(lists):
    out = []
    for xs in lists:
        for item in xs:
            out.append(item)
    return out


def filter_clone(function, xs):
    out = []
    for x in xs:
        if function(x):
            out.append(x)
    return out


def length(xs):
    ll = 0
    for x in xs:
        ll += 1
    return ll


def map_clone(function, xs):
    out = []
    for x in xs:
        out.append(function(x))
    return out


def foldl(function, xs, acc):
    for x in xs:
        acc = function(acc, x)
    return acc


def foldr(function, xs, acc):
    for x in xs[::-1]:
        acc = function(x, acc)
    return acc


def reverse(xs):
    out = []
    for x in xs[::-1]:
        out.append(x)
    return out
