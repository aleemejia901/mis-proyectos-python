nombre = input("¿Cómo te llamas? ")
edad = int(input("¿Cuántos años tienes? "))

print("Hola", nombre + "!")

if edad >= 18:
    print("Ya puedes estudiar Ingeniería de Software")
elif edad >= 14:
    años = 18 - edad
    print("Te faltan", años, "años, aprovecha para practicar Python")
else:
    print("Eres muy joven, tienes todo el tiempo del mundo")
