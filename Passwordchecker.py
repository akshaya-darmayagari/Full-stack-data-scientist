a = input("Enter your password: ")
if (len(a) >= 8   and any(ch.isdigit() for ch in a) and any(ch.isupper() for ch in a) and any(ch.islower() for ch in a)  and any(ch in "@#$" for ch in a)):
    print("Strong password")
else:
    print("Weak password")
