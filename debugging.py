def divisors(num):

    divisors = [ i for i in range(1, num + 1) if num % i == 0 ]

    return divisors


def run():

    try:

        num = input("Ingresa un numero: ")

        assert num.isnumeric(), "Debes ingresar un numero"

        if int(num) < 0:
            raise ValueError("Debes ingresar numeros positivos")

        print(divisors(int(num)))
        print("terminado")
    
    except ValueError  as ve:
        print(ve)

if __name__ == "__main__":
    run()