# Caesar Cipher CLI
Caesar Cipher in the command-line made in Python.

Originally made for my school's computer science class homework assignment, but expanded upon to include extra features for fun.

## Features
- Classic Caesar Cipher encryption gameplay
- Customisable encryption key (not secure for real-world use)
- Works for both capital and lowercase letters and numbers (alphanumeric)
- Cycles back if out of bounds (i.e.: `0 - 1 -> 9`, `9 + 1 -> 0`, `A - 1 -> Z`, `Z + 1 -> A`, `a - 1 -> z`, `z + 1 -> a`)
    (Does not work for symbols and other special characters)
- Symmetric decryption by inputting the negative of encryption key into the same function

## Usage
### Local
- Download `Python 3.X.X` and `main.py` and run `main.py`

### Online
- Open this link in your browser: **https://onlinegdb.com/IRGQKi8Mt** and click the `Run` button
