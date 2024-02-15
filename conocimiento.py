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
                r".*buen(a|o)s (dias|tardes|noches).*",
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
            "regex": [r".*salir.*", r".*adios.*", r".*bye.*", r".*hasta luego.*"],
            "respuesta": [""],
        },
        # ////////////////////////////////////////////////Identificacion
        {
            "intent": "quien_eres",
            "regex": [r".*(quien).*(tu).*", r".*(quien).*(eres).*"],
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
            "regex": [r".*(pon|recomienda| dame|recomiendame ).* (musica)"],
            "respuesta": [
                "ahi te va esta rola",
                "esta es mi favorita",
                "chance esta te pueda gustar",
            ],
        },
        # ////////////////////////////////////////////////otro(musica)
        {
            "intent": "otro_musica",
            "regex": [r".*(pon|saca|dame).* otro.*"],
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
                "Yo digo que %1 es al hora excelente para rankear: ",
            ],
        },
        # ////////////////////////////////////////////////otro(hora)
        {
            "intent": "otro_hora",
            "regex": [r".*(enseñamela|dimela|dime).* (de nuevo).*"],
            "respuesta": [
                "Sale pues, la hora es %1",
                "La hora perfecta pa perder LP es %1",
                "Pues la hora es %1",
            ],
        },
        # ////////////////////////////////////////////////funcionamiento
        {
            "intent": "funcionamiento",
            "regex": [
                r".*(para que).*(sirves|funciones)",
                r".*(cual).*(funcion|funciones|funcionalidad |objetivo)",
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
