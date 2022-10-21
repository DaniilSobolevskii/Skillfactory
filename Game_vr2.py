playground =[
    ["#", "1",  "2",  "3"],
    ["1", "_",  "_",  "_"],
    ["2", "_",  "_",  "_"],
    ["3", "_",  "_",  "_"]
]
def hi():
    print()
    print("Добро подаловать в игру 'Крестики- Нолики'")
    print("Побеждает игрок, чьи символы выстроятся в ряд из трех ")
    print("Ряд может быть собран по вертикали, горизонтали и по диагонали ")
    print()
    print()
hi()
def show():
    for row in playground:
        print(*row)
    #for a in range (4):
    #    row = "  ".join(playground[a])
     #   print(row)
        #print(playground[a][0], playground[a][1],playground[a][2], playground[a][3])




def move():
    while True:
        cords = input("     Введите координаты через пробел: ").split()

        if len(cords) != 2:
            print("Координат должно быть 2!")
            continue

        x, y = cords

        if not(x.isdigit()) or not(y.isdigit()):
            print ("Введите число!")
            continue

        x, y = int(x), int(y)

        if 0>x or  x>3 or 0>y or y>3:
            print ("Координаты вне диапозона")
            continue

        if playground[x][y] != "_":
            print("Клетка занята!")
            continue
        return x, y



def win():
    win_cords =  [((1,1), (2,2), (3,3)),((1,3), (2,2), (3,1)), ((1,1), (1,2), (1,3)),
                  ((1,1), (2, 1), (3,1)), ((1,2), (2,2), (3,2)), ((1,3), (2,3),(3,3)),
                  ((2,1), (2,2), (2,3)), ((3,1), (3,2), (3,3))]

    for cords in win_cords:
        symbols= []
        for i in cords:
            symbols.append(playground[i[0]][i[1]])
        if symbols == ["X", "X", "X"]:
            print('Выиграл первый игрок!')
            show()
            return True
        if symbols == ["0", "0", "0"]:
            print('Выиграл второй игрок!')
            return True
    return False
win()



num = 0
while True:
    num +=1

    show()


    if num % 2 ==1:
        print()
        print("Ходит первый игрок")
    else:
        print()
        print("Ходит второй игрок")

    x, y = move( )
    if num % 2 == 1:
        playground[x][y] = 'X'
    else:
        playground[x][y] = '0'

    if win():
        break

    if num == 9:
        break
        print("ничья")




