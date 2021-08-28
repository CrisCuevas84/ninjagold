from django.shortcuts import render, redirect
from random import randint


def inicio(request):
    if 'gold_amount' not in request.session:    # Esta diciendo que si no está en la sesion, lo cree como cero
        request.session['gold_amount'] = 0 # Para guardar la cantidad de oro en sesión , podemos consultar la variable de sesión a nivel de vista
    return render(request, 'index.html')

def process_money(request):
    if "farm" in request.POST:  # Se pregunta si cuando se envio post, en el formulario va farm 
        farmPrize = randint(10, 20) # Dándolo un valor aleatorio entre 10 y 20
        request.session['gold_amount'] += farmPrize

    if "cave" in request.POST: 
        cavePrize = randint(5, 10) 
        request.session['gold_amount'] += cavePrize

    if "house" in request.POST:  
        housePrize = randint(2, 5) 
        request.session['gold_amount'] += housePrize

    if "casino" in request.POST:   
        casinoPrize = randint(-50, 50) 
        request.session['gold_amount'] += casinoPrize
    return redirect('/')
