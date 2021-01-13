## getting square root with a try catch
# try:
#     user_input = int(input("Square Number?: "))
#     print(user_input**2)
# except (TypeError, ValueError) as e:
#     print("Please enter a number for this reason: ")
#     print(e)

## 

while (True): 
    try:
        user_input = int(input("Square Number?: "))
        print(user_input**2)
        break
    except ValueError:
        print("That didn't work. Give me a number please")
            


