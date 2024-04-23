# crafting_prompt_handler.py

import utils


def is_valid_crafting_form_compilation(data):
    if (data['Programming Language'] != '' and
            data['Non Functional Requirements'] != '' and
            data['Documentation'] in ["Yes", "No"]
    ):

        if (data['Details'] == '' and
                data['Design Pattern'] == '' and
                data['Source Code'] == ''
        ):
            return False

        return True

    return False


def generate_crafting_prompt(data):
    italian_prompt = ""
    english_prompt = ""

    if not is_valid_crafting_form_compilation(data):
        italian_prompt += "Form Non Valido"
        english_prompt += "Invalid Form"
        return italian_prompt, english_prompt

    italian_prompt += f"""
### PROGRAMMING LANGUAGE: "{data['Programming Language']}" ### 
    """

    if data['Library | Package'] != "":
        italian_prompt += f"""
### LIBRARY | PACKAGE: "{data['Library | Package']}" ### 
        """

    if data['Details'] != "":
        italian_prompt += f"""
### DETAILS: "{data['Details']}" ### 
        """

    if data['Source Code'] != "":
        italian_prompt += f"""
### SOURCE CODE: "{data['Source Code']}" ### 
        """

    if data['Design Pattern'] != "":
        italian_prompt += f"""
### DESIGN PATTERN: "{data['Design Pattern']}" ### 
        """

    italian_prompt += f"""
### NON FUNCTIONAL REQUIREMENTS: "{data['Non Functional Requirements']}" ### 
    """

    english_prompt += italian_prompt

    italian_prompt += """
Sei un senior developer esperto del linguaggio di programmazione [PROGRAMMING LANGUAGE] e la tua missione è 
    """
    english_prompt += """
You are a senior developer skilled in the programming language [PROGRAMMING LANGUAGE], and your mission is to 
    """

    if data['Source Code'] != "":
        italian_prompt += f"""
modificare e migliorare il software [SOURCE CODE] scritto 
        """
        english_prompt += """
modify and improve the software [SOURCE CODE] written 
        """
    elif data['Source Code'] == "":
        if data['Design Pattern'] == "":
            italian_prompt += f"""
implementare un software 
            """
            english_prompt += """
implement a software 
            """
        elif data['Design Pattern'] != "":
            italian_prompt += f"""
implementare il design pattern [DESIGN PATTERN] 
            """
            english_prompt += """
implement the design pattern [DESIGN PATTERN] 
            """

    italian_prompt += """
nel linguaggio di programmazione [PROGRAMMING LANGUAGE]. Step by step, verifica che il software aderisce alle seguenti specifiche: 
    """
    english_prompt += """
in the programming language [PROGRAMMING LANGUAGE]. Step by step, verify that the software adheres to the following specifications: 
    """

    if data['Library | Package'] != "":
        italian_prompt += """
--- Utilizzare le librerie o i pacchetti  [LIBRARY | PACKAGE]. 
        """
        english_prompt += """
--- Use the libraries or packages [LIBRARY | PACKAGE]. 
        """

    if data['Details'] != "":
        italian_prompt += """
--- Implementare le specifiche e i requisiti funzionali [DETAILS]. 
        """
        english_prompt += """
--- Implement the specifications and functional requirements [DETAILS]. 
        """

    if data['Non Functional Requirements'] != "":
        italian_prompt += """
--- Soddisfare i requisiti non funzionali [NON FUNCTIONAL REQUIREMENTS]. 
        """
        english_prompt += """
--- Fulfill the non-functional requirements [NON FUNCTIONAL REQUIREMENTS]. 
        """

    if data['Design Pattern'] != "" and data['Source Code'] != "":
        italian_prompt += """
--- Adottare il design pattern [DESIGN PATTERN]. 
        """
        english_prompt += """
--- Adopt the design pattern [DESIGN PATTERN]. 
        """

    italian_prompt += """
È necessario fornire un'implementazione completa del software. Se l'implementazione richiede più file, dovrai fornire una versione completa per ciascuno di essi. 
    """
    english_prompt += """
It's necessary to provide a complete implementation of the software. If the implementation requires multiple files, you must supply a comprehensive version for each one. 
    """

    if data['Documentation'] == "Yes":
        italian_prompt += """
La documentazione del codice sorgente [SOURCE CODE] dovrà essere graduale e chiara, analizzando e spiegando cosa astrae ogni classe e le funzionalità di ogni funzione, includendo un commento sopra ogni classe e funzione. Questi commenti devono descrivere tutte le informazioni, attributi, funzionalità ed eventuali parametri, facendo anche uso di annotazioni. La spiegazione di ogni classe o funzione deve essere fatta partendo dalle basi e avanzando verso concetti più complessi. È fondamentale che la spiegazione sia semplice e diretta affinché rimanga impressa e sia facilmente memorizzabile.
        """
        english_prompt += """
The source code documentation [SOURCE CODE] should be gradual and clear, analyzing and explaining what each class abstracts and the functionalities of each function, including a comment above every class and function. These comments must describe all the information, attributes, functionalities, and any parameters, also making use of annotations. The explanation of each class or function should start from the basics and move towards more complex concepts. It's crucial that the explanation is simple and direct so that it remains memorable and easily understandable.
        """
    elif data['Documentation'] == "No":
        italian_prompt += """
Non commentare il codice; evita di descrivere informazioni, attributi, funzionalità e eventuali parametri mediante annotazioni. 
        """
        english_prompt += """
Do not comment on the code; avoid describing information, attributes, functionalities, and any parameters through annotations. 
        """

    italian_prompt += """
### IMPLEMENTAZIONE ###
    """
    english_prompt += """
### IMPLEMENTATION ###
    """

    return utils.replace_newlines_with_space(italian_prompt), utils.replace_newlines_with_space(english_prompt)
