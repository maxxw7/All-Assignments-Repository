import django.http


def homePageView(request):
    return django.http.HttpResponse("Hello, World!")