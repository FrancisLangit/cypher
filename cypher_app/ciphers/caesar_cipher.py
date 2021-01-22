import string

class CaesarCipher:
    """Represents text to be ciphered into a Caesar Cipher.

    Attributes:
        text (str): Text to cipher.
        key (int): Number of right shifts to make on the alphabet.
    """


    def __init__(self, text, key):
        """Initializes attributes of CaesarCipher."""
        self.text = text
        self.key = key
        self.key_limit = 26


    def cipher(self):
        """Ciphers text into a Caesar Cipher.

        Adapted from tutorialspoint.com's "Cryptography with Python - Caesar C
        ipher" from (https://www.tutorialspoint.com/cryptography_with_python/c
        ryptography_with_python_caesar_cipher.htm).

        Args:
            None

        Returns:
            str: Text encrypted into a Caesar Cipher
        """
        if not self.key > self.key_limit:
            cipher = ""
            for i in range(len(self.text)):
                char = self.text[i]
                if char.isupper():
                    cipher += chr((ord(char) + self.key - 65) % 26 + 65)
                elif char.islower():
                    cipher += chr((ord(char) + self.key - 97) % 26 + 97)
                else:
                    cipher += char
            return cipher
        else:
            return f"Chosen key of {self.key} is over limit of {self.key_limit}."


    def _decipher_char(self, char):
        """Deciphers a single character in a Caesar Cipher.

        Meant for use within class only, particularly in decipher method.

        Args:
            char: String character to be deciphered.

        Returns:
            str: Deciphered char. 
        """
        if char.isupper():
            alphabet = string.ascii_uppercase
        else:
            alphabet = string.ascii.lowercase
        position = alphabet.find(char)
        new_position = (position - self.key) % 26
        return alphabet[new_position]


    def decipher(self):
        """Deciphers a Caesar Cipher based on key provided.

        Adapted from GitHub user A08's "cc_decrypt.py" from (https://gist.gith
        ub.com/AO8/3a89ba7c8f032c7a1ff505baa3ce970e).

        Args:
            None

        Returns:
            str: Deciphered text. 
        """
        deciphered_text = ''
        for char in self.text:
            if char.isalpha():
                deciphered_text += self._decipher_char(char)
            else:
                deciphered_text += char
        return deciphered_text