import requests


class Meals:
    def mealByName(self, name):
        meal = []
        r = requests.get(f"http://www.themealdb.com/api/json/v1/1/search.php?s={name}")
        if type(name) is str and r.json()["meals"] != None:
            meal.append({"meal": r.json()["meals"][0]["strMeal"]})
            meal.append({"category": r.json()["meals"][0]["strCategory"]})
            meal.append({"instructions": r.json()["meals"][0]["strInstructions"]})
            ing = []
            for i in range(1, 21):
                ing.append(r.json()["meals"][0]["strIngredient"+str(i)])
            ingList = []
            for string in ing:
                if string != "" and string != None and string not in ingList:
                    ingList.append(string)
            meal.append({"ingredients": ingList})
            return meal

        else:
            raise Exception("Error bad type or meal is not in database")

    def listAllMealsByFirstLetter(self, letter):
        meals = []
        r = requests.get(f"https://www.themealdb.com/api/json/v1/1/search.php?f={letter}")
        if type(letter) is str and letter.lower() in "abcdefghijklmnopqrstuwxyz" and r.json()["meals"] != None:
            for meal in r.json()["meals"]:
                meals.append(meal["strMeal"])
            return meals
        else:
            raise Exception("Error bad type or not letter")

    def howManyMealsStartingWithLetter(self, letter):
        r = requests.get(f"https://www.themealdb.com/api/json/v1/1/search.php?f={letter}")
        if type(letter) is str and letter.lower() in "abcdefghijklmnopqrstuwxyz":
            if r.json()["meals"] == None:
                return 0
            return len(r.json()["meals"])
        else:
            raise Exception("Error bad type or not letter")

    def lookupFullMealDetailsById(self, id):
        meal = []
        r = requests.get(f"https://www.themealdb.com/api/json/v1/1/lookup.php?i={id}")
        if type(id) is int and r.json()["meals"] != None:
            meal.append({"id": r.json()["meals"][0]["idMeal"]})
            meal.append({"meal": r.json()["meals"][0]["strMeal"]})
            meal.append({"category": r.json()["meals"][0]["strCategory"]})
            meal.append({"instructions": r.json()["meals"][0]["strInstructions"]})
            ing = []
            for i in range(1, 21):
                ing.append(r.json()["meals"][0]["strIngredient" + str(i)])
            ingList = []
            for string in ing:
                if string != "" and string != None and string not in ingList:
                    ingList.append(string)
            meal.append({"ingredients": ingList})
            return meal
        else:
            raise Exception("Error bad type or id")

    def mealsStartingWithLetterWithoutBaking(self, letter):
        meals = []
        r = requests.get(f"https://www.themealdb.com/api/json/v1/1/search.php?f={letter}")
        if type(letter) is str and letter.lower() in "abcdefghijklmnopqrstuwxyz":
            if r.json()["meals"] == None:
                return []
            for meal in r.json()["meals"]:
                if meal["strTags"] != None:
                    if "Baking" not in meal["strTags"]:
                        meals.append((meal["strMeal"], meal["strCategory"]))
                else:
                    meals.append((meal["strMeal"], meal["strCategory"]))
            if len(meals) == 0:
                return "No meals"
            return meals
        else:
            raise Exception("Error bad type or not letter")

    def mealWithSmallestNumberOfIngredientsStartingWithLetter(self, letter):
        mealName = []
        number = [30]
        r = requests.get(f"https://www.themealdb.com/api/json/v1/1/search.php?f={letter}")
        if type(letter) is str and letter.lower() in "abcdefghijklmnopqrstuwxyz":
            if r.json()["meals"] == None:
                return []
            for meal in r.json()["meals"]:
                list = []
                for i in range(1, 21):
                    list.append(meal["strIngredient"+str(i)])
                ingList = []
                for string in list:
                    if string != "" and string != None:
                        ingList.append(string)
                if len(ingList) <= number[-1]:
                    mealName.append(meal["strMeal"])
                    number.append(len(ingList))
            return mealName
        else:
            raise Exception("Error bad type or not letter")


class CategoriesAreaIngredients:

    def filterByMainIngredient(self, ingredient):
        mealList = []
        r = requests.get(f"https://www.themealdb.com/api/json/v1/1/filter.php?i={ingredient}")
        if type(ingredient) is str:
            if r.json()["meals"]== None:
                raise Exception("Error no ingredient")
            for meal in r.json()["meals"]:
                mealList.append(meal["strMeal"])
            return mealList
        else:
            raise Exception("Error bad type")

    def filterByCategory(self, category):
        mealList = []
        r = requests.get(f"https://www.themealdb.com/api/json/v1/1/filter.php?c={category}")
        if type(category) is str:
            if r.json()["meals"] == None:
                raise Exception("Error no category")
            for meal in r.json()["meals"]:
                mealList.append(meal["strMeal"])
            return mealList
        else:
            raise Exception("Error bad type")

    def filterByArea(self, area):
        mealList = []
        r = requests.get(f"https://www.themealdb.com/api/json/v1/1/filter.php?a={area}")
        if type(area) is str:
            if r.json()["meals"] == None:
                raise Exception("Error no area")
            for meal in r.json()["meals"]:
                mealList.append(meal["strMeal"])
            return mealList
        else:
            raise Exception("Error bad type")

    def makeShoppingListToMeals(self, *meals):
        list = []
        if len(meals) != 0:
            for meal in meals:
                r = requests.get(f"http://www.themealdb.com/api/json/v1/1/search.php?s={meal}")
                if type(meal) is str and r.json()["meals"] != None:
                    for i in range(1, 21):
                        list.append(r.json()["meals"][0]["strIngredient"+str(i)])
                else:
                    raise Exception("Error bad type or meal is not in database")
            shoppingList = []
            for string in list:
                if string != "" and string != None and string not in shoppingList:
                    shoppingList.append(string)
            return shoppingList
        raise Exception("Error bad type or meal is not in database")

class Recipe:

    def recipeByMealName(self, meal):
        r = requests.get(f"http://www.themealdb.com/api/json/v1/1/search.php?s={meal}")
        if type(meal) is str and r.json()["meals"] != None:
            return r.json()["meals"][0]["strInstructions"]
        else:
            raise Exception("Error bad type or meal is not in database")

    def recipeWithSmallestNumberOfIngredientsStartingWithLetter(self, letter):
        meals = []
        number = [30]
        r = requests.get(f"https://www.themealdb.com/api/json/v1/1/search.php?f={letter}")
        if type(letter) is str and letter.lower() in "abcdefghijklmnopqrstuwxyz":
            if r.json()["meals"] == None:
                return ""
            for meal in r.json()["meals"]:
                list = []
                for i in range(1, 21):
                    list.append(meal["strIngredient" + str(i)])
                ingList = []
                for string in list:
                    if string != "" and string != None:
                        ingList.append(string)
                if len(ingList) <= number[-1]:
                    meals.append((meal["strMeal"], meal["strInstructions"]))
                    number.append(len(ingList))
            return meals
        else:
            raise Exception("Error bad type or not letter")

print(Recipe().recipeWithSmallestNumberOfIngredientsStartingWithLetter('s'))