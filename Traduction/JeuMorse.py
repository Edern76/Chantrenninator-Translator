import random

Morse = {'A': '.-', 'B': '-...', 'C':'-.-.', 'D': '-..',
         'E': '.', 'F': '..-.', 'G': '--.', 'H': '....',
         'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..',
         'M': '--', 'N': '-.', 'O': '---', 'P': '.--.',
         'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-',
         'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
         'Y': '-.--', 'Z': '--..',
        
        '0': '-----', '1': '.----', '2': '..---',
        '3': '...--', '4': '....-', '5': '.....',
        '6': '-....', '7': '--...', '8': '---..',
        '9': '----.',
         
         '?': '..--..', '!': '-.-.--', '.': '.-.-.-',
         ';': '-.-.-.', ':': '---...', ',': '--..--',
         "'": '.----.', '-': '-....-', '(': '-.--.',
         ')': '-.--.-', '"': '.-..-.'
        }

hasard = random.randint(33,90)

while (hasard > 34 and hasard < 39) or (hasard > 41 and hasard < 44) or (hasard > 46 and hasard < 48) or (hasard > 59 and hasard < 63) or (hasard > 63 and hasard < 65):
    hasard = random.randint(33,90)

print(chr(hasard))