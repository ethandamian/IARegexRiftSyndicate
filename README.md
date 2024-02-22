# Tarea de Laboratorio #3: Modelando un ChatBot 👾

## Link del Bot 🔗
Con el siguiente link se puede agregar el bot a un canal 
<br>
https://discord.com/api/oauth2/authorize?client_id=1204854598028759112&permissions=0&scope=bot

>[!IMPORTANT]
> Para que el bot funciones correctamente, se debe tener conversacion con el en un canal que se llame "bot-testing-general" 

## Link del repositorio 🔗
El link del repositorio del proyecto se encuentra en el siguiente link
<br>
https://github.com/ethandamian/IARegexRiftSyndicate

## Comportamientos que quisimos desarrollar ⁉️

Este bot lo realizamos con la intención de que contestara cosas sobre League of Legends, usando expresiones regulares.

## Intents usados y regex ✳️

Algunos de los intents en el bot son:

* __"bienvenida"__
  - **Regex:** ```r".*hola.*"```, ```r".*buen(a|o)s (d(i|í)as|tardes|noches).*"```

* __"quien_eres"__
    - **Regex:** `r".*(qui(e|é)n).*(tu|tú).*"`, `r".*(qui(e|é)n).*(eres).*"`

* __"hora"__
  - **Regex:** `r".*\b(hora).*"`

* __"otro_hora"__
  - **Regex:** `r".*(enseñamela|dimela|dime).* (de nuevo).*"`

* __"muestra_cinematica"__
  - **Regex:** `r".*(enseñame|muestrame|dame).*(una cinematica.)*"`

* __"que_campeon_soy"__
  - **Regex:** `r".*(dime|que).*(campeon soy.)*"`

* __"numero_campeones"__
  - **Regex:** `r".*(cuantos campeones hay en lol?|cual es el numero de campeones de lol?).*"`
  
* __"mascota"__
  - **Regex:** `r".*(tu mascota).*(favorita|preferida).*",
                r".*(tu animal).*(favorito|preferido).*",
                r".*(animal).*(mas|más).*(te gusta).*"`
* __"consejo"__
  - **Regex:** `r".*(recomendaci(o|ó)n|recomienda|recomi(é|e)ndame|consejo|recomendar).*(mejorar)*.*",
                r".*(c(ó|o)mo).*(mejoro).*"`
    
* __"rol_mas_popular"__
  - **Regex:** `r".*(rol).*(m(a|á)s)*.*(popular|famoso|conocido)*.*"`

* __"sistema_de_clasificacion"__
  - **Regex:** `r".*(funci(o|ó)n|funcionamiento|funciona).*(clasificaci(o|ó)n|clasificar)*.*"`
 
* __"grieta_del_invocador"__
  - **Regex:** `r".*((grieta|rift) de(l)* invocador).*"`
 
* __"lineas"__
  - **Regex:** `r".*(l(i|í)nea).*(medio).*"`

* __"linea_superior"__
  - **Regex:** `r".*(l(i|í)nea).*(superior|bar(o|ó)n).*"`

* __"jungla"__
  - **Regex:** `r".*(jungla).*"`

* __"linea_del_medio"__
  - **Regex:** `r".*(l(i|í)nea).*(medio).*"`

* __"linea_inferior"__
  - **Regex:** `r".*(l(i|í)nea).*(inferior|bot).*"`

* __"agradecimiento"__
  - **Regex:** `r".*(gracias|agradecid(o|a)).*"`
* __"historia"__
  - **Regex:** `r".*(cuentame|cuenta|dime|echate)*(una)?historia.*"`
