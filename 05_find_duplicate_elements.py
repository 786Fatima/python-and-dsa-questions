# Find duplicate elements in a list

def find_duplicates(input_list=[]):
    seen = set()
    duplicates = set()
    for item in input_list:
        if item in seen:
            duplicates.add(item)
        else:
            seen.add(item)
    return list(duplicates)

# Example
if __name__ == "__main__":
    ipt_list = input("Enter a list of elements separated by spaces: ").split()
    dup_elements = find_duplicates(ipt_list)
    print("Duplicate Elements:", dup_elements)