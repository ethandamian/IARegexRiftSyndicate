import os, time, string, random, re
import requests
import json
from random import randrange
from champion import *


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


def extraer_nombre_campeon(cadena):
    patron = r"\b(?:Aatrox|Ahri|Akali|Akshan|Alistar|Amumu|Anivia|Annie|Aphelios|Ashe|AurelionSol|Azir|Bard|Belveth|Blitzcrank|Brand|Braum|Briar|Caitlyn|Camille|Cassiopeia|Chogath|Corki|Darius|Diana|Draven|DrMundo|Ekko|Elise|Evelynn|Ezreal|Fiddlesticks|Fiora|Fizz|Galio|Gangplank|Garen|Gnar|Gragas|Graves|Gwen|Hecarim|Heimerdinger|Hwei|Illaoi|Irelia|Ivern|Janna|JarvanIV|Jax|Jayce|Jhin|Jinx|Kaisa|Kalista|Karma|Karthus|Kassadin|Katarina|Kayle|Kayn|Kennen|Khazix|Kindred|Kled|KogMaw|KSante|Leblanc|LeeSin|Leona|Lillia|Lissandra|Lucian|Lulu|Lux|Malphite|Malzahar|Maokai|MasterYi|Milio|MissFortune|MonkeyKing|Mordekaiser|Morgana|Naafiri|Nami|Nasus|Nautilus|Neeko|Nidalee|Nilah|Nocturne|Nunu|Olaf|Orianna|Ornn|Pantheon|Poppy|Pyke|Qiyana|Quinn|Rakan|Rammus|RekSai|Rell|Renata|Renekton|Rengar|Riven|Rumble|Ryze|Samira|Sejuani|Senna|Seraphine|Sett|Shaco|Shen|Shyvana|Singed|Sion|Sivir|Skarner|Smolder|Sona|Soraka|Swain|Sylas|Syndra|TahmKench|Taliyah|Talon|Taric|Teemo|Thresh|Tristana|Trundle|Tryndamere|TwistedFate|Twitch|Udyr|Urgot|Varus|Vayne|Veigar|Velkoz|Vex|Vi|Viego|Viktor|Vladimir|Volibear|Warwick|Xayah|Xerath|XinZhao|Yasuo|Yone|Yorick|Yuumi|Zac|Zed|Zeri|Ziggs|Zilean|Zoe|Zyra)\b"
    match = re.search(patron, cadena, re.IGNORECASE)
    if match:

        return match.group(0)
    else:
        return None


def dar_champion_info(champ):
    # champ_name = extraer_nombre_campeon(champ)
    champ_file = champ + ".json"  # Nombre del archivo basado en el nombre del campeón
    champ_path = os.path.join(
        "champion", champ_file
    )  # Ruta relativa al directorio actual

    if os.path.exists(champ_path):
        with open(champ_path, "r", encoding="utf-8") as f:
            champ_data = json.load(f)
            lore = champ_data["data"][champ]["lore"]
            return lore
    else:
        return "No se encontró información para este campeón."


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
    hora = json_data["name"]
    return hora

def dar_recomendacion():
    consejos = [
            "Para mejorar en el juego debes practicar, aprender de cada derrota y ¡divertirse en la Grieta del Invocador!",
            "Diviértete explorando las habilidades de tus campeones favoritos. Cuanto más los conozcas, ¡mejor te irá en las partidas!",
            "No olvides echar un vistazo al minimapa. Saber dónde están tus aliados y enemigos es clave para tomar decisiones acertadas.",
            "Únete a tu equipo para conquistar dragones, torres y el barón Nashor. ¡Éstos objetivos son la clave de la victoria!",
            "Coloca wards para iluminar el mapa. Así podrás evitar sorpresas y emboscadas enemigas.",
            "No te rindas. Aprende de cada derrota y sigue adelante. ¡La próxima partida será mejor!",
            ]
    return random.choice(consejos)

def linea_superior():
    return "Línea superior: Está situada en la parte superior del mapa. Sin importar si estás del lado azul (con tu base abajo a la izquierda) o en el lado rojo (con tu base arriba a la derecha), esta línea siempre será la superior. Los jugadores en la línea superior suelen decir que es una isla, ya que estos campeones reciben la menor cantidad de ayuda de las otras líneas a través del juego."
    
def jungla():
    return "Jungla: La jungla es el área entre las líneas de la parte superior, media e inferior del mapa. Los jugadores que eligen campeones de jungla no se quedan en una línea, sino que se mueven por la jungla, matando monstruos y ayudando a sus compañeros de equipo en las líneas. Los jugadores de jungla son conocidos por ser los que más ayudan a sus compañeros de equipo a lo largo del juego."
    
def linea_del_medio():
    return "Línea del medio: La línea del medio está situada en el centro del mapa. Los jugadores en la línea del medio suelen ser campeones que tienen habilidades de ataque a distancia o habilidades que les permiten moverse rápidamente por el mapa. Los jugadores de la línea del medio suelen ser los que más daño infligen a lo largo del juego."
    
def linea_inferior():
    return "Línea inferior: La línea inferior está situada en la parte inferior del mapa. Los jugadores en la línea inferior suelen ser campeones que tienen habilidades de ataque a distancia o habilidades que les permiten curar a sus compañeros de equipo. Los jugadores de la línea inferior suelen ser los que más daño infligen a lo largo del juego."
    


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
