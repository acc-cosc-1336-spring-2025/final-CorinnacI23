def get_most_likely_ancestor_consensus(dna_string1, dna_string2):
    positions = []
    for i in range(len(dna_string1) - len(dna_string2) + 1):
        if dna_string1[i:i + len(dna_string2)] == dna_string2:
            positions.append(i + 1)  # Convert to 1-based index
    return tuple(positions)  # Return multiple values as individual parameters


def is_valid_dna_sequence(seq):
    return all(base in "ACGT" for base in seq)


def main():
    while True:
        # Get and validate main DNA string
        while True:
            dna_string1 = input("Enter a DNA string (9-16 characters): ").upper()
            if 8 < len(dna_string1) <= 16 and is_valid_dna_sequence(dna_string1):
                break
            else:
                print("Invalid DNA string. Must be between 9 and 16 characters and only contain A, C, G, T.")

        # Get and validate DNA substring
        while True:
            dna_string2 = input("Enter a 4-character DNA substring: ").upper()
            if len(dna_string2) == 4 and is_valid_dna_sequence(dna_string2):
                break
            else:
                print("Invalid substring. Must be exactly 4 characters and contain only A, C, G, T.")

        # Get and display results
        positions = get_most_likely_ancestor_consensus(dna_string1, dna_string2)
        if positions:
            print("Positions (1-based):", *positions)
        else:
            print("Substring not found.")

        # Ask user to continue or exit
        cont = input("Do you want to try again? (y/n): ").strip().lower()
        if cont != 'y':
            print("Goodbye!")
            break


if __name__ == "__main__":
    main()
