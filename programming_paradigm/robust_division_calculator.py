def safe_divide(numerator, denominator):

    try:
        numerator = float(numerator)
        denominator = float(denominator)

        result = numerator / denominator
        return f"The result of the division is {result:.2f}"

    except ZeroDivisionError:
        return "Error: Cannot divide by zero."
    except ValueError:
        return "Error: Please enter numeric values only."
