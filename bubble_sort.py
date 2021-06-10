import random
def bubble_sort(li):
    for i in range(len(li)-1): #第i趟
        exchange = False
        for j in range(len(li)-i-1): #箭头指到位置
            if li[j]>li[j+1]:
                li[j],li[j+1] = li[j+1], li[j]
                exchange = True
        print(li)
        if not exchange:
            return

li = [1,2,3,4,5,6,7,8,9]
print(li)
bubble_sort(li)
