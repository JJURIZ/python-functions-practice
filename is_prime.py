def is_prime(num):
    if num >= 2:
        for i in range(2, num ):
            if (num % i) == 0:
                return False
        #after the complete for n loop
        return True
    else:
        return False

print(is_prime(11))