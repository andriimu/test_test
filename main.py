from utils import (
read_file,  
find_max, find_min, 
middle_value, 
average_value, 
longest_arr, 
longest_lower_arr
)




def main(file_path):
    numbers = read_file(file_path)
    max_number = find_max(numbers)
    min_number = find_min(numbers)
    median_number = middle_value(numbers)
    mean_number = average_value(numbers)
    longest_increas = longest_arr(numbers)
    longest_decreas = longest_lower_arr(numbers)

    print(f"Максимальне число: {max_number}")
    print(f"Мінімальне число: {min_number}")
    print(f"Медіана: {median_number}")
    print(f"Середнє арифметичне: {mean_number}")
    print(f"Послідовність, яка збільшується: {longest_increas}")
    print(f"Послідовність, яка зменшується: {longest_decreas}")


if __name__ == "__main__":
    file_path = "./data/10m.txt"  
    main(file_path)