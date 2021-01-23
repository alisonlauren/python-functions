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
# . Ramit's email address:
print(ramit['email'])
# 2. First of Ramit's interests: 
print(ramit['interests'][0])
# Jasmine's email address: 
print(ramit['friends'][0]['email'])
# Second of Jan's interests:           ")
print(ramit['friends'][1]['interests'][1])
