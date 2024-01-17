def order_food(lst): 
    # your code here
    options_count = {}

    for developer in lst:
        meal_option = developer['meal']
        options_count[meal_option] = options_count.get(meal_option, 0) + 1

    return options_count
