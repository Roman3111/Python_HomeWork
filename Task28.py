# Задача 28: Напишите рекурсивную функцию sum(a, b), возвращающую сумму двух целых неотрицательных чисел.
# Из всех арифметических операций допускаются только +1 и -1. Также нельзя использовать циклы.
# Пример:

# 2 2
#     4

def sum(A, B):
 if (B==0):
  return A
 else:
  return sum(A+1,B-1)

a = int(input("Введите A-> "))
print()
b = int(input("Введите B-> "))
print()
if (a>=b):
 print (sum(a,b))
else:
    print(sum(b,a))

# def sum(a, b):
#     if b == 0:
#         return a
#     else:
#         return sum(a ^ b, (a & b) << 1)    