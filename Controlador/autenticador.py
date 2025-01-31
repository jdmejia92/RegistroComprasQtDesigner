import os

# Ruta del archivo de usuarios
ARCHIVO_USUARIOS = "usuarios.txt"

def crear_archivo_usuarios():
    """Crea el archivo de usuarios con el usuario admin por defecto si no existe."""
    if not os.path.exists(ARCHIVO_USUARIOS):
        with open(ARCHIVO_USUARIOS, "w", encoding="utf-8") as archivo:
            archivo.write("admin,admin\n")
        print(f"Archivo {ARCHIVO_USUARIOS} creado con el usuario 'admin' y contraseña 'admin'.")

def cargar_usuarios():
    """Carga los usuarios y contraseñas desde el archivo."""
    usuarios = {}
    with open(ARCHIVO_USUARIOS, "r", encoding="utf-8") as archivo:
        for linea in archivo:
            usuario, clave = linea.strip().split(",")
            usuarios[usuario] = clave
    return usuarios

def autenticar_usuario(usuario, clave):
    """Autentica al usuario."""
    usuarios = cargar_usuarios()
    if usuario in usuarios and usuarios[usuario] == clave:
        return True
    return False

def agregar_usuario(usuario, clave):
    """Agrega un nuevo usuario al archivo."""
    with open(ARCHIVO_USUARIOS, "a", encoding="utf-8") as archivo:
        archivo.write(f"{usuario},{clave}\n")
    print(f"Usuario '{usuario}' agregado correctamente.")

# Crear el archivo de usuarios si no existe
crear_archivo_usuarios()

# Ejemplo de uso
if __name__ == "__main__":
    # Autenticar al usuario
    usuario = input("Usuario: ")
    clave = input("Contraseña: ")

    if autenticar_usuario(usuario, clave):
        print("¡Autenticación exitosa!")
    else:
        print("Usuario o contraseña incorrectos.")

    # Agregar un nuevo usuario (opcional)
    nuevo_usuario = input("¿Desea agregar un nuevo usuario? (s/n): ").lower()
    if nuevo_usuario == "s":
        nuevo_usuario = input("Nuevo usuario: ")
        nueva_clave = input("Nueva contraseña: ")
        agregar_usuario(nuevo_usuario, nueva_clave)