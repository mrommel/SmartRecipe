
# goto web app root

cd ~/Prog/SmartRecipe/smartrecipe

# run web server

workon venv
./start.sh start 
./start.sh restart
./start.sh stop
deactivate

# data migration
python manage.py makemigrations data
python manage.py sqlmigrate data 0002
python manage.py migrate

# translations
cd ~/Prog/SmartReceipt/smartrecipe/data/
python ../manage.py makemessages -l de -e html,txt -e xml
python ../manage.py compilemessages

# Links
- http://chefville.wikia.com/wiki/Ingredient
- http://docs.python-guide.org/en/latest/dev/virtualenvs/
- http://www.django-rest-framework.org/

# VirtualEnv
// cd ~/Prog/SmartRecipe/smartrecipe
// source venv/bin/activate
// deactivate

# install something - keep it
pip3 freeze > requirements.txt

# install requirements
pip3 install -r requirements.txt

# admin password
admin + forrecipe