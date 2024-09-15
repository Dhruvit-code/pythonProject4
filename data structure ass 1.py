def get_hemoglobin_status(gender, hemoglobin_value):
    if gender.lower() == 'female':
        if hemoglobin_value < 117:
            return 'low'
        elif 117 <= hemoglobin_value <= 155:
            return 'normal'
        else:
            return 'high'
    elif gender.lower() == 'male':
        if hemoglobin_value < 134:
            return 'low'
        elif 134 <= hemoglobin_value <= 167:
            return 'normal'
        else:
            return 'high'
    else:
        return 'Invalid gender'


def main():
    print("Welcome to the Hemoglobin Status Checker!")

    gender = input("Please enter your biological gender (female/male): ").strip()
    try:
        hemoglobin_value = float(input("Please enter your hemoglobin value (g/l): ").strip())
    except ValueError:
        print("Invalid input for hemoglobin value. Please enter a numeric value.")
        return

    status = get_hemoglobin_status(gender, hemoglobin_value)

    if status == 'Invalid gender':
        print("Error: The gender entered is not valid. Please enter 'female' or 'male'.")
    else:
        print(f"Your hemoglobin status is: {status}")


if __name__ == "__main__":
    main()







