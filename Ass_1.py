#  1 & 2 task
def main():
    try:
        a = float(input("Enter numerator: "))
        b = float(input("Enter denominator: "))

        if b == 0:
            raise ZeroDivisionError("Error: Cannot divide by zero")
        else:
            c = a / b
            print(f"Answer is: {c}");
    except ZeroDivisionError as e:
        print(e);
    except ValueError:
        print("Invalid input. Please enter numeric values.");
if __name__ == "__main__":
    main()
else:
    print("Error");


# // 3rd task -->
# /*Suppose, we have to open a file with the help of the file explorer.
# we use the constructor which open the folder. if, there is a problem while 
# opening the file, the catch statement provide error message to the user
# and finally statement ensures that the file is successfully close. */


# //4th task -->
# suppose, we take a program in which we have to manage a library.
# we have to check weather a user enter a correct book name and also
# check the author name or book title is mentioned in the book for checking
# purpose.
