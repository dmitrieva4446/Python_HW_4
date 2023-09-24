'''
Требуется найти в массиве list_1 самый близкий по величине элемент к заданному числу k и вывести его.
'''

list_1 = [1, 4, 3, 10, 8, 6, 5, 2]
k = 8
t = True


for i in range(0, len(list_1)):
    if list_1[i] == k:
        print(list_1[i])
        t = False
c = 1
while c < k and t:
# if t:
    for i in range(0, len(list_1)):
        if list_1[i] == k - c:
            print(list_1[i])
            t = False
        if list_1[i] == k + c:
            print(list_1[i])
            t = False
    c += 1