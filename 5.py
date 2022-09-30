# Напишите программу, которая принимает на вход координаты двух точек
# и находит расстояние между ними в 2D пространстве.

# Пример:

#  A (3,6); B (2,1) -> 5,09
#  A (7,-5); B (1,-1) -> 7,21

print('Введите координаты точки А.')
Xa = int(input('x: '))
Ya = int(input('y: '))

print('Введите координаты точки B.')
Xb = int(input('x: '))
Yb = int(input('y: '))

from math import sqrt
AB = sqrt((Xb - Xa) ** 2 + (Yb - Ya) ** 2)

print(f'Расстояние между точками равно {round(AB, 2)}')
