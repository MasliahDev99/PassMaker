#!/usr/bin/env Python3

import random
import string

class PasswordGenerator:
    """ Este Objeto se encargara de manejar la generacion de contraseñas """
    def __init__(self, length: int = 12 ,use_upper: bool = True, use_lower: bool = True, 
                 use_digits: bool = True, use_special: bool = True):
        """ 
        Crea una instancia de generador de contraseñas
        
        args:
            length (int): La longitud deseada para la contraseña.
            use_upper (bool): Incluye letras mayúsculas en la contraseña si es True.
            use_lower (bool): Incluye letras minúsculas en la contraseña si es True.
            use_digits (bool): Incluye números en la contraseña si es True.
            use_special (bool): Incluye caracteres especiales en la contraseña si es True.
        """
        self.length = length
        self.use_upper = use_upper
        self.use_lower = use_lower
        self.use_digits = use_digits
        self.use_special = use_special

        self._validate_length()

    def _validate_length(self):
        """ Verifica que la longitud sea suficiente para incluir todos los tipos de caracteres seleccionados. """
        # Calcula cuántos tipos de caracteres se van a incluir
        min_length = sum([self.use_upper, self.use_lower, self.use_digits, self.use_special])
        if self.length < min_length:
            raise ValueError("La longitud debe ser suficiente para incluir al menos un carácter de cada tipo seleccionado.")
        if self.length > 256:
            raise ValueError("La longuitud maxima es 256")
    
    def set_lenght(self,length:int)->int:
        self.length = length
        self._validate_length()

    def _set_characters(self) -> str:
        """ 
        Prepara el conjunto de caracteres válidos según las opciones seleccionadas.

        return:
            str: Todos los caracteres que se pueden usar en la contraseña.
        """
        characters = ''
        if self.use_upper:
            characters += string.ascii_uppercase
        if self.use_lower:
            characters += string.ascii_lowercase
        if self.use_digits:
            characters += string.digits
        if self.use_special:
            characters += string.punctuation
        
        if not characters:
            raise ValueError("Debes seleccionar al menos un tipo de carácter para la contraseña.")

        return characters
        
    def generate_password(self) -> str:
        characters = self._set_characters()
        password = []
        if self.use_upper:
            password.append(random.choice(string.ascii_uppercase))
        if self.use_lower:
            password.append(random.choice(string.ascii_lowercase))
        if self.use_digits:
            password.append(random.choice(string.digits))
        if self.use_special:
            password.append(random.choice(string.punctuation))

        remaining_length = self.length - len(password)
        if remaining_length > 0:
            password.extend(random.choice(characters) for _ in range(remaining_length))

        random.shuffle(password)
        return ''.join(password)