# Code for computing mean and standard deviation from data in file
# Name: Your Name, Roll No: Your Roll No

import sys
import math

def main():
    if len(sys.argv) != 3:
        print("Usage: python3 avsd.py <no_of_data_points> <data_filename>")
        sys.exit(1)

    Ndata = int(sys.argv[1])
    filename = sys.argv[2]
    data = []

    try:
        with open(filename, 'r') as f:
            for _ in range(Ndata):
                line = f.readline()
                if not line:
                    break
                parts = line.strip().split()
                if len(parts) !=2:
                    continue
                _, value_str = parts
                value = float(value_str)
                data.append(value)
    except FileNotFoundError:
        print("Error: File not found.")
        sys.exit(1)

    average = sum(data) / Ndata
    variance = sum((x - average)**2 for x in data) / Ndata
    sd = math.sqrt(variance)

    with open("output.txt", "w") as fout:
        fout.write(f"average = {average:.4f}, s.d. = {sd:.4f}\n")

if __name__ == "__main__":
    main()
