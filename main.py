sonlar = [1, 2, 3, 4, 5]
vaznlar = [2, 3, 4, 5, 6]
umumiy_ogirlik = sum(a * b for a, b in zip(sonlar, vaznlar))
print(umumiy_ogirlik)
