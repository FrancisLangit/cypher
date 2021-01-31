class MorseCode:
     """Represents text to be ciphered into Morse Code.

     Attributes:
          text (str): Text to be ciphered into morse code.
          morse_code_dict (dict): Dictionary of morse code equivalents.
     """


     def __init__(self, text):
          """Initializes MorseCode class attributes."""
          self.text = text
          self.morse_code_dict = { 
               # Letters
               'A': '.-'    ,      'B': '-...'   ,      'C': '-.-.'  , 
               'D': '-..'   ,      'E': '.'      ,      'F': '..-.'  , 
               'G': '--.'   ,      'H': '....'   ,      'I': '..'    , 
               'J': '.---'  ,      'K': '-.-'    ,      'L': '.-..'  , 
               'M': '--'    ,      'N': '-.'     ,      'O': '---'   , 
               'P': '.--.'  ,      'Q': '--.-'   ,      'R': '.-.'   , 
               'S': '...'   ,      'T': '-'      ,      'U': '..-'   , 
               'V': '...-'  ,      'W': '.--'    ,      'X': '-..-'  , 
               'Y': '-.--'  ,      'Z': '--..'   , 

               # Digits
               '1': '.----' ,      '2': '..---'  ,      '3': '...--' , 
               '4': '....-' ,      '5': '.....'  ,      '6': '-....' , 
               '7': '--...' ,      '8': '---..'  ,      '9': '----.' , 
               '0': '-----' , 

               # Punctuation Marks
               '.': '.-.-.-',      ',': '--..--' ,      '?': '..--..',
               "'": '.----.',      '!': '-.-.--' ,      '/': '-..-.' ,
               "(": '-.--.' ,      ')': '-.--.-' ,      '&': '.-...' ,
               ":": '---...',      ';': '-.-.-.' ,      '=': '-...-' ,
               '+': '.-.-.' ,      '-': '-....-' ,      '_': '..--.-',
               '"': '.-..-.',      '$': '...-..-',      '@': '.--.-.',

               # Space
               ' ': '.......',  
          } 


     def cipher(self): 
          """Ciphers a string into morse code.

          Args:
              None

          Returns:
              tuple: ([int] Error Code, [str] Output Text) 
                  [int] Error Code - 0 if with error. 1 without error.
                  [str] Output Text - Ciphered text or error message.
          """
          try:
               cipher = '' 
               for char in self.text.upper(): 
                    if char != ' ': 
                         cipher += self.morse_code_dict[char] + ' '
                    else: 
                         cipher += '....... '
          except KeyError as e: 
               return (1, f"Error. Cannot translate {e} to morse code.")
          return (0, cipher)


     def decipher_split_section(self, split_section):
          """Deciphers a split section of morse code string to English.

          Args:
              split_section: Split section of self.text.split().

          Returns:
              str: Split section element deciphered into English.
          """
          if split_section in self.morse_code_dict.values():
               ascii_chars = list(self.morse_code_dict.keys())
               morse_codes = list(self.morse_code_dict.values())
               return ascii_chars[morse_codes.index(split_section)]
          else:
               return " "


     def decipher(self):
          """Deciphers Morse Code to English.

          Args:
              None

          Returns:
              tuple: ([int] Error Code, [str] Output Text) 
                  [int] Error Code - 0 if with error. 1 without error.
                  [str] Output Text - Diphered text or error message.
          """
          if any(char.isalnum() for char in self.text):
               return (1, ("Morse code to decipher must not contain " 
                       "alpha-numeric text."))
          deciphered_text = ""
          for split_section in self.text.split():
               deciphered_text += self.decipher_split_section(split_section)
          return (0, deciphered_text)