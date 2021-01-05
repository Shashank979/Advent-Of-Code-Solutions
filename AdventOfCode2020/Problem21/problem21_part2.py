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

    wrong_ingredients = {}
    for key, value in allergens.items():
        allergens[key] = list(value)

    while True:
        ingredient = 0
        for allergen in allergens:
            if len(allergens[allergen]) == 1:
                wrong_ingredients[allergen] = allergens[allergen][0]
                ingredient = allergens[allergen][0]
        if ingredient == 0:
            break
        for allergen, value in allergens.items():
            for a in value:
                if a == ingredient:
                    new_list = allergens[allergen]
                    new_list.remove(a)
                    allergens[allergen] = new_list
    sorted_list = sorted(wrong_ingredients)
    
    for x in sorted_list:
        print(wrong_ingredients[x] + ",", end = "")

    
main()