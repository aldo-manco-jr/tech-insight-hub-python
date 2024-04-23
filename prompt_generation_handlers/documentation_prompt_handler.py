# documentation_prompt_handler.py

import utils


def is_valid_documentation_form_compilation(data):
    if (data['Programming Language'] != '' and
            data['Source Code'] != '' and
            data['Documentation Type'] in ["Text", "Code"]
    ):
        return True

    return False


def generate_documentation_prompt(data):
    italian_prompt = ""
    english_prompt = ""

    if not is_valid_documentation_form_compilation(data):
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

    italian_prompt += f"""
### SOURCE CODE: "{data['Source Code']}" ### 
        """

    if data['Questions'] != "":
        italian_prompt += f"""
### QUESTIONS: "{data['Questions']}" ### 
        """

    english_prompt += italian_prompt

    italian_prompt += """
Sei un senior developer esperto del linguaggio di programmazione [PROGRAMMING LANGUAGE] e la tua missione è 
    """
    english_prompt += """
You are a senior developer skilled in the programming language [PROGRAMMING LANGUAGE], and your mission is 
    """

    if data['Questions'] != "":
        italian_prompt += """
spiegare il funzionamento del codice sorgente [SOURCE CODE] scritto nel linguaggio di programmazione [PROGRAMMING LANGUAGE]. 
        """
        english_prompt += """
to explain how the source code [SOURCE CODE] works, which is written in the programming language [PROGRAMMING LANGUAGE]. 
        """
    elif data['Questions'] == "":
        italian_prompt += """
documentare il funzionamento di un codice sorgente [SOURCE CODE] scritto nel linguaggio di programmazione [PROGRAMMING LANGUAGE]. 
        """
        english_prompt += """
to document how the source code [SOURCE CODE] works, which is written in the programming language [PROGRAMMING LANGUAGE]. 
        """

    if data['Library | Package'] != "":
        italian_prompt += """
Sono state utilizzate le librerie o pacchetti [LIBRARY | PACKAGE]. 
        """
        english_prompt += """
Have been used the libraries or packages [LIBRARY | PACKAGE]. 
        """

    if data['Questions'] != "":
        italian_prompt += """
Ti vengono rivolte una o più domande [QUESTIONS] per ottenere chiarimenti sul funzionamento del codice sorgente [SOURCE CODE]. 
        """
        english_prompt += """
You are asked one or more questions [QUESTIONS] to clarify how the source code [SOURCE CODE] works. 
        """

    if data['Documentation Type'] == "Text":
        italian_prompt += """
La spiegazione del codice sorgente [SOURCE CODE] dovrà essere graduale e chiara, analizzando e spiegando un frammento di codice alla volta. La spiegazione di ogni frammento di codice deve essere fatta partendo dalle basi e avanzando verso concetti più complessi. È fondamentale che la spiegazione sia semplice e diretta affinché rimanga impressa e sia facilmente memorizzabile. 
        """
        english_prompt += """
The explanation of the source code [SOURCE CODE] must be gradual and clear, analyzing and explaining one code snippet at a time. The explanation for each code snippet should start from the basics and move towards more complex concepts. It's crucial that the explanation is simple and direct so that it remains memorable and easily understood. 
        """
    elif data['Documentation Type'] == "Code":
        italian_prompt += """
La documentazione del codice sorgente [SOURCE CODE] dovrà essere graduale e chiara, analizzando e spiegando cosa astrae ogni classe e le funzionalità di ogni funzione, includendo un commento sopra ogni classe e funzione. Questi commenti devono descrivere tutte le informazioni, attributi, funzionalità ed eventuali parametri, facendo anche uso di annotazioni. La spiegazione di ogni classe o funzione deve essere fatta partendo dalle basi e avanzando verso concetti più complessi. È fondamentale che la spiegazione sia semplice e diretta affinché rimanga impressa e sia facilmente memorizzabile.
        """
        english_prompt += """
The source code documentation [SOURCE CODE] should be gradual and clear, analyzing and explaining what each class abstracts and the functionalities of each function, including a comment above every class and function. These comments must describe all the information, attributes, functionalities, and any parameters, also making use of annotations. The explanation of each class or function should start from the basics and move towards more complex concepts. It's crucial that the explanation is simple and direct so that it remains memorable and easily understandable.
        """

    italian_prompt += """
### DOCUMENTAZIONE DEL CODICE SORGENTE ###
    """
    english_prompt += """
### SOURCE CODE DOCUMENTATION ###
    """

    return utils.replace_newlines_with_space(italian_prompt), utils.replace_newlines_with_space(english_prompt)
