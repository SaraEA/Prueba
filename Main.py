import random
print("Hola mundo")


password = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"

length = int(input("Escribe la longitud de tu contraseña:"))

passwordsave = ""

for i in range(length):
    passwordsave += random.choice(password)

print(passwordsave)

