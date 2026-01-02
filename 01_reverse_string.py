# Reverse a string without using slicing

def reverse_string(s):
    rev_str = ''
    for char in s:
        rev_str = char + rev_str
    return rev_str

# Example
if __name__ == "__main__":
    ipt_str = input("Enter a string to reverse: ")
    print("Original String:", ipt_str)
    print("Reversed String:", reverse_string(ipt_str))