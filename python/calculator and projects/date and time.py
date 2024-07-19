from datetime import datetime

def calculate_age(birth_year, birth_month):
    current_year = datetime.now().year
    current_month = datetime.now().month

    age = current_year - birth_year

    if current_month < birth_month:
        age -= 1

    return age

def main():
    try:
        birth_year = int(input("Enter your birth year: "))
        birth_month = int(input("Enter your birth month (1-12): "))

        if birth_month < 1 or birth_month > 12:
            print("Invalid birth month. Please enter a number between 1 and 12.")
            return

        age = calculate_age(birth_year, birth_month)
        print(f"You are {age} years old.")

    except ValueError:
        print("Invalid input. Please enter valid numbers.")

if __name__ == "__main__":
    main()
