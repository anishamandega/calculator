# importing libraries
import os.path


# defined my function
def calculator():
    # used a try except block
    while True:
        try:
            # printed the choices that my user has
            print("""
Please select one of the following  options:
view = would you like to all the equations in the text file
add  = would you like to add new sum into the text file 
exit = exist the calculator 
            """)
            # asked my user to input there choice
            choice = input("Enter here:").lower()

            # used a while loop make sure my user enters one of the options
            while choice not in ("view", "add", "exit"):
                print("The choice you have selected is invalid, please try again\n")

                # printed the options my user has
                print("""
Please select one of the following options:
view = would you like to all the equations in the text file
add  = would you like to add new sum into the text file  
exit = exist the calculator
                            """)

                # asked my user for input
                choice = input("Enter here:").lower()

            if choice in ("view", "add", "exit"):

                # used if statements
                if choice == "view":

                    print("You have selected to view the equations\n")

                    # asked my user for input
                    file_name = str(input("Please enter the name of the file:"))

                    # checked if my file was empty or not
                    # used if and else statement
                    if os.path.getsize(file_name) > 0:
                        print("The file is currently empty enter some equations first")

                    else:

                        # opened my file
                        file_name = open(file_name)
                        print(f"""
                        These are the current sums in the text file:

                        {file_name.read()}""")

                        # closed my file
                        file_name.close()

                elif choice == "add":

                    print("You have selected to add a new equation\n")

                    # asked my user to enter to numbers
                    num1 = int(input("Please enter a number:"))
                    num2 = int(input("Please a second number:"))

                    # printed the options they have
                    print("""
Please select one of the following options:
add      = adding the two numbers
subtract = subtracting the two numbers 
multiply = multiplying the two numbers
divide   = dividing the two numbers
                                                        """)

                    # asked the user to enter there choice
                    calculate = input("Enter here:").lower()

                    # used a while loop to make sure my user choices one of the options
                    while calculate not in ("add", "subtract", "multiply", "divide"):
                        print("The option you have selected doesnt exist please try again")

                        print("""
Please select one of the following options:
add      = adding the two numbers
subtract = subtracting the two numbers 
multiply = multiplying the two numbers
divide   = dividing the two numbers
                                """)
                        calculate = input("Enter here:")
                    if calculate in ("add", "subtract", "multiply", "divide"):

                        # opened my sums.txt file and appended to it
                        with open("sums.txt", "a") as files:

                            # used if and elif statement
                            if calculate == "add":

                                # added the two numbers inputted by the user
                                result = num1 + num2

                                # printed the results
                                print(f"The addition of {num1} + {num2} is equal {result}\n")

                                # wrote to my sums.txt file
                                files.write(f"The addition of {num1} + {num2} is equal to {result}\n")

                            elif calculate == "subtract":

                                # subtracted the two numbers inputted by the user
                                result = num1 - num2

                                # printed the results
                                print(f"The  subtraction of {num1} - {num2} is equal to {result}\n")

                                # wrote to my sums.txt file
                                files.write(f"The subtraction of {num1} - {num2} is equal to {result}\n")

                            elif calculate == "multiply":

                                # multiplied the two numbers inputted by the user
                                result = num1 * num2

                                # printed the results
                                print(f"The multiplication of {num1} * {num2} is equal to {result}\n")

                                # wrote to my sums.txt file
                                files.write(f"The multiplication of {num1} * {num2} is equal to {result}\n")

                            elif calculate == "divide":

                                # divided the two numbers my user entered
                                result = num1 / num2

                                # printed the results
                                print(f"The division of {num1}/{num2} is equal to {result}\n")

                                # wrote to my sums.txt file
                                files.write(f"The division of {num1}/{num2} is equal to {result}\n")

                # gave my user a choice to exit the program
                elif choice == "exit":
                    print(f"""You have selected to exit the calculator
Bye!!""")
                    exit()
                    break

        # handles ValueError exceptions
        except ValueError:
            print("You have entered an invalid input please try again")

        # handles ZeroDivisionError exceptions
        except ZeroDivisionError:
            print("You can't divide by zero, please try again")

        # handles FileNotFoundError exceptions
        except FileNotFoundError:
            print("The file you have entered doesn't exist, please try again")

        # handles others exceptions
        except Exception:
            print("You have entered a wrong input, please try again")


# called my function
calculator()



