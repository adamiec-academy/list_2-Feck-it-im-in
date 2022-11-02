def is_prime(n):
    if n > 1:
        for j in range(2, int(n / 2) + 1):
            if (n % j) == 0:
                return False
        else:
            return True
    else:
        return False


def is_diabolic(n):
    return
#not yet done
