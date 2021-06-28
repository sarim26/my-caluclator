
def addition():
    num1 = input("Enter a number")
    num2 = input("Enter a number to add")
    answer_add = float(num1) + float(num2)
    print(answer_add)
def subtract():
    num3 = input("enter a number")
    num4 = input("enter your second number")
    answer_substract = float(num3) - float(num4)
    print(answer_substract)

    def multiply():

        num5 = input("enter a number")
        num6 = input("enter your second number")
        answer_multiply = float(num4) * float(num6)
        print(answer_multiply)

        def divide():
            num7 = input ("enter a number")
            num8 = input ("enter your second number")
            answer_divide = float(num7) / float(num8)
            print(answer_divide)

            ask = input ("You want to add, subtract, multiply or divide numbers?")

            if ask == "add":
                add()

            elif ask == "subtract":
                subtract()

                if ask == "multiply":
                    multiply()

                elif ask == "divide":
                    divide()
