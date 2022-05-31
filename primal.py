def its_prime(number: int) -> bool:
    # result=[i for i in range(1, number+1) if number % i == 0]
    # return len(result)==2
    for i in range(2,number):
        if number % i == 0:
            return False
        return True
    return False


def run():
    print(its_prime("Comida"))

if __name__ == '__main__':
    run()
