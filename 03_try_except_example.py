# try-except example
def divide_numbers(num1, num2):
    try:
        result = num1 / num2
    except ZeroDivisionError:
        return "Error: Cannot divide by zero."
    else:
        return f"The result is {result}"
    finally:
        print("Execution completed.")
        
# Example
if __name__ == "__main__":
    try:
        n1 = float(input("Enter the numerator: "))
        n2 = float(input("Enter the denominator: "))
        print(divide_numbers(n1, n2)) 
    except ValueError:
        print("Error: Invalid value provided.")