import random
usuarios=[]

for _ in range(10):
    nombre=random.choice(['Juan','Andrea','Sara','Jorge'])
    contrasena=random.choice(['admin123','arboles000'])
    edad=random.randint(18,62)
    usuario=[nombre, contrasena, edad]
    usuarios.append(usuario)

print(usuarios)