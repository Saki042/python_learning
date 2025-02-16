#Print with separator
print("Isha", 2, 95.78, True, sep="\n")

#Check even or odd
n = int(input("Take input: "))
if n%2==0:
    print("evn")
else:
    print("odd")

#Find second largest 
def second_smallest(arr):
    first, second = float('inf'), float('inf')
    for num in arr:
        if num < first:
            second = first
            first = num
        elif  first < num < second:
            second = num
    return second
arr = [3, 40, 54, 6, 8, 29, 39]
print(second_smallest(arr))

# 