# ----------------------------------------------------------------------
# Base de conocimiento
# La base de conocimiento representa una lista de todos los casos o intents.
#
# Cada caso o intent es un diccionario que incluye los siguientes keys (propiedades):
# - intent: Nombre para identificar el intent
# - regex: Lista de posibles expresiones regulares asociadas al intent, donde los parámetros se obtienen del texto parentizado en la expresión regular
# - respuesta: Lista de posibles respuestas al usuario, indicando los parámetros obtenidos con la notación %1, %2, %3, etc para cada parámetro
# ----------------------------------------------------------------------
def conocimientoT():
    """
    Define la base de conocimiento de glados

    :return El conicimiento a mostrar
    :rtype str
    """
    conocimiento = [
        # ////////////////////////////////////////////////Bienvenida.
        {
            "intent": "bienvenida",
            "regex": [
                r".*hola.*",
                r".*buen(a|o)s (d(i|í)as|tardes|noches).*",
            ],
            "respuesta": ["Ah, Hola... ", "Hola, soy una IA de conversación."],
        },
        # ////////////////////////////////////////////////Chiste.
        {
            "intent": "chiste",
            "regex": [r".*chiste.*", r".*broma.*"],
            "respuesta": ["Bien", "Ahí te va"],
        },
        # ////////////////////////////////////////////////Chiste.
        {
            "intent": "estado",
            "regex": [
                r"^.*me siento (.*)$",
            ],
            "respuesta": ["Por que te sientes %1"],
        },
        # ////////////////////////////////////////////////Fin.
        {
            "intent": "terminar",
            "regex": [r".*salir.*", r".*adi(o|ó)s.*", r".*bye.*", r".*hasta luego.*"],
            "respuesta": [""],
        },
        # ////////////////////////////////////////////////Identificacion
        {
            "intent": "quien_eres",
            "regex": [r".*(qui(e|é)n).*(tu|tú).*", r".*(qui(e|é)n).*(eres).*"],
            "respuesta": [
                "Excelente pregunta, supongo que solo soy un bot especializado en LOL",
                "Alguien que esta aqui para ayudarte en lo que este relacionado con LOL",
                "Si, bueno esa es una buena pregunta, en resumidas cuentas soy un bot de LOL",
                "Pues me llamo Nexus AI:D",
            ],
        },
        # ////////////////////////////////////////////////musica
        {
            "intent": "musica",
            "regex": [
                r".*(pon|recomienda|dame|recomi(e|é)ndame).* (m(u|ú)sica|canci(o|ó)n|rola)"
            ],
            "respuesta": [
                "ahi te va esta rola",
                "esta es mi favorita",
                "chance esta te pueda gustar",
            ],
        },
        # ////////////////////////////////////////////////otro(musica)
        {
            "intent": "otro_musica",
            "regex": [r".*(pon|saca|dame).* otr(o|a).*", r".*otr(o|a)"],
            "respuesta": [
                "Aqui te dejo otra ",
                "Esta cancion es buena ",
                "va, tambien esta esta ",
            ],
        },
        # ////////////////////////////////////////////////Hora
        {
            "intent": "hora",
            "regex": [r".*\b(hora).*"],
            "respuesta": [
                "La hora perfecta para rankear es:  ",
                "Son las: ",
                "La hora para meterse al lolsito es: ",
            ],
        },
        # ////////////////////////////////////////////////otro(hora)
        {
            "intent": "otro_hora",
            "regex": [r".*(enseñamela|dimela|dime).* (de nuevo).*"],
            "respuesta": [
                "Sale pues, la hora es:",
                "La hora perfecta pa perder LP es:",
                "Pues la hora es:",
            ],
        },
        # ////////////////////////////////////////////////funcionamiento
        {
            "intent": "funcionamiento",
            "regex": [
                r".*(para qu(e|é)).*(sirves|funcionas)",
                r".*(cu(a|á)l).*(funci(o|ó)n|funciones|funcionalidad |objetivo)",
            ],
            "respuesta": [
                "Basicamente mi objetivo es darte recomendaciones y consejos sobre LOL",
                "Pues, mi funcion es ayudarte en lo que ocupes del lolsito",
                "Sirvo para facilitarte informacion de League of Legends ;)",
            ],
        },
        # ////////////////////////////////////////////////otro(funcionamiento)
        {
            "intent": "otro_funcionamiento",
            "regex": [r".*otr(a|o).*(funcionalidad|funcion|objetivo).*"],
            "respuesta": [""],
        },
        # ////////////////////////////////////////////////mascota favorita
        {
            "intent": "mascota",
            "regex": [
                r".*(tu mascota).*(favorita|preferida).*",
                r".*(tu animal).*(favorito|preferido).*",
                r".*(animal).*(mas|más).*(te gusta)",
            ],
            "respuesta": [
                "Mi mascota favorita es un Poro hacker para poder espiar estrategias enemigas!",
                "Mi mascota favorita es un Poro, son tan adorables!",
                "Mi animal favorito es un Poro hacker!",
            ],
        },
        # ////////////////////////////////////////////////consejo
        {
            "intent": "consejo",
            "regex": [
                r".*(recomendaci(o|ó)n|recomienda|recomi(é|e)ndame|consejo|recomendar).*(mejorar)*"
            ],
            "respuesta": [
                "Mi consejo para mejorar en el juego es practicar, aprender de cada derrota y ¡divertirse en la Grieta del Invocador!",
                "Diviértete explorando las habilidades de tus campeones favoritos. Cuanto más los conozcas, ¡mejor te irá en las partidas!",
                "No olvides echar un vistazo al minimapa. Saber dónde están tus aliados y enemigos es clave para tomar decisiones acertadas.",
                "Únete a tu equipo para conquistar dragones, torres y el barón Nashor. ¡Éstos objetivos son la clave de la victoria!",
                "Coloca wards para iluminar el mapa. Así podrás evitar sorpresas y emboscadas enemigas.",
                "No te rindas. Aprende de cada derrota y sigue adelante. ¡La próxima partida será mejor!",
            ],
        },
        {
            "intent": "agradecimiento",
            "regex": [r".*(gracias|agradecid(o|a)).*"],
            "respuesta": [
                "Me da gusto haber sido de ayuda",
                "De nada, para eso estoy",
                "No hay de qué, para eso estoy",
            ],
        },
        # ////////////////////////////////////////////////Cualquier caso no contemplado.
        {
            "intent": "desconocido",
            "regex": [r".*"],
            "respuesta": [
                "No te entendí ¿Puedes repetirlo por favor?",
                "Creo que no tengo información al respecto; lo siento",
                "Disculpa, no comprendí lo que dices",
            ],
        },
        # ////////////////////////////////////////////////
    ]
    return conocimiento
