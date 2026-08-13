# Ransomware Recovery with Python

## Scenario

As part of the AIG Shields Up: Cybersecurity virtual experience, I worked on a simulated ransomware recovery scenario involving an encrypted ZIP file.

A password wordlist was provided as part of the exercise.

## Objective

The objective was to develop a Python script capable of testing passwords from the provided wordlist against the encrypted ZIP file and identifying the correct password.

## Approach

The script:

1. Opens the encrypted ZIP file.
2. Opens the provided password wordlist.
3. Iterates through each password.
4. Removes whitespace and newline characters from each entry.
5. Attempts to extract the ZIP file using the candidate password.
6. Handles unsuccessful attempts using exception handling.
7. Stops when the correct password is found.
8. Reports when no password is found in the wordlist.

## Python Implementation

The solution uses Python's built-in `zipfile` module to work with the encrypted ZIP archive.

Key programming concepts demonstrated:

- Functions
- File handling
- Loops
- Conditional statements
- Exception handling
- Boolean variables
- Python's `zipfile` module

## Result

The script successfully identified the correct password during the simulated exercise and allowed the encrypted file to be extracted.

## Skills Demonstrated

- Python scripting
- Basic cybersecurity automation
- Password wordlist attacks
- File handling
- Problem solving
- Exception handling
- Ransomware recovery concepts

## Disclaimer

This project was completed in a simulated cybersecurity environment as part of the AIG Shields Up: Cybersecurity virtual experience program. It is intended for educational purposes.
