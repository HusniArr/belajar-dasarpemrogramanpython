profile = {
    "id" : 2,
    "name" : "mario",
    "hobbies" : ("playing with luigi", "saving the mushroom kingdom"),
    "is_female" : False,
    "affliations": [
        {
            "name": "luigi",
            "affliation": "brother"
        },
        {
            "name": "mushroom kingdom",
            "affliation" : "protector"
        }
    ]
}

print("name:", profile["name"])
print("hobbies:", profile["hobbies"])
print("affliations")

for item in profile["affliations"]:
    print(" -> %s (%s)" % (item["name"], item["affliation"]))