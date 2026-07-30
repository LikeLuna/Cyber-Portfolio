import numpy as np


matrix = np.array([[(row+col)%26 for col in range(26)]for row in range(26)])


"""
same as 
for i in range 0 to 25: 
    for j in range 0 to 25:
        arr[i][j]=(i+j)%26

Now for 2nd row 1 st element must start with B 
i= 1 j = 0 
i+j = 1 -> 0= A 1=B
"""

y = ord('B')-65
z = ord('D')-65

# print(matrix[y][z])   #must be 4 for E

# x = matrix[y][z]
# print(chr(x+65))




"""

logic of vigeneria 
enter a plain text 
choose a cipher key 
increase cipher key length to match the plain text
"""



"""
Encryption Logic: 

Lets say the word is : HELLO 
mask with orange     : ORANG

Now we will see H and O match which letter in table: V and that will be new encryption letter

"""
import numpy as np

matrix = np.array([[(row + col) % 26 for col in range(26)] for row in range(26)])


def masking(plain_text, key):
    """Extends the key to match the length of the letters in plain_text (skips spaces)."""
    mask = ""
    key_pos = 0
    for ch in plain_text:
        if ch.isalpha():
            mask += key[key_pos % len(key)].upper()
            key_pos += 1
        else:
            mask += ch  # keep spaces/punctuation as placeholders
    return mask


def vigenere_encrypt(plain_text, key):
    mask = masking(plain_text, key)
    encrypted = ""
    for p_ch, k_ch in zip(plain_text, mask):
        if p_ch.isalpha():
            x = ord(p_ch.upper()) - 65
            y = ord(k_ch) - 65
            c = matrix[x][y]
            new_ch = chr(c + 65)
            encrypted += new_ch.lower() if p_ch.islower() else new_ch
        else:
            encrypted += p_ch
    return encrypted


def vigenere_decrypt(cipher_text, key):
    mask = masking(cipher_text, key)
    decrypted = ""
    for c_ch, k_ch in zip(cipher_text, mask):
        if c_ch.isalpha():
            c = ord(c_ch.upper()) - 65
            k = ord(k_ch) - 65
            p = (c - k) % 26          # reverse of (row+col)%26
            new_ch = chr(p + 65)
            decrypted += new_ch.lower() if c_ch.islower() else new_ch
        else:
            decrypted += c_ch
    return decrypted


plain_text = "My NamE Bogambo"
key = "orange"

encrypted = vigenere_encrypt(plain_text, key)
decrypted = vigenere_decrypt(encrypted, key)

print("Plain:     ", plain_text)
print("Encrypted: ", encrypted)
print("Decrypted: ", decrypted)
