
# goto web app root

cd ~/Prog/SmartReceipt/smartreceipt

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
cd ~/Prog/SmartReceipt/smartreceipt/data/
python ../manage.py makemessages -l de -e html,txt -e xml
python ../manage.py compilemessages

Links
# http://chefville.wikia.com/wiki/Ingredient
# http://docs.python-guide.org/en/latest/dev/virtualenvs/

# VirtualEnv
cd /Users/mrommel/Prog/SmartReceipt/smartreceipt
source venv/bin/activate
deactivate

# install something - keep it
pip freeze > requirements.txt

# install requirements
pip install -r requirements.txt

# admin password
admin + forrecipe