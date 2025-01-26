class Calculator:
    # Class attribute
    calculation_type = "Arithmetic Operations"

    # Static method that performs addition
    @staticmethod
    def add(a, b):
        return a + b

    # Class method that performs multiplication and references the class attribute
    @classmethod
    def multiply(cls, a, b):
        print(f"Calculation type: {cls.calculation_type}")
        return a * b
