phonebook_dict = {
  'Alice': '703-493-1834',
  'Bob': '857-384-1234',
  'Elizabeth': '484-584-2923'
}
print("Elizabeth's phone number ")
print(phonebook_dict["Elizabeth"])
phonebook_dict['Kareem'] = '938-489-1234'
phonebook_dict.pop('Alice', None)
phonebook_dict['Bob'] = '968-345-2345'
print("Final Product: ")
print(phonebook_dict)


