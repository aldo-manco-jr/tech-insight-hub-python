# pattern_prompt_handler.py

import utils


def is_valid_pattern_form_compilation(data):
    if (data['Pattern'] != '' and
            data['Data'] != '' and
            data['Type'] != ''
    ):
        return True

    return False


def generate_pattern_prompt(data):
    italian_prompt = ""
    english_prompt = ""

    if not is_valid_pattern_form_compilation(data):
        italian_prompt += "Form Non Valido"
        english_prompt += "Invalid Form"
        return italian_prompt, english_prompt

    if data['Type'] != "":
        italian_prompt += f"""
### PATTERN: "{data['Pattern']}" ### 
        """
        italian_prompt += f"""
### FORMAT: "{data['Pattern']}" ###
        """

    italian_prompt += f"""
### DATA: "{data['Data']}" ### 
        """

    if data['Details'] != "":
        italian_prompt += f"""
### DETAILS: "{data['Details']}" ### 
        """

    english_prompt += italian_prompt

    if data['Type'] == "Pattern":
        italian_prompt += """
Sei un'intelligenza artificiale progettata per identificare un modello/pattern e applicarlo ai dati forniti. La tua missione è applicare il modello/pattern utilizzato nel testo [PATTERN] ai dati forniti [DATA]
        """
        english_prompt += """
You are an artificial intelligence designed to identify a model/pattern and apply it to the provided data. Your mission is to apply the model/pattern used in the text [PATTERN] to the data provided [DATA]
        """
    elif data['Type'] == "Format":
        italian_prompt += """
Sei un'intelligenza artificiale progettata per convertire dei dati forniti in un formato specificato. La tua missione è trasformare i dati forniti in [DATA] nel formato [FORMAT], facendo in modo che il risultato sia esteticamente gradevole
        """
        english_prompt += """
You are an artificial intelligence designed to convert provided data into a specified format. Your mission is to transform the specified data provided in [DATA] into the format [FORMAT], ensuring that the result is aesthetically pleasing
        """

    if data['Details'] != "":
        if data['Type'] == "Pattern":
            italian_prompt += """
 tenendo in considerazione le istruzioni aggiuntive su come identificare correttamente il modello [DETAILS]
            """
            english_prompt += """
 considering the extra guidelines on how to properly identify the pattern [DETAILS]
            """
        elif data['Type'] == "Format":
            italian_prompt += """
. Tieni in considerazione le istruzioni aggiuntive fornite in [DETAILS] su come convertire correttamente i dati forniti nel formato specificato. 
            """
            english_prompt += """ 
. Consider the extra guidelines provided in [DETAILS] on how to properly convert the provided data into the specified format. 
            """

    if data['Type'] == "Pattern":
        italian_prompt += """
. Devi procedere step by step:
--- Riconoscere il modello all'interno del testo fornito
--- Successivamente, applicare il modello riconosciuto ai dati forniti. 
### PATTERN APPLICATO AI NUOVI DATI ###
        """
        english_prompt += """
. You need to follow a step-by-step approach:
--- Identify the pattern in the text provided
--- Then, apply the identified pattern to the given data. 
### PATTERN APPLIED TO NEW DATA ###
        """
    elif data['Type'] == 'Format':
        italian_prompt += """
### DATI CONVERTITI NEL NUOVO FORMATO [FORMAT] ###
        """
        english_prompt += """
### DATA CONVERTED IN THE FORMAT [FORMAT] ###
        """

    return utils.replace_newlines_with_space(italian_prompt), utils.replace_newlines_with_space(english_prompt)
