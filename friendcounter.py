


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
print(countFriends(ramit))





    


