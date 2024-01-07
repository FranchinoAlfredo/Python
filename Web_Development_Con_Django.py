# Importa il modulo HttpResponse da django.http
from django.http import HttpResponse
from django.urls import path
from django.shortcuts import render

# Importa il modulo django
from django.conf import settings

# Configura le impostazioni di Django
settings.configure(
    DEBUG=True,
    ROOT_URLCONF=__name__,
)

# Crea una vista per la homepage
def home(request):
    return HttpResponse('Benvenuto nella pagina principale!')

# Crea una vista per la pagina di informazioni
def info(request):
    return HttpResponse('Questa è una pagina di informazioni.')

# Crea una vista con un parametro dinamico
def saluta_utente(request, nome):
    return HttpResponse(f'Ciao, {nome}!')

# Definisci le URL dell'applicazione Django
urlpatterns = [
    path('', home),
    path('info/', info),
    path('utente/<str:nome>/', saluta_utente),
]

# Avvia l'applicazione Django
if __name__ == '__main__':
    from django.core import management

    # Esegui il comando di gestione di Django per avviare il server
    management.execute_from_command_line(['runserver'])
