def add(x, y):
    ans = x + y
    print(x, "+", y, "=", ans)

def subtract(x, y):
    ans = x - y
    print(x, "-", y, "=", ans)

def multiply(x, y):
    ans = x * y
    print(x, "*", y, "=", ans)

def divide(x, y):
    ans = x / y
    print(x, "/", y, "=", ans)

while True:
    try:
        operation = input("\nEnter operation (m, d, s, a): ")
        x = input("\nEnter first digit: ")
        x = int(x)
        y = input("\nEnter second digit: ")
        y = int(y)
        if operation == "m":
            multiply(x, y)
        elif operation == "d":
            divide(x, y)
        elif operation == "s":
            subtract(x, y)
        elif operation == "a":
            add(x, y)
    except:
        print("\nError occurred")
    
