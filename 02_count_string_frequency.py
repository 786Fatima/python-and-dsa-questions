# Count frequency of characters in a string

def count_string_frequency(s):
    freq_count = {}
    for char in s:
        if char in freq_count:
            freq_count[char] += 1
        else:
            freq_count[char] = 1
    return freq_count

# Example
if __name__ == "__main__":  
    ipt_str = input("Enter a string to count character's frequency: ")
    freq = count_string_frequency(ipt_str)
    print("Character Frequency:", freq)