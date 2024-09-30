# Swap two numbers without using a third variable
def swap_without_third_variable(a, b):
    """
    Swaps two numbers without using a third variable.
    
    Parameters:
    a (int): The first number.
    b (int): The second number.
    
    Returns:
    tuple: Swapped values of a and b.
    
    Example:
    a = 5, b = 10
    After swap: a = 10, b = 5
    """
    print("\nSwapping without third variable:")
    a = a + b  # Sum of a and b
    b = a - b  # Now b becomes the original a
    a = a - b  # Now a becomes the original b
    return a, b

# Swap two numbers using a third variable
def swap_with_third_variable(a, b):
    """
    Swaps two numbers using a third variable.
    
    Parameters:
    a (int): The first number.
    b (int): The second number.
    
    Returns:
    tuple: Swapped values of a and b.
    
    Example:
    a = 10, b = 5
    After swap: a = 5, b = 10
    """
    print("\nSwapping with third variable:")
    c = a  # Assign value of a to c (third variable)
    a = b  # Assign value of b to a
    b = c  # Assign value of c (which holds original a) to b
    return a, b

def main():
    # Input from the user
    a = int(input("Enter the first number: "))
    b = int(input("Enter the second number: "))

    # Swap without third variable
    a, b = swap_without_third_variable(a, b)
    print(f"First number after swap: {a}")
    print(f"Second number after swap: {b}")

    # Swap again using third variable
    a, b = swap_with_third_variable(a, b)
    print(f"First number after swap (with third variable): {a}")
    print(f"Second number after swap (with third variable): {b}")
    
    # Incrementing the third variable (used earlier as c)
    c = a  # Reusing variable 'a' as c (or assigning c again)
    c += 1  # Incrementing c by 1
    print(f"Value of c (incremented third variable): {c}")

# Run the main function
if __name__ == "__main__":
    main()
