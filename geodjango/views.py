from django.shortcuts import render
from django.core.mail import send_mail
from django.conf import settings
from sitedesvins.models import Commande

def home(request):
    return render(request, 'home.html')


def carte(request):
    return render(request, 'pages/carte.html')


def map(request):
    return render(request, 'pages/map.html')


def service(request):

    return render(request, 'pages/service.html')

def ask_service(request):

    print("Salut, votre commande a été prise en compte.")
    message = request.POST.get("message")
    mail = request.POST.get("mail")
    passw = request.POST.get("passw")
    
    
    
    commande = Commande(mail=mail, passw=passw, message=message)

    commande.save()

    if request.method == 'POST':
       
        mail = request.POST['mail']

        send_mail('Votre commande de banane', 'Votre demande a bien été enrégistrée. Merci et à bientôt !', settings.EMAIL_HOST_USER, [mail], fail_silently=False)

    return render(request, 'pages/service.html')


def stat(request):

    if request.method == 'POST':
        
        mail = request.POST['mail']

        send_mail('Votre commande de banane', 'Votre demande a bien été enrégistrée. Merci et à bientôt !', settings.EMAIL_HOST_USER, [mail], fail_silently=False)

    return render(request, 'pages/stat.html')