import random
import string
l=int(input("Length:"))
ch=string.ascii_letters + string.digits+string.punctuation
b=''.join(random.choice(ch) for _ in range(l))
print(b)