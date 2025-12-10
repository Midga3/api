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
def форрейндж(i1, i2):
    for i in range(i1):
        exec(str(i2))
def форин(i1, i2):
    for i in i1:
        exec(str(i2))
def макс(i1):
    return(max(i1))
def мин(i1):
    return(min(i1))
def 
M = []
for i in range(1016, 7938):
    if i % 3 == 0 and i % 7 != 0 and i % 17 != 0 and i % 19 != 0 and i % 27 != 0:
      M.append(i)
принт(M)
принт(кол(M))
принт(макс(M))
ифравно(1, 1, print("Hello!"))
