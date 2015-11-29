
# goto web app root

cd ~/Prog/SmartReceipt/smartreceipt

# run web server

python manage.py runserver

# data migration

python manage.py makemigrations data
python manage.py sqlmigrate data 0002
python manage.py migrate

# translations

cd ~/Prog/SmartReceipt/smartreceipt/data/
python ../manage.py makemessages -l de -e html,txt -e xml
python ../manage.py compilemessages



# http://chefville.wikia.com/wiki/Ingredient