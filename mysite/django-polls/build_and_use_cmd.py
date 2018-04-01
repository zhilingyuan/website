#build package cmd
python setup.py sdist
#install
pip install --user django-polls/dist/django-polls-0.1.tar.gz