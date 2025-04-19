<!-- web: gunicorn --config gunicorn.conf.py gettingstarted.wsgi -->
web: sh setup.sh &amp;&amp; streamlit run StreamLitApp.py

# python3 -m venv --upgrade-deps .venv
# source .venv/bin/activate
# pip install -r requirements.txt

# python3 -m streamlit run StreamLitApp.py

# Uncomment this `release` process if you are using a database, so that Django's model
# migrations are run as part of app deployment, using Heroku's Release Phase feature:
# https://docs.djangoproject.com/en/5.2/topics/migrations/
# https://devcenter.heroku.com/articles/release-phase
# release: ./manage.py migrate --no-input
