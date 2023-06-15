import random
import string
len=8
a='abcdefghijklmnopqrstuvwxyzQWERTYUIOPLKJHGFDSAZXCVBNM123456789+-*//][}{)*(&^%$#@!]'

password = random.sample(a, len-4)

password.append(random.choice(string.ascii_lowercase))
password.append(random.choice(string.ascii_uppercase))
password.append(random.choice(string.digits))
password.append(random.choice(string.punctuation))
random.shuffle(password)

print(''.join(password))