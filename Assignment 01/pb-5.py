def draw_pyramid(n):
    for i in range(1, n+1):
        print('#' * i)

number = int(input("Enter a number: "))
draw_pyramid(number)
