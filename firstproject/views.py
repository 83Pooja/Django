from django.http import HttpResponse,render

def aboutUs(request):
    return  HttpResponse("welcome to Wscubetech")


def courseUs(request):
    return  HttpResponse("welcome to Wscubetech1")

def courseDetails(request,courseid):
    return  HttpResponse("courseid")

def hello(request):
    return render(request,'hello.html')

