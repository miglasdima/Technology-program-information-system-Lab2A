print("11111111111111111111111111\n")
print("Перша константа", False)
print("Друга константа",  NotImplemented)
print("Третя константа", None)
print("\n22222222222222222222222222\n")
print(abs(-12.5), f"є рівним {abs(12.5)}")
print("bin (3)=", bin(3))
print("hex(255)=", hex(255))
print("\n33333333333333333333333333\n")
print("Розгалуження")
A = True
print("Значить А=True" if A else "Значить А=False")
print("Цикл")
for i in range(10):
    print(i)
print("\n4444444444444444444444444\n")
A = 0
try:
    print("Наприклад", 10/A, "?")
except Exception as e:
    print(e)
finally:
    print("Результат")
print("\n6666666666666666666666666\n")
this_is_lambda = lambda first, last: f'Цей код написав: {first} {last}'
print("Це просто функція:", this_is_lambda)
print("Це її виклик:", this_is_lambda('Мигляс', 'Дмитро'))