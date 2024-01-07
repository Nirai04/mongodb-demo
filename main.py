import json
import pymongo

file1 = open("recipe.json","r")
file2 = open("restaurant.json","r")

recipe_str=file1.read()
restaurant_str=file2.read()

recipe=json.loads(recipe_str)
reataurant=json.loads(restaurant_str)

#print(recipe[0]["Name"])         
#print(recipe[1]["Name"])  
for i in range(len(recipe)):
    for col in recipe[i]:
        print(recipe[i][col],end = " ")
    print()

