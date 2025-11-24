Input = []
N = int(input("Enter the number of inputs: "))

for i in range(1, N+1):
    number = int(input(f"Enter number {i}: "))
    Input.append(number)

def Add():
    result = 0
    for i in Input:
        result += i
    print("Addition =", result)

def sub():
    result = Input[0]
    for i in Input[1:]:
        result -= i
    print("Subtraction =", result)

def mul():
    result = 1
    for i in Input:
        result *= i
    print("Multiplication =", result)

def div():
    result = Input[0]
    for i in Input[1:]:
        result /= i
    print("Division =", result)

def operations():
    print("1.Addition")
    print("2.Subtraction")
    print("3.Multiplication")
    print("4.Division")

operations()
op = int(input("Choose the operation (1–4): "))

if op == 1:
    Add()
elif op == 2:
    sub()
elif op == 3:
    mul()
elif op == 4:
    div()
else:
    print("Invalid option")
