# Unique Prime Numbers “Hidden” in Binary Strings

## Table of Contents
1. [Project Overview](#project-overview)  
2. [Problem Statement](#problem-statement)  
3. [Features](#features)  
4. [Installation](#installation)  
5. [Usage](#usage)  
6. [Examples](#examples)  
7. [Implementation Details](#implementation-details)  
   - [Basic Solution](#basic-solution)  
   - [Optimized Solution](#optimized-solution)  
8. [Testing & Performance](#testing--performance)  
9. [Complexity Analysis](#complexity-analysis)  
10. [Team Contributions](#team-contributions)  
11. [License](#license)  

---

## Project Overview
This project addresses a Python coding challenge designed to assess algorithmic and data structure skills. The task involves identifying all unique prime numbers hidden within a given binary string that are less than a specified integer N. The project includes both **basic** and **optimized** solutions for performance comparison.

---

## Problem Statement
Given a binary string and an integer N:

1. Extract all possible substrings from the binary string.  
2. Convert each substring from binary to decimal.  
3. Identify unique prime numbers smaller than N.  
4. Display results according to the following rules:  
   - If fewer than 6 prime numbers are found: display all.  
   - If 6 or more prime numbers are found: display the first three smallest and the last three largest primes.  

Invalid binary strings should return an error message.

---

## Features
- Extract all substrings from a binary string.  
- Convert substrings to decimal numbers.  
- Identify prime numbers below a given threshold N.  
- Display results according to the number of primes found.  
- Compare performance between basic and optimized solutions.  

---

## Installation
1. Clone the repository:  
   ```bash
   git clone <repository_url>
   ```
2. Navigate to the project directory:

   ```bash
   cd unique-primes-binary
    ```
3. Install required packages (if any):
   ```bash
   pip install -r requirements.txt
   ```
## Usage

Run the Python scripts with the following commands:

```bash
python "Basic Solution 1 (sets).py"
python "Optimised solution (sets).py"
```

## Examples

| Input                 | Output                       | Notes                                                 |
|-----------------------|-------------------------------|-------------------------------------------------------|
| `1010110,100`         | `2, 3, 5, 11, 43`            | Total prime numbers = 5                               |
| `01101011,50`         | `2, 3, 5, 7, 13`             | Total prime numbers = 5                               |
| `1101011,80`          | `2, 3, 5, 7, 11, 13`         | Displays first 3 smallest and last 3 largest primes (≥6 primes) |
| `10010110,150`        | `2, 3, 5, 7, 11, 13, 23`     | Moderate length string, multiple primes              |
| `11110011,80`         | `2, 3, 5, 7, 11, 13`         | Repeating pattern, several primes                    |
| `01010101,50`         | `2, 3, 5, 7, 11, 13`         | Alternating pattern, multiple primes                 |
| `101010111001,200`    | `2, 3, 5, 7, 11, 13, 17, 19` | Larger string, first 3 smallest and last 3 largest primes shown |
| `COMP1010,20`         | `0: Invalid binary strings`  | Not a binary string                                  |

### Implementation Details

### Basic Solution

**File:** [Basic Solution 1 (sets).py](./Basic%20Solution%201%20(sets).py)  

**Approach:**
- Uses `set()` to store decimal and prime numbers.  
- Converts binary substrings to decimal and checks each for primality.  
- Prints either all primes or the first three smallest and last three largest if ≥6 primes found.  

### Optimized Solution

**File:** [Optimised solution (sets).py](./Optimised%20solution%20(sets).py)  

**Approach:**
- Improved primality check using 6k ± 1 rule.  
- Uses bitwise operations for faster binary-to-decimal conversion.  
- Optimized for runtime, efficiently handling large inputs (<60 seconds).

## Testing & Performance

Both solutions were tested with 10 increasingly large binary strings.

### Example runtime comparison:

| Test Case | Basic Runtime (s) | Optimized Runtime (s) |
|-----------|-----------------|---------------------|
| Case 1    | 0.00008         | 0.00008             |
| Case 2    | 0.00024         | 0.00018             |
| Case 3    | 0.00017         | 0.00016             |
| Case 4    | 0.00177         | 0.00078             |
| Case 5    | 0.01199         | 0.00413             |
| Case 6    | 0.67008         | 0.23138             |
| Case 7    | 15.32339        | 4.83460             |
| Case 8    | 21.74988        | 6.37104             |
| Case 9    | 53.46694        | 16.45944            |
| Case 10   | >60             | 22.00073            |

Optimized solution significantly improves runtime for large inputs using:

- Efficient primality checking  
- Bitwise operations for binary conversion

## Complexity Analysis

**Basic Solution:**  
- **Time:** O(n²√m) — n = length of binary string, m = max decimal value  
- **Space:** O(n²) for storing all decimal substrings  

**Optimized Solution:**  
- **Time:** O(n²√m / 3) — using 6k ± 1 optimization  
- **Space:** O(n²)  

Optimized solution achieves faster runtime for large inputs without using external libraries.

## Summary

This project demonstrates how to efficiently find unique prime numbers hidden in binary strings. Two approaches were implemented:

- **Basic Solution:** Simple and easy-to-understand implementation using sets, suitable for small to medium inputs.  
- **Optimized Solution:** Improved runtime and efficiency using advanced primality checks (6k ± 1 rule) and bitwise operations, capable of handling larger inputs within reasonable time limits.  

Key takeaways:  
- Understanding of binary-to-decimal conversions and substring generation.  
- Efficient prime number checking and handling of large datasets.  
- Clear demonstration of performance optimization and complexity analysis.  

The project also includes testing, runtime comparisons, and a structured approach suitable for coding interviews or algorithmic practice.







