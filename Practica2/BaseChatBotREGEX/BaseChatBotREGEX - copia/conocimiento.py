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
        # ////////////////////////////////////////////////musica
        {
            "intent": "musica",
            "regex": [r".*(pon|recomienda)+ (musica)"],
            "respuesta": [
                "ahi te va",
                "esta es mi favorita",
            ],
        },
        # ////////////////////////////////////////////////otro
        {
            "intent": "otro",
            "regex": [r"(pon|saca|dame).* otro"],
            "respuesta": ["Aqui te dejo otra"],
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
