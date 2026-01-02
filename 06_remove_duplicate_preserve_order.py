# Remove duplicates while preserving order

def remove_duplicates_preserve_order(input_list=[]):
    seen = set()
    result = []
    for item in input_list:
        if item not in seen:
            seen.add(item)
            result.append(item)
    return result

# Example
if __name__ == "__main__":  
    ipt_list = input("Enter a list of elements separated by spaces: ").split()
    unique_list = remove_duplicates_preserve_order(ipt_list)
    print("List after removing duplicates while preserving order:", unique_list)