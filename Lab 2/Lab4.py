# LAB 4 (HASAAN AHMAD SP22-BSE-017 )
birthday_dict = {
  
    "Hasaan Ahmad": "03/14/2002",
    "Mohammad": "01/17/2010",
    "Ali": "12/10/2003"
}

print("Welcome to the birthday dictionary. We know the birthdays of:")
for name in birthday_dict:
    print(name)

name = input("Who's birthday do you want to look up?\n")

if name in birthday_dict:
    birthday = birthday_dict[name]
    print(f"{name}'s birthday is {birthday}.")
else:
    print("Sorry, we don't have birthday information for that person.")
