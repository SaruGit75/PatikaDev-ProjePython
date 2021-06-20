def flatten(top):

    for i in top:
        if isinstance(i, list):
            print(i)
            yield from flatten(i)
        else:
            yield i

liste = [[1,'a',['cat'],2],[[[3]],'dog'],4,5]

duz_liste = [i for i in flatten(liste)]
print(duz_liste)
