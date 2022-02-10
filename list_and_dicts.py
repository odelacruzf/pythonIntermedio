
def run():
    
    my_list =[1, "hello", True, 4.5]
    my_dict ={"firstname": "oscar", "lastname":"De la cruz"}

    super_list = [

        {"firstname": "oscar", "lastname":"De la cruz"},
        {"firstname": "juan", "lastname":"De la cruz"},
        {"firstname": "lucia", "lastname":"De la cruz"},
        {"firstname": "tania", "lastname":"Castillo"}

    ]

    for item in super_list:
        print(item)


    super_dict ={

        "naturals_nums": [1,2,3,4,5],
        "integer_nums": [-1,-2,-3, 0, 1,2,3],
        "floating_nums": [1.1, 4.5, 6.43]
    }

    for key, value in super_dict.items():
        print(key, "-", value)



if __name__ == "__main__":
    run()