import random
import string

def password_generator(length: int = 10):
    characters =  string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for i in range(length))
    return password
print('Your new password is: ' + password_generator())