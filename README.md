# Project-Elevate-Labs.

# 🔐 Password Strength Analyzer & Custom Wordlist Generator

A simple Python tool to:
1. Analyze password strength using the zxcvbn library
2. Generate custom wordlists based on personal inputs with optional leetspeak and year combinations

---

##  Features
- Password strength score (0–4)
- Estimated crack time and feedback
- Wordlist generation with:
  - Names, pet names, dates
  - Leetspeak substitutions
  - Year-based suffixes



## Installation
```bash
pip install zxcvbn
```

---

##  Usage
### Analyze Password
```bash
python password_analyzer.py -p "MyP@ssw0rd123"
```

### Generate Custom Wordlist
```bash
python password_analyzer.py -i anmol kant cyber -y 1999 2024 --leetspeak
```
- Output: `custom_wordlist.txt`

---

## Screenshots
### Password Strength Example:
```
Password: MyP@ssw0rd123
Score: 3
Crack Time: 2 hours
Suggestions:
 - Add more unique characters
 - Avoid common patterns
```

### Wordlist Output:
```
anmol
kant
cyber
@nmol
k@nt
cyb3r
anmol1999
cyber2024
...
```

---

## Project Structure
```
├── password_analyzer.py  # Main script
├── custom_wordlist.txt   # Output file
└── README.md             # Project instructions
```






