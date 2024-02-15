import os, time, string, random, re
import requests
import json
from random import randrange


def contar_chiste():
    """
    Cuenta un chiste de forma aleatoria

    :return El chiste que se va a contar
    :rtype str
    """
    chistes = [
        "Hay dos personas en un restaurante:\nX-Camarero, traigame una fanta de naranja\nM.-Lo siento señor, no nos queda Fanta, ¿Le va bien un Kas?\nX-Está bien.\nDespués de un rato, el camarero vulve con una fanta. ¿Cómo se llamó el videojuego? \nAl Final Fanta sí.\n",
        "¿Cuál es el mejor juego de terror de la Wii?\n La Wiija. XD XD XD",
        "Se abre el telón y sale Leonardo Dantés muy constipado. ¿Como se llama el videojuego? Dantés Enfermo.",
        'Esto es una consola de Nintendo sin juegos de Mario. ¿Cómo se llama la película?: "Misión imposible"',
        "Esto es una encuesta de a ver que boss de FF es mas difícil y gana artemisa.",
    ]
    chiste = random.choice(chistes)
    return chiste


def contar_funcionamiento():
    """
    Cuenta un funcionamiento de forma aleatoria

    :return El funcionamiento que se va a contar
    :rtype str
    """
    funcionamientos = [
        "Basicamente mi objetivo es darte recomendaciones y consejos sobre LOL",
        "Pues, mi funcion es ayudarte en lo que ocupes del lolsito",
        "Sirvo para facilitarte informacion de League of Legends ;)",
        "Pues, supongo que solo soy una ayuda para algo que necesites del GOAT juego",
    ]
    funcion = random.choice(funcionamientos)
    return funcion


def poner_musica():
    canciones = [
        "https://www.youtube.com/watch?v=kYtGl1dX5qI",
        "https://www.youtube.com/watch?v=fmI_Ndrxy14",
        "https://www.youtube.com/watch?v=C3GouGa0noM",
        "https://www.youtube.com/watch?v=F5tSoaJ93ac",
    ]
    cancion = random.choice(canciones)
    return cancion


def dar_hora():
    response = requests.get(
        "https://timeapi.io/api/Time/current/zone?timeZone=America/Mexico_City"
    )
    json_data = json.loads(response.text)
    hora = json_data["time"]
    return hora


def despedida(user_input):
    """
    Devuelve la despedida de glados

    :param str user_input: El texto escrito por el usuario
    :return La despedida de glados
    :rtype str
    """
    des = user_input.split()
    despedida_usuario = ["salir", "adios", "bye", "hasta luego", "adiós"]
    despedida_glados = ["Adiós", "Bye!", "¡Hasta la vista, baby!"]
    despedida_definitiva = ""
    for i in des:
        if i in des:
            despedida_definitiva = random.choice(despedida_glados)
    return despedida_definitiva
