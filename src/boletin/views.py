from django.shortcuts import render
from .forms import RegModelForm, ContactForm
from .models import Registrado

# Create your views here.

def inicio(request):
	titulo = "HOLA"
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
		for key, value in form.cleaned_data.items():
			print (key, value)
		#for key in form.cleaned_data:
		#	print (key)
		#	print(form.cleaned_data.get(key))
		#nombre = form.cleaned_data.get("nombre")
		#email = form.cleaned_data.get("email")
		#mensaje = form.cleaned_data.get("mensaje")
		#print(email, mensaje, nombre)
	context = {
		"form": form,
	}
	return render(request, "forms.html", context)