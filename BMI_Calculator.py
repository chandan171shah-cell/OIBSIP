# user input
try:
    weight = float(input("Enter your weight in kilograms (kg): "))
    height = float(input("Enter your height in meters (m): "))

    # Basic input validation
    if weight <= 0 or height <= 0:
        print("Error: Weight and height must be positive numbers.")
    else:
        # Calculate BMI
        BMI = weight / (height ** 2)

        # Classify BMI category
        if BMI < 18.5:
            category = "Underweight"
            advice = "You should include more nutritious food in your diet."
        elif 18.5 <= BMI < 24.9:
            category = "Normal weight"
            advice = "Great! Maintain your healthy lifestyle."
        elif 25 <= BMI < 29.9:
            category = "Overweight"
            advice = "Try to include regular exercise and control your diet."
        else:
            category = "Obese"
            advice = "Consult a doctor and improve diet and exercise habits."

        # Display result
        print("\n======= BMI Report =======")
        print(f"Weight: {weight} kg")
        print(f"Height: {height} m")
        print(f"Your BMI is: {BMI:.2f}")
        print(f"Category: {category}")
        print(f"Health Tip: {advice}")
        print("==========================")

except ValueError:
    print("Invalid input! Please enter numeric values only.")