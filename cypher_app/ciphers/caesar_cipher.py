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


    def cipher(self):
        """Ciphers text into a Caesar Cipher.

        Args:
            None

        Returns:
            str: Text encrypted into a Caesar Cipher
        """
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