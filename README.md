# pickmymeal
Leverage spoonacular API to pick a random meal to cook

Expects: `python3` and `requests` library

First you'll have to sign up & get an API key here:

https://market.mashape.com/spoonacular/recipe-food-nutrition

Then you can use like this:

`./pickmymeal.py # outputs 1 random recipe`

or

`./pickmymeal.py 10 # outputs 10 random recipes`

or even

`./pickmymeal.py 5 vegetarian,dessert # outputs 5 vegetarian desserts`

Note that API key will be cached in local dir in this file:

.key

All tags available*:

vegetarian
vegan
glutenFree
dairyFree
sustainable
lowFodmap
ketogenic
whole30

* I think - maybe I missed some or new ones were added :)