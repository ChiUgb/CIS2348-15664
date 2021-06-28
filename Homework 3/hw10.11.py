# Chiamaka Ugbaja
# 1772427
class FoodItem:

    # Defined constructor with parameters to initialize
    # attributes (name, fat, carbs, protein)
    def __init__(self, name="None", fat=0.0, carbs=0.0, protein=0.0):
        self.name = name
        self.fat = fat
        self.carbs = carbs
        self.protein = protein

    def get_calories(self, num_servings):  # calculated total calories based on formula
        # Calorie formula
        calories = ((self.fat * 9) + (self.carbs * 4) + (self.protein * 4)) * num_servings
        return calories

    def print_info(self):  # printed nutritional information with user input
        print('Nutritional information per serving of {}:'.format(self.name))
        print('   Fat: {:.2f} g'.format(self.fat))
        print('   Carbohydrates: {:.2f} g'.format(self.carbs))
        print('   Protein: {:.2f} g'.format(self.protein))


if __name__ == "__main__": # executes first to fill variables and run before class FoodItem
    first_food_item = FoodItem()

    item_name = input()
    amount_fat = float(input())
    amount_carbs = float(input())
    amount_protein = float(input())

    second_food_item = FoodItem(item_name, amount_fat, amount_carbs, amount_protein)
    num_servings = float(input())

    first_food_item.print_info()
    print('Number of calories for {:.2f} serving(s): {:.2f}'.format(num_servings,
                                                                    first_food_item.get_calories(num_servings)))

    print()

    second_food_item.print_info()
    print('Number of calories for {:.2f} serving(s): {:.2f}'.format(num_servings,
                                                                    second_food_item.get_calories(num_servings)))
