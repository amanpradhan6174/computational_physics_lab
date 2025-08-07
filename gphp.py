# Name: Aman Pradhan, RollNo: 2311020
# SectionA: Odd no. sum and factorial
# SectionB: GP and HP series sum
# SectionC: Matrix operations AB, D·C, BC

import sys

# Function to read matrix or vector from file
def read_matrix(filename):
    matrix = []
    try:
        with open(filename, 'r') as f:
            for line in f:
                row = [float(num) for num in line.strip().split()]
                if row:
                    matrix.append(row)
    except FileNotFoundError:
        print(f"Error: File {filename} not found.")
        sys.exit(1)
    return matrix

# Matrix multiplication A x B
def multiply_matrices(A, B):
    rows_a = len(A)
    cols_a = len(A[0])
    rows_b = len(B)
    cols_b = len(B[0])
    result = [[0 for _ in range(cols_b)] for _ in range(rows_a)]
    for i in range(rows_a):
        for j in range(cols_b):
            for k in range(cols_a):
                result[i][j] += A[i][k] * B[k][j]
    return result

# Dot product of column vectors D · C
def dot_product_vectors(D, C):
    if len(D) != len(C):
        print("Error: Vector sizes mismatch.")
        sys.exit(1)
    result = 0
    for i in range(len(D)):
        result += D[i][0] * C[i][0]
    return result

# Matrix-vector multiplication B x C
def multiply_matrix_vector(B, C):
    rows_b = len(B)
    cols_b = len(B[0])
    rows_c = len(C)
    if cols_b != rows_c:
        print("Error: B columns must match C rows.")
        sys.exit(1)
    result = [[0] for _ in range(rows_b)]
    for i in range(rows_b):
        for j in range(cols_b):
            result[i][0] += B[i][j] * C[j][0]
    return result

# Main function
def main():
    # SECTION A: Odd number sum and factorial
    N1, sum_of_odds = 20, 0
    odd_numbers = []
    for i in range(N1):
        odd = 2 * i + 1
        sum_of_odds += odd
        odd_numbers.append(odd)

    factorial_N1 = 1
    for i in range(1, 9):
        factorial_N1 *= i

    # SECTION B: GP and HP series
    N2, t0, r = 15, 1.25, 0.5
    sum_gp, sum_hp = 0, 0
    for n in range(N2):
        term_gp = t0 * (r ** n)
        sum_gp += term_gp
        term_hp = 1 / term_gp
        sum_hp += term_hp

    # SECTION C: Matrix Operations
    A = read_matrix("asgn0_matA")
    B = read_matrix("asgn0_matB")
    C = read_matrix("asgn0_vecC")
    D = read_matrix("asgn0_vecd")

    AB = multiply_matrices(A, B)
    DC = dot_product_vectors(D, C)
    BC = multiply_matrix_vector(B, C)

    # Write all output to file
    with open("output.txt", "w") as f:
        f.write("Name: Aman Pradhan, RollNo: 2311020\n\n")

        # Section A
        f.write("SECTION A: Sum of first 20 odd numbers & Factorial of 8\n")
        f.write(f"List of first {N1} odd numbers:\n{odd_numbers}\n")
        f.write(f"Sum of these odd numbers: {sum_of_odds}\n")
        f.write(f"Factorial of 8: {factorial_N1}\n\n")

        # Section B
        f.write("SECTION B: Sum of first 15 terms of GP and HP\n")
        f.write(f"Sum of GP (t0={t0}, r={r}, N={N2}): {sum_gp:.5f}\n")
        f.write(f"Sum of HP (reciprocal of above GP terms): {sum_hp:.5f}\n\n")

        # Section C
        f.write("SECTION C: Matrix Operations\n")
        f.write("Matrix A × B (AB):\n")
        for row in AB:
            f.write("  ".join(f"{val:.2f}" for val in row) + "\n")

        f.write("\nDot product D · C: {:.2f}\n".format(DC))

        f.write("\nMatrix B × C (BC):\n")
        for row in BC:
            f.write(f"{row[0]:.2f}\n")

    # Also print results to terminal
    print("Results written to output.txt")

if __name__ == "__main__":
    main()
