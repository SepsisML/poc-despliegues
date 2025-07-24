FROM python:3.10.8

# Establecer el directorio de trabajo
WORKDIR /app

# Copiar e instalar dependencias
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copiar todo el código y el modelo
COPY . .

# Exponer el puerto
EXPOSE 80
# Como necesitamos hacer funcionar los imports de la aplicación
# entonces nos ubicamos en la carpeta padre "/" de app.
WORKDIR /
# Comando para iniciar FastAPI con Uvicorn
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "80"]