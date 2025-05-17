# Function definition (repeated here for self-contained test)
def get_most_likely_ancestor_consensus(dna_string1, dna_string2):
    positions = []
    for i in range(len(dna_string1) - len(dna_string2) + 1):
        if dna_string1[i:i + len(dna_string2)] == dna_string2:
            positions.append(i + 1)  # Convert to 1-based index
    return tuple(positions)  # Return as individual values


# ---- Test ----
def test_get_most_likely_ancestor_consensus():
    # Test input
    dna_string1 = "GATATATGCATATACTT"
    dna_string2 = "ATAT"

    # Expected output: 2, 4, 10
    pos1, pos2, pos3 = get_most_likely_ancestor_consensus(dna_string1, dna_string2)

    assert (pos1, pos2, pos3) == (2, 4, 10), f"Expected (2, 4, 10), but got ({pos1}, {pos2}, {pos3})"
    print("Test passed: get_most_likely_ancestor_consensus returns 2 4 10 correctly.")

# Run the test
test_get_most_likely_ancestor_consensus()
