# PassMaker

**PassMaker** es una herramienta para la generación, evaluación, encriptación y gestión de contraseñas. Diseñada para estudiantes y profesionales de informática que necesitan manejar contraseñas de manera segura y eficiente.

## Características

- **Generación de Contraseñas:** Crea contraseñas aleatorias con configuraciones personalizables.
- **Evaluación de Contraseñas:** Evalúa la fortaleza de las contraseñas generadas.
- **Encriptación de Contraseñas:** Utiliza cifrado RSA para mantener las contraseñas seguras.
- **Gestión de Contraseñas:** Guarda y encripta contraseñas, y verifica si ya están en el historial.

## Instalación

1. Clona el repositorio:

    ```bash
    git clone <URL_DEL_REPOSITORIO>
    ```

2. Navega al directorio del proyecto:

    ```bash
    cd PassMaker
    ```

3. Instala las dependencias necesarias:

    ```bash
    pip install -r requirements.txt
    ```

## Uso

### Ejemplo de Script para Generación y Gestión de Contraseñas

El script `main.py` demuestra cómo utilizar **PassMaker** para generar, evaluar, guardar y encriptar contraseñas. Aquí te muestro cómo usarlo:

```python
#!/usr/bin/env python3
import os
from genPass import GenPass

def main():
    # Configuración inicial
    length = int(input("Ingrese la longitud de las contraseñas: "))
    current_path = os.getcwd()
    history_file = 'password_history.txt'

    # Crear instancia de GenPass
    genpass = GenPass(length=length, current_path=current_path)

    # Generar una contraseña
    password = genpass.generate_passowrd()
    print(f"Contraseña generada: {password}")

    # Evaluar la contraseña
    evaluation = genpass.evaluate_password(password)
    print(f"Evaluación de la contraseña: {evaluation}")

    # Obtener perfil de seguridad
    profile = genpass.security_profile(password)
    print(f"Perfil de seguridad: {profile}")

    # Guardar la contraseña en un archivo
    filename = 'generated_passwords.txt'
    genpass.save_passwords_to_file([password], filename)
    print(f"Contraseña guardada en {filename}")

    # Encriptar el archivo de contraseñas
    genpass.encrypt_password_file(filename)
    print(f"Archivo de contraseñas encriptado.")

    # Para pruebas, lee el archivo encriptado y desencripta las contraseñas
    encrypted_filename = f"encrypted_{filename}"
    encrypted_content = genpass.file_manager.read_file(encrypted_filename)
    decrypted_passwords = [genpass.decrypt_password(enc_pwd) for enc_pwd in encrypted_content]
    
    print(f"Contraseñas desencriptadas: {decrypted_passwords}")

    # Verifica si la contraseña ya está en el historial
    password_exists = genpass.check_password_history(password, history_file)
    if password_exists:
        print("La contraseña ya existe en el historial.")
    else:
        print("La contraseña no está en el historial.")

