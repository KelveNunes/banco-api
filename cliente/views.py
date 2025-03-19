from django.shortcuts import render


def cliente(request):
    return render(request, 'cliente/cliente.html')

def forgotPassword(request):
    return render(request, 'cliente/forgotPassword.html')

def newUser(request):
    return render(request, 'cliente/newUser.html')