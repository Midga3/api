def принт(n):
    print(n)
def ифравно(i1, i2, i3):
    if i1 == i2:
        exec(str(i3))
def ифравноиначе(i1, i2, i3, i4):
    if i1 == i2:
        exec(str(i3))
    else:
        exec(str(i4))
def иф(i1, i2):
    if f"{i1}":
        exec(str(i2))
def добавить(i1, i2):
    i1.append(i2)
def кол(i1):
    return(len(i1))
def форрейндж(i1, i2, i3):
    for i in range(i1, i2):
        exec(str(i2))
def форин(i1, i2):
    for i in i1:
        exec(str(i2))
def макс(i1):
    return(max(i1))
def мин(i1):
    return(min(i1))
def стоп():
    exit()
def запуск(i1):
    exec(str(i1))
M = []
for i in range(1813, 6861):
    if i % 5 == 0 and i % 6 != 0 and i % 10 != 0 and i % 15 != 0 and i % 23 != 0:
        добавить(M, i)
принт(M)
принт(кол(M))
принт(макс(M))
