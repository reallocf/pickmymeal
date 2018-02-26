##
# Wraps returned spoonacular JSON object for easier usability
#
class Meal():

    def __init__(self, mealResp):
        self.name = mealResp["title"]
        self.dishTypes = self.parseList(mealResp["dishTypes"])
        self.cuisines = self.parseList(mealResp["cuisines"])
        self.occasions = self.parseList(mealResp["occasions"])
        self.winePairings = self.parseList(mealResp["winePairing"]["pairedWines"]) if mealResp["winePairing"] else "None listed"
        self.likeCount = mealResp["aggregateLikes"]
        self.time = mealResp.get("readyInMinutes", 0) + mealResp.get("preparationMinutes", 0) + mealResp.get("cookingMinutes", 0)
        self.cost = int(round(mealResp.get("pricePerServing", 0))) / 100.0
        self.servingSize = mealResp["servings"]
        self.veryPopular = mealResp["veryPopular"]
        self.veryHealthy = mealResp["veryHealthy"]
        self.dairyFree = mealResp["dairyFree"] # My gf is lactose intolerant
        self.sourceUrl = mealResp["sourceUrl"]
        self.spoonacularUrl = mealResp["spoonacularSourceUrl"]

    def parseList(self, inputList):
        return ", ".join(inputList) if inputList else "None listed"

    def __str__(self):
        ret = f""" ----------------------------------------------------------------------------------------------------------------------------
|                     name:  {self.name}
|               dish types:  {self.dishTypes}
|                 cuisines:  {self.cuisines}
|                occasions:  {self.occasions}
|             wine pairing:  {self.winePairings}
|          number of likes:  {self.likeCount}
|       total time to make:  {self.time} minutes
| approx. cost per serving:  ${self.cost}
|             serving size:  {self.servingSize}
|             very popular:  {self.veryPopular}
|             very healthy:  {self.veryHealthy}
|               dairy free:  {self.dairyFree}
|               source url:  {self.sourceUrl}
|          spoonacular url:  {self.spoonacularUrl}"""
        return ret
