def leapyear(year):

    if (year % 400 == 0) and (year % 100 == 0) or (year % 4 ==0) and (year % 100 != 0):
        return "is a leap year"

    else:
        return "is not a leap year"
if __name__ == "__main__":
    if leapyear(2000)== "is a leap year" and leapyear(2001)== "is not a leap year":
        print("Test for leapyear() function was successful!!")
    else:
        print("The leapyear() function is not working properly")
