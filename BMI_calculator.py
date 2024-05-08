def calculate_bmi(w, h):
    return w / (h ** 2)

def get_bmi_category(bmi):
    if bmi < 18.5:
        return "Underweight"
    elif bmi < 25:
        return "Normal weight"
    elif bmi < 30:
        return "Overweight"
    else:
        return "Obese"

def main():
    while True:
        try:
            w = float(input("Enter your weight in kilograms: "))
            h = float(input("Enter your height in meters: "))
            if w <= 0 or h <= 0:
                raise ValueError("Weight and height must be positive numbers.")
            bmi = calculate_bmi(w, h)
            print("Your BMI is: {:.2f}".format(bmi))
            print("BMI Category:", get_bmi_category(bmi))
        except ValueError as e:
            print("Invalid input:", e)
        except Exception as e:
            print("An error occurred:", e)
        finally:
            choice = input("Do you want to calculate another BMI? (yes/no): ")
            if choice.lower() != "yes":
                break

if __name__ == "__main__":
    main()
