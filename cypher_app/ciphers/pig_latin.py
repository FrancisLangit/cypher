import re


class PigLatin:
    """Represents text to be ciphered into Pig Latin.

    Attributes:
        text (str): Text to be ciphered into Pig Latin.
        vowels (str): Uppercase and lowercase vowels. Defined in __init__.
    """


    def __init__(self, text):
        """Initializes attributes of PigLatin."""
        self.text = text
        self.vowels = 'aeiouAEIOU'


    def _cipher_word(self, word):
        """Ciphers a word into Pig Latin. 

        Adapated from 301_Moved_Permantently's revised translate_to_piglatin f
        unction in (https://codereview.stackexchange.com/questions/127871/pig-
        latin-translator-in-python).

        Meant for use with class only.
        
        Args:
            word (str): Word to be ciphered into Pig Latin.

        Returns:
            str: Word ciphered into Pig Latin.
        """
        first_letter, *remaining_letters = word
        if first_letter in 'aeiouAEIOU':
            return word + 'yay'
        else:
            return ''.join(remaining_letters) + first_letter + 'ay'


    def _decipher_word(self, word):
        """Deciphers a word from Pig Latin to English. 

        Adapated from 301_Moved_Permantently's revised translate_to_english fu
        nction in (https://codereview.stackexchange.com/questions/127871/pig-l
        atin-translator-in-python).

        Meant for use with class only.
        
        Args:
            word (str): Word to be deciphered into English.

        Returns:
            str: Word deciphered into English.
        """
        if word.endswith('yay'):
            return word[:-3]
        else:
            *remaining_letters, last_letter, a, y = word
            return last_letter + ''.join(remaining_letters)


    def cipher(self):
        """Ciphers self.text into Pig Latin.

        Args:
            None

        Returns:
            str: Text ciphered into Pig Latin
        """
        cipher = ""
        partitions = re.compile(r"[\w']+|[.,!?;]|\s").findall(self.text)
        for partition in partitions:
            # Only translate partition if made of alphabetical characters.
            if partition.isalpha():
                cipher += self._cipher_word(partition)
            else:
                cipher += partition
        return cipher