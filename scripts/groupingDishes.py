'''
You have a list of dishes. Each dish is associated with a list of ingredients used to prepare it. You want to group the dishes by ingredients, so that for each ingredient you'll be able to find all the dishes that contain it (if there are at least 2 such dishes).

Return an array where each element is a list with the first element equal to the name of the ingredient and all of the other elements equal to the names of dishes that contain this ingredient. The dishes inside each list should be sorted lexicographically. The result array should be sorted lexicographically by the names of the ingredients in its elements.

ex
input:
 dishes = [["Salad", "Tomato", "Cucumber", "Salad", "Sauce"],
            ["Pizza", "Tomato", "Sausage", "Sauce", "Dough"],
            ["Quesadilla", "Chicken", "Cheese", "Sauce"],
            ["Sandwich", "Salad", "Bread", "Tomato", "Cheese"]]
output:
groupingDishes(dishes) = [["Cheese", "Quesadilla", "Sandwich"],
                            ["Salad", "Salad", "Sandwich"],
                            ["Sauce", "Pizza", "Quesadilla", "Salad"],
                            ["Tomato", "Pizza", "Salad", "Sandwich"]]

'''
from collections import defaultdict
def groupingDishes(dishes):
    # defaultdict allows us to initialize each list as empty.
    ingredient_dict = defaultdict(list) # {ingredient: list of dishes containing ingredient}
    for dish in dishes:
        # read ingredients of dish
        ingredients = dish[1:]
        for ingredient in ingredients:
            # add this dish to the list of dishes associated with this ingredient
            ingredient_dict[ingredient].append(dish[0])
    # we need to sort each list of dishes lexicographically
    result = [[ingredient]+sorted(ingredient_dict[ingredient]) for ingredient in ingredient_dict if len(ingredient_dict[ingredient]) > 1]
    # now we need to sort by ingredient, which is at position 0.
    result = sorted(result, key=lambda x: x[0])
    return result

dishes = [["Salad", "Tomato", "Cucumber", "Salad", "Sauce"],
            ["Pizza", "Tomato", "Sausage", "Sauce", "Dough"],
            ["Quesadilla", "Chicken", "Cheese", "Sauce"],
            ["Sandwich", "Salad", "Bread", "Tomato", "Cheese"]]

print(groupingDishes(dishes))