def count_lines_in_text_file(filename):
    with open(filename, 'r') as file:
        line_count = sum(1 for line in file)
    return line_count

# Example usage
text_filename = 'hasini.txt'  # Replace with your text file name
print("Number of lines in text file:", count_lines_in_text_file(text_filename))