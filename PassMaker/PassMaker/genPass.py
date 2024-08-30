#!/usr/bin/env python3
import os
from files import File
from passwordevaluator import PasswordEvaluator
from passwordgenerator import PasswordGenerator
from passwordsecurity import PasswordSecurity

class GenPass:
    def __init__(self, length: int = 12,current_path:str = None,use_upper: bool = True, use_lower: bool = True, 
                 use_digits: bool = True, use_special: bool = True):
       
       
        self.generator = PasswordGenerator(length, use_upper, use_lower, use_digits, use_special)
        self.evaluator = PasswordEvaluator()
        self.encryptor = PasswordSecurity('RSA')
        self.file_manager = File(current_path)

    def generate_passowrd(self)->str:
        """
            Genera la contraseña 
        """
        return self.generator.generate_password()

    def evaluate_password(self, password: str):
        """ 
            Evalua la contraseña ingresada
        """
        return self.evaluator.evaluate(password)

    def security_profile(self, password: str) -> dict:
        """ 
            Muestra el perfil de seguridad de la contraseña ingresada
        """
        return self.evaluator.spc(password)    

    def check_password_history(self, password: str, history_file_path: str):
        """ 
        Este método verifica si la contraseña ingresada se repite en el archivo de contraseñas 
            args:
                password (str): Contraseña generada 
                history_file_path (str): Ruta del archivo de las contraseñas, historial
            return:
                Devuelve si la contraseña se encuentra en el archivo de contraseñas históricas
        """
        used_password = self.file_manager.read_file(history_file_path)
        
        # Asegúrate de que used_password sea una cadena vacía en lugar de None
        if used_password is None:
            used_password = ""
        
        return password in used_password.splitlines()


    

    def save_passwords_to_file(self, passwords: list, filename: str, dest_path: str = None):
        """ 
        Guarda las contraseñas en un archivo


        """
        content = "\n".join(passwords)
        self.file_manager.save_to_file(filename, content, dest_path)

    def generates_and_save_password(self, count_passwords: int, filename:str , dest_path: str = None):
        """ 
        Genera varias contraseñas y opcionalmente guarda las contraseñas en un archivo .txt.
        
        args:   
            count_passwords (int): Cantidad de contraseñas a generar
            filename (str): Nombre del archivo en el que se guardarán las contraseñas.
            save_in_file (bool): Si es True, guarda las contraseñas en un archivo.
            dest_path (str): Directorio donde se guardará el archivo 
        """
        passwords = [self.generate_password() for _ in range(count_passwords)]
        self.save_passwords_to_file(passwords,filename,dest_path)
        print(f"El archivo {filename} se ha generado exitosamente en {dest_path}")


    # metodos de seguridad
    def encrypt_passowrd(self,password):
        """
            Se encarga de encryptar la contraseña
            args:
                password(str): Contraseña especificada.
            return:
                Retorna la contraseña especificada encriptada
        """
        return self.encryptor.encrypt(password)

    def decrypt_password(self,ciphertext:str):
        """
            Se encarga de desencriptar la contraseña encriptada 
        """
        return self.encryptor.decrypt(ciphertext)

    def encrypt_password_file(self, file_path: str):
        """
        Encripta el contenido del archivo de contraseñas y guarda el resultado en un nuevo archivo.

        args:
            file_path (str): Ruta del archivo que contiene las contraseñas en texto plano.

        return:
            None
        """
        if not os.path.exists(file_path):
            raise FileNotFoundError(f"El archivo {file_path} no existe.")
        
        # Leer el contenido del archivo
        content_passwords = self.file_manager.read_file(file_path)
        
        # Encriptar cada contraseña
        encrypted_content = []
        for password in content_passwords:
            encrypted_content.append(self.encrypt_passowrd(password))
        
        # Nombre del nuevo archivo encriptado
        encrypted_filename = f"encrypted_{os.path.basename(file_path)}"
        
        # Guardar el contenido encriptado en un nuevo archivo
        encrypted_content_str = "\n".join(encrypted_content)
        self.file_manager.save_to_file(encrypted_filename, encrypted_content_str, dest_path=os.path.dirname(file_path))
        
        print(f"Las contraseñas han sido encriptadas y guardadas en {encrypted_filename}")


    


 
    