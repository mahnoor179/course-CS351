def prime(num):
    check = False
    if num > 1:
        for i in range(2, num):
            if (num % i) == 0:
                check = True
                break
    if check:
        return "not prime number"
    else:
        return "is prime number"
if __name__ == "__main__":
    if prime(3)=="is prime number" and prime(29)=="is prime number":
        print("Test for prime() function was successful!!")
    else:
        print("The prime() function is not working properly")
