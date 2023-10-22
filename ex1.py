num = 0
x = 2000

while x < 3201:
    if x % 7 == 0 and x % 5 != 0:
        if x == 3199:
            print(x, end=".")
        else:
            print(x, end=", ")
        num += 1
    x += 1

print("\nTotal count:", num)    
