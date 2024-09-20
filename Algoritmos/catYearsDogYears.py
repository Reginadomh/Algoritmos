'''
Programa que calcula la edad de un perro y la edad de un gato a partir de los años humano que tenga
'''

def calculate_pet_ages(human_years):
    # Calculate cat years
    if human_years == 1:
        cat_years = 15
    elif human_years == 2:
        cat_years = 15 + 9
    else:
        cat_years = 15 + 9 + (human_years - 2) * 4

    # Calculate dog years
    if human_years == 1:
        dog_years = 15
    elif human_years == 2:
        dog_years = 15 + 9
    else:
        dog_years = 15 + 9 + (human_years - 2) * 5

    return {
        'Años humano': human_years,
        'Años gato': cat_years,
        'Años perro': dog_years
    }

# Test the function with an example input
humanYears = 10
ages = calculate_pet_ages(humanYears)
print(ages)
