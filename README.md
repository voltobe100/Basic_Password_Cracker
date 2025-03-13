# Password Cracker

A simple password cracker that uses wordlists to brute-force hash comparisons.

## Features

✅ Supports MD5, SHA-1, and SHA-256 hashing algorithms  
✅ Uses a wordlist file for dictionary attacks  
✅ Command-line interface for ease of use

## Requirements

- Python 3.x

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/password-cracker.git
   cd password-cracker
   ```
2. No additional dependencies are required; Python's built-in `hashlib` is used.

## Usage

Run the script with the following command:

```bash
python password_cracker.py <hash_value> <wordlist.txt> --algorithm <md5|sha1|sha256>
```

### Example

To crack an MD5 hash:

```bash
python password_cracker.py 5f4dcc3b5aa765d61d8327deb882cf99 wordlist.txt --algorithm md5
```

Output:

```
[+] Password found: password
```

## Notes

- Ensure you have a valid wordlist (e.g., `rockyou.txt` for better results).
- This script is for educational and ethical hacking purposes only.
