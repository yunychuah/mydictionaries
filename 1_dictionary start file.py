import random

#this dictionary has 3 elements,
#keys are names of individuals and values are their corresponding phone numbers

phonebook = {} #creates an empty dictionary, creates teh object phonebook but there are noe elements in it 
phonebook = {'Chris':'555−1111',
             'Katie':'555−2222',
             'Joanne':'555−3333'}



print()
print('*****  start section 1 - print dictionary ********')
print()

mydictionary = dict(m=8, n=9) #key is n, value is 9
print(mydictionary)


print(len(phonebook)) #prints out the number of objects in your dictionary,prints out 3
print(type(phonebook)) #allows you to know what type of variable you are working with


print()
print('*****  end section 1 ********')
print()


print()
print('*****  start section 2 - search dictionary ********')
print()


#phone = (phonebook['Chris']) #give them the key, "chris" and then it will return the value in the dictionary
#saved the phone number into a variable "phone"

name = 'Chris' #python is cases sensitive so won't work if you do chris

if name in phonebook:
    print(phonebook[name])
else:
    print(f"{name} is not in the phonebook")


print()
print('*****  end section 2 ********')
print()





print()
print('*****  start section 3 - edit/append dictionary ********')
print()

print (phonebook)

phonebook['Chris'] = '555-0123' #chris already has a number so it just updated it
phonebook['Joe'] = "555-4444" #joe is not in there so it was APPENDED

print(phonebook)


print()
print('*****  end section 3 ********')
print()



print()
print('*****  start section 4 - delete/remove from dictionary ********')
print()

print(phonebook)

del phonebook['Chris']

print(phonebook)



print()
print('*****  end section 4 ********')
print()






print()
print('*****  start section 5 - iterate through keys, values, items ********')
print()

for key in phonebook: #key is the iterator, can be k or i or whatever you want
    print(f"the key is {key} and the value is {phonebook[key]}") #calls a dictionary and gives it a key

for value in phonebook.values(): #iterates thorugh/cycles through all values in dictionary
    print(value) #prints out all the values, aka the phone numbers

for key,value in phonebook.items(): 
    print(f"the key is {key} and the value is {value}")

for ph_tuple in phonebook.items():#if you don't split it like the above where you split it into key and value
    print(ph_tuple)#produces a tuple, which means immutable(aka you can't alter it)
 #so diff btwn line 103 and 106 is that 103 splits up the key and value so you can manipulate it 
 #but 106 does not split it up and it produces a tuple so you cannot manipulate 

print()
print('*****  end section 5 ********')
print()



print()
print('*****  start section 6 - using get and clear ********')
print()
#get functions says go look for 'Chris' in the phonebook dictionary
#if there is not match then print out 999
#so if you change 'Chris' to 'chris' you will get 999 and not the phone number
phone = phonebook.get('Chris','999')
print(phone)

#clear will clear out all elements in the dictionary but will not delete the dictionary
#so it produces {} b/c empty dictionary
#keep in mind it DOES NOT delete the dictionary itself
phonebook.clear() 
print(phonebook) #will produce and empty dictionary


print()
print('*****  end section 6 ********')
print()


print()
print('*****  start section 7 - using pop method ********')
print()

#pop removes key value pair out of dictionary and allow you to get the value and save it into a variable
remove = phonebook.pop('Chris','not found') #like the get medhod you can have a default value if not found, in this case 'not found'
print(remove) #will print out 555-1111 which is the value of chris which was removed
print(phonebook)




print()
print('*****  end section 7 ********')
print()



print()
print('*****  start section 8 - using popitem ********')
print()

#pick a random key value pair amd pop it out of the dictionary for you
a = phonebook.popitem(0)

print(a)
print(phonebook)

#but this isnt random b/c it will keep removing the last key value pair
#so to fix this look in section 9, use lists

print()
print('*****  end section 8 ********')
print()



print()
print('*****  start section 9 - using random and converting to list ********')
print()

phonebook_list = list(phonebook) #creates a list of the keys from the phonebook dictionary
print(phonebook_list) #gives a list of the keys chris katie joanne
random_key = random.choice(phonebook_list)
print(random_key) #will print out a random key from phonebook
print(phonebook[random_key]) #prints out the value of the key that was chosen by random_key, so for chris it will pring out 555-1111


print(phonebook[random.choice(list(phonebook_list))])
#will print: Chris
#            555-1111 
print()
print('*****  end section 9 ********')
print()








