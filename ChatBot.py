# ------------------------------------------------#
#  ChatBot.py                                     #
# ------------------------------------------------#

import string, re, random, sys
from conocimiento import conocimientoT
from ResponseFunctions import (
    contar_chiste,
    contar_funcionamiento,
    dar_hora,
    despedida,
    extraer_nombre_campeon,
    muestra_cinematica,
    muestra_quiz_campeon,
    poner_musica,
    dar_champion_info,
    dar_recomendacion,
    linea_superior,
    jungla,
    linea_del_medio,
    linea_inferior,
    contar_historia,
    regiones,
    quizes
)


class ChatBot:
    """
    Clase ChatBot para simular una conversación
    sobre videojuegos
    """

    contexto = "DEFAULT"
    entrada = ""

    def __init__(self):
        """
        ChatBot consta de una base de conocimiento
        representada como una lista de casos o intents.
        """
        self.conocimiento = (
            []
        )  # agarra un diccionario de conocimiento.py, y por cada caso se toma la llave regex
        for caso in conocimiento:
            caso["regex"] = list(
                map(lambda x: re.compile(x, re.IGNORECASE), caso["regex"])
            )
            self.conocimiento.append(caso)

    def responder(self, user_input):
        """
        Flujo básico para identificar coincidencias de intents para responder al usuario.
        Con el texto del usuario como parámetro, los paso a realizarse son:
        1. Encontrar el caso de la base de conocimiento usando expresiones regulares
        2. Si es necesario, realizar acciones asociadas al intent (por ejemplo: consultar información adicional)
        3. Seleccionar una respuesta de la lista de respuestas según el caso del intent
        4. Si es necesario, identificar los parámetros o entidades del texto para dar formato a la respuesta seleccionada
        5. Devolver la respuesta

        :param str user_input: El texto escrito por el usuario
        :return Un texto de respuesta al usuario
        :rtype: str
        """
        caso = self.encontrar_intent(user_input)
        self.identifica_contexto(caso)
        informacion_adicional = self.acciones(caso, user_input)
        respuesta = self.convertir_respuesta(
            random.choice(caso["respuesta"]), caso, user_input
        )
        respuesta_final = (respuesta + "\n" + informacion_adicional).strip()
        return respuesta_final

    def encontrar_intent(self, user_input):
        """
        Encuentra el caso o intent asociado en la base de conocimiento

        :param str user_input: El texto escrito por el usuario
        :return El diccionario que representa el caso o intent deseado
        :rtype: str
        """
        for caso in self.conocimiento:
            for regularexp in caso["regex"]:
                match = regularexp.match(user_input)
                if match:
                    self.regexp_selected = regularexp
                    return caso
        return {}

    def identifica_contexto(self, caso):
        """
        Asegura que el contexto sea el adecuado para que
        ChatBot responde de manera coherente

        :param dict caso: El intent del cual se solicita información
        """
        intent = caso["intent"]
        if intent == "bienvenida":
            self.contexto = "BIENVENIDA"
        elif intent == "saludo":
            self.contexto = "SALUDO"
        elif intent == "que_haces":
            self.contexto = "QUE_HACES"
        elif intent == "chiste":
            self.contexto = "CHISTE"
        elif intent == "musica":
            self.contexto = "MUSICA"
        elif intent == "quien_eres":
            self.contexto = "QUIEN_ERES"
        elif intent == "hora":
            self.contexto = "HORA"
        elif intent == "champion_lore":
            self.contexto = "CHAMPION_LORE"
        elif intent == "funcionamiento":
            self.contexto = "FUNCIONAMIENTO"
        elif intent == "mascota":
            self.contexto = "MASCOTA"
        elif intent == "consejo":
            self.contexto = "CONSEJO"
        elif intent == "rol_mas_popular":
            self.contexto = "ROL_MAS_POPULAR"
        elif intent == "sistema_de_clasificacion":
            self.contexto = "SISTEMA_DE_CLASIFICACION"
        elif intent == "grieta_del_invocador":
            self.contexto = "GRIETA_DEL_INVOCADOR"
        elif intent == "lineas":
            self.contexto = "LINEAS"
        elif intent == "linea_superior":
            self.contexto = "LINEA_SUPERIOR"
        elif intent == "jungla":
            self.contexto = "JUNGLA"
        elif intent == "linea_del_medio":
            self.contexto = "LINEA_MEDIA"
        elif intent == "linea_inferior":
            self.contexto = "LINEA_INFERIOR"
        elif intent == "agradecimiento":
            self.contexto = "AGRADECIMIENTO"
        elif intent == "historia":
            self.contexto = "HISTORIA"
        elif intent == "region":
            self.contexto = "REGION"
        # INICIA PARTE ROGER
        elif intent == "preferencia_campeon":
            self.contexto = "PREFERENCIA_CAMPEON"
        elif intent == "preferencia_posicion":
            self.contexto = "PREFERENCIA_POSICION"
        elif intent == "numero_campeones":
            self.contexto = "NUMERO_CAMPEONES"
        elif intent == "consejos_farmeo":
            self.contexto = "CONSEJOS_FARMEO"
        elif intent == "muestra_cinematica":
            self.contexto = "MUESTRA_CINEMATICA" 
        elif intent == "que_campeon_soy":
            self.contexto = "QUE_CAMPEON_SOY"    
        # FINALIZA PARTE ROGER
        elif intent == "quiz":
            self.contexto = "QUIZ"
        elif intent == "ok":
            self.contexto = "OK"
        elif intent == "no":
            self.contexto = "NO"
        elif intent == "desconocido":
            self.contexto = "DEFAULT"

    def convertir_respuesta(self, respuesta, caso, user_input):
        """
        Cambia los textos del tipo %1, %2, %3, etc., por su correspondiente propiedad
        identificada en los grupos parentizados de la expresión regular asociada.

        :param str respuesta: Una respuesta que desea convertirse
        :param dict caso: El caso o intent asociado a la respuesta
        :param str user_input: El texto escrito por el usuario
        :return La respuesta con el cambio de parámetros
        :rtype: str
        """
        respuesta_cambiada = respuesta
        intent = caso["intent"]
        match = self.regexp_selected.match(user_input)
        if intent == "estado":
            respuesta_cambiada = respuesta_cambiada.replace("%1", match.group(1))
        return respuesta_cambiada

    def acciones(self, caso, user_input):
        """
        Obtiene información adicional necesaria para dar una respuesta coherente al usuario.
        El tipo de acciones puede ser una consulta de información, revisar base de datos, generar
        un código, etc. y el resultado final es expresado como una cadena de texto

        :param dict caso: El caso o intent asociado a la respuesta
        :return Texto que representa información adicional para complementar la respuesta al usuario
        :rtype: str
        """
        intent = caso["intent"]
        if intent == "chiste":
            return contar_chiste()
        elif intent == "musica":
            return poner_musica()
        elif intent == "otro_musica":
            return self.da_respuesta_apropiada(user_input)
        elif intent == "otro_hora":
            return self.da_respuesta_apropiada(user_input)
        elif intent == "otro_funcionamiento":
            return self.da_respuesta_apropiada(user_input)
        elif intent == "hora":
            return dar_hora()
        elif intent == "champion_lore":
            nombre_champ = extraer_nombre_campeon(user_input)
            if nombre_champ:
                return dar_champion_info(nombre_champ)
            else:
                return (
                    "No conozco a ese champ. Chance te entendere mejor si me das el nombre solo con la primera en mayuscula, sin espacios tipo: "
                    "TwistedFate"
                    " o "
                    "MissFortune"
                    ""
                )
        elif intent == "muestra_cinematica":
            return muestra_cinematica()
        elif intent == "que_campeon_soy":
            return muestra_quiz_campeon()
        elif intent == "otra_cinematica":
            return self.da_respuesta_apropiada(user_input)
        elif intent == "consejo":
            return dar_recomendacion()
        elif intent == "lineas":
            return (
                linea_superior()
                + "\n"
                + jungla()
                + "\n"
                + linea_del_medio()
                + "\n"
                + linea_inferior()
            )
        elif intent == "linea_superior":
            return linea_superior()
        elif intent == "jungla":
            return jungla()
        elif intent == "linea_del_medio":
            return linea_del_medio()
        elif intent == "linea_inferior":
            return linea_inferior()
        elif intent == "historia":
            return contar_historia()
        elif intent == "otra_historia":
            return self.da_respuesta_apropiada(user_input)
        elif intent == "region":
            return regiones()
        elif intent == "quiz":
            return quizes()
        elif intent == "otro":
            return self.da_respuesta_apropiada(user_input)
        elif intent == "terminar":
            print(despedida(user_input))
            sys.exit(0)
        return ""

    def da_respuesta_apropiada(self, user_input):
        """
        Devuelve la respuesta según el contexto en el que se encuentre

        :param str user_input: El texto escrito por el usuario
        :return Texto que representa la respuesta
        :rtype str
        """
        if self.contexto == "CHISTE":
            return "Aquí va otro: " + contar_chiste()
        elif self.contexto == "MUSICA":
            return "Te dejo otra cancion: " + poner_musica()
        elif self.contexto == "HORA":
            return dar_hora()
        elif self.contexto == "MUESTRA_CINEMATICA":
            return muestra_cinematica()
        elif self.contexto == "FUNCIONAMIENTO":
            return contar_funcionamiento()
        elif self.contexto == "HISTORIA":
            return contar_historia()
        elif self.contexto == "CONSEJO":
            return dar_recomendacion()
        elif self.contexto == "DEFAULT":
            return "¿Podrías tratar de expresarte mejor?"
        else:
            return "¿Podrías tratar de expresarte mejor?"


# ---------------------------------------#
#  Base de conocimiento                 #
# ---------------------------------------#
conocimiento = conocimientoT()


# ---------------------------------------#
#  Interfaz de texto                    #
# ---------------------------------------#
def chatBot():
    input_usuario = ""
    asistente = ChatBot()
    while input_usuario != " ":
        try:
            input_usuario = input(">> ")
        except EOFError:
            print("Saliendo...")
            sys.exit(0)
        except KeyboardInterrupt:
            print("Saliendo...")
            sys.exit(0)
        else:
            print(asistente.responder(input_usuario))


if __name__ == "__main__":
    chatBot()
