from django.test import TestCase

# Create your tests here.
def app(environ,start_response):
    status='200 ok'  
    headers=[
        (Content_type'.'text/plain')
    ]
    return 'ura!'

