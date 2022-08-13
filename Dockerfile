# usamos una imagen existente compatible con versiones de python
FROM tiangolo/uwsgi-nginx-flask:python3.8
# creamos un directorio de trabajo build_context
RUN mkdir /application
WORKDIR /application
# copiamos el archivo y lo pegamos en el directorio build_context
COPY ./requirements.txt /application
RUN python3 -m pip install -r requirements.txt
COPY . /application
EXPOSE 5000
# Run Flask command
CMD ["gunicorn", "-b", "0.0.0.0:5000", "wsgi:app"]
