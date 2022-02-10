DATA = [
    {
        'name': 'Facundo',
        'age': 72,
        'organization': 'Platzi',
        'position': 'Technical Coach',
        'language': 'python',
    },
    {
        'name': 'Luisana',
        'age': 33,
        'organization': 'Globant',
        'position': 'UX Designer',
        'language': 'javascript',
    },
    {
        'name': 'HÃ©ctor',
        'age': 19,
        'organization': 'Platzi',
        'position': 'Associate',
        'language': 'ruby',
    },
    {
        'name': 'Gabriel',
        'age': 20,
        'organization': 'Platzi',
        'position': 'Associate',
        'language': 'javascript',
    },
    {
        'name': 'Isabella',
        'age': 30,
        'organization': 'Platzi',
        'position': 'QA Manager',
        'language': 'java',
    },
    {
        'name': 'Karo',
        'age': 23,
        'organization': 'Everis',
        'position': 'Backend Developer',
        'language': 'python',
    },
    {
        'name': 'Ariel',
        'age': 32,
        'organization': 'Rappi',
        'position': 'Support',
        'language': '',
    },
    {
        'name': 'Juan',
        'age': 17,
        'organization': '',
        'position': 'Student',
        'language': 'go',
    },
    {
        'name': 'Pablo',
        'age': 32,
        'organization': 'Master',
        'position': 'Human Resources Manager',
        'language': 'python',
    },
    {
        'name': 'Lorena',
        'age': 56,
        'organization': 'Python Organization',
        'position': 'Language Maker',
        'language': 'python',
    },
]


def run():

    #obtiene todos los desarrolladores que programan en python
    all_python_devs = [ worker["name"]  for worker in DATA if worker["language"] == "python"  ]  

    for worker in all_python_devs:
        print(worker)

    #obtiene todos los nombres de las personas que trabajan en platzi
    all_platzi_workers = [ worker["name"] for worker in DATA if worker["organization"] == "Platzi" ]

    for worker in all_platzi_workers:
        print(worker)
    
    #obtiene todas las personas que sea mayores de 18 años
    adults = list( filter(lambda worker: worker["age"] > 18, DATA) )

    #obiene el nombre de todas las personas mayores a 18 años. usa la lista adults
    adults = list( map(lambda worker: worker["name"], adults) )


    #nueva lista de diccionarios agregando una nueva llave que indique si es un adulto o no
    old_people = list( map(lambda worker: worker | {"old": worker["age"] > 70}   , DATA) )

    for worker in old_people:
        print(worker)
        




    for worker in adults:
        print(worker)

if __name__ == "__main__":
    run()