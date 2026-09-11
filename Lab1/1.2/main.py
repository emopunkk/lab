from module1 import calculate_expression
from module2 import calculate_sum_and_product
def main():
    while True:
        print("\n")
        print("1 Обчислити вираз: y = log10(x) + e^x")
        print("2 Сума парних і добуток непарних (0-20)")
        print("0 Вихід з програми")
        print("="*40)
        choice = input("Оберіть дію (0, 1 або 2): ")
        if choice == '1':
            while True:
                try:
                    x = float(input("\nВведіть значення x (x > 0): "))
                    if x <= 0:
                        print("Помилка: x має бути строго більшим за 0")
                    else:
                        y = calculate_expression(x)
                        print(f"Результат обчислення: y = {y:.4f}")
                        break
                except ValueError:
                    print("Помилка: Введіть коректне число!")
                    
        elif choice == '2':
            print("\nОбчислення для діапазону від 0 до 20...")
            sum_even, prod_odd = calculate_sum_and_product()
            print(f"Сума усіх парних чисел: {sum_even}")
            print(f"Добуток усіх непарних чисел: {prod_odd}")
            
        elif choice == '0':
            print("\nЗавершення роботи програми...")
            break
            
        else:
            print("\nНекоректний вибір, будь ласка, введіть 0, 1 або 2.")

#точка входу в програму
if __name__ == "__main__":
    main()
    
    # Затримка закриття консолі
    input("\nНатисніть Enter, щоб закрити вікно...")