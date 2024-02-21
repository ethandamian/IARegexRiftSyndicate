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
        # ////////////////////////////////////////////////Aatrox
        {
            "intent": "champion_lore",
            "regex": [
                r".*\b(Aatrox|Ahri|Akali|Akshan|Alistar|Amumu|Anivia|Annie|Aphelios|Ashe|AurelionSol|Azir|Bard|Belveth|Blitzcrank|Brand|Braum|Briar|Caitlyn|Camille|Cassiopeia|Chogath|Corki|Darius|Diana|Draven|DrMundo|Ekko|Elise|Evelynn|Ezreal|Fiddlesticks|Fiora|Fizz|Galio|Gangplank|Garen|Gnar|Gragas|Graves|Gwen|Hecarim|Heimerdinger|Hwei|Illaoi|Irelia|Ivern|Janna|JarvanIV|Jax|Jayce|Jhin|Jinx|Kaisa|Kalista|Karma|Karthus|Kassadin|Katarina|Kayle|Kayn|Kennen|Khazix|Kindred|Kled|KogMaw|KSante|Leblanc|LeeSin|Leona|Lillia|Lissandra|Lucian|Lulu|Lux|Malphite|Malzahar|Maokai|MasterYi|Milio|MissFortune|MonkeyKing|Mordekaiser|Morgana|Naafiri|Nami|Nasus|Nautilus|Neeko|Nidalee|Nilah|Nocturne|Nunu|Olaf|Orianna|Ornn|Pantheon|Poppy|Pyke|Qiyana|Quinn|Rakan|Rammus|RekSai|Rell|Renata|Renekton|Rengar|Riven|Rumble|Ryze|Samira|Sejuani|Senna|Seraphine|Sett|Shaco|Shen|Shyvana|Singed|Sion|Sivir|Skarner|Smolder|Sona|Soraka|Swain|Sylas|Syndra|TahmKench|Taliyah|Talon|Taric|Teemo|Thresh|Tristana|Trundle|Tryndamere|TwistedFate|Twitch|Udyr|Urgot|Varus|Vayne|Veigar|Velkoz|Vex|Vi|Viego|Viktor|Vladimir|Volibear|Warwick|Xayah|Xerath|XinZhao|Yasuo|Yone|Yorick|Yuumi|Zac|Zed|Zeri|Ziggs|Zilean|Zoe|Zyra).*",
                r".*(cuenta|dime|cuentame|hablame|platicame|ahora).*(la historia|el lore|sobre|acerca|de).*(Aatrox|Ahri|Akali|Akshan|Alistar|Amumu|Anivia|Annie|Aphelios|Ashe|AurelionSol|Azir|Bard|Belveth|Blitzcrank|Brand|Braum|Briar|Caitlyn|Camille|Cassiopeia|Chogath|Corki|Darius|Diana|Draven|DrMundo|Ekko|Elise|Evelynn|Ezreal|Fiddlesticks|Fiora|Fizz|Galio|Gangplank|Garen|Gnar|Gragas|Graves|Gwen|Hecarim|Heimerdinger|Hwei|Illaoi|Irelia|Ivern|Janna|JarvanIV|Jax|Jayce|Jhin|Jinx|Kaisa|Kalista|Karma|Karthus|Kassadin|Katarina|Kayle|Kayn|Kennen|Khazix|Kindred|Kled|KogMaw|KSante|Leblanc|LeeSin|Leona|Lillia|Lissandra|Lucian|Lulu|Lux|Malphite|Malzahar|Maokai|MasterYi|Milio|MissFortune|MonkeyKing|Mordekaiser|Morgana|Naafiri|Nami|Nasus|Nautilus|Neeko|Nidalee|Nilah|Nocturne|Nunu|Olaf|Orianna|Ornn|Pantheon|Poppy|Pyke|Qiyana|Quinn|Rakan|Rammus|RekSai|Rell|Renata|Renekton|Rengar|Riven|Rumble|Ryze|Samira|Sejuani|Senna|Seraphine|Sett|Shaco|Shen|Shyvana|Singed|Sion|Sivir|Skarner|Smolder|Sona|Soraka|Swain|Sylas|Syndra|TahmKench|Taliyah|Talon|Taric|Teemo|Thresh|Tristana|Trundle|Tryndamere|TwistedFate|Twitch|Udyr|Urgot|Varus|Vayne|Veigar|Velkoz|Vex|Vi|Viego|Viktor|Vladimir|Volibear|Warwick|Xayah|Xerath|XinZhao|Yasuo|Yone|Yorick|Yuumi|Zac|Zed|Zeri|Ziggs|Zilean|Zoe|Zyra).* ",
            ],
            "respuesta": [""],
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
                r".*(animal).*(mas|más).*(te gusta).*",
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
                r".*(recomendaci(o|ó)n|recomienda|recomi(é|e)ndame|consejo|recomendar).*(mejorar)*.*"
            ],
            "respuesta": ["Claro.", "Por supuesto."],
        },
        {
            "intent": "rol_mas_popular",
            "regex": [r".*(rol).*(m(a|á)s)*.*(popular|famoso|conocido)*.*"],
            "respuesta": [
                "Como tal no hay un rol más popular en League of Legends, pero el de tirador (ADC) y media suelen ser comunes."
            ],
        },
        {
            "intent": "sistema_de_clasificacion",
            "regex": [
                r".*(funci(o|ó)n|funcionamiento|funciona).*(clasificaci(o|ó)n|clasificar)*.*"
            ],
            "respuesta": [
                "El sistema de clasificación de LOL se basa en Ligas y Divisiones, como Bronce, Plata, Oro, Platino, Diamante, Maestro, Gran Maestro o Retador. Cada Liga tiene cuatro divisiones, excepto Maestro, Gran Maestro y Retador. El objetivo es ganar partidas clasificatorias para subir de división o ascender de Liga. A medida que ganas partidas, ganas Puntos de Liga (LP), y al alcanzar cierta cantidad, puedes disputar una serie para avanzar. Ganar la serie te lleva a la siguiente división o Liga, mientras que perder disminuye tus LP y puede incluso hacer que caigas de división o Liga. El sistema también incluye promociones, donde debes ganar una serie de partidas consecutivas para ascender a una nueva Liga. Además, existen los puntos de Maestría para campeones específicos, que se ganan al jugar bien con un campeón en partidas clasificatorias. El rendimiento individual y del equipo, así como el MMR (Matchmaking Rating), también influyen en cuántos LP ganas o pierdes en cada partida."
            ],
        },
        {
            "intent": "grieta_del_invocador",
            "regex": [r".*((grieta|rift) de(l)* invocador).*"],
            "respuesta": [
                "La Grieta del Invocador es el mapa principal de League of Legends, donde se llevan a cabo las partidas. Está dividido en tres calles, con torres y súbditos enemigos, y una jungla con monstruos neutrales y objetivos como el Barón Nashor y los dragones elementales. Es el mapa más emblemático del juego y el más jugado por la comunidad."
            ],
        },
        {
            "intent": "lineas",
            "regex": [r".*(l(i|í)neas).*(hay|existen)*.*"],
            "respuesta": ["Existen tres líneas en League of Legends"],
        },
        {
            "intent": "linea_superior",
            "regex": [r".*(l(i|í)nea).*(superior|bar(o|ó)n).*"],
            "respuesta": [""],
        },
        {
            "intent": "jungla",
            "regex": [r".*(jungla).*"],
            "respuesta": [""],
        },
        {
            "intent": "linea_del_medio",
            "regex": [r".*(l(i|í)nea).*(medio).*"],
            "respuesta": [""],
        },
        {
            "intent": "linea_inferior",
            "regex": [r".*(l(i|í)nea).*(inferior|bot).*"],
            "respuesta": [""],
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
