import hashlib
import argparse

# Function to hash a word using the specified algorithm
def hash_word(word, algorithm):
    hash_func = getattr(hashlib, algorithm, None)
    if hash_func:
        return hash_func(word.encode()).hexdigest()
    else:
        raise ValueError("Unsupported hash algorithm")

# Function to attempt cracking the hash
def crack_password(hash_value, wordlist_file, algorithm):
    try:
        with open(wordlist_file, "r", encoding="utf-8") as file:
            for word in file:
                word = word.strip()
                if hash_word(word, algorithm) == hash_value:
                    print(f"[+] Password found: {word}")
                    return word
        print("[-] Password not found in wordlist.")
    except FileNotFoundError:
        print("[!] Wordlist file not found.")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Basic Password Cracker using wordlists")
    parser.add_argument("hash", help="The hashed password to crack")
    parser.add_argument("wordlist", help="Path to the wordlist file")
    parser.add_argument("--algorithm", default="md5", choices=["md5", "sha1", "sha256"], help="Hash algorithm (default: md5)")
    
    args = parser.parse_args()
    crack_password(args.hash, args.wordlist, args.algorithm)
