from django.http import HttpResponse

def aboutUs(request):
    return  HttpResponse("welcome to Wscubetech")


def courseUs(request):
    return  HttpResponse("welcome to Wscubetech1")

def courseDetails(request,courseid):
    return  HttpResponse("courseid")
