# 1. Usar imagen base ligera oficial de Python 3.12
FROM python:3.12-slim

# 2. Establecer el directorio de trabajo dentro del contenedor
WORKDIR /app

# 3. Copiar las dependencias primero (para aprovechar la caché de Docker)
COPY requirements.txt .

# 4. Instalar dependencias
RUN pip install --no-cache-dir -r requirements.txt

# 5. Copiar el resto del código fuente
COPY . .

# 6. Crear un usuario no-root por seguridad y cambiar permisos (Requisito 2.e)
# Creamos un usuario llamado 'appuser'
RUN useradd -m appuser && chown -R appuser /app
# Cambiamos al usuario creado
USER appuser

# 7. Comando para iniciar la aplicación
# (Asegúrate de que 'main.py' sea el nombre de tu archivo principal)
CMD ["python", "main.py"]
