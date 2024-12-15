def get_input_array(name):
    while True:
        user_input = input(f"Введите элементы массива {name} через пробел: ")
        try:
            # Преобразуем ввод в список целых чисел
            array = list(map(int, user_input.split()))
            return array
        except ValueError:
            print("Ошибка: Пожалуйста, введите только целые числа.")

def find_unique_in_A(A, B):
    # Находим элементы, которые есть в A только в одном экземпляре
    unique_in_A = [x for x in A if A.count(x) == 1]
    
    # Находим повторяющиеся элементы в B
    duplicates_in_B = set(x for x in B if B.count(x) > 1)

    # Находим пересечение уникальных элементов из A и повторяющихся из B
    result = list(duplicates_in_B.intersection(unique_in_A))
    return result

def find_elements_only_in_A_or_B(A, B):
    # Находим элементы, которые есть только в A или только в B
    set_A = set(A)
    set_B = set(B)
    
    # Элементы, которые есть только в A или только в B
    unique_elements = (set_A - set_B).union(set_B - set_A)
    return list(unique_elements)

def find_repeated_in_B(A, B):
    # Находим элементы из A, которые повторяются в B
    repeated_in_B = [x for x in set(A) if B.count(x) > 1]
    return repeated_in_B

def main():
    while True:
        print("\nМеню:")
        print("1. Ввести массив A")
        print("2. Ввести массив B")
        print("3. Найти повторяющиеся элементы в B, которые есть в A только в одном экземпляре")
        print("4. Найти элементы, которые есть только в A или только в B")
        print("5. Найти элементы массива A, повторяющиеся в массиве B несколько раз")
        print("6. Выход")

        choice = input("Выберите действие (1-6): ")

        if choice == '1':
            A = get_input_array("A")
            print(f"Массив A: {A}")
        elif choice == '2':
            B = get_input_array("B")
            print(f"Массив B: {B}")
        elif choice == '3':
            try:
                result = find_unique_in_A(A, B)
                print(f"Повторяющиеся элементы в B, которые есть в A только в одном экземпляре: {result}")
            except NameError:
                print("Ошибка: Сначала введите массивы A и B.")
        elif choice == '4':
            try:
                result = find_elements_only_in_A_or_B(A, B)
                print(f"Элементы, которые есть только в A или только в B: {result}")
            except NameError:
                print("Ошибка: Сначала введите массивы A и B.")
        elif choice == '5':
            try:
                result = find_repeated_in_B(A, B)
                print(f"Элементы массива A, повторяющиеся в массиве B несколько раз: {result}")
            except NameError:
                print("Ошибка: Сначала введите массивы A и B.")
        elif choice == '6':
            print("Выход из программы.")
            break
        else:
            print("Ошибка: Пожалуйста, выберите корректный пункт меню.")

if __name__ == "__main__":
    main()