if __name__ == '__main__':
    n = int(input())
    number = ""
    if 1 <= n <= 150:
        x = 1
        while x <= n:
            print(x, end="")
            x += 1
    else:
        print("Enter the number between 1 to 150")
