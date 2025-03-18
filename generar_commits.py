import os
import subprocess
from datetime import datetime, timedelta

# Configuración de GitHub
GIT_NAME = "aviescobar"
GIT_EMAIL = "aviescobar1710@gmail.com"
REPO_PATH = "/home/avi/Documentos/Git/"  # Ruta de tu repo local

# Rango de fechas: 22 de diciembre de 2024 al 20 de enero de 2025
start_date = datetime(2024, 12, 22)  # Fecha de inicio
end_date = datetime(2025, 1, 20)     # Fecha final

# Acceder al repositorio
os.chdir(REPO_PATH)

# Configurar usuario de Git
subprocess.run(["git", "config", "user.name", GIT_NAME])
subprocess.run(["git", "config", "user.email", GIT_EMAIL])

# Generar commits en el rango de fechas
current_date = start_date
while current_date <= end_date:
    fecha_str = current_date.strftime("%Y-%m-%d %H:%M:%S")
    
    # Crear o modificar un archivo
    with open("actividad.txt", "a") as f:
        f.write(f"Commit en {fecha_str}\n")
    
    # Agregar y hacer commit con la fecha específica
    subprocess.run(["git", "add", "actividad.txt"])
    subprocess.run(["git", "commit", "--date", fecha_str, "-m", f"Commit en {fecha_str}"])
    
    # Avanzar al siguiente día
    current_date += timedelta(days=1)

# Subir los cambios a GitHub
subprocess.run(["git", "push", "origin", "main"])  # Cambia "main" por "master" si es necesario

print("✅ ¡Commits generados y subidos con éxito!")
