import requests, json
from django.shortcuts import render
from django.core.mail import EmailMessage

def Index(request):
    return render(request, 'index.html')

def Contact(request):
    context = {'message': '', 'success': False}
    name = request.POST.get("name", None)
    email = request.POST.get("email", None)
    comments = request.POST.get("comments", None)
    captcha_token = request.POST.get("captcha_token", None)

    if not name:
        context['message'] = 'Debes completar el campo de nombre'
    
    if not email:
        if not context['message']:
            context['message'] = 'Debes completar el campo de nombre'

    if not comments:
        if not context['message']:
            context['message'] = 'Debes completar el campo de nombre'

    if not captcha_token:
        if not context['message']:
            context['message'] = 'Solicitud invalida'
    else:
        #Validate token
        url = 'https://www.google.com/recaptcha/api/siteverify'
        data = {'secret': '6Ld4CDQgAAAAAFgr9VxdulH9KjtpRYO7RlcT_cFO', 'response': captcha_token}

        captcha_validation = requests.post(url, data = data)

        if captcha_validation.status_code == 200:
            validation_response = json.loads(captcha_validation.content)
            
            if not validation_response['success']:
                context['message'] = 'Solicitud invalida'

        else:
            context['message'] = 'Solicitud invalida'


    if not context['message']:
        try:
            EmailMessage('Patricio Carestia - ' + email, 'Mensaje de: ' + name + '\nDescripcion: ' +comments, to=['patriciocarestia@gmail.com']).send()
            
            context['success'] = True
            context['message'] = 'Mensaje enviado con éxito, te responderé a la brevedad.'

        except Exception as e:
            context['message'] = 'No se ha podido enviar el mensaje, por favor, vuelve a intentar'

    return render(request, 'index.html', context)