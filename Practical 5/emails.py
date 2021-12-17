name_from_email = {}
email = input("Email: ")

while email != "":
    fix_email = email.split('@')[0]
    parts = fix_email.split('.')
    name = " ".join(parts).title()

    checking = input(f"Is your name {name}? (Y/n) ").lower()
    if checking != "y" and checking != "":
        name = input("Name: ")
    name_from_email[email] = name
    email = input("Email: ")

for email, name in name_from_email.items():
    print(f"{name} ({email})")
