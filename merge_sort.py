def merge(li, low, mid, high):
    # 一次归并，前提是两个有序列表
    # low到mid是一段有序列表，mid+1到high是另一段有序列表
    # 初始化i和j所指的位置
    i = low
    j = mid+1
    ltmp = []
    while i<=mid and j<=high:#只要左右两边都有数，那就比一下这两数
        if li[i] < li[j]:
            ltmp.append(li[i])
            i += 1
        else:
            ltmp.append(li[j])
            j += 1
    # while执行完后，两个有序列表肯定有一个没数了
    while i <= mid:
        ltmp.append(li[i])
        i += 1
    while j <= high:
        ltmp.append(li[j])
        j += 1
    li[low:high+1] = ltmp

# li = [2,4,5,7,1,3,6,8]
# merge(li,0,3,7)
# print(li)

def merge_sort(li,low,high):
    if low < high: #至少有两个元素，递归
        mid = (low+high)//2
        merge_sort(li,low,mid)
        merge_sort(li,mid+1,high)
        merge(li,low,mid,high)

li = list(range(1000))
import random
random.shuffle(li)
print(li)
merge_sort(li,0,len(li)-1)
print(li)