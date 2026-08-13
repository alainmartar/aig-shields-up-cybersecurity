# AIG Shields Up: Cybersecurity Virtual Experience

## Overview

This repository documents my work from the AIG Shields Up: Cybersecurity virtual experience program on Forage.

The simulation covered two cybersecurity scenarios:

1. Apache Log4j vulnerability identification and response
2. Ransomware recovery using Python

The projects were completed in a simulated cybersecurity environment and are presented here as part of my cybersecurity portfolio.

---
## Project 1 — Log4j Vulnerability Response

### Scenario

A simulated AIG environment contained infrastructure potentially affected by the Apache Log4j vulnerability.

### Objective

Analyze the available cybersecurity advisory information, identify potentially affected infrastructure, assess the risk, and communicate the vulnerability to the responsible team.

### Activities

- Reviewed CISA cybersecurity advisory information related to Apache Log4j.
- Identified the infrastructure containing Log4j from the provided infrastructure inventory.
- Identified the responsible product team and infrastructure owner.
- Assessed the potential impact of the vulnerability, including Remote Code Execution (RCE).
- Drafted a security advisory email communicating the vulnerability, risk, and recommended remediation.
- Recommended patching/updating affected Log4j components and verification of remediation.

### Skills & Concepts

- Vulnerability Management
- Risk Assessment
- Security Advisories
- CVE Analysis
- Apache Log4j / Log4Shell
- CISA Cybersecurity Guidance
- Remediation Planning
- Security Communication

---

## Project 2 — Ransomware Recovery with Python

### Scenario

A simulated ransomware incident involved an encrypted ZIP file. A password wordlist was provided as part of the exercise.

### Objective

Develop a Python script to test passwords from the provided wordlist and identify the password required to extract the encrypted ZIP file.

### Implementation

The Python script:

- Reads candidate passwords from a wordlist.
- Removes unnecessary whitespace and newline characters.
- Attempts to extract the encrypted ZIP using each candidate password.
- Handles unsuccessful password attempts using exception handling.
- Stops when the correct password is identified.
- Reports when no password is found in the provided wordlist.

### Technologies

- Python 3
- `zipfile`
- File handling
- Loops
- Conditional logic
- Exception handling
- Password wordlists

### Result

The script successfully identified the correct password during the simulation and extracted the encrypted file.

---

## Learning Outcomes

This virtual experience provided hands-on practice with:

- Vulnerability identification and assessment
- Cybersecurity advisory development
- Risk and impact communication
- Vulnerability remediation
- Python scripting for cybersecurity tasks
- Password wordlist attacks
- Basic ransomware response concepts

---

## Program

**AIG Shields Up: Cybersecurity Virtual Experience Program**  
Forage | 2026

> This repository documents my individual work and learning from a simulated cybersecurity environment. It does not represent professional employment or work performed for AIG.
