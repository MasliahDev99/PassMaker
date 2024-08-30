#!/usr/bin/env python3

import os

class File:
    def __init__(self, current_path: str):
        """ 
        Inicializa una instancia para manejar archivos en una ruta específica.
        
        args:
            current_path (str): La ruta del directorio en el que trabajará la instancia.
        
        raises:
            ValueError: Si la ruta proporcionada no existe.
        """
        if os.path.exists(current_path):
            self.current_path = current_path
        else:
            raise ValueError(f"\n[!] Error: La ruta especificada no existe: {current_path}")

    def save_to_file(self, filename: str, content, dest_path: str = None):
        """ 
        Crea un archivo con el nombre y contenido especificados.
        
        args:
            filename (str): El nombre del archivo que deseas crear.
            content  El contenido que quieres escribir en el archivo.
            dest_path (str, opcional): La ruta donde se guardará el archivo. Si no se especifica, se guardará en la ruta actual.
        
        return:
            None: Crea el archivo en la ruta especificada o en la ruta actual si no se proporciona una ruta de destino.
        
        raises:
            FileNotFoundError: Si la ruta especificada para guardar el archivo no es válida.
        """
        #si no tiene extencion .txt se lo agregamos por defecto
        if not filename.lower().endswith('.txt'):
            filename += '.txt'

        # Define la ruta completa del archivo
        if dest_path:
            full_path = os.path.join(dest_path, filename)
        else:
            full_path = os.path.join(self.current_path, filename)
        
        # Crea o sobrescribe el archivo en la ruta especificada
        
        try:
            with open(full_path, 'w') as file:
                file.write(content)
            print(f"\n[+] El archivo '{filename}' se ha guardado en '{full_path}' exitosamente.")
        except Exception as e:
            raise FileNotFoundError(f"\n[!] Error al intentar guardar el archivo en la ruta {full_path}: {e}")
    
    def read_file(self,file_path)->str:
        """ 
        """
        try:
            if os.path.exists(file_path):
                with open(file_path,'r',encoding='utf-8') as file:
                    file_ = file.read().splitlines()
                return file_
        except FileNotFoundError as f:
            print(f)

