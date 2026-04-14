def Add(a,b):
    return a + b
def Subtract(a,b):
    return a - b
def Multiply(a,b):
    return a * b
def Divide(a,b):
    if b == 0:
        return "Error: Division by zero is not allowed."    
    return a / b

def get_input():
    a = float(input("Enter The First Number : ")).strip()
    if not isinstance(a, float):#ckeck if the input is a number
        print("Invalid input. Please enter a number.")
        return get_input()

    b = float(input("Enter The Second Number : ")).strip()
    if not isinstance(b, float):
        print("Invalid input. Please enter a number.")
        return get_input()

    return a, b
def  Calculate():

    option = (int)(input("Enter The Operation Number 1.+ 2.- 3.* 4./ 5.Exit : "))
    match option:
        case 1:
            a, b = get_input()
            b = float(input("Enter The Second Number : "))
            print(Add(a,b))
        case 2:
            a, b = get_input()
            print(Subtract(a,b))
        case 3:
            a, b = get_input()
            print(Multiply(a,b))
        case 4:
            a, b = get_input()
            print(Divide(a,b))
        case 5:
            print("Exiting the calculator. Goodbye!")
            exit()
        case _:
            print("Invalid Option")
            

def main():
    while True:
        Calculate()

main()

