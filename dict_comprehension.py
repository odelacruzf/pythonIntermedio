import math 

def run():

    #forma normal
    #my_dict ={}

    #for i in range(1,101):
        #my_dict[i]= i**3
    
    #print(my_dict)

    #dict comprehension
    my_dict = {i: i**3 for i in range(1,101) }
    my_dict3 = {i: i**3 for i in range(1,101) if i % 3 != 0}

    print(my_dict, my_dict3)

    #dict comprehesion, con los 1000 primeros numeros 
    #natuales con sus raices cuadradas como valor

    numeros = {i: math.sqrt(i)  for i in range(1, 1001) }
    print("numeros: ", numeros)

if __name__ == '__main__':
    run()