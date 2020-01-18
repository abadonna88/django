from django.http import HttpResponse


def index(requests):
    return HttpResponse("YOBA. YOUR IN RESPONSE INDEX")
