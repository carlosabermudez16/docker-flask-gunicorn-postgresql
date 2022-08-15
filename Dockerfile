# usamos una imagen existente compatible con versiones de python
FROM python:3
# creamos un directorio de trabajo build_context
RUN mkdir /application
WORKDIR /application
# copiamos el archivo y lo pegamos en el directorio build_context
COPY ./requirements.txt /application
RUN pip install --upgrade pip
RUN python3 -m pip install -r requirements.txt
COPY . /application
# Run Flask command
CMD ["gunicorn", "-b", "0.0.0.0:5000","--log-level=debug", "wsgi:app"]
