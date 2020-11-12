lists = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20,
         21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40]
add = [1, 2, 3, 38, 39, 40]
bev = []
num = 40
for i in range(0, num):
    print(i)

    print('hi  ' + str(num))

    for x in range(0, len(add)):
        if add[x] == lists[i]:
            print('hi')
            lists.pop(lists[i])
        if len(lists) != num:
            num -= num


print(lists)
