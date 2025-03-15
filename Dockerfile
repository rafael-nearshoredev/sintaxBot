# Usar Python 3.12
FROM python:3.12

# Definir directorio de trabajo
WORKDIR /app

# Copiar los archivos necesarios
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Descargar modelo de spaCy
RUN python -m spacy download es_core_news_sm

# Copiar el código de la app
COPY app/ app/

# Exponer el puerto 8000
EXPOSE 8000

# Comando para correr la aplicación
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]