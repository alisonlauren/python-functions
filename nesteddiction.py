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
print("  1. Ramit's email address:  ")
print(ramit['email'])
print("  2. First of Ramit's interests:  ")
print(ramit['interests'][0])
print("  3. Jasmine's email address:  ")
print(ramit['friends'][0]['email'])
print("  4. Second of Jan's interests:           ")
print(ramit['friends'][1]['interests'][1])
