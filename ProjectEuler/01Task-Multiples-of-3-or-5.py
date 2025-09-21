def sumof3n5(x:int) -> int:
    sum3n5 = 0
    for i in range(x):
        if i%3 == 0:
            sum3n5 += i
            # print(i)
        elif i%5 == 0:
            # print(i)
            sum3n5 += i
    return sum3n5

# the return is 3, 5, 6, and 9 -> 23
print(sumof3n5(10))
# the question is 233168
print(sumof3n5(1000))