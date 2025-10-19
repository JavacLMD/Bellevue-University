
## Constants
COMPANY_NAME = "Investors R Us"

##Functions
def print_welcome():
    print(f"Welcome to {COMPANY_NAME}!")


## Using while loop to ensure valid float input before continuing
def get_float_input(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Invalid input. Please enter a numeric value.")

def get_int_input(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Invalid input. Please enter a whole number.")

## Function to calculate years to double investment
def calculate_years_til_doubled(initial, rate):
    rate_decimal = rate / 100
    rate_decimal += 1    

    doubled_investment = initial * 2
    principal = initial
    years = 0

    while (principal < doubled_investment):
        years += 1
        principal *= rate_decimal 
        print(f"Year Number {years}: Investment Amount: ${principal:,.2f}")

    print(f"\nIt will take {years} years to double your initial investment of ${initial:,.2f} at an annual interest rate of {rate}%.\n")
    
## Main Program Execution

def main():
    print_welcome();
    initial_investment = get_float_input("Enter initial investment amount (Type as whole number. EX: 1000 or 1000.50): ")
    annual_interest_rate = get_float_input("Enter annual interest rate (Type as whole number. EX: 5 for 5% or 5.5 for 5.5%): ")
    print(f"\nCalculating the number of years to double your investment of ${initial_investment:,.2f} at an annual interest rate of {annual_interest_rate}%...\n")
    calculate_years_til_doubled(initial_investment, annual_interest_rate)
    
if __name__ == "__main__":
    main()
