import unittest
from src.main import Meals
from src.main import CategoriesAreaIngredients
from src.main import Recipe

class MealsTests(unittest.TestCase):

    def setUp(self):
        self.temp = Meals()

# Meal by name tests
    def test_mealByName_Pierogi(self):
        meal = [{'meal': 'Pierogi (Polish Dumplings)'}, {'category': 'Side'},
                {'instructions': 'To prepare the sauerkraut filling, melt the butter in a skillet over medium heat. Stir in the onion, and cook until translucent, about 5 minutes. Add the drained sauerkraut and cook for an additional 5 minutes. Season to taste with salt and pepper, then remove to a plate to cool.\r\n\r\nFor the mashed potato filling, melt the butter in a skillet over medium heat. Stir in the onion, and cook until translucent, about 5 minutes. Stir into the mashed potatoes, and season with salt and white pepper.\r\n\r\nTo make the dough, beat together the eggs and sour cream until smooth. Sift together the flour, salt, and baking powder; stir into the sour cream mixture until dough comes together. Knead the dough on a lightly floured surface until firm and smooth. Divide the dough in half, then roll out one half to 1/8 inch thickness. Cut into 3 inch rounds using a biscuit cutter.\r\n\r\nPlace a small spoonful of the mashed potato filling into the center of each round. Moisten the edges with water, fold over, and press together with a fork to seal. Repeat procedure with the remaining dough and the sauerkraut filling.\r\n\r\nBring a large pot of lightly salted water to a boil. Add perogies and cook for 3 to 5 minutes or until pierogi float to the top. Remove with a slotted spoon.'},
                {'ingredients': ['Butter', 'Chopped Onion', 'Sauerkraut', 'Potatoes', 'Eggs', 'Sour Cream', 'Flour', 'Salt', 'Baking Powder']}]

        self.assertEqual(
            meal,
            self.temp.mealByName("Pierogi"))

    def test_mealByName_Arrabiata_upper_and_lower(self):
        meal = [{'meal': 'Pierogi (Polish Dumplings)'}, {'category': 'Side'},
                {'instructions': 'To prepare the sauerkraut filling, melt the butter in a skillet over medium heat. Stir in the onion, and cook until translucent, about 5 minutes. Add the drained sauerkraut and cook for an additional 5 minutes. Season to taste with salt and pepper, then remove to a plate to cool.\r\n\r\nFor the mashed potato filling, melt the butter in a skillet over medium heat. Stir in the onion, and cook until translucent, about 5 minutes. Stir into the mashed potatoes, and season with salt and white pepper.\r\n\r\nTo make the dough, beat together the eggs and sour cream until smooth. Sift together the flour, salt, and baking powder; stir into the sour cream mixture until dough comes together. Knead the dough on a lightly floured surface until firm and smooth. Divide the dough in half, then roll out one half to 1/8 inch thickness. Cut into 3 inch rounds using a biscuit cutter.\r\n\r\nPlace a small spoonful of the mashed potato filling into the center of each round. Moisten the edges with water, fold over, and press together with a fork to seal. Repeat procedure with the remaining dough and the sauerkraut filling.\r\n\r\nBring a large pot of lightly salted water to a boil. Add perogies and cook for 3 to 5 minutes or until pierogi float to the top. Remove with a slotted spoon.'},
                {'ingredients': ['Butter', 'Chopped Onion', 'Sauerkraut', 'Potatoes', 'Eggs', 'Sour Cream', 'Flour',
                                 'Salt', 'Baking Powder']}]
        self.assertEqual(meal, self.temp.mealByName("PieRogI"))

    def test_mealByName_golabki_in_upper(self):
        meal = [{'meal': 'Gołąbki (cabbage roll)'}, {'category': 'Beef'},
                {'instructions': 'Bring a large pot of lightly salted water to a boil. Place cabbage head into water, cover pot, and cook until cabbage leaves are slightly softened enough to remove from head, 3 minutes. Remove cabbage from pot and let cabbage sit until leaves are cool enough to handle, about 10 minutes.\r\n\r\nRemove 18 whole leaves from the cabbage head, cutting out any thick tough center ribs. Set whole leaves aside. Chop the remainder of the cabbage head and spread it in the bottom of a casserole dish.\r\n\r\nMelt butter in a large skillet over medium-high heat. Cook and stir onion in hot butter until tender, 5 to 10 minutes. Cool.\r\n\r\nStir onion, beef, pork, rice, garlic, 1 teaspoon salt, and 1/4 teaspoon pepper together in a large bowl.\r\n\r\nPreheat oven to 350 degrees F (175 degrees C).\r\n\r\nPlace about 1/2 cup beef mixture on a cabbage leaf. Roll cabbage around beef mixture, tucking in sides to create an envelope around the meat. Repeat with remaining leaves and meat mixture. Place cabbage rolls in a layer atop the chopped cabbage in the casserole dish; season rolls with salt and black pepper.\r\n\r\nWhisk tomato soup, tomato juice, and ketchup together in a bowl. Pour tomato soup mixture over cabbage rolls and cover dish wish aluminum foil.\r\n\r\nBake in the preheated oven until cabbage is tender and meat is cooked through, about 1 hour.'},
                {'ingredients': ['Cabbage', 'Butter', 'Onion', 'Ground Beef', 'Ground Pork', 'Rice', 'Garlic', 'Salt', 'Black Pepper', 'Tomato Puree']}]

        self.assertEqual(meal, self.temp.mealByName("GOŁĄBKI"))

    def test_mealByName_meal_with_space(self):
        meal = [{'meal': 'Polskie Naleśniki (Polish Pancakes)'}, {'category': 'Dessert'},
                {'instructions': 'Add flour, eggs, milk, water, and salt in a large bowl then mix with a hand mixer until you have a smooth, lump-free batter.\r\nAt this point, mix in the butter or the vegetable oil. Alternatively, you can use them to grease the pan before frying each pancake.\r\nHeat a non-stick pan over medium heat, then pour in the batter, swirling the pan to help it spread.\r\nWhen the pancake starts pulling away a bit from the sides, and the top is no longer wet, flip it and cook shortly on the other side as well.\r\nTransfer to a plate. Cook the remaining batter until all used up.\r\nServe warm, with the filling of your choice.'},
                {'ingredients': ['Flour', 'Eggs', 'Milk', 'Water', 'Salt', 'Sugar', 'Butter']}]

        self.assertEqual(meal, self.temp.mealByName("Polskie Nalesniki"))

    def test_mealByName_with_space_after_pierogi(self):
        meal = [{'meal': 'Pierogi (Polish Dumplings)'}, {'category': 'Side'},
                {
                    'instructions': 'To prepare the sauerkraut filling, melt the butter in a skillet over medium heat. Stir in the onion, and cook until translucent, about 5 minutes. Add the drained sauerkraut and cook for an additional 5 minutes. Season to taste with salt and pepper, then remove to a plate to cool.\r\n\r\nFor the mashed potato filling, melt the butter in a skillet over medium heat. Stir in the onion, and cook until translucent, about 5 minutes. Stir into the mashed potatoes, and season with salt and white pepper.\r\n\r\nTo make the dough, beat together the eggs and sour cream until smooth. Sift together the flour, salt, and baking powder; stir into the sour cream mixture until dough comes together. Knead the dough on a lightly floured surface until firm and smooth. Divide the dough in half, then roll out one half to 1/8 inch thickness. Cut into 3 inch rounds using a biscuit cutter.\r\n\r\nPlace a small spoonful of the mashed potato filling into the center of each round. Moisten the edges with water, fold over, and press together with a fork to seal. Repeat procedure with the remaining dough and the sauerkraut filling.\r\n\r\nBring a large pot of lightly salted water to a boil. Add perogies and cook for 3 to 5 minutes or until pierogi float to the top. Remove with a slotted spoon.'},
                {'ingredients': ['Butter', 'Chopped Onion', 'Sauerkraut', 'Potatoes', 'Eggs', 'Sour Cream', 'Flour',
                                 'Salt', 'Baking Powder']}]
        self.assertEqual(meal, self.temp.mealByName("pierogi "))


    def test_mealByName_Exception_not_existing_meal(self):
        self.assertRaises(Exception, self.temp.mealByName, "afshoa")

    def test_mealByName_Exception_with_space_before_meal(self):
        self.assertRaises(Exception, self.temp.mealByName, " pierogi")

    def test_mealByName_Exception_int(self):
        self.assertRaises(Exception, self.temp.mealByName, 1)

    def test_mealByName_Exception_empty_list(self):
        self.assertRaises(Exception, self.temp.mealByName, [])

    def test_mealByName_Exception_list_with_meal_name(self):
        self.assertRaises(Exception, self.temp.mealByName, ["Pierogi"])

    def test_mealByName_Exception_negative_int(self):
        self.assertRaises(Exception, self.temp.mealByName, -31)

    def test_mealByName_Exception_float(self):
        self.assertRaises(Exception, self.temp.mealByName, 31.13411)

    def test_mealByName_Exception_negative_float(self):
        self.assertRaises(Exception, self.temp.mealByName, -5.41242)

    def test_mealByName_Exception_dict(self):
        self.assertRaises(Exception, self.temp.mealByName, {})

    def test_mealByName_Exception_tuple(self):
        self.assertRaises(Exception, self.temp.mealByName, ())

# List all meals by first letter

    def test_listAllMealsByFirstLetter_lower_a(self):
        self.assertEqual(['Apple Frangipan Tart', 'Apple & Blackberry Crumble', 'Apam balik', 'Ayam Percik'],self.temp.listAllMealsByFirstLetter("a"))

    def test_listAllMealsByFirstLetter_upper_A(self):
        self.assertEqual(['Apple Frangipan Tart', 'Apple & Blackberry Crumble', 'Apam balik', 'Ayam Percik'],self.temp.listAllMealsByFirstLetter("A"))

    def test_listAllMealsByFirstLetter_upper_A(self):
        self.assertEqual(
            ['Bakewell tart', 'Bread and Butter Pudding', 'Beef Wellington', 'Baingan Bharta', 'Beef Brisket Pot Roast', 'Beef Sunday Roast', 'Braised Beef Chilli', 'Beef stroganoff', 'Broccoli & Stilton soup', 'Bean & Sausage Hotpot', 'Banana Pancakes', 'Beef Dumpling Stew', 'Beef and Mustard Pie', 'Beef and Oyster pie', 'Blackberry Fool', 'Battenberg Cake', 'Beef Bourguignon', 'Brie wrapped in prosciutto & brioche', 'Boulangère Potatoes', 'BeaverTails', 'Brown Stew Chicken', 'Beef Lo Mein', 'Baked salmon with fennel & tomatoes', 'Budino Di Ricotta', 'Breakfast Potatoes', 'Bitterballen (Dutch meatballs)', 'BBQ Pork Sloppy Joes', 'Beef Banh Mi Bowls with Sriracha Mayo, Carrot & Pickled Cucumber', 'Big Mac', 'Bigos (Hunters Stew)', 'Boxty Breakfast','Beef Rendang', 'Burek']
            , self.temp.listAllMealsByFirstLetter("b"))

    def test_listAllMealsByFirstLetter_lower_z(self):
        self.assertRaises(Exception, self.temp.listAllMealsByFirstLetter, "z")

    def test_listAllMealsByFirstLetter_lower_q(self):
        self.assertRaises(Exception, self.temp.listAllMealsByFirstLetter, "q")

    def test_listAllMealsByFirstLetter_Exception_bad_str(self):
        self.assertRaises(Exception, self.temp.listAllMealsByFirstLetter, "fa")

    def test_listAllMealsByFirstLetter_Exception_with_space_before_letter(self):
        self.assertRaises(Exception, self.temp.listAllMealsByFirstLetter, " f")

    def test_listAllMealsByFirstLetter_Exception_with_space_after_letter(self):
        self.assertRaises(Exception, self.temp.listAllMealsByFirstLetter, " f")

    def test_listAllMealsByFirstLetter_Exception_empty_list(self):
        self.assertRaises(Exception, self.temp.listAllMealsByFirstLetter, [])

    def test_listAllMealsByFirstLetter_Exception_list_with_letter(self):
        self.assertRaises(Exception, self.temp.listAllMealsByFirstLetter, ["s"])

    def test_listAllMealsByFirstLetter_Exception_dict(self):
        self.assertRaises(Exception, self.temp.listAllMealsByFirstLetter, {})

    def test_listAllMealsByFirstLetter_Exception_tuple(self):
        self.assertRaises(Exception, self.temp.listAllMealsByFirstLetter, ())

    def test_listAllMealsByFirstLetter_Exception_int(self):
        self.assertRaises(Exception, self.temp.listAllMealsByFirstLetter, 7)

    def test_listAllMealsByFirstLetter_Exception_negative_int(self):
        self.assertRaises(Exception, self.temp.listAllMealsByFirstLetter, -27)

    def test_listAllMealsByFirstLetter_Exception_float(self):
        self.assertRaises(Exception, self.temp.listAllMealsByFirstLetter, 15.231)

    def test_listAllMealsByFirstLetter_Exception_negative_float(self):
        self.assertRaises(Exception, self.temp.listAllMealsByFirstLetter, -951.413871)

# How many meals starting with letter
    def test_howManyMealsStartingWithLetter_lower_a(self):
        self.assertEqual(4, self.temp.howManyMealsStartingWithLetter("a"))

    def test_howManyMealsStartingWithLetter_upper_a(self):
        self.assertEqual(4, self.temp.howManyMealsStartingWithLetter("A"))

    def test_howManyMealsStartingWithLetter_upper_q(self):
        self.assertEqual(25, self.temp.howManyMealsStartingWithLetter("P"))

    def test_howManyMealsStartingWithLetter_lower_x(self):
        self.assertEqual(0, self.temp.howManyMealsStartingWithLetter("x"))


    def test_howManyMealsStartingWithLetter_Exception_bad_str(self):
        self.assertRaises(Exception, self.temp.howManyMealsStartingWithLetter, "gx")

    def test_howManyMealsStartingWithLetter_Exception_empty_list(self):
        self.assertRaises(Exception, self.temp.howManyMealsStartingWithLetter, [])

    def test_howManyMealsStartingWithLetter_Exception_list_with_letter(self):
        self.assertRaises(Exception, self.temp.howManyMealsStartingWithLetter, ["g"])

    def test_howManyMealsStartingWithLetter_Exception_dict(self):
        self.assertRaises(Exception, self.temp.howManyMealsStartingWithLetter, {})

    def test_howManyMealsStartingWithLetter_Exception_tuple(self):
        self.assertRaises(Exception, self.temp.howManyMealsStartingWithLetter, ())

    def test_howManyMealsStartingWithLetter_Exception_int(self):
        self.assertRaises(Exception, self.temp.howManyMealsStartingWithLetter, 3)

    def test_howManyMealsStartingWithLetter_Exception_negative_int(self):
        self.assertRaises(Exception, self.temp.howManyMealsStartingWithLetter, -7)

    def test_howManyMealsStartingWithLetter_Exception_float(self):
        self.assertRaises(Exception, self.temp.howManyMealsStartingWithLetter, 15.231)

    def test_howManyMealsStartingWithLetter_Exception_negative_float(self):
        self.assertRaises(Exception, self.temp.howManyMealsStartingWithLetter, -38.13831)

# lookup full meal details by id

    def test_lookupFullMealDetailsById_52772(self):
        meal = [{'id': '52772'}, {'meal': 'Teriyaki Chicken Casserole'}, {'category': 'Chicken'},
                {'instructions': 'Preheat oven to 350° F. Spray a 9x13-inch baking pan with non-stick spray.\r\nCombine soy sauce, ½ cup water, brown sugar, ginger and garlic in a small saucepan and cover. Bring to a boil over medium heat. Remove lid and cook for one minute once boiling.\r\nMeanwhile, stir together the corn starch and 2 tablespoons of water in a separate dish until smooth. Once sauce is boiling, add mixture to the saucepan and stir to combine. Cook until the sauce starts to thicken then remove from heat.\r\nPlace the chicken breasts in the prepared pan. Pour one cup of the sauce over top of chicken. Place chicken in oven and bake 35 minutes or until cooked through. Remove from oven and shred chicken in the dish using two forks.\r\n*Meanwhile, steam or cook the vegetables according to package directions.\r\nAdd the cooked vegetables and rice to the casserole dish with the chicken. Add most of the remaining sauce, reserving a bit to drizzle over the top when serving. Gently toss everything together in the casserole dish until combined. Return to oven and cook 15 minutes. Remove from oven and let stand 5 minutes before serving. Drizzle each serving with remaining sauce. Enjoy!'},
                {'ingredients': ['soy sauce', 'water', 'brown sugar', 'ground ginger', 'minced garlic', 'cornstarch', 'chicken breasts', 'stir-fry vegetables', 'brown rice']}]

        self.assertEqual(meal, self.temp.lookupFullMealDetailsById(52772))

    def test_lookupFullMealDetailsById_53021(self):
        meal = [{'id': '53021'}, {'meal': 'Gołąbki (cabbage roll)'}, {'category': 'Beef'},
                {'instructions': 'Bring a large pot of lightly salted water to a boil. Place cabbage head into water, cover pot, and cook until cabbage leaves are slightly softened enough to remove from head, 3 minutes. Remove cabbage from pot and let cabbage sit until leaves are cool enough to handle, about 10 minutes.\r\n\r\nRemove 18 whole leaves from the cabbage head, cutting out any thick tough center ribs. Set whole leaves aside. Chop the remainder of the cabbage head and spread it in the bottom of a casserole dish.\r\n\r\nMelt butter in a large skillet over medium-high heat. Cook and stir onion in hot butter until tender, 5 to 10 minutes. Cool.\r\n\r\nStir onion, beef, pork, rice, garlic, 1 teaspoon salt, and 1/4 teaspoon pepper together in a large bowl.\r\n\r\nPreheat oven to 350 degrees F (175 degrees C).\r\n\r\nPlace about 1/2 cup beef mixture on a cabbage leaf. Roll cabbage around beef mixture, tucking in sides to create an envelope around the meat. Repeat with remaining leaves and meat mixture. Place cabbage rolls in a layer atop the chopped cabbage in the casserole dish; season rolls with salt and black pepper.\r\n\r\nWhisk tomato soup, tomato juice, and ketchup together in a bowl. Pour tomato soup mixture over cabbage rolls and cover dish wish aluminum foil.\r\n\r\nBake in the preheated oven until cabbage is tender and meat is cooked through, about 1 hour.'},
                {'ingredients': ['Cabbage', 'Butter', 'Onion', 'Ground Beef', 'Ground Pork', 'Rice', 'Garlic', 'Salt', 'Black Pepper', 'Tomato Puree']}]
        self.assertEqual(meal, self.temp.lookupFullMealDetailsById(53021))


    def test_lookupFullMealDetailsById_Exception_bad_id(self):
        self.assertRaises(Exception, self.temp.howManyMealsStartingWithLetter, 3)

    def test_lookupFullMealDetailsById_Exception_negative_int(self):
        self.assertRaises(Exception, self.temp.howManyMealsStartingWithLetter, -7)

    def test_lookupFullMealDetailsById_Exception_float(self):
        self.assertRaises(Exception, self.temp.howManyMealsStartingWithLetter, 15.231)

    def test_lookupFullMealDetailsById_Exception_negative_float(self):
        self.assertRaises(Exception, self.temp.howManyMealsStartingWithLetter, -38.13831)

    def test_lookupFullMealDetailsById_Exception_empty_string(self):
        self.assertRaises(Exception, self.temp.howManyMealsStartingWithLetter, "")

    def test_lookupFullMealDetailsById_Exception_int_in_str(self):
        self.assertRaises(Exception, self.temp.howManyMealsStartingWithLetter, "53021")

    def test_lookupFullMealDetailsById_Exception_int_in_list(self):
        self.assertRaises(Exception, self.temp.howManyMealsStartingWithLetter, [53021])

    def test_lookupFullMealDetailsById_Exception_int_in_str_in_list(self):
        self.assertRaises(Exception, self.temp.howManyMealsStartingWithLetter, ["53021"])

    def test_lookupFullMealDetailsById_Exception_dict(self):
        self.assertRaises(Exception, self.temp.howManyMealsStartingWithLetter, {})

    def test_lookupFullMealDetailsById_Exception_tuple(self):
        self.assertRaises(Exception, self.temp.howManyMealsStartingWithLetter, ())

# Meals starting with letter without baking

    def test_mealsStartingWithLetterWithoutBaking_lower_a(self):
        self.assertEqual(
            [('Apple & Blackberry Crumble', 'Dessert'), ('Apam balik', 'Dessert'), ('Ayam Percik', 'Chicken')]
            , self.temp.mealsStartingWithLetterWithoutBaking("a"))

    def test_mealsStartingWithLetterWithoutBaking_upper_a(self):
        self.assertEqual(
            [('Apple & Blackberry Crumble', 'Dessert'), ('Apam balik', 'Dessert'), ('Ayam Percik', 'Chicken')]
            , self.temp.mealsStartingWithLetterWithoutBaking("A"))

    def test_mealsStartingWithLetterWithoutBaking_upper_q(self):
        self.assertEqual(
            [('Pad See Ew', 'Chicken'), ('Potato Gratin with Chicken', 'Chicken'), ('Poutine', 'Miscellaneous'),
             ('Pilchard puttanesca', 'Pasta'), ('Pork Cassoulet', 'Pork'), ('Pancakes', 'Dessert'),
             ('Pumpkin Pie', 'Dessert'), ('Peanut Butter Cheesecake', 'Dessert'), ('Peach & Blueberry Grunt', 'Dessert'),
             ('Parkin Cake', 'Dessert'), ('Provençal Omelette Cake', 'Vegetarian'), ('Prawn & Fennel Bisque', 'Side'),
             ('Pate Chinois', 'Beef'), ('Pouding chomeur', 'Dessert'), ('Peanut Butter Cookies', 'Dessert'),
             ('Pizza Express Margherita', 'Miscellaneous'), ('Paszteciki (Polish Pasties)', 'Beef'), ('Pierogi (Polish Dumplings)','Side'),
             ('Polskie Naleśniki (Polish Pancakes)', 'Dessert'), ('Piri-piri chicken and slaw', 'Chicken'),
             ('Portuguese prego with green piri-piri', 'Beef'), ('Portuguese barbecued pork (Febras assadas)', 'Pork'),
             ('Portuguese fish stew (Caldeirada de peixe)', 'Seafood'), ('Portuguese custard tarts', 'Dessert')]
            , self.temp.mealsStartingWithLetterWithoutBaking("P"))

    def test_mealsStartingWithLetterWithoutBaking_lower_x(self):
        self.assertEqual([], self.temp.mealsStartingWithLetterWithoutBaking("x"))


    def test_mealsStartingWithLetterWithoutBaking_Exception_bad_str(self):
        self.assertRaises(Exception, self.temp.mealsStartingWithLetterWithoutBaking, "sa")

    def test_mealsStartingWithLetterWithoutBaking_Exception_with_space_before_letter(self):
        self.assertRaises(Exception, self.temp.mealsStartingWithLetterWithoutBaking, " a")

    def test_mealsStartingWithLetterWithoutBaking_Exception_with_space_after_letter(self):
        self.assertRaises(Exception, self.temp.mealsStartingWithLetterWithoutBaking, "a ")

    def test_mealsStartingWithLetterWithoutBaking_Exception_empty_list(self):
        self.assertRaises(Exception, self.temp.mealsStartingWithLetterWithoutBaking, [])

    def test_mealsStartingWithLetterWithoutBaking_Exception_list_with_letter(self):
        self.assertRaises(Exception, self.temp.mealsStartingWithLetterWithoutBaking, ["d"])

    def test_mealsStartingWithLetterWithoutBaking_Exception_dict(self):
        self.assertRaises(Exception, self.temp.mealsStartingWithLetterWithoutBaking, {})

    def test_mealsStartingWithLetterWithoutBaking_Exception_tuple(self):
        self.assertRaises(Exception, self.temp.mealsStartingWithLetterWithoutBaking, ())

    def test_mealsStartingWithLetterWithoutBaking_Exception_int(self):
        self.assertRaises(Exception, self.temp.mealsStartingWithLetterWithoutBaking, 1)

    def test_mealsStartingWithLetterWithoutBaking_Exception_negative_int(self):
        self.assertRaises(Exception, self.temp.mealsStartingWithLetterWithoutBaking, -51)

    def test_mealsStartingWithLetterWithoutBaking_Exception_float(self):
        self.assertRaises(Exception, self.temp.mealsStartingWithLetterWithoutBaking, 25.53)

    def test_mealsStartingWithLetterWithoutBaking_Exception_negative_float(self):
        self.assertRaises(Exception, self.temp.mealsStartingWithLetterWithoutBaking, -28.421)

# Meal with smallest number of ingredients starting with letter

    def test_mealWithSmallestNumberOfIngredientsStartingWithLetter_lower_a(self):
        self.assertEqual(
            ['Apple Frangipan Tart', 'Apple & Blackberry Crumble', 'Apam balik']
            , self.temp.mealWithSmallestNumberOfIngredientsStartingWithLetter("a"))

    def test_mealWithSmallestNumberOfIngredientsStartingWithLetter_lower_A(self):
        self.assertEqual(
            ['Apple Frangipan Tart', 'Apple & Blackberry Crumble', 'Apam balik']
            , self.temp.mealWithSmallestNumberOfIngredientsStartingWithLetter("A"))

    def test_mealWithSmallestNumberOfIngredientsStartingWithLetter_lower_x(self):
        self.assertEqual([], self.temp.mealWithSmallestNumberOfIngredientsStartingWithLetter("x"))

    def test_mealWithSmallestNumberOfIngredientsStartingWithLetter_lower_n(self):
        self.assertEqual(['Nutty Chicken Curry'], self.temp.mealWithSmallestNumberOfIngredientsStartingWithLetter("n"))


    def test_mealWithSmallestNumberOfIngredientsStartingWithLetter_Exception_bad_str(self):
        self.assertRaises(Exception, self.temp.mealWithSmallestNumberOfIngredientsStartingWithLetter, "sa")

    def test_mealWithSmallestNumberOfIngredientsStartingWithLetter_Exception_with_space_before_str(self):
        self.assertRaises(Exception, self.temp.mealWithSmallestNumberOfIngredientsStartingWithLetter, " a")

    def test_mealWithSmallestNumberOfIngredientsStartingWithLetter_Exception_with_space_after_str(self):
        self.assertRaises(Exception, self.temp.mealWithSmallestNumberOfIngredientsStartingWithLetter, "a ")

    def test_mealWithSmallestNumberOfIngredientsStartingWithLetter_Exception_empty_list(self):
        self.assertRaises(Exception, self.temp.mealWithSmallestNumberOfIngredientsStartingWithLetter, [])

    def test_mealWithSmallestNumberOfIngredientsStartingWithLetter_Exception_list_with_letter(self):
        self.assertRaises(Exception, self.temp.mealWithSmallestNumberOfIngredientsStartingWithLetter, ["d"])

    def test_mealWithSmallestNumberOfIngredientsStartingWithLetter_Exception_dict(self):
        self.assertRaises(Exception, self.temp.mealWithSmallestNumberOfIngredientsStartingWithLetter, {})

    def test_mealWithSmallestNumberOfIngredientsStartingWithLetter_Exception_tuple(self):
        self.assertRaises(Exception, self.temp.mealWithSmallestNumberOfIngredientsStartingWithLetter, ())

    def test_mealWithSmallestNumberOfIngredientsStartingWithLetter_Exception_int(self):
        self.assertRaises(Exception, self.temp.mealWithSmallestNumberOfIngredientsStartingWithLetter, 1)

    def test_mealWithSmallestNumberOfIngredientsStartingWithLetter_Exception_negative_int(self):
        self.assertRaises(Exception, self.temp.mealWithSmallestNumberOfIngredientsStartingWithLetter, -51)

    def test_mealWithSmallestNumberOfIngredientsStartingWithLetter_Exception_float(self):
        self.assertRaises(Exception, self.temp.mealWithSmallestNumberOfIngredientsStartingWithLetter, 25.53)

    def test_mealWithSmallestNumberOfIngredientsStartingWithLetter_Exception_negative_float(self):
        self.assertRaises(Exception, self.temp.mealWithSmallestNumberOfIngredientsStartingWithLetter, -28.421)

    def tearDown(self):
        self.temp = None


class CategoriesAreaIngredientsTests(unittest.TestCase):

    def setUp(self):
        self.temp = CategoriesAreaIngredients()

# Filter by main ingredient

    def test_filterByMainIngredient_lower_banana(self):
        self.assertEqual(['Banana Pancakes', 'Callaloo Jamaican Style', 'Chocolate Avocado Mousse'], self.temp.filterByMainIngredient("banana"))

    def test_filterByMainIngredient_upper_banana(self):
        self.assertEqual(['Banana Pancakes', 'Callaloo Jamaican Style', 'Chocolate Avocado Mousse'], self.temp.filterByMainIngredient("BANANA"))

    def test_filterByMainIngredient_mixed_size_chicken(self):
        self.assertEqual(['Brown Stew Chicken', 'Chicken & mushroom Hotpot', 'Chicken Alfredo Primavera', 'Chicken Basquaise', 'Chicken Congee', 'Chicken Handi', 'Kentucky Fried Chicken', 'Kung Pao Chicken', 'Pad See Ew', 'Piri-piri chicken and slaw', 'Thai Green Curry'], self.temp.filterByMainIngredient("CHicKeN"))

    def test_filterByMainIngredient_with_space_after_ingredient(self):
        self.assertEqual(['Brown Stew Chicken', 'Chicken & mushroom Hotpot', 'Chicken Alfredo Primavera', 'Chicken Basquaise', 'Chicken Congee', 'Chicken Handi', 'Kentucky Fried Chicken', 'Kung Pao Chicken', 'Pad See Ew', 'Piri-piri chicken and slaw', 'Thai Green Curry'], self.temp.filterByMainIngredient("chicken "))

    def test_filterByMainIngredient_weird_str(self):
        self.assertRaises(Exception, self.temp.filterByMainIngredient, "snkgnklgnb")

    def test_filterByMainIngredient_with_space_before_ingredient(self):
        self.assertRaises(Exception, self.temp.filterByMainIngredient, " chicken")

    def test_filterByMainIngredient_Exception_int(self):
        self.assertRaises(Exception, self.temp.filterByMainIngredient, 12)

    def test_filterByMainIngredient_Exception_empty_list(self):
        self.assertRaises(Exception, self.temp.filterByMainIngredient, [])

    def test_filterByMainIngredient_Exception_list_with_ingredient_name(self):
        self.assertRaises(Exception, self.temp.filterByMainIngredient, ["Chicken"])

    def test_filterByMainIngredient_Exception_negative_int(self):
        self.assertRaises(Exception, self.temp.filterByMainIngredient, -331)

    def test_filterByMainIngredient_Exception_float(self):
        self.assertRaises(Exception, self.temp.filterByMainIngredient, 32.23421)

    def test_filterByMainIngredient_Exception_negative_float(self):
        self.assertRaises(Exception, self.temp.filterByMainIngredient, -6.23)

    def test_filterByMainIngredient_Exception_dict(self):
        self.assertRaises(Exception, self.temp.filterByMainIngredient, {})

    def test_filterByMainIngredient_Exception_tuple(self):
        self.assertRaises(Exception, self.temp.filterByMainIngredient, ())

# Filter by category
    def test_filterByCategory_lower_seafood(self):
        self.assertEqual(
            ['Baked salmon with fennel & tomatoes', 'Cajun spiced fish tacos', 'Escovitch Fish', 'Fish fofos', 'Fish pie', 'Fish Stew with Rouille', 'Garides Saganaki', 'Grilled Portuguese sardines', 'Honey Teriyaki Salmon', 'Kedgeree', 'Kung Po Prawns', 'Laksa King Prawn Noodles', 'Mediterranean Pasta Salad', 'Mee goreng mamak', 'Nasi lemak', 'Portuguese fish stew (Caldeirada de peixe)', 'Recheado Masala Fish', 'Salmon Avocado Salad', 'Salmon Prawn Risotto', 'Saltfish and Ackee', 'Seafood fideuà', 'Shrimp Chow Fun', 'Sledz w Oleju (Polish Herrings)', 'Spring onion and prawn empanadas', 'Three Fish Pie', 'Tuna and Egg Briks', 'Tuna Nicoise']
            , self.temp.filterByCategory("seafood"))

    def test_filterByCategory_upper_dessert(self):
        self.assertEqual(
            ['Apam balik', 'Apple & Blackberry Crumble', 'Apple Frangipan Tart', 'Bakewell tart', 'Banana Pancakes',
             'Battenberg Cake', 'BeaverTails', 'Blackberry Fool', 'Bread and Butter Pudding', 'Budino Di Ricotta',
             'Canadian Butter Tarts', 'Carrot Cake', 'Cashew Ghoriba Biscuits', 'Chelsea Buns', 'Chinon Apple Tarts',
             'Choc Chip Pecan Pie', 'Chocolate Avocado Mousse', 'Chocolate Caramel Crispy', 'Chocolate Gateau',
             'Chocolate Raspberry Brownies', 'Chocolate Souffle', 'Christmas cake', 'Christmas Pudding Flapjack',
             'Christmas Pudding Trifle', 'Classic Christmas pudding', 'Dundee cake', 'Eccles Cakes', 'Eton Mess',
             'Honey Yogurt Cheesecake', 'Hot Chocolate Fudge', 'Jam Roly-Poly', 'Key Lime Pie', 'Krispy Kreme Donut',
             'Madeira Cake', 'Mince Pies', 'Nanaimo Bars', 'New York cheesecake', 'Pancakes', 'Parkin Cake',
             'Peach & Blueberry Grunt', 'Peanut Butter Cheesecake', 'Peanut Butter Cookies', 'Pear Tarte Tatin',
             'Polskie Naleśniki (Polish Pancakes)', 'Portuguese custard tarts', 'Pouding chomeur', 'Pumpkin Pie',
             'Rock Cakes', 'Rocky Road Fudge', 'Rogaliki (Polish Croissant Cookies)', 'Salted Caramel Cheescake',
             'Seri muka kuih', 'Spotted Dick', 'Sticky Toffee Pudding', 'Sticky Toffee Pudding Ultimate',
             'Strawberry Rhubarb Pie', 'Sugar Pie', 'Summer Pudding', 'Tarte Tatin', 'Timbits', 'Treacle Tart',
             'Tunisian Orange Cake', 'Walnut Roll Gužvara', 'White chocolate creme brulee']
            , self.temp.filterByCategory("DESSERT"))

    def test_filterByCategory_mixed_size_dessert(self):
        self.assertEqual(
            ['Apam balik', 'Apple & Blackberry Crumble', 'Apple Frangipan Tart', 'Bakewell tart', 'Banana Pancakes', 'Battenberg Cake', 'BeaverTails', 'Blackberry Fool', 'Bread and Butter Pudding', 'Budino Di Ricotta', 'Canadian Butter Tarts', 'Carrot Cake', 'Cashew Ghoriba Biscuits', 'Chelsea Buns', 'Chinon Apple Tarts', 'Choc Chip Pecan Pie', 'Chocolate Avocado Mousse', 'Chocolate Caramel Crispy', 'Chocolate Gateau', 'Chocolate Raspberry Brownies', 'Chocolate Souffle', 'Christmas cake', 'Christmas Pudding Flapjack', 'Christmas Pudding Trifle', 'Classic Christmas pudding', 'Dundee cake', 'Eccles Cakes', 'Eton Mess', 'Honey Yogurt Cheesecake', 'Hot Chocolate Fudge', 'Jam Roly-Poly', 'Key Lime Pie', 'Krispy Kreme Donut', 'Madeira Cake', 'Mince Pies', 'Nanaimo Bars', 'New York cheesecake', 'Pancakes', 'Parkin Cake', 'Peach & Blueberry Grunt', 'Peanut Butter Cheesecake', 'Peanut Butter Cookies', 'Pear Tarte Tatin', 'Polskie Naleśniki (Polish Pancakes)', 'Portuguese custard tarts', 'Pouding chomeur', 'Pumpkin Pie', 'Rock Cakes', 'Rocky Road Fudge', 'Rogaliki (Polish Croissant Cookies)', 'Salted Caramel Cheescake', 'Seri muka kuih', 'Spotted Dick', 'Sticky Toffee Pudding', 'Sticky Toffee Pudding Ultimate', 'Strawberry Rhubarb Pie', 'Sugar Pie', 'Summer Pudding', 'Tarte Tatin', 'Timbits', 'Treacle Tart', 'Tunisian Orange Cake', 'Walnut Roll Gužvara', 'White chocolate creme brulee']
            , self.temp.filterByCategory("DeSserT"))

    def test_filterByCategory_with_space_after_category(self):
        self.assertEqual(
            ['Apam balik', 'Apple & Blackberry Crumble', 'Apple Frangipan Tart', 'Bakewell tart', 'Banana Pancakes',
             'Battenberg Cake', 'BeaverTails', 'Blackberry Fool', 'Bread and Butter Pudding', 'Budino Di Ricotta',
             'Canadian Butter Tarts', 'Carrot Cake', 'Cashew Ghoriba Biscuits', 'Chelsea Buns', 'Chinon Apple Tarts',
             'Choc Chip Pecan Pie', 'Chocolate Avocado Mousse', 'Chocolate Caramel Crispy', 'Chocolate Gateau',
             'Chocolate Raspberry Brownies', 'Chocolate Souffle', 'Christmas cake', 'Christmas Pudding Flapjack',
             'Christmas Pudding Trifle', 'Classic Christmas pudding', 'Dundee cake', 'Eccles Cakes', 'Eton Mess',
             'Honey Yogurt Cheesecake', 'Hot Chocolate Fudge', 'Jam Roly-Poly', 'Key Lime Pie', 'Krispy Kreme Donut',
             'Madeira Cake', 'Mince Pies', 'Nanaimo Bars', 'New York cheesecake', 'Pancakes', 'Parkin Cake',
             'Peach & Blueberry Grunt', 'Peanut Butter Cheesecake', 'Peanut Butter Cookies', 'Pear Tarte Tatin',
             'Polskie Naleśniki (Polish Pancakes)', 'Portuguese custard tarts', 'Pouding chomeur', 'Pumpkin Pie',
             'Rock Cakes', 'Rocky Road Fudge', 'Rogaliki (Polish Croissant Cookies)', 'Salted Caramel Cheescake',
             'Seri muka kuih', 'Spotted Dick', 'Sticky Toffee Pudding', 'Sticky Toffee Pudding Ultimate',
             'Strawberry Rhubarb Pie', 'Sugar Pie', 'Summer Pudding', 'Tarte Tatin', 'Timbits', 'Treacle Tart',
             'Tunisian Orange Cake', 'Walnut Roll Gužvara', 'White chocolate creme brulee']
            , self.temp.filterByCategory("DESSERT "))

    def test_filterByCategory_weird_str(self):
        self.assertRaises(Exception, self.temp.filterByCategory, "hdshlohgap")

    def test_filterByCategory_with_space_before_category(self):
        self.assertRaises(Exception, self.temp.filterByCategory, " Dessert")

    def test_filterByCategory_Exception_int(self):
        self.assertRaises(Exception, self.temp.filterByCategory, 132)

    def test_filterByCategory_Exception_empty_list(self):
        self.assertRaises(Exception, self.temp.filterByCategory, [])

    def test_filterByCategory_Exception_list_with_category_name(self):
        self.assertRaises(Exception, self.temp.filterByCategory, ["Dessert"])

    def test_filterByCategory_Exception_negative_int(self):
        self.assertRaises(Exception, self.temp.filterByCategory, -3)

    def test_filterByCategory_Exception_float(self):
        self.assertRaises(Exception, self.temp.filterByCategory, 3.23)

    def test_filterByCategory_Exception_negative_float(self):
        self.assertRaises(Exception, self.temp.filterByCategory, -63.3)

    def test_filterByCategory_Exception_dict(self):
        self.assertRaises(Exception, self.temp.filterByCategory, {})

    def test_filterByCategory_Exception_tuple(self):
        self.assertRaises(Exception, self.temp.filterByCategory, ())


# Filter by area
    def test_filterByArea_upper_polish(self):
        self.assertEqual(
            ['Bigos (Hunters Stew)', 'Gołąbki (cabbage roll)', 'Paszteciki (Polish Pasties)', 'Pierogi (Polish Dumplings)', 'Polskie Naleśniki (Polish Pancakes)', 'Rogaliki (Polish Croissant Cookies)', 'Rosół (Polish Chicken Soup)', 'Sledz w Oleju (Polish Herrings)']
            , self.temp.filterByArea("POLISH"))

    def test_filterByArea_lower_polish(self):
        self.assertEqual(
            ['Bigos (Hunters Stew)', 'Gołąbki (cabbage roll)', 'Paszteciki (Polish Pasties)',
             'Pierogi (Polish Dumplings)', 'Polskie Naleśniki (Polish Pancakes)', 'Rogaliki (Polish Croissant Cookies)',
             'Rosół (Polish Chicken Soup)', 'Sledz w Oleju (Polish Herrings)']
            , self.temp.filterByArea("polish"))

    def test_filterByArea_mixed_size_polish(self):
        self.assertEqual(
            ['Bigos (Hunters Stew)', 'Gołąbki (cabbage roll)', 'Paszteciki (Polish Pasties)',
             'Pierogi (Polish Dumplings)', 'Polskie Naleśniki (Polish Pancakes)', 'Rogaliki (Polish Croissant Cookies)',
             'Rosół (Polish Chicken Soup)', 'Sledz w Oleju (Polish Herrings)']
            , self.temp.filterByArea("PoLisH"))

    def test_filterByArea_Canadian(self):
        self.assertEqual(
            ['BeaverTails', 'Breakfast Potatoes', 'Canadian Butter Tarts', 'Montreal Smoked Meat', 'Nanaimo Bars',
             'Pate Chinois', 'Pouding chomeur', 'Poutine', 'Rappie Pie', 'Split Pea Soup', 'Sugar Pie', 'Timbits', 'Tourtiere']
            , self.temp.filterByArea("Canadian"))

    def test_filterByArea_with_space_after_area(self):
        self.assertEqual(
            ['Bigos (Hunters Stew)', 'Gołąbki (cabbage roll)', 'Paszteciki (Polish Pasties)',
             'Pierogi (Polish Dumplings)', 'Polskie Naleśniki (Polish Pancakes)', 'Rogaliki (Polish Croissant Cookies)',
             'Rosół (Polish Chicken Soup)', 'Sledz w Oleju (Polish Herrings)']
            , self.temp.filterByArea("polish "))


    def test_filterByArea_weird_str(self):
        self.assertRaises(Exception, self.temp.filterByArea, "adkgh;iaplshg")

    def test_filterByArea_with_space_before_area(self):
        self.assertRaises(Exception, self.temp.filterByArea, " Polish")

    def test_filterByArea_Exception_int(self):
        self.assertRaises(Exception, self.temp.filterByArea, 42)

    def test_filterByArea_Exception_empty_list(self):
        self.assertRaises(Exception, self.temp.filterByArea, [])

    def test_filterByArea_Exception_list_with_area_name(self):
        self.assertRaises(Exception, self.temp.filterByArea, ["Polish"])

    def test_filterByArea_Exception_negative_int(self):
        self.assertRaises(Exception, self.temp.filterByArea, -31)

    def test_filterByArea_Exception_float(self):
        self.assertRaises(Exception, self.temp.filterByArea, 34.33)

    def test_filterByArea_Exception_negative_float(self):
        self.assertRaises(Exception, self.temp.filterByArea, -6.413)

    def test_filterByArea_Exception_dict(self):
        self.assertRaises(Exception, self.temp.filterByArea, {})

    def test_filterByArea_Exception_tuple(self):
        self.assertRaises(Exception, self.temp.filterByArea, ())

    def tearDown(self):
        self.temp = None

# Make shopping list to meals

    def test_makeShoppingListToMeals_one_meal_upper(self):
        self.assertEqual(
            ['Butter', 'Chopped Onion', 'Sauerkraut', 'Potatoes', 'Eggs', 'Sour Cream', 'Flour', 'Salt', 'Baking Powder']
            ,self.temp.makeShoppingListToMeals("PIEROGI"))

    def test_makeShoppingListToMeals_one_meal_lower(self):
        self.assertEqual(
            ['Butter', 'Chopped Onion', 'Sauerkraut', 'Potatoes', 'Eggs', 'Sour Cream', 'Flour', 'Salt', 'Baking Powder']
            ,self.temp.makeShoppingListToMeals("pierogi"))

    def test_makeShoppingListToMeals_one_meal_mixed_size(self):
        self.assertEqual(
            ['Butter', 'Chopped Onion', 'Sauerkraut', 'Potatoes', 'Eggs', 'Sour Cream', 'Flour', 'Salt', 'Baking Powder']
            ,self.temp.makeShoppingListToMeals("PIerOgI"))

    def test_makeShoppingListToMeals_two_meals_lower(self):
        self.assertEqual(
            ['Butter', 'Chopped Onion', 'Sauerkraut', 'Potatoes', 'Eggs', 'Sour Cream', 'Flour', 'Salt', 'Baking Powder', 'Cabbage', 'Onion', 'Ground Beef', 'Ground Pork', 'Rice', 'Garlic', 'Black Pepper', 'Tomato Puree']
            ,self.temp.makeShoppingListToMeals("pierogi", "gołąbki"))

    def test_makeShoppingListToMeals_two_meals_lower_upper(self):
        self.assertEqual(
            ['Butter', 'Chopped Onion', 'Sauerkraut', 'Potatoes', 'Eggs', 'Sour Cream', 'Flour', 'Salt', 'Baking Powder', 'Cabbage', 'Onion', 'Ground Beef', 'Ground Pork', 'Rice', 'Garlic', 'Black Pepper', 'Tomato Puree']
            ,self.temp.makeShoppingListToMeals("pierogi", "GOŁĄBKI"))

    def test_makeShoppingListToMeals_many_meals_lower(self):
        self.assertEqual(
            ['Butter', 'Chopped Onion', 'Sauerkraut', 'Potatoes', 'Eggs', 'Sour Cream', 'Flour', 'Salt',
             'Baking Powder', 'Cabbage', 'Onion', 'Ground Beef', 'Ground Pork', 'Rice', 'Garlic', 'Black Pepper',
             'Tomato Puree', 'Milk', 'Water', 'Sugar',
             'penne rigate', 'olive oil', 'garlic', 'chopped tomatoes', 'red chile flakes', 'italian seasoning',
             'basil', 'Parmigiano-Reggiano']
            ,self.temp.makeShoppingListToMeals("pierogi", "gołąbki", "polskie nalesniki", "arrabiata"))

    def test_makeShoppingListToMeals_weird_str(self):
        self.assertRaises(Exception, self.temp.makeShoppingListToMeals, "adkgh;iaplshg")

    def test_makeShoppingListToMeals_with_space_before_meal_name(self):
        self.assertRaises(Exception, self.temp.makeShoppingListToMeals, " Pierogi")

    def test_makeShoppingListToMeals_Exception_many_arguments_one_in_the_end_int(self):
        self.assertRaises(Exception, self.temp.makeShoppingListToMeals, "pierogi", "gołąbki", "polskie nalesniki", "arrabiata", 42)

    def test_makeShoppingListToMeals_Exception_many_arguments_one_int_the_middle_int(self):
        self.assertRaises(Exception, self.temp.makeShoppingListToMeals, "pierogi", "gołąbki", 3, "polskie nalesniki", "arrabiata")

    def test_makeShoppingListToMeals_Exception_many_arguments_one_int_front_int(self):
        self.assertRaises(Exception, self.temp.makeShoppingListToMeals, 8, "pierogi", "gołąbki", "polskie nalesniki", "arrabiata")

    def test_makeShoppingListToMeals_Exception_int(self):
        self.assertRaises(Exception, self.temp.makeShoppingListToMeals, 42)

    def test_makeShoppingListToMeals_Exception_empty_list(self):
        self.assertRaises(Exception, self.temp.makeShoppingListToMeals, [])

    def test_makeShoppingListToMeals_Exception_many_arguments_one_in_the_end_empty_list(self):
        self.assertRaises(Exception, self.temp.makeShoppingListToMeals, "pierogi", "gołąbki", "polskie nalesniki", "arrabiata", [])

    def test_makeShoppingListToMeals_Exception_many_arguments_one_in_the_middle_empty_list(self):
        self.assertRaises(Exception, self.temp.makeShoppingListToMeals, "pierogi", "gołąbki", [], "polskie nalesniki", "arrabiata")

    def test_makeShoppingListToMeals_Exception_many_arguments_one_in_front_empty_list(self):
        self.assertRaises(Exception, self.temp.makeShoppingListToMeals, [], "pierogi", "gołąbki", "polskie nalesniki", "arrabiata")

    def test_makeShoppingListToMeals_Exception_many_arguments_one_in_front_list(self):
        self.assertRaises(Exception, self.temp.makeShoppingListToMeals, ["polskie nalesniki", "arrabiata"], "pierogi", "gołąbki", "polskie nalesniki", "arrabiata")

    def test_makeShoppingListToMeals_Exception_many_arguments_one_in_the_end_list(self):
        self.assertRaises(Exception, self.temp.makeShoppingListToMeals, "pierogi", "gołąbki", "polskie nalesniki", "arrabiata", ["pierogi", "gołąbki"])

    def test_makeShoppingListToMeals_Exception_many_arguments_one_in_the_middle_list(self):
        self.assertRaises(Exception, self.temp.makeShoppingListToMeals, "pierogi", "gołąbki", ["pierogi", "gołąbki"], "polskie nalesniki", "arrabiata")

    def test_makeShoppingListToMeals_Exception_list_with_meal_name(self):
        self.assertRaises(Exception, self.temp.makeShoppingListToMeals, ["gołąbki"])

    def test_makeShoppingListToMeals_Exception_negative_int(self):
        self.assertRaises(Exception, self.temp.makeShoppingListToMeals, -31)

    def test_makeShoppingListToMeals_Exception_float(self):
        self.assertRaises(Exception, self.temp.makeShoppingListToMeals, 34.33)

    def test_makeShoppingListToMeals_Exception_negative_float(self):
        self.assertRaises(Exception, self.temp.makeShoppingListToMeals, -6.413)

    def test_makeShoppingListToMeals_Exception_dict(self):
        self.assertRaises(Exception, self.temp.makeShoppingListToMeals, {})

    def test_makeShoppingListToMeals_Exception_many_arguments_one_in_the_end_dict(self):
        self.assertRaises(Exception, self.temp.makeShoppingListToMeals, "pierogi", "gołąbki", "polskie nalesniki", "arrabiata", {})

    def test_makeShoppingListToMeals_Exception_many_arguments_one_in_the_middle_dict(self):
        self.assertRaises(Exception, self.temp.makeShoppingListToMeals, "pierogi", "gołąbki", {}, "polskie nalesniki", "arrabiata")

    def test_makeShoppingListToMeals_Exception_many_arguments_one_in_front_dict(self):
        self.assertRaises(Exception, self.temp.makeShoppingListToMeals, {}, "pierogi", "gołąbki", "polskie nalesniki", "arrabiata")

    def test_makeShoppingListToMeals_Exception_tuple(self):
        self.assertRaises(Exception, self.temp.makeShoppingListToMeals, ())

    def test_makeShoppingListToMeals_Exception_many_arguments_one_in_the_end_tuple(self):
        self.assertRaises(Exception, self.temp.makeShoppingListToMeals, "pierogi", "gołąbki", "polskie nalesniki", "arrabiata", ())

    def test_makeShoppingListToMeals_Exception_many_arguments_one_in_the_middle_tuple(self):
        self.assertRaises(Exception, self.temp.makeShoppingListToMeals, "pierogi", "gołąbki", (), "polskie nalesniki", "arrabiata")

    def test_makeShoppingListToMeals_Exception_many_arguments_one_in_front_tuple(self):
        self.assertRaises(Exception, self.temp.makeShoppingListToMeals, (), "pierogi", "gołąbki", "polskie nalesniki", "arrabiata")

    def tearDown(self):
        self.temp = None

class RecipeTests(unittest.TestCase):

    def setUp(self):
        self.temp = Recipe()

# Recipe by meal name
    def test_recipeByMealName_lower_pierogi(self):
        self.assertEqual("To prepare the sauerkraut filling, melt the butter in a skillet over medium heat. Stir in the onion, and cook until translucent, about 5 minutes. Add the drained sauerkraut and cook for an additional 5 minutes. Season to taste with salt and pepper, then remove to a plate to cool.\r\n\r\nFor the mashed potato filling, melt the butter in a skillet over medium heat. Stir in the onion, and cook until translucent, about 5 minutes. Stir into the mashed potatoes, and season with salt and white pepper.\r\n\r\nTo make the dough, beat together the eggs and sour cream until smooth. Sift together the flour, salt, and baking powder; stir into the sour cream mixture until dough comes together. Knead the dough on a lightly floured surface until firm and smooth. Divide the dough in half, then roll out one half to 1/8 inch thickness. Cut into 3 inch rounds using a biscuit cutter.\r\n\r\nPlace a small spoonful of the mashed potato filling into the center of each round. Moisten the edges with water, fold over, and press together with a fork to seal. Repeat procedure with the remaining dough and the sauerkraut filling.\r\n\r\nBring a large pot of lightly salted water to a boil. Add perogies and cook for 3 to 5 minutes or until pierogi float to the top. Remove with a slotted spoon.", self.temp.recipeByMealName("pierogi"))

    def test_recipeByMealName_upper_pierogi(self):
        self.assertEqual("To prepare the sauerkraut filling, melt the butter in a skillet over medium heat. Stir in the onion, and cook until translucent, about 5 minutes. Add the drained sauerkraut and cook for an additional 5 minutes. Season to taste with salt and pepper, then remove to a plate to cool.\r\n\r\nFor the mashed potato filling, melt the butter in a skillet over medium heat. Stir in the onion, and cook until translucent, about 5 minutes. Stir into the mashed potatoes, and season with salt and white pepper.\r\n\r\nTo make the dough, beat together the eggs and sour cream until smooth. Sift together the flour, salt, and baking powder; stir into the sour cream mixture until dough comes together. Knead the dough on a lightly floured surface until firm and smooth. Divide the dough in half, then roll out one half to 1/8 inch thickness. Cut into 3 inch rounds using a biscuit cutter.\r\n\r\nPlace a small spoonful of the mashed potato filling into the center of each round. Moisten the edges with water, fold over, and press together with a fork to seal. Repeat procedure with the remaining dough and the sauerkraut filling.\r\n\r\nBring a large pot of lightly salted water to a boil. Add perogies and cook for 3 to 5 minutes or until pierogi float to the top. Remove with a slotted spoon.", self.temp.recipeByMealName("PIEROGI"))

    def test_recipeByMealName_mixed_size_pierogi(self):
        self.assertEqual("To prepare the sauerkraut filling, melt the butter in a skillet over medium heat. Stir in the onion, and cook until translucent, about 5 minutes. Add the drained sauerkraut and cook for an additional 5 minutes. Season to taste with salt and pepper, then remove to a plate to cool.\r\n\r\nFor the mashed potato filling, melt the butter in a skillet over medium heat. Stir in the onion, and cook until translucent, about 5 minutes. Stir into the mashed potatoes, and season with salt and white pepper.\r\n\r\nTo make the dough, beat together the eggs and sour cream until smooth. Sift together the flour, salt, and baking powder; stir into the sour cream mixture until dough comes together. Knead the dough on a lightly floured surface until firm and smooth. Divide the dough in half, then roll out one half to 1/8 inch thickness. Cut into 3 inch rounds using a biscuit cutter.\r\n\r\nPlace a small spoonful of the mashed potato filling into the center of each round. Moisten the edges with water, fold over, and press together with a fork to seal. Repeat procedure with the remaining dough and the sauerkraut filling.\r\n\r\nBring a large pot of lightly salted water to a boil. Add perogies and cook for 3 to 5 minutes or until pierogi float to the top. Remove with a slotted spoon.", self.temp.recipeByMealName("PIerOgI"))

    def test_recipeByMealName_meal_with_space(self):
        self.assertEqual("Add flour, eggs, milk, water, and salt in a large bowl then mix with a hand mixer until you have a smooth, lump-free batter.\r\nAt this point, mix in the butter or the vegetable oil. Alternatively, you can use them to grease the pan before frying each pancake.\r\nHeat a non-stick pan over medium heat, then pour in the batter, swirling the pan to help it spread.\r\nWhen the pancake starts pulling away a bit from the sides, and the top is no longer wet, flip it and cook shortly on the other side as well.\r\nTransfer to a plate. Cook the remaining batter until all used up.\r\nServe warm, with the filling of your choice.", self.temp.recipeByMealName("Polskie nalesniki"))

    def test_recipeByMealName_with_space_after_meal_name(self):
        self.assertEqual("To prepare the sauerkraut filling, melt the butter in a skillet over medium heat. Stir in the onion, and cook until translucent, about 5 minutes. Add the drained sauerkraut and cook for an additional 5 minutes. Season to taste with salt and pepper, then remove to a plate to cool.\r\n\r\nFor the mashed potato filling, melt the butter in a skillet over medium heat. Stir in the onion, and cook until translucent, about 5 minutes. Stir into the mashed potatoes, and season with salt and white pepper.\r\n\r\nTo make the dough, beat together the eggs and sour cream until smooth. Sift together the flour, salt, and baking powder; stir into the sour cream mixture until dough comes together. Knead the dough on a lightly floured surface until firm and smooth. Divide the dough in half, then roll out one half to 1/8 inch thickness. Cut into 3 inch rounds using a biscuit cutter.\r\n\r\nPlace a small spoonful of the mashed potato filling into the center of each round. Moisten the edges with water, fold over, and press together with a fork to seal. Repeat procedure with the remaining dough and the sauerkraut filling.\r\n\r\nBring a large pot of lightly salted water to a boil. Add perogies and cook for 3 to 5 minutes or until pierogi float to the top. Remove with a slotted spoon.", self.temp.recipeByMealName("Pierogi "))

    def test_recipeByMealName_weird_str(self):
        self.assertRaises(Exception, self.temp.recipeByMealName, "adkgh;iaplshg")

    def test_recipeByMealName_with_space_before_meal_name(self):
        self.assertRaises(Exception, self.temp.recipeByMealName, " Pierogi")

    def test_recipeByMealName_Exception_int(self):
        self.assertRaises(Exception, self.temp.recipeByMealName, 42)

    def test_recipeByMealName_Exception_empty_list(self):
        self.assertRaises(Exception, self.temp.recipeByMealName, [])

    def test_recipeByMealName_Exception_list_with_meal_name(self):
        self.assertRaises(Exception, self.temp.recipeByMealName, ["gołąbki"])

    def test_recipeByMealName_Exception_negative_int(self):
        self.assertRaises(Exception, self.temp.recipeByMealName, -31)

    def test_recipeByMealName_Exception_float(self):
        self.assertRaises(Exception, self.temp.recipeByMealName, 34.33)

    def test_recipeByMealName_Exception_negative_float(self):
        self.assertRaises(Exception, self.temp.recipeByMealName, -6.413)

    def test_recipeByMealName_Exception_dict(self):
        self.assertRaises(Exception, self.temp.recipeByMealName, {})

    def test_recipeByMealName_Exception_tuple(self):
        self.assertRaises(Exception, self.temp.recipeByMealName, ())

# Recipe with smallest number of ingredients starting with letter
    def test_recipeWithSmallestNumberOfIngredientsStartingWithLetter_lower_a(self):
        self.assertEqual([('Apple Frangipan Tart', 'Preheat the oven to 200C/180C Fan/Gas 6.\r\nPut the biscuits in a large re-sealable freezer bag and bash with a rolling pin into fine crumbs. Melt the butter in a small pan, then add the biscuit crumbs and stir until coated with butter. Tip into the tart tin and, using the back of a spoon, press over the base and sides of the tin to give an even layer. Chill in the fridge while you make the filling.\r\nCream together the butter and sugar until light and fluffy. You can do this in a food processor if you have one. Process for 2-3 minutes. Mix in the eggs, then add the ground almonds and almond extract and blend until well combined.\r\nPeel the apples, and cut thin slices of apple. Do this at the last minute to prevent the apple going brown. Arrange the slices over the biscuit base. Spread the frangipane filling evenly on top. Level the surface and sprinkle with the flaked almonds.\r\nBake for 20-25 minutes until golden-brown and set.\r\nRemove from the oven and leave to cool for 15 minutes. Remove the sides of the tin. An easy way to do this is to stand the tin on a can of beans and push down gently on the edges of the tin.\r\nTransfer the tart, with the tin base attached, to a serving plate. Serve warm with cream, crème fraiche or ice cream.'),
                          ('Apple & Blackberry Crumble', 'Heat oven to 190C/170C fan/gas 5. Tip the flour and sugar into a large bowl. Add the butter, then rub into the flour using your fingertips to make a light breadcrumb texture. Do not overwork it or the crumble will become heavy. Sprinkle the mixture evenly over a baking sheet and bake for 15 mins or until lightly coloured.\r\nMeanwhile, for the compote, peel, core and cut the apples into 2cm dice. Put the butter and sugar in a medium saucepan and melt together over a medium heat. Cook for 3 mins until the mixture turns to a light caramel. Stir in the apples and cook for 3 mins. Add the blackberries and cinnamon, and cook for 3 mins more. Cover, remove from the heat, then leave for 2-3 mins to continue cooking in the warmth of the pan.\r\nTo serve, spoon the warm fruit into an ovenproof gratin dish, top with the crumble mix, then reheat in the oven for 5-10 mins. Serve with vanilla ice cream.'),
                          ('Apam balik', 'Mix milk, oil and egg together. Sift flour, baking powder and salt into the mixture. Stir well until all ingredients are combined evenly.\r\n\r\nSpread some batter onto the pan. Spread a thin layer of batter to the side of the pan. Cover the pan for 30-60 seconds until small air bubbles appear.\r\n\r\nAdd butter, cream corn, crushed peanuts and sugar onto the pancake. Fold the pancake into half once the bottom surface is browned.\r\n\r\nCut into wedges and best eaten when it is warm.')],
                         self.temp.recipeWithSmallestNumberOfIngredientsStartingWithLetter("a"))

    def test_recipeWithSmallestNumberOfIngredientsStartingWithLetter_upper_a(self):
        self.assertEqual([('Apple Frangipan Tart', 'Preheat the oven to 200C/180C Fan/Gas 6.\r\nPut the biscuits in a large re-sealable freezer bag and bash with a rolling pin into fine crumbs. Melt the butter in a small pan, then add the biscuit crumbs and stir until coated with butter. Tip into the tart tin and, using the back of a spoon, press over the base and sides of the tin to give an even layer. Chill in the fridge while you make the filling.\r\nCream together the butter and sugar until light and fluffy. You can do this in a food processor if you have one. Process for 2-3 minutes. Mix in the eggs, then add the ground almonds and almond extract and blend until well combined.\r\nPeel the apples, and cut thin slices of apple. Do this at the last minute to prevent the apple going brown. Arrange the slices over the biscuit base. Spread the frangipane filling evenly on top. Level the surface and sprinkle with the flaked almonds.\r\nBake for 20-25 minutes until golden-brown and set.\r\nRemove from the oven and leave to cool for 15 minutes. Remove the sides of the tin. An easy way to do this is to stand the tin on a can of beans and push down gently on the edges of the tin.\r\nTransfer the tart, with the tin base attached, to a serving plate. Serve warm with cream, crème fraiche or ice cream.'),
                          ('Apple & Blackberry Crumble', 'Heat oven to 190C/170C fan/gas 5. Tip the flour and sugar into a large bowl. Add the butter, then rub into the flour using your fingertips to make a light breadcrumb texture. Do not overwork it or the crumble will become heavy. Sprinkle the mixture evenly over a baking sheet and bake for 15 mins or until lightly coloured.\r\nMeanwhile, for the compote, peel, core and cut the apples into 2cm dice. Put the butter and sugar in a medium saucepan and melt together over a medium heat. Cook for 3 mins until the mixture turns to a light caramel. Stir in the apples and cook for 3 mins. Add the blackberries and cinnamon, and cook for 3 mins more. Cover, remove from the heat, then leave for 2-3 mins to continue cooking in the warmth of the pan.\r\nTo serve, spoon the warm fruit into an ovenproof gratin dish, top with the crumble mix, then reheat in the oven for 5-10 mins. Serve with vanilla ice cream.'),
                          ('Apam balik', 'Mix milk, oil and egg together. Sift flour, baking powder and salt into the mixture. Stir well until all ingredients are combined evenly.\r\n\r\nSpread some batter onto the pan. Spread a thin layer of batter to the side of the pan. Cover the pan for 30-60 seconds until small air bubbles appear.\r\n\r\nAdd butter, cream corn, crushed peanuts and sugar onto the pancake. Fold the pancake into half once the bottom surface is browned.\r\n\r\nCut into wedges and best eaten when it is warm.')],
                         self.temp.recipeWithSmallestNumberOfIngredientsStartingWithLetter("A"))

    def test_recipeWithSmallestNumberOfIngredientsStartingWithLetter_upper_a(self):
        self.assertEqual([('Spaghetti Bolognese', 'Put the onion and oil in a large pan and fry over a fairly high heat for 3-4 mins. Add the garlic and mince and fry until they both brown. Add the mushrooms and herbs, and cook for another couple of mins.\r\n\r\nStir in the tomatoes, beef stock, tomato ketchup or purée, Worcestershire sauce and seasoning. Bring to the boil, then reduce the heat, cover and simmer, stirring occasionally, for 30 mins.\r\n\r\nMeanwhile, cook the spaghetti in a large pan of boiling, salted water, according to packet instructions. Drain well, run hot water through it, put it back in the pan and add a dash of olive oil, if you like, then stir in the meat sauce. Serve in hot bowls and hand round Parmesan cheese, for sprinkling on top.'),
                          ('Spicy Arrabiata Penne', 'Bring a large pot of water to a boil. Add kosher salt to the boiling water, then add the pasta. Cook according to the package instructions, about 9 minutes.\r\nIn a large skillet over medium-high heat, add the olive oil and heat until the oil starts to shimmer. Add the garlic and cook, stirring, until fragrant, 1 to 2 minutes. Add the chopped tomatoes, red chile flakes, Italian seasoning and salt and pepper to taste. Bring to a boil and cook for 5 minutes. Remove from the heat and add the chopped basil.\r\nDrain the pasta and add it to the sauce. Garnish with Parmigiano-Reggiano flakes and more basil and serve warm.'),\
                          ('Stovetop Eggplant With Harissa, Chickpeas, and Cumin Yogurt', 'Heat the oil in a 12-inch skillet over high heat until shimmering. Add the eggplants and lower the heat to medium. Season with salt and pepper as you rotate the eggplants, browning them on all sides. Continue to cook, turning regularly, until a fork inserted into the eggplant meets no resistance (you may have to stand them up on their fat end to finish cooking the thickest parts), about 20 minutes, lowering the heat and sprinkling water into the pan as necessary if the eggplants threaten to burn or smoke excessively.\r\n\r\n2.\r\nMix the harissa, chickpeas and tomatoes together, then add to the eggplants. Cook until the tomatoes have blistered and broken down, about 5 minutes more. Season with salt and pepper and add water as necessary to thin to a saucy consistency. Meanwhile, combine the yogurt and cumin in a serving bowl. Season with salt and pepper.\r\n\r\n3.\r\nTop the eggplant mixture with the parsley, drizzle with more extra virgin olive oil, and serve with the yogurt on the side.'),
                          ('Squash linguine', 'Heat oven to 200C/180C fan/gas 6. Put the squash and garlic on a baking tray and drizzle with the olive oil. Roast for 35-40 mins until soft. Season.\r\nCook the pasta according to pack instructions. Drain, reserving the water. Use a stick blender to whizz the squash with 400ml cooking water. Heat some oil in a frying pan, fry the sage until crisp, then drain on kitchen paper. Tip the pasta and sauce into the pan and warm through. Scatter with sage.')],
                         self.temp.recipeWithSmallestNumberOfIngredientsStartingWithLetter("s"))

    def test_recipeWithSmallestNumberOfIngredientsStartingWithLetter_weird_str(self):
        self.assertRaises(Exception, self.temp.recipeWithSmallestNumberOfIngredientsStartingWithLetter, "adkgh;iaplshg")

    def test_recipeWithSmallestNumberOfIngredientsStartingWithLetter_with_space_before_letter(self):
        self.assertRaises(Exception, self.temp.recipeWithSmallestNumberOfIngredientsStartingWithLetter, " a")

    def test_recipeWithSmallestNumberOfIngredientsStartingWithLetter_with_space_after_letter(self):
        self.assertRaises(Exception, self.temp.recipeWithSmallestNumberOfIngredientsStartingWithLetter, "a ")

    def test_recipeWithSmallestNumberOfIngredientsStartingWithLetter_Exception_int(self):
        self.assertRaises(Exception, self.temp.recipeWithSmallestNumberOfIngredientsStartingWithLetter, 42)

    def test_recipeWithSmallestNumberOfIngredientsStartingWithLetter_Exception_empty_list(self):
        self.assertRaises(Exception, self.temp.recipeWithSmallestNumberOfIngredientsStartingWithLetter, [])

    def test_recipeWithSmallestNumberOfIngredientsStartingWithLetter_Exception_list_with_meal_name(self):
        self.assertRaises(Exception, self.temp.recipeWithSmallestNumberOfIngredientsStartingWithLetter, ["a"])

    def test_recipeWithSmallestNumberOfIngredientsStartingWithLetter_Exception_negative_int(self):
        self.assertRaises(Exception, self.temp.recipeWithSmallestNumberOfIngredientsStartingWithLetter, -31)

    def test_recipeWithSmallestNumberOfIngredientsStartingWithLetter_Exception_float(self):
        self.assertRaises(Exception, self.temp.recipeWithSmallestNumberOfIngredientsStartingWithLetter, 34.33)

    def test_recipeWithSmallestNumberOfIngredientsStartingWithLetter_Exception_negative_float(self):
        self.assertRaises(Exception, self.temp.recipeWithSmallestNumberOfIngredientsStartingWithLetter, -6.413)

    def test_recipeWithSmallestNumberOfIngredientsStartingWithLetter_Exception_dict(self):
        self.assertRaises(Exception, self.temp.recipeWithSmallestNumberOfIngredientsStartingWithLetter, {})

    def test_recipeWithSmallestNumberOfIngredientsStartingWithLetter_Exception_tuple(self):
        self.assertRaises(Exception, self.temp.recipeWithSmallestNumberOfIngredientsStartingWithLetter, ())


    def tearDown(self):
        self.temp = None

if __name__ == '__main__':
    unittest.main()
