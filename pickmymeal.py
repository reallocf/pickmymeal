#!/usr/bin/env python
import requests
import json
import sys
from os import path
from Meal import Meal

validMealTags = set(["vegetarian",
                    "vegan",
                    "glutenFree",
                    "dairyFree",
                    "sustainable",
                    "lowFodmap",
                    "ketogenic",
                    "whole30"])

def main():
    mealCount, mealTags = parseArgs()
    validateInput(mealCount, mealTags)
    resp = makeApiRequest(mealCount, mealTags)
    if resp.status_code != requests.codes.ok:
        printResponseError(resp)
        sys.exit(0)
    meals = parseMeals(resp)
    for meal in meals:
        print(meal)

##
# Look for number and/or tags passed via args
# Exit if >2 args passed
#
def parseArgs():
    mealCountDefault = "0"
    mealTagsDefault = ""
    if len(sys.argv) > 3:
        print("Too many arguments passed.")
        sys.exit(0)
    if len(sys.argv) == 3:
        if sys.argv[1].isdigit():
            return sys.argv[1], sys.argv[2]
        else:
            return sys.argv[2], sys.argv[1]
    elif len(sys.argv) == 2:
        if sys.argv[1].isdigit():
            return sys.argv[1], mealTagsDefault
        else:
            return mealCountDefault, sys.argv[1]
    else:
        return mealCountDefault, mealTagsDefault

##
# Make sure mealCount and mealTags make sense
# mealCount is limited at 50
#
def validateInput(mealCount, mealTags):
    if int(mealCount) < 0 or int(mealCount) > 50:
        print("Meal Count too high.")
        exit(0)
    if mealTags:
        for tag in mealTags.split(','):
            if tag not in validMealTags:
                print("Invalid meal tag:", tag)
                exit(0)

##
# Hit Spoonacular API
# limitLicense=true to save $$
#
def makeApiRequest(mealCount, mealTags):
    headers = {'X-Mashape-Key': getApiKey(), 'Accept': 'application/json'}
    url = getUrl(mealCount, mealTags)
    return requests.get(url=url, headers=headers)

##
# Cache api key in '.key' file in local directory
#
def getApiKey():
    if path.exists('.key'):
        with open('.key', 'r') as f:
            return f.read()
    else:
        userInput = input("Api Key: ")
        with open('.key', 'w') as f:
            f.write(userInput)
        return userInput

def getUrl(mealCount, mealTags):
    url = 'https://spoonacular-recipe-food-nutrition-v1.p.mashape.com/recipes/random?limitLicense=true'
    if mealCount:
        url = url + f'&number={mealCount}'
    if mealTags:
        url = url + f'&tags={mealTags}'
    return url

##
# Parse json response into list of Meal classes
#
def parseMeals(resp):
    data = json.loads(resp.text)
    return [Meal(meal) for meal in data["recipes"]]

def printResponseError(resp):
    print("Improper request respone.")
    print("If cached key is bad/outdated, delete '.key' file.")
    print("Error Message:")
    print(resp.text)

    
if __name__ == '__main__':
    main()

