def cube(num):
    return num ** 3
def bythree(num):
    if num % 3 == 0:
        return cube(num)
    else:
        return False
print(bythree(9))
print(bythree(4))