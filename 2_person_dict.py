person = {} #start off with empty dictionary called person
person["fname"] = "Joe"
person["lname"] = "Fonebone"
person["age"] = 51
person["spouse"] = "Edna"
person["children"] = ["Ralph", "Betty", "Joey"]
person["pets"] = {"dog": "Fido", "cat": "Sox"}

#print(person)#dictionary within a dictionary 

#print out the name of the second child
print(person['children'][1])

#print out the name of the cat
print(person['pets']['cat'])

#iterate thorugh all children and print out out each child
for value in person.values(): 
    print(person['children'])
    break

#print our the pets in this format:
#type of pet: dog name of pet:Fido
pet = person.get('pets')
for key,value in pet.items():
    print(f"type of pet:{key} name of pet:{value}")
