import os

def calculate_expected_offspring(counts):
    """
    Calculate the expected number of dominant phenotype offspring.

    Parameters:
    counts (list of int): A list of six integers representing the number of couples for each genotype pairing:
                          [AA-AA, AA-Aa, AA-aa, Aa-Aa, Aa-aa, aa-aa]

    Returns:
    float: The expected number of dominant phenotype offspring.
    """
    # Define the expected dominant offspring per couple for each genotype pairing
    expected_per_couple = [2, 2, 2, 1.5, 1, 0]

    # Calculate the total expected number of dominant offspring
    total_expected = sum(couple_count * expectation for couple_count, expectation in zip(counts, expected_per_couple))

    return total_expected

def prompt_file_path(prompt_message):
    """
    Prompt the user to enter a file path and validate its existence.

    Parameters:
    prompt_message (str): The message displayed to prompt the user.

    Returns:
    str: A valid file path entered by the user.
    """
    while True:
        file_path = input(prompt_message).strip('"').strip("'")  # Remove quotes if entered
        if os.path.isfile(file_path):
            return file_path
        else:
            print(f"Error: The file '{file_path}' does not exist. Please enter a valid file path.\n")

def prompt_output_choice():
    """
    Prompt the user to choose the output method.

    Returns:
    int: 0 for console output, 1 for file output.
    """
    while True:
        print("\nChoose the output method:")
        print("0 - Display results on the console")
        print("1 - Export results to a .txt file")
        choice = input("Enter 0 or 1: ").strip()
        if choice in ['0', '1']:
            return int(choice)
        else:
            print("Invalid input. Please enter 0 or 1.\n")

def prompt_output_file_path():
    """
    Prompt the user to enter an output file path.

    Returns:
    str: The output file path entered by the user.
    """
    while True:
        file_path = input("Enter the output file path (e.g., C:/Users/Blue/Desktop/output.txt): ").strip('"').strip("'")
        # Check if the directory exists
        directory = os.path.dirname(file_path)
        if directory == '':
            # Current directory is assumed
            return file_path
        elif os.path.isdir(directory):
            return file_path
        else:
            print(f"Error: The directory '{directory}' does not exist. Please enter a valid file path.\n")

def read_input_file(input_file_path):
    """
    Read and parse the input file.

    Parameters:
    input_file_path (str): Path to the input file.

    Returns:
    list of list of int: A list where each element is a list of six integers representing a test case.
    """
    test_cases = []
    try:
        with open(input_file_path, 'r') as file:
            lines = file.readlines()
            for line_num, line in enumerate(lines, start=1):
                line = line.strip()
                if not line:
                    continue  # Skip empty lines
                parts = line.split()
                if len(parts) != 6:
                    print(f"Warning: Line {line_num} does not contain exactly 6 integers. Skipping this line.")
                    continue
                try:
                    counts = list(map(int, parts))
                    if any(count < 0 or count > 20000 for count in counts):
                        print(f"Warning: Line {line_num} contains integers outside the range 0 to 20,000. Skipping this line.")
                        continue
                    test_cases.append(counts)
                except ValueError:
                    print(f"Warning: Line {line_num} contains non-integer values. Skipping this line.")
                    continue
    except Exception as e:
        print(f"An error occurred while reading the input file: {e}")
        return []
    return test_cases

def write_output_file(output_file_path, results):
    """
    Write the results to the specified output file.

    Parameters:
    output_file_path (str): Path to the output file.
    results (list of str): List of result strings to write.
    """
    try:
        with open(output_file_path, 'w') as file:
            for result in results:
                file.write(result + '\n')
        print(f"\nResults have been successfully written to '{output_file_path}'.")
    except Exception as e:
        print(f"An error occurred while writing to the output file: {e}")

def main():
    print("=== Expected Dominant Offspring Calculator ===\n")

    # Step 1: Prompt for input file path
    input_file_path = prompt_file_path("Enter the path to the input .txt file: ")

    # Step 2: Read and parse the input file
    test_cases = read_input_file(input_file_path)
    if not test_cases:
        print("No valid test cases found in the input file. Exiting the program.")
        return

    # Step 3: Calculate expected offspring for each test case
    results = []
    for counts in test_cases:
        expected = calculate_expected_offspring(counts)
        # Format the result to one decimal place
        results.append(f"{expected:.1f}")

    # Step 4: Prompt for output choice
    output_choice = prompt_output_choice()

    if output_choice == 0:
        # Display results on the console
        print("\n=== Expected Number of Dominant Phenotype Offspring ===")
        for result in results:
            print(result)
    else:
        # Prompt for output file path
        output_file_path = prompt_output_file_path()
        # Write results to the output file
        write_output_file(output_file_path, results)

    print("\nProgram completed successfully.")

if __name__ == "__main__":
    main()
