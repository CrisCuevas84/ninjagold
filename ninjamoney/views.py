from django.shortcuts import render, redirect
from random import randint
from datetime import datetime


def inicio(request):
    if 'gold_amount' not in request.session:    # Esta diciendo que si no está en la sesion, lo cree como cero
        request.session['gold_amount'] = 0 # Para guardar la cantidad de oro en sesión , podemos consultar la variable de sesión a nivel de vista
        request.session['moves'] = [] 
    return render(request, 'index.html')

def process_money(request):
    time = datetime.now().strftime("%Y-%m-%d %H:%M:%S %p")
    if "farm" in request.POST:  # Se pregunta si cuando se envio post, en el formulario va farm 
        farmPrize = randint(10, 20) # Dándolo un valor aleatorio entre 10 y 20
        request.session['gold_amount'] += farmPrize
        request.session['moves'].append([farmPrize , 'farm', time])

    if "cave" in request.POST: 
        cavePrize = randint(5, 10) 
        request.session['gold_amount'] += cavePrize
        request.session['moves'].append([cavePrize, 'cave', time])

    if "house" in request.POST:  
        housePrize = randint(2, 5) 
        request.session['gold_amount'] += housePrize
        request.session['moves'].append([housePrize, 'house', time])

    if "casino" in request.POST:   
        casinoPrize = randint(-50, 50) 
        request.session['gold_amount'] += casinoPrize
        request.session['moves'].append([casinoPrize, 'casino', time])      
    return redirect('/')
