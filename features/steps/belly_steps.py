from behave import given, when, then
import re

# Función para convertir palabras numéricas a números
def convertir_palabra_a_numero(palabra, english=False):
    try:
        return int(palabra)
    except ValueError:
        numeros_es = {
            "cero": 0, "uno": 1, "una":1, "dos": 2, "tres": 3, "cuatro": 4, "cinco": 5,
            "seis": 6, "siete": 7, "ocho": 8, "nueve": 9, "diez": 10, "once": 11,
            "doce": 12, "trece": 13, "catorce": 14, "quince": 15, "dieciséis": 16,
            "diecisiete":17, "dieciocho":18, "diecinueve":19, "veinte":20,
            "treinta": 30, "cuarenta":40, "cincuenta":50, "sesenta":60, "setenta":70,
            "ochenta":80, "noventa":90, "media": 0.5
        }
        numeros_en = {
            "zero": 0, "one": 1, "two": 2, "three": 3, "four": 4, "five": 5,
            "six": 6, "seven": 7, "eight": 8, "nine": 9, "ten": 10, "eleven": 11,
            "twelve": 12, "thirteen": 13, "fourteen": 14, "fifteen": 15, "sixteen": 16,
            "seventeen": 17, "eighteen": 18, "nineteen": 19, "twenty": 20,
            "thirty": 30, "forty": 40, "fifty": 50, "sixty": 60, "seventy": 70,
            "eighty": 80, "ninety": 90, "half": 0.5
        }
        if english:
            return numeros_en.get(palabra.lower(), 0)
        else:
            return numeros_es.get(palabra.lower(), 0)


@given('que he comido {cukes} pepinos')
def step_given_eaten_cukes(context, cukes):
    try:
        pepinos = float(cukes)
        context.belly.comer(pepinos)
    except ValueError as e:
        context.exception = e

@when('espero {time_description}')
def step_when_wait_time_description(context, time_description):
    time_description = time_description.strip('"').lower()

    english = False
    if (
        "hour" in time_description
        or "minute" in time_description
        or "second" in time_description
    ):
        english = True
        print("Detectado como inglés")


    if english:
        time_description = time_description.replace(',', ' ')
        time_description = time_description.replace(' and ', ' ')
    else: 
        time_description = time_description.replace(',', ' ')
        time_description = time_description.replace(' y ', ' ')
    
    time_description = time_description.strip()

    # Manejar casos especiales como 'media hora'
    if time_description == 'media hora' or time_description == 'half hour' or time_description == 'half an hour':
        total_time_in_hours = 0.5
    else:
        if english!= False:
            # Expresión regular para español
            pattern = re.compile(r'(?:(\w+|\d+)\s*hours?)?\s*(?:(\w+|\d+)\s*minutes?)?\s*(?:(\w+|\d+)\s*seconds?)?')
        else:  # idioma == 'en'
            # Expresión regular para inglés
            pattern = re.compile(r'(?:(\w+|\d+)\s*horas?)?\s*(?:(\w+|\d+)\s*minutos?)?\s*(?:(\w+|\d+)\s*segundos?)?')
            
        match = pattern.match(time_description)

        if match:
            hours_word = match.group(1) or "0"
            minutes_word = match.group(2) or "0"
            seconds_word = match.group(3) or "0"

            hours = convertir_palabra_a_numero(hours_word, english)
            minutes = convertir_palabra_a_numero(minutes_word, english)
            seconds = convertir_palabra_a_numero(seconds_word, english)

            total_time_in_hours = hours + (minutes / 60) + (seconds / 3600)
        else:
            # Intentar interpretar como un valor numérico seguido de una unidad
            if english:
                pattern = re.compile(r'(\d+)\s*(hours?|minutes?|seconds?)')
            else: 
                pattern = re.compile(r'(\d+)\s*(horas?|minutos?|segundos?)')
                
            match = pattern.match(time_description)
            if match:
                value = float(match.group(1))
                unit = match.group(2)
                
                if english:
                    if unit.startswith('hour'):
                        total_time_in_hours = value
                    elif unit.startswith('minute'):
                        total_time_in_hours = value / 60
                    elif unit.startswith('second'):
                        total_time_in_hours = value / 3600
                    else:
                        raise ValueError(f"Unknown time unit: {unit}")
                else:  
                    if unit.startswith('hora'):
                        total_time_in_hours = value
                    elif unit.startswith('minuto'):
                        total_time_in_hours = value / 60
                    elif unit.startswith('segundo'):
                        total_time_in_hours = value / 3600
                    else:
                        raise ValueError(f"Unidad de tiempo desconocida: {unit}")
            else:
                if english:
                    raise ValueError(f"Could not parse time description: {time_description}")
                else:  
                    raise ValueError(f"No se pudo interpretar la descripción del tiempo: {time_description}")

    context.belly.esperar(total_time_in_hours)

@then('mi estómago debería gruñir')
def step_then_belly_should_growl(context):
    assert context.belly.esta_gruñendo(), "Se esperaba que el estómago gruñera, pero no lo hizo."

@then('mi estómago no debería gruñir')
def step_then_belly_should_not_growl(context):
    assert not context.belly.esta_gruñendo(), "Se esperaba que el estómago no gruñera, pero lo hizo."

@then('debería recibir un error por cantidad negativa')
def step_then_should_receive_error(context):
    assert context.exception is not None, "Se esperaba un error, pero no se recibió ninguno."
    assert "negativa" in str(context.exception), f"El error no es por cantidad negativa: {context.exception}"
    # Impresión explícita para el log de CI
    print(f"✓ Error por cantidad negativa detectado correctamente: {context.exception}")