## Small Exercise One
phonebook_dict = {
  'Alice': '703-493-1834',
  'Bob': '857-384-1234',
  'Elizabeth': '484-584-2923'
}

print(" ")
print("======Small Exercise One=========")
print("Elizabeth's phone number ")
print(phonebook_dict["Elizabeth"])
phonebook_dict['Kareem'] = '938-489-1234'
phonebook_dict.pop('Alice')
phonebook_dict['Bob'] = '968-345-2345'
print("Final Product: ")
print(phonebook_dict)
print("==================================")
print(" ")

##Small Exercise Two

ramit = {
  'name': 'Ramit',
  'email': 'ramit@gmail.com',
  'interests': ['movies', 'tennis'],
  'friends': [
    {
      'name': 'Jasmine',
      'email': 'jasmine@yahoo.com',
      'interests': ['photography', 'tennis']
    },
    {
      'name': 'Jan',
      'email': 'jan@hotmail.com',
      'interests': ['movies', 'tv']
    }
  ]
}
print(" ")
print("======Small Exercise Two=========")
print("  1. Ramit's email address:  ")
print(ramit['email'])
print("  2. First of Ramit's interests:  ")
print(ramit['interests'][0])
print("  3. Jasmine's email address:  ")
print(ramit['friends'][0]['email'])
print("  4. Second of Jan's interests:           ")
print(ramit['friends'][1]['interests'][1])
print("==================================")
print(" ")

## Small Exercise Three
ramit = {
  'name': 'Ramit',
  'email': 'ramit@gmail.com',
  'interests': ['movies', 'tennis'],
  'friends': [
    {
      'name': 'Jasmine',
      'email': 'jasmine@yahoo.com',
      'interests': ['photography', 'tennis']
    },
    {
      'name': 'Jan',
      'email': 'jan@hotmail.com',
      'interests': ['movies', 'tv']
    }
  ],
  
}
#defining function "countFriends", putting in friend_dictionary as the parameter
def countFriends(friend_dictionary):
    #friend count = length of the dictionary within the key of friends
    friend_count = len(friend_dictionary["friends"])
    #return friend count, which essentially is just calling the function i created
    return friend_count
#print using my function with the dictionary listed before, ramit
print(" ")
print("------Count Friends Function-----")
print(countFriends(ramit))
print(" ")


