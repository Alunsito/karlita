from django.shortcuts import render
from django.core.mail import send_mail
from django.conf import settings

from .forms import RegModelForm, ContactForm
from .models import Registrado

# Create your views here.

def inicio(request):
	titulo = "Bienvenidos"
	abc = "123"
	if request.user.is_authenticated:
		titulo = "Bienvenido %s" %(request.user)
	form = RegModelForm(request.POST or None)

	context = {
		"abc": abc,
		"titulo": titulo,
		"el_form" : form,
	}

	if form.is_valid():
		instance = form.save(commit=False)
		if not instance.nombre:
			instance.nombre = "Usuario"
		instance.save()

		context = {
			"titulo": "Gracias por registrarte %s!" %(instance.nombre)
		}

		print (instance)
		print (instance.timestamp)
		#form_data = form.cleaned_data
		#abc = form_data.get("email")
		#abc2 = form_data.get("nombre")
		#obj = Registrado.objects.create(email=abc, nombre=abc2)
	
	return render (request, "inicio.html", context)

def contact(request):
	form = ContactForm(request.POST or None)
	if form.is_valid():
		#for key, value in form.cleaned_data.items():
		#	print (key, value)
		#for key in form.cleaned_data:
		#	print (key)
		#	print(form.cleaned_data.get(key))
		form_nombre = form.cleaned_data.get("nombre")
		form_email = form.cleaned_data.get("email")
		form_mensaje = form.cleaned_data.get("mensaje")
		asunto = 'Formulario de Contacto'
		email_from = settings.EMAIL_HOST_USER
		email_to = [email_from, "test@gmail.com"]
		mensaje_email = "%s: %s enviado por %s" %(form_nombre, form_mensaje, form_email)
		#print(email, mensaje, nombre)
		send_mail(asunto,
			mensaje_email,
			email_from,
			[email_to],
			fail_silently=False
			)
	context = {
		"form": form,
	}
	return render(request, "forms.html", context)