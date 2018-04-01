#simulate a user interacting with the code at view level
#we could use in the test.py or in the python manage.py shell
from django.test.utils import setup_test_environment
setup_test_environment()

from django.test import Client
client=Client()

#with that ready we ask client do follow work
response=client.get('/')
response.status_code

#and
from django.urls import reverse
response=client.get(reverse('polls:index'))
response.status_code
response.content
response.context['latest_question_list']

