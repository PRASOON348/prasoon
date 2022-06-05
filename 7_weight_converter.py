weight = int(input("enter your weight:"))
convert = input("l(pounds) or k(kilos):")
if convert == "l":
    weight = weight*0.45
    print(f"you are {weight} kilos")
else:
    weight = weight/0.45
    print(f"you are {weight} pounds")