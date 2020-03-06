class Meal:
    def __init__(self, name, ingredients):
        self.name = name
        self.ingredients = ingredients

m1 = Meal('Basic Burger', ['Lettuce','Tomato','Onion','Patty'])
m2 = Meal('Cheese Burger', ['Cheese','Tomato','Patty','Lettuce'])
m3 = Meal('Jays Burger', ['Onion','Tomato','Patty','Lettuce'])
m4 = Meal('Highwater Burger', ['Tomato','Patty', 'Lettuce','Cheese'])
meals = [m1,m2,m3,m4]

def number_unique_meal(meals):
    sort_meals = set()
    for m in meals:
        m.ingredients.sort()
        sort_meals.add(tuple(m.ingredients))
    return len(sort_meals)

print(number_unique_meal(meals))




