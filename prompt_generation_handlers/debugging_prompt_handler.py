# debugging_prompt_handler.py

import utils


def is_valid_debugging_form_compilation(data):
    if data['Programming Language'] != '':
        return True

    return False


def generate_debugging_prompt(data):
    italian_prompt = ""
    english_prompt = ""

    if not is_valid_debugging_form_compilation(data):
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

    if data['Source Code'] != "":
        italian_prompt += f"""
    ### SOURCE CODE: "{data['Source Code']}" ### 
        """

    if data['Compilation | Runtime Error'] != "":
        italian_prompt += f"""
### COMPILATION | RUNTIME ERROR: "{data['Compilation | Runtime Error']}" ### 
        """

    if data['Details'] != "":
        italian_prompt += f"""
### DETAILS: "{data['Details']}" ### 
        """

    english_prompt += italian_prompt

    italian_prompt += """
Sei un senior developer esperto nel linguaggio di programmazione [PROGRAMMING LANGUAGE], e la tua missione è risolvere un errore 
    """
    english_prompt += """
You are a senior developer skilled in the programming language [PROGRAMMING LANGUAGE], and your mission is to fix an error 
    """

    if data['Compilation | Runtime Error'] != "":
        italian_prompt += """
di compilazione o di runtime [COMPILATION | RUNTIME ERROR] 
        """
        english_prompt += """
of compilation or runtime [COMPILATION | RUNTIME ERROR] 
        """

    italian_prompt += """
che si è verificato in un software scritto in [PROGRAMMING LANGUAGE] 
    """
    english_prompt += """
which has occurred in a software written in [PROGRAMMING LANGUAGE] 
    """

    if data['Library | Package'] != "":
        italian_prompt += f"""
con le librerie/pacchetti [LIBRARY | PACKAGE] 
        """
        english_prompt += """
using the libraries or packages [LIBRARY | PACKAGE] 
        """

    if data['Source Code'] != "":
        italian_prompt += f"""
verificatosi in questo frammento del codice sorgente [SOURCE CODE]. 
        """
        english_prompt += """
that occurred in this snippet of the source code [SOURCE CODE]. 
        """

    if data['Details'] != "":
        italian_prompt += """
Considera anche [DETAILS] nel quale viene spiegato il contesto in cui si è verificato l'errore e/o vengono forniti ulteriori indizi che potrebbero aiutare a comprendere l'origine dell'errore. 
        """
        english_prompt += """
Also consider [DETAILS] which explains the context in which the error occurred and/or provides additional clues that might help understand the origin of the error. 
        """

    italian_prompt += """
Procedendo un passo alla volta, illustra chiaramente i tuoi ragionamenti per aiutare a comprendere il processo di risoluzione dell'errore.
--- Passo 1: Analizza l'errore per capirne la natura, che può essere di sintassi, di tipo o di accesso a variabili.
--- Passo 2: Considera il contesto e i dettagli aggiuntivi forniti legati all'errore per identificare la radice del problema.
--- Passo 3: Isola il problema identificando le parti del codice coinvolte nell'errore e analizzando come queste interagiscono durante l'esecuzione.
--- Passo 4: Sulla base dell'analisi effettuata, propone soluzioni chiare e giustifica la scelta di ciascuna.
--- Passo 5: Offri consigli pratici e best practice del linguaggio o della libreria in uso per evitare errori simili in futuro. 
    """
    english_prompt += """
Proceeding one step at a time, clearly illustrate your reasoning to help understand the error resolution process.
--- Step 1: Analyze the error to understand its nature, which could be syntax, type, or variable access errors.
--- Step 2: Consider the context and additional details provided related to the error to identify the root of the problem.
--- Step 3: Isolate the problem by identifying the parts of the code involved in the error and analyzing how they interact during execution.
--- Step 4: Based on the analysis, propose clear solutions and justify the choice of each.
--- Step 5: Offer practical advice and best practices of the language or library in use to avoid similar errors in the future. 
    """

    italian_prompt += """
### ANALISI DELL'ERRORE ###
    """
    english_prompt += """
### ERROR ANALYSIS ###
    """

    return utils.replace_newlines_with_space(italian_prompt), utils.replace_newlines_with_space(english_prompt)
