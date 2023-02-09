# 1) print out the value for the key 'history' using the dictionary below


sampleDict = { 
   "class":{ #class has one key, student
      "student":{ #class dictionary has 1 key, student
         "name":"Mike", #student has 2 keys, name and marks
         "marks":{ #marks has 2 keys, physicas and history
            "physics":70,
            "history":80
         }
      }
   }
}

#initial: 
#print(sampleDict['class']['student']['marks']['history'])

#class answer
score = sampleDict['class']['student']['marks']['history']
print(score)

# 2) Add 2 inches to the son's height. #add means dont hardcode

dict={"son's name": "Lucas", "son's eyes": "green", "son's height": 32, "son's weight": 25}

#class answer
dict["son's height"] += 2
print(dict)

# 3) Given a Python dictionary, Change Brad’s salary to 8500

sampleDict = {
     'emp1': {'name': 'Jhon', 'salary': 7500},
     'emp2': {'name': 'Emma', 'salary': 8000},
     'emp3': {'name': 'Brad', 'salary': 6500}
}

#initial:
#for key,value in sampleDict.items():
   #sampleDict['emp3']['salary'] = '8500'
   #print(sampleDict)
   #break

#class answer:
sampleDict['emp3']['salary'] = 8500 #this is hard coding, don't do unless in situations like this
print(sampleDict)
   
# 4 )Given the dictionary below, add a new key - 'work' with the values shown below:
#       "work": ["Apology", "Phaedo", "Republic", "Symposium"]
dict={"name": "Plato", "country": "Ancient Greece", "born": -427, "teacher": "Socrates", "student": "Aristotle"}

dict['work'] = ["Apology", "Phaedo", "Republic", "Symposium"] #make sure to put the brackets[] b/c on directions there is [] so means it's a list
print(dict)

