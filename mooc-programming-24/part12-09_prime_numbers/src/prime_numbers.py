def prime_numbers():
    def is_prime(n):
        for i in range (2, n):
            if n % i == 0:
                return False
            
        return True
    n = 2

    while True:
        if is_prime(n):
            yield n
        n += 1