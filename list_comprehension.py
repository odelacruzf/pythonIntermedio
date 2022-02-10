

def run():

    #forma normal
    #squares =[]
    
    #for i in range(1, 101):
        #if i % 3 != 0:
            #squares.append(i**2)

    #utilizando list comprehension
    squares = [i**2 for i in range(1,101) if i % 3 != 0]
    
    print(squares)

    #Multiplos de 4 que a la vez sean tambien multiplos de 6 y 9, hasta 5 digitos

    multiplos = [ i for i in range(1, 100000) if i % 4 == 0 and i % 6 == 0 and i % 9 == 0 ]

    print(multiplos)


if __name__ == "__main__":
    run()