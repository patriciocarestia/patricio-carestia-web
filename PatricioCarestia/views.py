from django.shortcuts import render
from django.core.mail import EmailMessage

def Index(request):
    return render(request, 'index.html')

def Contact(request):
    context = {'message': ''}
    name = request.POST.get("name", None)
    email = request.POST.get("email", None)
    comments = request.POST.get("comments", None)

    if not name:
        context['message'] = 'Debes completar el campo de nombre'
    
    if not email:
        if not context['message']:
            context['message'] = 'Debes completar el campo de nombre'

    if not comments:
        if not context['message']:
            context['message'] = 'Debes completar el campo de nombre'

    if not context['message']:
        try:
            EmailMessage('Patricio Carestia - ' + email, 'Mensaje de: ' + name + '\nDescripcion: ' +comments, to=['patriciocarestia@gmail.com']).send()
            
            context['message'] = 'Mensaje enviado con éxito, te responderé a la brevedad.'
        except Exception as e:
            print(str(e))
            context['message'] = 'No se ha podido enviar el mensaje, por favor, vuelve a intentar'

    return render(request, 'index.html', context)

def Avanz(request):
    return render(request, 'avanz.html')

def Reader(request):
    return render(request, 'reader.html')

def Pet(request):
    return render(request, 'pet.html')

def Giveaway(request):
    return render(request, 'giveaway.html')