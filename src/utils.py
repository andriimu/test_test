
def read_file(file_path):
    """
    Reads a file that contains integers separated by spaces and returns a list of these numbers.
    
    Arguments:
        file_path (str): The path to the file to be read.
        
    Returns:
        List[int]: A list of integers read from the file.
    """
    with open(file_path, 'r') as file:
        numbers = list(map(int, file.read().split()))
    return numbers


def find_max(numbers: list[int]) -> int:
    """
    Finds and returns the maximum number from a list of integers.
    
    Arguments:
        numbers (list[int]): A list of integers.
        
    Returns:
        int: The maximum number from the list.
    """
    return max(numbers)


def find_min(numbers: list[int]) -> int:
    """
    Finds and returns the minimum number from a list of integers.
    
    Arguments:
        numbers (list[int]): A list of integers.
        
    Returns:
        int: The minimum number from the list.
    """
    return min(numbers)


def average_value(numbers: list[int]) -> float|int:
    """
    Calculates and returns the average value of a list of integers.
    
    Arguments:
        numbers (list[int]): A list of integers.
        
    Returns:
        float | int: The average value of the list. If the list is empty, returns 0.
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
    Calculates and returns the middle value of a list of integers.

    Arguments:
        numbers (list[int]): A list of integers.

    Returns:
        float | int: The middle value of the list. If the list is empty, returns 0.
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
    Finds and returns the longest subsequence of increasing numbers in a list of integers.

    Arguments:
        numbers (list[int]): A list of integers.

    Returns:
        list[int]: The longest subsequence of increasing numbers from the list. If the list is empty, returns an empty list.
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
    Finds and returns the longest subsequence of decreasing numbers in a list of integers.

    Arguments:
        numbers (list[int]): A list of integers.

    Returns:
        list[int]: The longest subsequence of decreasing numbers from the list. If the list is empty, returns an empty list.
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

