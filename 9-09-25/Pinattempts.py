def validate():
    a="1234"
    for i in range(1,4):
        print("Enter your pin for",i,"time")
        b=input()
        if a==b:
            return "Login successful"
    return "Invalid Pin"
print(validate())