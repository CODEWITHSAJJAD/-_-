import tkinter as tk
def FIBONACCI_GENERATOR(num):
    if num==0:
        return 0
    elif num==1:
        return 1
    else:
        return FIBONACCI_GENERATOR(num-1)+FIBONACCI_GENERATOR(num-2)


if __name__ == '__main__':
    num = int(input("please enter a number to generate its FIBONACCI Sequence:"))
    print(f"Your FIBONACCI Sequence for number {num} is:")
    for i in range(num):
        print(FIBONACCI_GENERATOR(i))
