#Вычисление площади и периметра прямоугольного треугольника
a = float(input("Введите катет 1: "))
b = float(input("Введите катет 2: "))
c = (a**2 + b**2)**0.5 #Вычисление гипотенузы #Вычисление гипотенузы
S=0.5 * a * b #Формула площади прямоугольного треугольника
P = a + b + c #Формула периметра треугольника
print("Площадь треугольника: ", S)
print("Периметр треугольника: ", P)

