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


    def decipher(self):
        letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

        for key in range(26):
            translated = ''

            for char in self.text:
                if char in letters:
                    num = letters.find(char)
                    num -= key

                    if num < 0:
                        num += len(letters)

                    translated += letters[num]

                else:
                    translated += symbol

        print(f'Key #{key}: {translated}')


text = CaesarCipher("hello world", 27)
print(text.cipher())