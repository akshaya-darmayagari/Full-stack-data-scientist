import random
b={"Sunny":35,"Cloudy":23,"Rainy":12,"Windy":20}
c=random.choice(list(b))
print("Weather:",c,"Temp:",b[c])
