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
    while(True):
        a = input("Enter The First Number : ")
        try:
            a = float(a)
            break
        except ValueError:
            print("Invalid input. Please enter a number.")

    while(True):
        b = input("Enter The Second Number : ")
        try:
            b = float(b)
            break
        except ValueError:
            print("Invalid input. Please enter a number.")

        

    return a, b
def  Calculate():

    option = input("Enter The Operation Number 1.+ 2.- 3.* 4./ 5.Exit : ")
    match option:
        case "1":
            a, b = get_input()
            print(Add(a,b))
        case "2":
            a, b = get_input()
            print(Subtract(a,b))
        case "3":
            a, b = get_input()
            print(Multiply(a,b))
        case "4":
            a, b = get_input()
            print(Divide(a,b))
        case "5":
            print("Exiting the calculator. Goodbye!")
            exit()
        case _:
            print("Invalid Option")
            

def main():
    while True:
        Calculate()

main()

