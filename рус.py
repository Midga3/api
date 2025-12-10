def принт(n):
    print(n)
def ифравно(i1, i2, i3):
    if i1 == i2:
        exec(str(i3).replace(" и ", " and "))
def ифравноиначе(i1, i2, i3, i4):
    if i1 == i2:
        exec(str(i3).replace(" и ", " and "))
    else:
        exec(str(i4))
def иф(i1, i2):
    if f"{i1}":
        exec(str(i2).replace(" и ", " and "))
def добавить(i1, i2):
    i1.append(i2)
def кол(i1):
    return(len(i1))
def форрейндж(i1, i2, i3):
    for i in range(i1, i2):
        exec(str(i3).replace(" и ", " and "))
def форин(i1, i2):
    for i in i1:
        exec(str(i2).replace(" и ", " and "))
def макс(i1):
    return(max(i1))
def мин(i1):
    return(min(i1))
def стоп():
    exit()
def запуск(i1):
    exec(str(i1))
def ввод(i1):
    return(input(i1))
def инт(i1):
    return(int(i1))
M = [1]
ифравно(1, 1, '''if 1 == 1 и 1 == 1:
    print(2)''')
принт(M)
принт(кол(M))
принт(макс(M))
