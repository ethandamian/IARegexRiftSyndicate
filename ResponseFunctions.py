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
def dar_champion_info(champion):
    """
    Devuelve la información de un campeón

    :param str champion: El campeón del que se quiere obtener información
    :return La información del campeón
    :rtype str
    """
    champion_json_file = champion + ".json"
    try:
        champion_data = getattr(champion, champion_json_file)
        info = champion_data  # You may need to parse the JSON data here if it's not already loaded
        return info
    except AttributeError:
        return "Champion information not found"


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
            "Mi consejo para mejorar en el juego es practicar, aprender de cada derrota y ¡divertirse en la Grieta del Invocador!",
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


def contar_historia():
    """
    Cuenta una historia de forma aleatoria

    :return La historia que se va a contar
    :rtype str
    """
    historias = [
        """```Viego no podía recordar casi nada de su antiguo país que no estuviera deformado por las sombras o por la angustia. 
        En sus recuerdos, había salido a las calles de arenisca y solo había visto a Isolde frente a él. 
        En cada fresco de cada pared estaba ella dentro de un mundo pintado que solo él podía tocar o ver. 
        Pero cuando quería alcanzarla, la ilusión se rompía, y allí estaba él, completamente rodeado por las aguas fétidas que se la habían llevado una vez más.\n\n
        Viego arrancó la espada de la roca y se irguió, golpeando el suelo y las paredes con el enorme peso de su arma mientras lloraba. 
        Luego permaneció inmóvil por largo rato, contemplando la antigua pintura del viejo reino como si hubiera visto algo nuevo. 
        Contemplando cómo era él antes de que la oscuridad engullera las Islas.\n\n
        ''Viego'', pronunció. ''Tan atractivo. Tan joven. ¿En qué te has convertido, Viego? ¿A dónde te has ido?''. 
        Tiró la pintura al piso; el marco crujió torpemente mientras el lienzo se estrujaba debajo.\n\n'
        '¿Dónde estás, Isolde?'', preguntó. ''¿Por qué no regresas a mi lado?''.\n\nPero ya conocía la respuesta.```""",

        """```Con un gruñido grave, el gran oso se incorporó. Una avalancha de nieve se desprendió de su titánica silueta. La tierra retumbó. Sacudió su pelaje y giró su pesada cabeza para avistar el horizonte entero. Sus fosas nasales se ensancharon.\n\n
        Podía saborear el tributo de sangre en el aire. Un escalofrío lo recorrió por completo. En algún lugar, las piedras fueron acomodadas para formar su runa. Se hizo un sacrificio en su nombre. Sintió cómo el poder de la veneración corría por sus extremidades.\n\n
        ''¡Valhir! ¡Invocamos tu furia! ¡Danos tu fuerza! ¡Cada muerte es una ofrenda!''.\n\n
        Con la promesa de la batalla, la masacre y la adoración, el corazón de Valhir latió al ritmo de los tambores de guerra que resonaban por toda la región. Podía escuchar las pisadas, el choque de las espadas, los lamentos de los moribundos.\n\n
        El llamado le hablaba a su cuerpo. El llamado se dirigía a él.\n\n
        Volibear se paró sobre sus patas traseras y rugió hacia los cielos. El sonido reverberó a lo largo de la helada tundra, penetrando en el alma de todo ser vivo en el Fréljord.```""",

        """```Fue durante los últimos y oscuros días de la Guerra de las Tres Hermanas, cuando Avarosa y Serylda movilizaron a sus guerreros hasta las montañas para enfrentarse a Lissandra ante las murallas de su propia fortaleza. No servirían a los amos sobrenaturales con los que ella se había comprometido. Esto le pondría un fin.\n\n
        La Bruja de Hielo le hizo un gesto a los ejércitos que dirigían, la gran alianza que por fin había sometido estas tierras salvajes. Los mortales Hijos del Hielo eran casi inmunes al frío del invierno. Los reyes troles deambularon a lo largo y ancho de la tundra, amasando vastas fortunas con sus conquistas. Incluso los majestuosos y terribles Caminantes Funestos, alejados de su forma original, ahora marchaban bajo las órdenes de las Tres.\n\n
        Todo esto, les recordó Lissandra a sus hermanas, era producto del trato que ella había hecho con los amos del reino de las profundidades: los seres que ella conocía como los Vigilantes. Fueron ellos quienes le revelaron los secretos primigenios del mundo. Serían ellos quienes obtendrían la victoria definitiva.\n\n
        Y fue entonces, en el punto más álgido de este amargo enfrentamiento, que finalmente llegaron los Vigilantes a Runaterra.\n\n
        La tierra se abrió, arrastrando a miles de guerreros al abismo debajo de ella, antes de que el primer ser del terror comenzara su existencia. Todo en el reino material era nuevo para este ser, desconcertado por nociones tales como la forma y la constancia. De inmediato, se manifestó en su contra. En una horrible revuelta de metamorfosis sin control, le brotaron cuernos y retazos de pelaje. Sus colosales extremidades como tentáculos se convirtieron en brazos humanoides articulados con dedos que arañaban la roca desnuda de las laderas de las montañas. Lo más grave fue que otros Vigilantes comenzaron a despertarse, atormentados por sus propias transformaciones horripilantes.\n\n```""",

        """```Más tarde, esa misma noche, visito a mamá, como siempre. Ella ya está dormida, por lo que dejo silenciosamente un gran saco de monedas sobre su tocador y le doy un beso en la frente.\n\n
        Se despierta y sonríe al ver a su muchacho de pie junto a su cama. Mientras toco su mejilla, ella observa el vendaje que llevo en la mano: fue cuando agarré la cuchilla del Desollador.\n\n
        ''Oh, Settrigh, mi amor, ¿qué pasó?'', dice, preocupada.\n\n
        ''Nada grave. Me corté en el trabajo, construyendo'', le digo.\n\n
        ''¿Qué construiste hoy, hijo?'', me pregunta.\n\n
        ''Un orfanato. Para los huérfanos, ma'', le respondo, mientras le doy un beso de buenas noches.\n\n
        ''Eres un buen chico'', dice.\n\n
        Sus ojos se llenan de lágrimas mientras se acomoda para volver a dormir, orgullosa de saber que su hijo se gana la vida de manera respetable.\n\n```""",

        """```En la llegada de la noche, la mitad de las casas en la aldea tienen sus ventanas tapiadas. Se puede escuchar a sus moradores adentro. Se puede escuchar que susurran, murmuran, ríen como maníacos. Sobre qué, no tengo idea. Serpientes. Relámpagos. La oscuridad. Las paredes cerrándose. Cuchillos. El mar. Se ríen y gritan y suena como si todos se hubieran vuelto locos, como si estuvieran atrapados en un cuarto con aquella parte suya que no se atreven a enfrentar. Suena como si todos fuéramos presa de la misma pesadilla.\n\n
        Después, las luces comienzan a apagarse. Una tras otra, en todas las casas tapiadas, las lámparas titilan y se extinguen. Y las voces se disuelven. Todas se callan de repente, excepto una. Hay algo que grazna detrás de la antigua forja. Murmura para sí. Sobre serpientes. Sobre relámpagos. Masculla sobre la oscuridad.\n\n
        Davil, aquel pobre diablo, convoca al ejército y entra a la forja. Y yo... Yo estoy allí, con él. Tengo mi cuchilla. Tengo mi linterna. Pero las filas son profundas y la luz arroja sombras por todos lados.\n\n
        No sé... qué fue lo que ocurrió con exactitud. Vi un rostro... o eso creo. Algo que me miraba, justo enfrente de Davil, pero era como si pudiera ver a través suyo. Como si ese rostro estuviera allí solo por mí. Todo asimétrico, con una arpillera torcida y dientes oxidados. Y detrás suyo... algo enorme. Unas piernas delgadas desparrancadas, algo vivo con cientos de pájaros negros agitándose dentro de una vieja jaula que arrojamos el año pasado al bosque. Y ojos. Muchos ojos.\n\n
        Ahora no queda nadie en Bosque Dorado. Si nadie vino por mí... Soy el único que queda. Escuchar cómo aquellos gritos se desvanecieron detrás de mí mientras la luz carmesí se expandía a través de los tallos del maíz... Ese crujido enfermizo, y los bramidos, chillidos atormentados de cerdos y caballos...\n\n
        ¡Y los cuervos! Cientos de ellos... ¡Miles! Pero, en realidad, no son cuervos. ¿Que no te das cuenta? ¡Son humo y fuego! ¡No son reales! No podían ser reales.\n\n
        ¡Ellos siguieron esa voz! ¡La voz profunda y estruendosa detrás de todo esto! ¿No lo ves? ¿Acaso no...?\n\n
        Oh, cielos... ¡Davil! ¡Lo dejé atrás! ¡Lo dejé allá, allá en las filas con aquel horrible espantapájaros! ¡Todos están muertos! Por todos los dioses... Debe haberme seguido. Una vez que prueba tu miedo, una vez que te conoce, no te suelta jamás. No te dejaré ir, no te dejaré...\n\n
        ¿Qué es esa voz?\n\n
        ¿Alguien la escucha?\n\n
        ¿Acaso no la escuchas?\n\n
        ¿Davil?\n\n```"""
    ]

    return random.choice(historias)


def regiones():
    """
    Devuelve la información de una región
    dependiendo de la opción que se le pase

    """


    regiones = {'AGUASTURBIAS': """```Situada en la lejanía, en el archipiélago de las Islas de la Llama Azul, Aguasturbias es una ciudad portuaria como ninguna otra: hogar de cazadores de serpientes, pandillas de muelle y contrabandistas de todo el mundo conocido. En este lugar se hacen fortunas y las ambiciones se destruyen en un abrir y cerrar de ojos. Para aquellos que huyen de la justicia, de las deudas o de los persecutores, Aguasturbias puede ser un lugar de nuevos comienzos, 
              ya que en estas calles retorcidas a nadie le interesa tu pasado. Pese a ello, en cada nuevo amanecer, siempre se pueden encontrar viajeros imprudentes flotando en el puerto, con las bolsas vacías y la garganta cortada...\n\n
                Si bien puede ser extremadamente peligrosa, en Aguasturbias abundan las oportunidades exentas de las ataduras de un gobierno oficial y de un reglamento del comercio. Si tienes el dinero, puedes comprar casi cualquier cosa: desde Hextech ilegal hasta los servicios de los criminales locales.\n\n
                Con el reciente derrocamiento del último ''rey saqueador'' de Aguasturbias, la ciudad atraviesa un periodo de transición en el que los capitanes más prominentes tratan de llegar a un acuerdo para definir su futuro. No obstante, mientras haya embarcaciones en buen estado y tripulaciones dispuestas a navegar en ellas, es probable que siga siendo uno de los lugares más coloridos y mejor conectados en Runaterra.```""",

                'CIUDAD DE BANDLE': """```Hay discrepancias con respecto al sitio exacto en el que se encuentra el hogar de los yordles; no obstante, algunos mortales afirman haber viajado a través de rutas invisibles hacia una tierra de curiosos encantos más allá del reino material. Hablan de un sitio mágico sin restricciones en el que los insensatos son llevados por el mal camino de las mil maravillas y terminan perdidos en un sueño.\n\n
                                        En la Ciudad de Bandle, se dice que todas las sensaciones se intensifican para quienes no son yordles. Los colores son más brillantes, los alimentos y las bebidas intoxican los sentidos durante años y, una vez que se prueban, son imposibles de olvidar. La luz del sol es eternamente dorada, las aguas son cristalinas y cada cosecha trae consigo una recompensa provechosa. Quizás algunas de estas afirmaciones sean verdad, o tal vez ninguna lo sea, los cuentacuentos jamás parecen ponerse de acuerdo sobre lo que verdaderamente vieron.\n\n
                                        Lo único que se sabe con certeza es que el tiempo no pasa por la Ciudad de Bandle y sus habitantes. Esto podría explicar por qué aquellos mortales que logran regresar parecen haber envejecido considerablemente, mientras que muchos otros nunca vuelven a ser vistos.```""",

                'DEMACIA': """```Al pertenecer a un reino poderoso y aferrado a la ley con una prestigiosa historia militar, los habitantes de Demacia valoran ante todo los ideales de justicia, de honor y del deber, al tiempo que se enorgullecen acérrimamente de su herencia cultural. Pero, a pesar de sus principios nobles, esta gran nación autónoma se ha vuelto cada vez más insular y aislacionista durante los últimos siglos.\n\n
                            Ahora, Demacia es un reino sumido en el caos.\n\n
                            Su capital, la gran ciudad de Demacia, fue fundada como un refugio frente a la hechicería tras la pesadilla de las Guerras Rúnicas, y construida a partir del enigma de la petricita, una peculiar roca blanca que disminuye la energía mágica. Es desde aquí que la familia real ha velado por la defensa de las aldeas y pueblos cercanos, las tierras de cultivo, los bosques y las montañas ricas en recursos minerales.\n\n
                            No obstante, tras la repentina muerte del rey Jarvan III, el resto de las familias nobles no ha aprobado aún la sucesión al trono de su único heredero, el joven príncipe Jarvan.\n\n
                            Quienes viven más allá de las fronteras sumamente resguardadas son vistos cada vez más con sospecha, mientras que varios antiguos aliados comenzaron a recurrir a otros en busca de protección en medio de estos tiempos inciertos. Algunos se atreven a murmurar que la edad de oro de Demacia ya pasó y, a menos que sus habitantes estén dispuestos a adaptarse al mundo cambiante (algo de lo que algunos no se creen capaces), el declive del reino parece inevitable.\n\n
                            Ni toda la petricita en su territorio podrá proteger a Demacia de sí misma.```""",
                'EL FRELJORD': """```El Fréljord es un lugar duro y despiadado en donde sus habitantes nacen siendo guerreros y tendrán que prosperar contra todo pronóstico.\n\n
                                Orgullosas y poseedoras de una independencia feroz, las tribus del Fréljord son consideradas salvajes, ásperas y ''bárbaras'' por sus vecinos a lo largo de Valoran, quienes desconocen las tradiciones antiguas que las forjaron. Varios miles de años atrás, la alianza entre las hermanas Avarosa, Serylda y Lissandra se quebró en una guerra que, sin saberlo, amenazó a toda Runaterra al sumir en caos y en un invierno casi permanente a las tierras del norte. Ahora, solo aquellos mortales verdaderamente excepcionales, inmunes a los estragos del fuego y del viento, son quienes aparentan estar destinados a liderar.\n\n
                                A pesar de los grandes esfuerzos de la Guardia de Hielo, aún perduran los mitos y las leyendas de los dioses antiguos, los yetis enigmáticos y los chamanes cambiapieles. Los invasores de la Garra Invernal abarcan más territorios con cada año que pasa, hostigando las fronteras de Demacia al sur y las de Noxus al este. Por su parte, algunas tribus y clanes desobedientes e independientes que buscan un futuro más pacífico han comenzado a aliarse con Ashe, la joven reina de los avarosanos.\n\n
                                A pesar de ello, los presagios son desalentadores. Sin lugar a dudas, la guerra regresará al Fréljord y nadie podrá escapar```""",
                'EL VACIO': """```Comenzando a gritos su existencia junto al nacimiento del universo, el Vacío es una manifestación de la nada inasible que se encuentra más allá. Es una fuerza con un hambre insaciable, esperando a través de los eones hasta que sus amos, los misteriosos Vigilantes, marquen la hora final.\n\n
                                Ser un mortal tocado por este poder significa sufrir un atisbo agonizante de eterna irrealidad, suficiente como para quebrar hasta la mente más fuerte. Los habitantes del Vacío son criaturas construidas, usualmente con una conciencia limitada, pero programadas con un propósito singular: desatar el olvido total por toda Runaterra.```""",
                
                'ISLA DE LA SOMBRA': """```Esta tierra condenada alguna vez fue el hogar de una civilización noble e iluminada, conocida por sus aliados y emisarios como las Islas Bendecidas. Sin embargo, hace más de mil años, un cataclismo mágico sin precedentes destrozó la barrera entre los reinos material y espiritual, combinándolos en uno solo que condenó instantáneamente a todos los seres vivos.\n\n
                                        Ahora, una malévola Niebla Negra cubre permanentemente las islas, mientras que la tierra misma está contaminada por la hechicería oscura. Los mortales que se atreven a aventurarse a sus lúgubres costas son despojados lentamente de su fuerza vital, lo cual, a su vez, atrae a los insaciables e implacables espíritus de los muertos.\n\n
                                        Quienes mueren dentro de la Niebla están condenados a asediar este lugar de pesadilla por toda la eternidad. Peor aún, el poder de las Islas de la Sombra se fortalece con cada año que pasa y los espectros más poderosos pueden alejarse cada vez más de las islas y rondar por toda Runaterra.```""",
                
                'IXTAL': """```Conocida por su maestría en magia elemental, Ixtal fue una de las primeras naciones independientes en unirse al imperio shurimano. En realidad, la cultura ixtali es mucho más antigua: formó parte de la gran diáspora hacia occidente que dio origen a civilizaciones como los Buhru, la magnífica Helia y los ascetas de Targón. Incluso, es muy probable que haya tenido una participación clave en la creación de los primeros Ascendidos.\n\n
                            Pero los magos de Ixtal sobrevivieron al Vacío y después a los Darkin, gracias a que se distanciaron de sus vecinos, interponiendo como escudo la naturaleza que los rodeaba. A pesar de que se perdió una gran parte, estaban comprometidos con la preservación de lo poco que quedaba.\n\n
                            Ahora, tras miles de años de reclusión en las profundidades de la selva, la sofisticada ciudad de arcología, Ixaocan, permanece casi intacta frente a la influencia externa. Después de haber presenciado, desde la distancia, la destrucción de las Islas Bendecidas, así como las subsecuentes Guerras Rúnicas, los ixtali ven al resto de las facciones de Runaterra como advenedizas y farsantes, por lo que utilizan su poderosa magia para mantener a los intrusos a distancia.```""",

                'JONIA': """```Rodeada por mares traicioneros, Jonia se compone de una serie de provincias aliadas repartidas por un gran archipiélago conocido por muchos como las Tierras Originarias. La búsqueda del equilibrio entre todas las cosas es lo que ha moldeado a la cultura jonia, por lo que el límite entre los reinos de lo material y lo espiritual suele ser más permeable ahí, en especial en los bosques silvestres y en las montañas.\n\n
                            Si bien los encantos de estas tierras pueden ser veleidosos, dada la naturaleza peligrosa y mágica de su fauna, la mayor parte de los jonios tuvo una vida próspera durante varios siglos. Los monasterios de los guerreros, las milicias provinciales e incluso Jonia misma habían bastado para protegerlos.\n\n
                            Pero eso terminó hace doce años, cuando Noxus atacó las Tierras Originarias. Las aparentemente infinitas huestes del imperio arrasaron con Jonia y tuvieron que pasar muchos años para que cayeran derrotadas, a un costo muy alto.\n\n
                            Ahora, Jonia existe en una paz inquieta. Las diferentes reacciones frente a la guerra dividieron la región. Algunos grupos, como los monjes Shojin o los Kinkou, buscan volver a la paz que conlleva el aislamiento y a las tradiciones pastoriles. Otras facciones más radicales, como la Hermandad Navori y la Orden de la Sombra, exigen la militarización de la magia de la tierra para crear una nación unificada que pueda vengarse de Noxus.\n\n
                            El destino de Jonia pende de un delicado equilibrio que muy pocos están dispuestos a alterar, pero que todos pueden sentir cómo se mueve inquietamente bajo sus pies.```""",
                'NOXUS': """```Noxus es un imperio poderoso con una reputación aterradora. Para quienes viven más allá de sus fronteras, es brutal, expansionista y amenazante. Sin embargo, para aquellos que logran ver más allá de su exterior bélico, se encuentran con una sociedad inusualmente inclusiva que respeta y cultiva las fortalezas y los talentos de los suyos.\n\n
                                Los Noxii fueron en el pasado feroces tribus barbáricas hasta que invadieron la antigua ciudad que ahora se encuentra en el corazón de su dominio. Amenazados por todos los flancos, pelearon encarnizadamente contra sus enemigos y expandieron sus fronteras año tras año. Esta lucha por la supervivencia moldeó la identidad de los noxianos modernos: gente profundamente orgullosa que valora la fuerza sobre todas las cosas, aunque esta puede manifestarse de diferentes maneras.\n\n
                                Cualquiera puede ascender a una posición de poder y respeto en Noxus si presenta la aptitud necesaria, más allá de su estrato social, antecedentes o riqueza. Aquellos que son capaces de ejercer la magia son tenidos en alta estima y son buscados con ahínco, con la intención de perfeccionar y aprovechar sus talentos al máximo en beneficio del imperio.\n\n
                                A pesar de este ideal meritocrático, las antiguas familias nobles aún ostentan un poder considerable y algunos temen que la mayor amenaza para Noxus no provenga de sus enemigos, sino desde dentro.```""",
                
                'PILTOVER': """``Piltóver es una ciudad próspera y progresista cuyo poder e influencia van en ascenso. Es el centro cultural de Valoran, donde el arte, la producción artesanal, el comercio y la innovación van de la mano. Su poder no viene del poder militar, sino de los motores del comercio y las ideas avanzadas.\n\n
                Ubicada en los acantilados sobre el distrito de Zaun y con vista al océano, flotas de barcos pasan por sus titánicas compuertas con artículos de todas partes del mundo. La riqueza que esto genera ha dado lugar a un crecimiento de la ciudad sin prececedentes. Piltóver se ha reinventado como una ciudad donde se pueden amasar enormes fortunas y hacer realidad los sueños. 
                Pujantes clanes de mercaderes pudieron desarrollarse en las actividades más increíbles: imponentes disparates artísticos, arcanas investigaciones sobre hextech y monumentos arquitectónicos enalteciendo su poder. Con una creciente cantidad de inventores en el emergente conocimiento de hextech, Piltóver se convirtió en un imán para los artesanos más habilidosos del mundo.```""",

                'SHURIMA': """El imperio de Shurima fue alguna vez una civilización floreciente que abarcó un continente entero. Forjada, en una era ya olvidada, por los poderosos dioses guerreros de los Huéspedes Ascendidos, unificó a todos los pueblos discrepantes del sur e impuso una paz duradera entre ellos.\n\n
                Pocos se atrevían a rebelarse. Y quienes lo hicieron, como la condenada nación de Icathia, fueron aplastados sin piedad.\n\n
                Sin embargo, después de varios miles de años de crecimiento y prosperidad, la ascensión fallida del último emperador shurimano redujo la capital a ruinas y las historias de la antigua gloria del imperio se convirtieron en mitos. 
                Ahora, la mayor parte de los habitantes nómadas de los desiertos de Shurima trata de sostener su endeble existencia valiéndose de la tierra despiadada. 
                Algunos construyeron pequeños puestos de avanzada para defender los pocos oasis disponibles, mientras que otros hurgan en catacumbas desaparecidas hace mucho tiempo, en busca de las incontables riquezas que, seguramente, yacen enterradas ahí. 
                También están aquellos que viven como mercenarios, quienes cobran por sus servicios antes de desaparecer en los páramos sin ley.\n\n
                Pese a ello, unos cuantos se atreven a soñar con el retorno de las viejas costumbres. De hecho, recientemente las tribus fueron alertadas por los susurros del corazón del desierto, los cuales afirman que el emperador Azir ha vuelto para guiarlos en una era nueva y maravillosa.```""",

                'TARGON': """```El Monte Targón es la cima más poderosa de Runaterra, una montaña imponente de roca calcinada por el sol en medio de una cordillera de cumbres de escala incomparable en el mundo. El Monte Targón, ubicado lejos de la civilización, es totalmente remoto y su cúspide casi imposible, excepto para el explorador más resuelto. Como todo lugar mitológico, el Monte Targón es faro de soñadores, locos y aventureros. Algunos de estos valientes intentan escalar la montaña inalcanzable, tal vez en busca de sabiduría o iluminación, o por perseguir la gloria o quizá motivados por un anhelo profundo de pisar su cumbre. El ascenso es prácticamente irrealizable, y aquellos pocos que de alguna manera logran sobrevivir para llegar a su cima, casi nunca hablan de lo que vieron. 
                Algunos vuelven con una mirada poseída y vacía, otros cambiados al punto de ser irreconocibles, imbuidos por un Aspecto de poder inhumano y sobrenatural, con un destino que pocos mortales comprenderían.```""",

                'ZAUN': """```Zaun es un gran distrito suburbano ubicado en la profundidad de los cañones y valles que rodean Piltóver. La poca luz que llega allí abajo se filtra por los vapores que salen de las tuberías corroídas y se refleja a través de los vitrales de la arquitectura industrial. Zaun y Piltóver estuvieron alguna vez unidas; ahora son sociedades separadas, pero simbióticas. 
                A pesar de existir sumida en una permanente luz crepuscular, Zaun progresa, su gente es enérgica y su cultura es rica. 
                La riqueza de Piltóver le permitió a Zaun desarrollarse a la par; un espejo oscuro de la ciudad de arriba. 
                Muchos de los artículos que ingresan a Piltóver encuentran la manera de entrar al mercado negro de Zaun, al igual que las peligrosas investigaciones de los inventores hextech, que se topan con demasiadas restricciones en la ciudad encumbrada, muchas veces son bien recibidas en Zaun. 
                El ilimitado desarrollo de tecnologías volátiles e industrias imprudentes corrompieron y pervirtieron grandes áreas de Zaun. Cantidades de desperdicios tóxicos quedan estancados en las partes más bajas de la ciudad, pero aún allí la gente encuentra la manera de existir y prosperar.```"""
              }
    
    llave_random = random.choice(list(regiones.keys()))

    return regiones[llave_random]
    

def quizes():
    links = ['https://www.sporcle.com/games/flux_capacitor/lol_champs?t=leagueoflegends',
             'http://leagueabilityquiz.com/',
             'https://quizizz.com/admin/quiz/5d03c12b47d580001a74fab1/league-of-legends',
             'https://triviacreator.com/quiz/EjZQFPPEf',
             'https://triviacreator.com/quiz/XYGxC9Y',
             'https://loldle.net/']
    
    return random.choice(links)
