def main():
    set_allergens = set([])
    ingredients = []
    file1 = 'input_problem21.txt'
    list_foods = []
    allergens = {} 
    input_file = open(file1).read().splitlines()
    for food in input_file:
        key = food.split(" (")[0].split(" ")
        value = food.split(" (")[1].replace(")", "")[9:].split(", ")
        for allergen in value:
            set_allergens.add(allergen)
        for ingredient in key:
            ingredients.append(ingredient)
        list_foods.append([value, key])
    
    for allergen in set_allergens:
        for index, food in enumerate(list_foods):
            if allergen in food[0]:
                if allergen not in allergens:
                    allergens[allergen] = set(list_foods[index][1])
                else:
                    allergens[allergen] = allergens[allergen].intersection(set(list_foods[index][1]))

    wrong_allergens = set([])
    for key, value in allergens.items():
        for allergen in value:
            wrong_allergens.add(allergen)
    
    counter = 0
    for ingredient in ingredients:
        if ingredient not in wrong_allergens:
            counter += 1
    print(counter)
    
main()