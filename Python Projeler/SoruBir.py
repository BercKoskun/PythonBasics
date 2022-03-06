### Bir listeyi düzleştiren (flatten) fonksiyon yazın. Elemanları birden çok katmanlı listelerden ([[3],2] gibi) oluşabileceği gibi, non-scalar verilerden de oluşabilir.
bl = []
def flattenfunction(l):
    for i in l:
        if type(i)==list:
            flattenfunction(i)
        else:
            bl.append(i)

flattenfunction ([[1,'a',['cat'],2],[[[3]],'dog'],4,5])
print(bl)
    


