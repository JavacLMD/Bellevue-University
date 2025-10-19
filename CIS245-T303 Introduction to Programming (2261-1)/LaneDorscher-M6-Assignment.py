## Author: Lane Dorscher
## Date: 10/18/2025
## Assignment: M6: Assignment - Python List Program
## Prompt: Asks the user to enter a series of 20 numbers. Then, the program should store the numbers in a list and display the following data:
##  The lowest number in the list.
##  The highest number in the list.
##  The total of the numbers in the list.
##  The average of the numbers in the list.


WELCOME_MESSAGE = "Welcome to the Number solver"
NUMBERS_NEEDED = 20

def print_welcome():
    print(WELCOME_MESSAGE)


def get_number_input(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Invalid input. Please enter a integer (non-floating point) value.")

def evaluate_numbers_list(numbers):
    sorted_list = sorted(numbers)
    smallest_num = sorted_list[0]
    largest_num = sorted_list[-1]
    sum_total = sum(numbers)
    average_num = sum_total / len(sorted_list)

    return (smallest_num, largest_num, sum_total, average_num)

def print_results(results_tuple):
    print("\n--------------------------------------------------")
    print("Results of the entered numbers: ")
    print("--------------------------------------------------")
    print(f"Smallest number: {results_tuple[0]}")
    print(f"Largest number: {results_tuple[1]}")
    print(f"Sum Total: {results_tuple[2]}")
    print(f"Average number: {results_tuple[3]:.2f}")
    print() #
    

def get_numbers_list():

    numbers = []
    for index in range(NUMBERS_NEEDED):
        num = get_number_input(f"Enter a number ({index+1}/{NUMBERS_NEEDED}): ")
        numbers.append(num)
    
    return numbers

def main():
    print_welcome()
    numbers = get_numbers_list()
    results = evaluate_numbers_list(numbers)
    print_results(results)

if (__name__ == "__main__"):
    main()