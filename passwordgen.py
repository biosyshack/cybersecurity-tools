import os, random

length = 12
chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()-'

print(''.join(random.choice(chars) for i in range(length)))
