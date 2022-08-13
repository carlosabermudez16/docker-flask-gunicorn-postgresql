----------------------------------------
vue init webpack frontend
npm install axios --save
npm install bootstrap-vue --save
----------------------------------------
pip freeze > requirements.txt

flask run --cert=adhoc --> para https
----------------------------------------
flask db init --> se ejecuta una única vez
flask db migrate -m "initial database" --> realiza la modificación en la base de datos
flask db upgrade --> cada vez que hay un cambio en el modelo
set FLASK_APP = wsgi:app
flask run
----------------------------------------
despliegue:
heroku login
heroku git:remote -a dashboard-intro
git push heroku main
heroku logs --tail
----------------------------------------
usando docker

