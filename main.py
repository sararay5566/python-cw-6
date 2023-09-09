# write your code here
person = {
    "name": "sara",
    "age": 17,
    "hobbies" : ['karate' ,'cooking', 'reading' ],
}

print(person['name'])
print(person['age'])

person["country"] = "italy"
print(person)
print(len(person))

person["hobbies"] = "swimming"
def check_hobbies(person):
    if len(person["hobbies"]) >=3:
        print("wow you are amazing")



