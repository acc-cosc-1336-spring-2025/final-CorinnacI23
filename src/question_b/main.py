def create_multiplication_table():
    table = []
    for i in range(1, 6):  # Rows: 1 to 5
        row = []
        for j in range(1, 11):  # Columns: 1 to 10
            row.append(i * j)
        table.append(row)
    return table


def display_multiplication_table(table):
    for row in table:
        for value in row:
            print(f"{value:<4}", end="")  # Left-aligned, width 4 for clean formatting
        print()  # Newline after each row


def main():
    while True:
        # Generate and display multiplication table
        table = create_multiplication_table()
        print("\nMultiplication Table:")
        display_multiplication_table(table)

        # Ask user to continue or quit
        choice = input("\nDo you want to continue? (y/n): ").lower()
        if choice != 'y':
            print("Goodbye!")
            break


if __name__ == "__main__":
    main()
