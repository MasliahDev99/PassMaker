#!/usr/bin/env python3

from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
import base64
import os

class PasswordSecurity:
    def __init__(self, method_encrypted: str):
        """
        Inicializa el sistema de seguridad de la contraseña.
        """
        if method_encrypted.upper() != 'RSA':
            raise ValueError("Actualmente solo se soporta RSA para encriptación.")
        self.method_encrypted = method_encrypted.upper()
        
        # Generar un par de claves RSA
        self.key_pair = RSA.generate(2048)  # Genera una clave RSA de 2048 bits
        self.public_key = self.key_pair.publickey()  # Clave pública
        self.private_key = self.key_pair  # Clave privada
        self.cipher = PKCS1_OAEP.new(self.public_key)  # Crea un objeto de cifrado con la clave pública

    def encrypt(self, plaintext: str) -> str:
        """
        Encripta un texto en claro utilizando RSA.

        args:
            plaintext (str): Texto en claro a encriptar.

        return:
            str: Texto en claro encriptado, codificado en base64.
        """
        encrypted = self.cipher.encrypt(plaintext.encode())
        return base64.b64encode(encrypted).decode()

    def decrypt(self, ciphertext: str) -> str:
        """
        Desencripta un texto cifrado utilizando RSA.

        args:
            ciphertext (str): Texto cifrado en base64 a desencriptar.

        return:
            str: Texto desencriptado.
        """
        cipher = PKCS1_OAEP.new(self.private_key)  # Crear un objeto de cifrado con la clave privada
        ciphertext_bytes = base64.b64decode(ciphertext)
        decrypted = cipher.decrypt(ciphertext_bytes)
        return decrypted.decode()

