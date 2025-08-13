# Code for computing AB, D·C and BC from matrices in file
# Name: Your Name, Roll No: Your Roll No

import numpy as np

# Read matrix from a file
def read_matrix(filename):
    with open(filename, 'r') as f:
        lines = f.readlines()
    matrix = []
    for line in lines:
        row = [float(x) for x in line.strip().split()]
        matrix.append(row)
    return np.array(matrix)

def main():
    # Read matrices from .tex files
    A = read_matrix("A.tex")
    B = read_matrix("B.tex")
    C = read_matrix("C.tex")
    D = read_matrix("D.tex")

    # Compute AB, D·C, BC
    AB = A @ B
    DC = D @ C
    BC = B @ C

    # Write to output.txt
    with open("output.txt", "w") as fout:
        fout.write("Matrix AB:\n")
        fout.write(str(AB) + "\n\n")

        fout.write("Dot Product D·C:\n")
        fout.write(str(DC) + "\n\n")

        fout.write("Matrix BC:\n")
        fout.write(str(BC) + "\n")

if __name__ == "__main__":
    main()
