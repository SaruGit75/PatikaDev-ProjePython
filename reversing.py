def rev(x):
    for i in range(len(x)):
        if type(x[i]) == list:
            x[i].reverse()
    x.reverse()
    return x

liste = [[1, 2], [3, 4], [5, 6, 7]]
print(rev(liste))
