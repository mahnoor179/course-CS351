def numcheck(num):
    if num > 0:
       return "Positive number"
    elif num == 0:
       return "Zero"
    else:
       return "Negative number"

if __name__ == "__main__":
    if numcheck(5)== "Positive number" and numcheck(2024)== "Positive number":
        print("Test for numcheck() function was successful!!")
    else:
        print("The numcheck() function is not working properly")
