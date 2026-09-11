def calculate_x(a, b):
    if a > b:
        return b * a + 1
    elif a == b:
        return -10
    else:
        return (a - 5) / b

def build_pyramid(n):
    lines = []
    
    # 1. Формуємо першу частину (зростання чисел до i)
    for i in range(1, n + 1):
        nums = list(range(1, i + 1))
        # використовуємо формат " {:2}" з пробілом перед для створення стовпців
        line_content = "".join(f" {x:2}" for x in nums).strip()
        lines.append(line_content)
        
    # 2. Формуємо другу частину (розширення зі спадними числами після N)
    for i in range(n - 1, 0, -1):
        nums = list(range(1, n + 1)) + list(range(n - 1, i - 1, -1))
        line_content = "".join(f" {x:2}" for x in nums).strip()
        lines.append(line_content)
        
    # 3. Формуємо центральний найширший рядок (з подвійним N, як на рисунку)
    nums_mid = list(range(1, n + 1)) + list(range(n, 0, -1))
    mid_line = "".join(f" {x:2}" for x in nums_mid).strip()
    
    # 4. Збираємо всю піраміду (верхня частина + центр + віддзеркалена верхня)
    all_lines_for_display = lines + [mid_line] + lines[::-1]
    
    # Знаходимо максимальну ширину для ідеального центрування
    max_width = max(len(line) for line in all_lines_for_display)
    
    print() 
    for line in all_lines_for_display:
        print(line.center(max_width))
    print()

# головний блок 
print("Завдання 1 функція 1 Обчислення X")
# перевірка для варіантів 1-10: числа a та b можуть бути лише додатними
while True:
    try:
        a = float(input("Введіть додатне число a: "))
        while a <= 0:
            print("Помилка, число 'a' має бути додатнім")
            a = float(input("Введіть додатне число a: "))
        break
    except ValueError:
        print("Помилка, введіть число")

while True:
    try:
        b = float(input("Введіть додатне число b: "))
        while b <= 0:
            print("Помилка, число 'b' має бути додатнім")
            b = float(input("Введіть додатне число b: "))
        break
    except ValueError:
        print("Помилка, введіть число")

# виклик першої функції
result_x = calculate_x(a, b)
print(f"Результат обчислення X: {result_x}")

print("\nЗавдання 1 функція 2 Побудова піраміди")
# перевірка аргументу N
while True:
    try:
        n = int(input("Введіть ціле число N (від 1 до 10): "))
        while n < 1 or n > 10:
            print("Помилка! Число N має бути в діапазоні від 1 до 10")
            n = int(input("Введіть ціле число N (від 1 до 10): "))
        break
    except ValueError:
        print("Помилка, введіть ціле число")

print("\nРезультат побудови піраміди:")
# виклик другої функції
build_pyramid(n)
input("\nНатисніть Enter, щоб закрити програму...")