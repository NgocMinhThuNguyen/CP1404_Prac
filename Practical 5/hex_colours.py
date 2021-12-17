COLOR_CODES = {"Ash Grey": "#b2beb5", "Asparagus": "#87a96b", "Aureolin": "#fdee00", "Azure1": "#f0ffff",
                "Azure2": "#e0eeee", "Azure3": "#c1cdcd", "Azure4": "#838b8b", "Baby Blue": "#89cff0",
                "Baby Pink": "#f4c2c2", "Baker-Miller Pink": "#ff91af"}

color_name = input("Enter color name you want: ").capitalize()

while color_name !=" ":
    print(f"{color_name} has the code of {COLOR_CODES.get(color_name)}")
    color_name = input("Enter color name you want: ").capitalize()
print("Thank you!")