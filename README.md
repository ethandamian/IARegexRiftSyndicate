# Tarea de Laboratorio #3: Modelando un ChatBot

## Link del Bot 
Con el siguiente link se puede agregar el bot a un canal 
<br>
https://discord.com/api/oauth2/authorize?client_id=1204854598028759112&permissions=0&scope=bot

>[!IMPORTANT]
> Para que el bot funciones correctamente, se debe tener conversacion con el en un canal que se llame "bot-testing-general" 

## Comportamientos que quisimos desarrollar

Este bot lo realizamos con la intención de que contestara cosas sobre League of Legends, usando expresiones regulares.

## Intents usados y regex

Algunos de los intents en el bot son:

* __"bienvenida"__
  - **Regex:** ```r".*hola.*"```, ```r".*buen(a|o)s (d(i|í)as|tardes|noches).*"```

* __"quien_eres"__
    - **Regex:** `r".*(qui(e|é)n).*(tu|tú).*"`, `r".*(qui(e|é)n).*(eres).*"`

* __"hora"__
  - **Regex:** `r".*\b(hora).*"`

* __"otro_hora"__
  - **Regex:** `r".*(enseñamela|dimela|dime).* (de nuevo).*"`
