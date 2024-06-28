
def read_file(file_path):
    """
    Зчитує файл, який містить цілі числа, розділені пробілами, і повертає список цих чисел.
    
    Аргументи:
        file_path (str): Шлях до файлу, який потрібно зчитати.
        
    Повертає:
        List[int]: Список цілих чисел, зчитаних з файлу.
    """
    with open(file_path, 'r') as file:
        numbers = list(map(int, file.read().split()))
    return numbers


def find_max(numbers: list[int]) -> int:
    """
    Знаходить і повертає максимальне число зі списку цілих чисел.
    
    Аргументи:
        numbers (list[int]): Список цілих чисел.
        
    Повертає:
        int: Максимальне число зі списку.
    """
    return max(numbers)


def find_min(numbers: list[int]) -> int:
    """
    Знаходить і повертає мінімальне число зі списку цілих чисел.
    
    Аргументи:
        numbers (list[int]): Список цілих чисел.
        
    Повертає:
        int: Мінімальне число зі списку.
    """
    return min(numbers)


def average_value(numbers: list[int]) -> float|int:
    """
    Обчислює і повертає середнє значення списку цілих чисел.
    
    Аргументи:
        numbers (list[int]): Список цілих чисел.
        
    Повертає:
        float | int: Середнє значення списку. Якщо список порожній, повертає 0.
    """
    total = 0
    count = 0
    for number in numbers:
        total += number
        count += 1

    if count == 0:
        return 0  
    
    return total / count


def middle_value(numbers: list[int]) -> float:
    """
    Обчислює і повертає середнє значення списку цілих чисел.

    Аргументи:
        numbers (list[int]): Список цілих чисел.

    Повертає:
        float | int: Середнє значення списку. Якщо список порожній, повертає 0.
    """
    n = len(numbers)
    if n == 0:
        return None
    
    if n % 2 == 1:
        middle_number = n // 2
        return numbers[middle_number]
    
    else:
        middle_number = n // 2 - 1
        second_middle_number = n // 2
        return (numbers[middle_number] + numbers[second_middle_number]) /2
    

def longest_arr(numbers: list[int]) -> list[int]:
    """
    Знаходить і повертає найдовшу підпослідовність зростаючих чисел у списку цілих чисел.

    Аргументи:
        numbers (list[int]): Список цілих чисел.

    Повертає:
        list[int]: Найдовша підпослідовність зростаючих чисел зі списку. Якщо список порожній, повертає порожній список.
    """
    if not numbers:
        return []

    max_length = 1
    current_length = 1
    max_start_index = 0
    current_start_index = 0

    for i in range(1, len(numbers)):
        if numbers[i] > numbers[i - 1]:
            current_length += 1
        else:
            if current_length > max_length:
                max_length = current_length
                max_start_index = current_start_index
            current_length = 1
            current_start_index = i

    if current_length > max_length:
        max_length = current_length
        max_start_index = current_start_index

    return numbers[max_start_index:max_start_index + max_length]



def longest_lower_arr(numbers: list[int]) -> list[int]:
    """
    Знаходить і повертає найдовшу підпослідовність спадних чисел у списку цілих чисел.

    Аргументи:
        numbers (list[int]): Список цілих чисел.

    Повертає:
        list[int]: Найдовша підпослідовність спадних чисел зі списку. Якщо список порожній, повертає порожній список.
    """
    if not numbers:
        return []

    max_length = 1
    current_length = 1
    max_start_index = 0
    current_start_index = 0

    for i in range(1, len(numbers)):
        if numbers[i] < numbers[i - 1]:
            current_length += 1
        else:
            if current_length > max_length:
                max_length = current_length
                max_start_index = current_start_index
            current_length = 1
            current_start_index = i

    if current_length > max_length:
        max_length = current_length
        max_start_index = current_start_index

    return numbers[max_start_index:max_start_index + max_length]

