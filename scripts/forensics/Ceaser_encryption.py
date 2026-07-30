"""

what we want is to keep our letters in range from A to Z that is 0 to 25 range for this we use 
x%26 
but if exceed : (x-65)%26
Now for our shifting with nth key : (x-65+key)%26 
Now to convert it into ascii : (x-65+key)%26 + 65
"""


%pip install wordfreq

from wordfreq import zipf_frequency
import re

# A reasonably wide net of short, common English words —
# these are exactly the kind of fragments that show up inside
# concatenated phrases like "TRYHACKME"
COMMON_FRAGMENTS = {
    "THE","AND","YOU","ARE","FOR","THIS","THAT","WITH","HAVE","FROM",
    "TRY","HACK","ME","IS","IT","TO","MY","HOW","WHAT","GOOD","HELLO",
    "WORLD","FLAG","KEY","CODE","WIN","CAN","GET"
}

def looks_english_substring(text, min_matches=1):
    """Catches English fragments even with no spaces (e.g. TRYHACKME)."""
    text_upper = text.upper()
    matches = [w for w in COMMON_FRAGMENTS if w in text_upper]
    return len(matches) >= min_matches, matches


def looks_english_dictionary(text, threshold=0.6):
    """Original whole-word check — good when spaces/punctuation exist."""
    tokens = "".join(c if c.isalpha() else " " for c in text.upper()).split()
    if not tokens:
        return False
    hits = sum(1 for w in tokens if zipf_frequency(w.lower(), 'en') > 1.5)
    return (hits / len(tokens)) >= threshold


def looks_english(text):
    """Try both strategies — spaced text OR no-space blob."""
    has_spaces = " " in text.strip()
    if has_spaces:
        return looks_english_dictionary(text)
    else:
        matched, fragments = looks_english_substring(text)
        return matched


def caesar_enc(plaintext, key):
    key %= 26
    return "".join(
        chr((ord(c) - 65 + key) % 26 + 65) if c.isalpha() else c
        for c in plaintext.upper()
    )

def caesar_dec(ciphertext, key):
    return caesar_enc(ciphertext, -key)

def brute_force(ciphertext):
    for k in range(26):
        text = caesar_dec(ciphertext, k)
        flag = "  <-- likely match" if looks_english(text) else ""
        print(f"Key {k:2}: {text}{flag}")


brute_force("JAJWDTSJ NS RD KFRNQD MFX PNQQJI XTRJTSJ")