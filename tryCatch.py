## getting square root with a try catch
# try:
#     user_input = int(input("Square Number?: "))
#     print(user_input**2)
# except (TypeError, ValueError) as e:
#     print("Please enter a number for this reason: ")
#     print(e)

## 

# while (True): 
#     try:
#         user_input = int(input("Square Number?: "))
#         print(user_input**2)
#         print("Thanks!")
#         break
#     except ValueError:
#         print("That didn't work. Give me a number please")
            


mylist = [5,6,7,8]
while (True):
    try:
        user_picks_number = int(input("Add number to my list: "))
        mylist.append(user_picks_number)
        print(mylist)
    except ValueError:
        print("Listen buddy, I asked for a number :")