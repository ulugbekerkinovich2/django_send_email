import datetime

from django.core.mail import BadHeaderError, send_mail
from django.http import HttpResponse, HttpResponseRedirect


from django.core.mail import send_mail
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

from send_email import settings

@csrf_exempt
def send_email(request):
    data = request.POST.get('data', '')
    subject = f'Hello, World! {data}'
    message = str(datetime.datetime.now())
    from_email = settings.EMAIL_HOST_USER
    recipient_list = ['ulugbek9015u@gmail.com']
    print('data', data)
    send_mail(subject, message, from_email, recipient_list,
              fail_silently=False)
    return HttpResponse('Email sent successfully!')

