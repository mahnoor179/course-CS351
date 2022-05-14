def number(num):

    if (num % 2) == 0:
       return "is Even"
    else:
       return "is Odd" 

if __name__ == "__main__":
    if number(2)== "is Even" and number(7)== "is Odd":
        print("Test for number() function was successful!!")
    else:
        print("The number() function is not working properly")
