# usamos una imagen existente compatible con versiones de python
FROM tiangolo/uwsgi-nginx-flask:python3.8
# creamos un directorio de trabajo build_context
RUN mkdir /application
WORKDIR /application
# copiamos el archivo y lo pegamos en el directorio build_context
COPY ./requirements.txt /application
RUN python3 -m pip install -r requirements.txt
COPY . /application
EXPOSE 4000
# Run Flask command
CMD gunicorn --worker-class --workers 8 --bind 0.0.0.0:4000 wsgi:app --max-requests 10000 --timeout 5 --keep-alive 5 --log-level info
#CMD ["gunicorn", "-b", "0.0.0.0:4000", "wsgi:app"]
