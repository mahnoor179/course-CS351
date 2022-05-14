def largest(num1,num2):
    if (num1 >= num2):
       val = num1
    else:
       val = num2


    return val
if __name__ == "__main__":
    if largest(20,5) == 20 and largest(21,3)== 21:
        print("Test for largest() function was successful!!")
    else:
        print("The largest() function is not working properly")
