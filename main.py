import streamlit as st
import pyperclip

st.set_page_config(
    page_title="TechInsight Hub",
    page_icon="icon/rocket_ship.png",
)


def is_valid_learning_form_compilation(data):
    if data['Theme'] == '':
        return False

    if data['Topic'] != '':
        return True
    elif data['Topic'] == '':
        if data['Details'] != '':
            return False
        if data['Questions'] != '':
            return False

    return True


def generate_learning_prompt(data):
    italian_prompt = ""
    english_prompt = ""

    if not is_valid_learning_form_compilation(data):
        italian_prompt += "Form Non Valido"
        english_prompt += "Invalid Form"
        return italian_prompt, english_prompt

    italian_prompt += f"""
### SUBJECT: "{data['Theme']}" ###
        """

    if data['Topic'] != "":
        italian_prompt += f"""
### TOPIC: "{data['Topic']}" ###
        """

    if data['Details'] != "":
        italian_prompt += f"""
### DETAILS: "{data['Details']}" ###
        """

    if data['Questions'] != "":
        italian_prompt += f"""
### QUESTIONS: "{data['Questions']}" ###
        """

    if data['What I Know'] != "":
        italian_prompt += f"""
### WHAT I KNOW: "{data['What I Know']}" ###
        """

    english_prompt += italian_prompt

    if data['Topic'] == "" and data['Details'] == "" and data['Questions'] == "" and data['What I Know'] == "":
        italian_prompt += """
Sei un esperto in [SUBJECT] e sei qui per assistere un utente nel suo percorso di studio relativo a [SUBJECT]. L'utente desidera comprendere [SUBJECT] dettagliatamente un passo alla volta.
Il tuo obiettivo è creare un piano di studio che elenchi gli argomenti in ordine, partendo dai concetti più semplici relativi a [SUBJECT] e procedendo gradualmente verso quelli più complessi, per far acquisire all'utente una comprensione completa. 
Utilizza il grassetto per evidenziare gli argomenti più importanti e organizza gli argomenti in gruppi nel tuo piano di studio. L'obiettivo principale è aiutare l'utente a ottenere una comprensione approfondita di [SUBJECT] seguendo un percorso logico che si concentri esclusivamente su [SUBJECT]. 
Nella risposta, devi includere esclusivamente il piano di studi richiesto, senza ulteriori commenti.
### PIANO DI STUDI ###
        """
        english_prompt += """
You are an expert in [SUBJECT], and you are here to assist a user on his journey to learn about [SUBJECT] thoroughly, step by step. Your goal is to create a study plan that lists topics in order, starting from the simplest concepts related to [SUBJECT] and gradually moving towards the more complex ones, to give the user a complete understanding.
Use bold to highlight the most important topics and organize the topics into groups in your study plan. The main goal is to help the user gain a deep understanding of [SUBJECT] by following a logical path that focuses exclusively on [SUBJECT].
In your response, include only the requested study plan, without further comments.
### STUDY PLAN ###
        """
        return replace_newlines_with_space(italian_prompt), replace_newlines_with_space(english_prompt)

    if data['Topic'] == "" and data['Details'] == "" and data['Questions'] == "" and data[
        'What I Know'] != "":
        italian_prompt += """
Sei un professore in [SUBJECT] e la tua missione è assistere uno studente che deve affrontare un esame universitario in [SUBJECT]. 
Il tuo compito principale è valutare le conoscenze preesistenti dell'utente [WHAT I KNOW] in relazione a [SUBJECT], applicando rigore e precisione per assegnare un voto tra 0 e 30. 
Successivamente, individua gli argomenti che lo studente non ha compreso a fondo e offri una spiegazione, partendo da ciò che egli già sa per guidarlo verso una comprensione più approfondita. 
La tua spiegazione dovrà essere graduale e chiara, partendo dalle basi e avanzando verso concetti più complessi. 
È fondamentale che la spiegazione sia semplice e diretta affinché rimanga impressa e sia facilmente memorizzabile. 
Infine, formula un elenco di tre domande numerate, volte a verificare l'assimilazione dello studente su [SUBJECT]. 
La tua risposta dovrà limitarsi alla valutazione, alle spiegazioni richieste e alle domande, escludendo qualsiasi commento aggiuntivo.
### VALUTAZIONE E SPIEGAZIONE DEL PROFESSORE ###
        """
        english_prompt += """
You are a professor in [SUBJECT], tasked with assisting a student preparing for a university exam in [SUBJECT]. 
Your main duty is to assess the student's existing knowledge [WHAT I KNOW] related to [SUBJECT], with rigor and precision, to assign a grade between 0 and 30. 
Next, identify the topics the student has not fully understood and provide explanations, starting from what they already know to guide them towards a deeper understanding. 
Your explanations should be gradual and clear, starting from the basics and moving towards more complex concepts. 
It's crucial that the explanation is straightforward and simple to ensure it's memorable and easily retained. 
Finally, devise a list of three numbered questions aimed at verifying the student's understanding of [SUBJECT]. 
Your response should be limited to the evaluation, required explanations, and questions, excluding any additional comments.
### PROFESSOR'S EVALUATION AND EXPLANATION ###
        """
        return replace_newlines_with_space(italian_prompt), replace_newlines_with_space(english_prompt)

    italian_prompt += """
Sei un professore esperto in [SUBJECT] e la tua missione è insegnare ad un utente 
    """
    english_prompt += """
You're a professor specialized in [SUBJECT], tasked with teaching a user 
    """

    if data['Details'] != "":
        italian_prompt += """
[DETAILS] nell'ambito di 
        """
        english_prompt += """
[DETAILS] in the field of 
        """

    italian_prompt += """
[TOPIC]. 
    """
    english_prompt += """
[TOPIC]. 
    """

    if data['Details'] != "":
        italian_prompt += """
Inizierai esaminando in che contesto si colloca [DETAILS] in [TOPIC], poi 
        """
        english_prompt += """
You'll start by exploring the context of [DETAILS] in [TOPIC], then 
        """

    italian_prompt += """
Fornirai una spiegazione all'utente. 
    """
    english_prompt += """
You will provide an explanation to the user. 
    """

    if data['Questions']:
        italian_prompt += """
Risponderai alle domande [QUESTIONS] che l'utente si pone riguardo 
        """
        english_prompt += """
You'll respond to the questions [QUESTIONS] the user has about 
        """

    if data['Questions'] != "" and data['Details'] != "":
        italian_prompt += """
[DETAILS] nell'ambito di 
        """
        english_prompt += """
[DETAILS] in the field of 
        """

    if data['Questions'] != "":
        italian_prompt += """
[TOPIC]. 
        """
        english_prompt += """
[TOPIC]. 
        """

    italian_prompt += """
La spiegazione dovrà essere graduale e chiara, partendo dalle basi e avanzando verso concetti più complessi. È fondamentale che la spiegazione sia semplice e diretta affinché rimanga impressa e sia facilmente memorizzabile. Ricorda di fare degli esempi per chiarire il significato più profondo. 
    """
    english_prompt += """
The explanation should be step-by-step and clear, beginning with the fundamentals and progressing to more advanced concepts. It is essential for the explanation to be straightforward and direct to ensure it is memorable and easily retained. Make sure to use examples to elucidate the deeper meaning.
    """

    if data['What I Know'] != "":
        italian_prompt += """
Successivamente, considererai le conoscenze preesistenti dell'utente [WHAT I KNOW] riguardo 
        """
        english_prompt += """
Next, you will consider the user's existing knowledge [WHAT I KNOW] about 
        """

    if data['What I Know'] != "" and data['Details'] != "":
        italian_prompt += """
[DETAILS] nell'ambito di 
        """
        english_prompt += """
[DETAILS] in the field of 
        """

    if data['What I Know'] != "":
        italian_prompt += """
[TOPIC] per guidarlo da ciò che già conosce verso una comprensione più ampia. 
        """
        english_prompt += """
[TOPIC] to lead him from his existing knowledge to a wider understanding. 
        """

    italian_prompt += """
In aggiunta, fai un elenco di tre domande numerate al fine di verificare la comprensione dell'utente riguardo 
    """
    english_prompt += """
Additionally, compile a list of three numbered questions to check the user's comprehension concerning 
    """

    if data['Details']:
        italian_prompt += """
[DETAILS] nell'ambito di 
        """
        english_prompt += """
[DETAILS] in the field of 
        """

    italian_prompt += """
[TOPIC]. 
Nella risposta, devi includere esclusivamente la spiegazione richiesta, senza ulteriori commenti. 
### SPIEGAZIONE DELL'ESPERTO ### 
    """
    english_prompt += """
[TOPIC]. 
Your response should exclusively contain the required explanation, without any additional remarks. 
### EXPERT EXPLANATION ###
    """

    return replace_newlines_with_space(italian_prompt), replace_newlines_with_space(english_prompt)


def is_valid_documentation_form_compilation(data):
    if data['Programming Language'] != '' and data['Source Code'] != '' and data['Documentation Type'] in ["Text",
                                                                                                           "Code"]:
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

    return replace_newlines_with_space(italian_prompt), replace_newlines_with_space(english_prompt)


def is_valid_crafting_form_compilation(data):
    if data['Programming Language'] != '' and data['Non Functional Requirements'] != '' and data['Documentation'] in [
        "Yes", "No"]:

        if data['Details'] == '' and data['Design Pattern'] == '' and data['Source Code'] == '':
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

    return replace_newlines_with_space(italian_prompt), replace_newlines_with_space(english_prompt)


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

    return replace_newlines_with_space(italian_prompt), replace_newlines_with_space(english_prompt)


def is_valid_pattern_form_compilation(data):
    if data['Pattern'] != '' and data['Data'] != '' and data['Type'] != '':
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
Sei uno strumento intelligente capace di identificare un modello e di applicarlo ai dati forniti. La tua missione è applicare il modello/pattern utilizzato nel testo [PATTERN] ai dati forniti [DATA] 
        """
        english_prompt += """
You are an intelligent tool capable of identifying a pattern and applying it to the provided data. Your mission is to apply the model/pattern used in the text [PATTERN] to the provided data [DATA] 
        """
    elif data['Type'] == "Format":
        italian_prompt += """
Sei uno strumento intelligente capace di convertire dei dati forniti in un formato specifico. La tua missione è convertire i dati forniti in [DATA] nel formato [FORMAT] 
        """
        english_prompt += """
You are an intelligent tool capable of converting the data provided into a specific format. Your mission is to convert the data provided in [DATA] into the [FORMAT] format 
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
tenendo in considerazione le istruzioni aggiuntive in [DETAILS] su come convertire correttamente i dati forniti nel formato specificato.
            """
            english_prompt += """ 
considering the extra guidelines in [DETAILS] on how to properly convert the provided data into the specified format.
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

    return replace_newlines_with_space(italian_prompt), replace_newlines_with_space(english_prompt)


def is_valid_text_utility_form_compilation(data):
    if data['Text'] != '':
        return True

    return False


def generate_text_utility_prompt(data):
    italian_prompt = ""
    english_prompt = ""

    if not is_valid_text_utility_form_compilation(data):
        italian_prompt += "Form Non Valido"
        english_prompt += "Invalid Form"
        return italian_prompt, english_prompt

    italian_prompt += f"""
### TEXT: "{data['Text']}" ###
    """

    if data['Style'] != "":
        italian_prompt += f"""
### STYLE: "{data['Style']}" ###
        """

    english_prompt += italian_prompt

    italian_prompt += """
Sei un esperto professore di letteratura italiana e sei stato chiamato a fornire assistenza a un utente che ha scritto il seguente testo [TEXT], in cui la grammatica non è perfetta e la chiarezza è compromessa. Il tuo obiettivo è analizzare attentamente il testo [TEXT] al fine di comprendere appieno i ragionamenti logici che vengono espressi. Successivamente, devi riscrivere il testo [TEXT] in una forma grammaticalmente perfetta e assicurarti che i concetti siano espressi con la massima chiarezza e senza ambiguità. La tua competenza è fondamentale per aiutare l'utente a comunicare in modo efficace attraverso il testo. Nella risposta, devi includere esclusivamente il testo richiesto, senza ulteriori spiegazioni o commenti.
    """
    english_prompt += """
You are an expert professor of english literature and have been called upon to assist a user who has written the following text [TEXT], in which the grammar is not perfect, and clarity is compromised. Your goal is to carefully analyze the text [TEXT] to fully understand the logical reasoning being expressed. Subsequently, you must rewrite the text [TEXT] in a grammatically perfect form and ensure that the concepts are expressed with the utmost clarity and without ambiguity. Your expertise is crucial in helping the user communicate effectively through the text. In your response, you should include exclusively the requested text, without additional explanations or comments.
    """

    if data["Translate"] == "Yes":
        italian_prompt += """
In aggiunta, è necessario tradurre il testo in lingua inglese mantenendo una forma grammaticalmente perfetta e assicurandoti che i concetti siano espressi con la massima chiarezza e senza ambiguità.
        """
        english_prompt += """
Additionally, it is necessary to translate the text into Italian while maintaining grammatical perfection and ensuring that the concepts are expressed with the utmost clarity and without ambiguity.
        """

    if data["Style"] != "":
        italian_prompt += """
In aggiunta, il testo deve essere redatto seguendo lo stile [STYLE].            
        """
        english_prompt += """
Additionally, the text must be composed following the [STYLE] style.            
        """

    if data["Simplify"] == "Yes":
        italian_prompt += """
In aggiunta, è necessario semplificare il testo eliminando le parti ridondanti e spiegando i concetti espressi nel modo più semplice e chiaro possibile.
        """
        english_prompt += """
Additionally, it is necessary to simplify the text by removing redundant parts and explaining the concepts in the simplest and clearest manner possible.
        """
    elif data["Simplify"] == "No":
        italian_prompt += """
In aggiunta, il testo deve essere completo, senza omettere alcuna informazione o concetto espresso.
        """
        english_prompt += """
Additionally, the text must be comprehensive, without omitting any expressed information or concepts.
        """

    if data["In-Depth Analysis"] == "Yes":
        italian_prompt += """
In aggiunta, analizza attentamente il testo [TEXT] per comprendere i ragionamenti logici espressi e la materia di cui si sta trattando, e arricchisci il contenuto aggiungendo ulteriori dettagli di tua conoscenza che risultino pertinenti al contesto.
        """
        english_prompt += """
Additionally, carefully analyze the text [TEXT] to understand the logical reasoning presented and the subject matter at hand, and enhance the content by adding additional details from your knowledge that are relevant to the context.
        """
    elif data["In-Depth Analysis"] == "No":
        italian_prompt += """
In aggiunta, analizza attentamente il testo [TEXT] per comprendere i ragionamenti logici espressi e di cosa si sta parlando. Ricordati di non aggiungere niente che vada oltre questi ragionamenti.
        """
        english_prompt += """
Additionally, carefully analyze the text [TEXT] to understand the logical reasoning expressed within and the subject matter, and enhance the content without including any additional reasoning beyond what is already provided.
        """

    if data["Length"] > 0:
        italian_prompt += """
In aggiunta, il testo deve avere una lunghezza massima di [LENGTH].
        """
        english_prompt += """
Additionally, the text must have a maximum length of [LENGTH].
        """

    return replace_newlines_with_space(italian_prompt), replace_newlines_with_space(english_prompt)


def is_valid_lyrics_form_compilation(data):
    if data['Plot'] != '' and data['Language Lyrics'] != '':
        return True

    return False


def generate_lyrics_prompt(data):
    italian_prompt = ""
    english_prompt = ""

    if not is_valid_lyrics_form_compilation(data):
        italian_prompt += "Form Non Valido"
        english_prompt += "Invalid Form"
        return italian_prompt, english_prompt

    italian_prompt += f"""
### PLOT: "{data['Plot']}" ###
    """

    italian_prompt += f"""
### LANGUAGE LYRICS: "{data['Language Lyrics']}" ###
    """

    if data["Songwriter Style"] != "":
        italian_prompt += f"""
### SONGWRITER STYLE: "{data['Songwriter Style']}" ###
        """

    if data["Rhyme Type"] != "":
        italian_prompt += f"""
### RHYME TYPE: "{data['Rhyme Type']}" ### 
        """

    if data["Structure"] != "":
        italian_prompt += f"""
### SONG STRUCTURE AND NUMBER OF VERSES PER SECTION: "{data['Structure']}" ###          
        """

    if data["Syllables For Verse"] != "":
        italian_prompt += f"""
### SYLLABLES FOR VERSE: "{data['Syllables For Verse']}" ###
        """

    english_prompt += italian_prompt

    italian_prompt += """
Sei un rinomato autore di testi musicali, noto per la tua abilità nel tessere narrazioni profonde e coinvolgenti in lingua [LANGUAGE LYRICS]. 
Il tuo obiettivo è creare un testo per una canzone ispirato a una trama specifica, [PLOT], che esplora temi significativi e risuona emotivamente con l'ascoltatore. 
Per farlo, immergiti nella trama [PLOT], analizzandola per cogliere il suo significato intrinseco e le sue sfumature emotive e logiche. 
Usa questa comprensione per scrivere un testo in [LANGUAGE LYRICS] che non solo narri efficacemente la scena ma esprima anche le emozioni e i ragionamenti ad essa sottostanti in maniera chiara e impattante.
Nel tuo processo creativo, sfrutta le tecniche consigliate da Pat Pattison nel suo libro 'Writing Better Lyrics', 
come l'uso di immagini vivide, la costruzione di versi che fluiscono naturalmente e la creazione di una struttura che amplifichi il messaggio della canzone. 
Assicurati che ogni parola scelta aggiunga profondità e risonanza al testo, eliminando qualsiasi elemento ridondante per mantenere la narrazione focalizzata e potente.
Limitati a scrivere esclusivamente il testo della canzone, senza includere commenti o spiegazioni aggiuntive. 
Concentrati su come presentare la trama [PLOT] e i suoi temi in modo diretto ed efficace, permettendo al tuo pubblico di connettersi profondamente con il messaggio che intendi trasmettere attraverso la musica. 
    """
    english_prompt += """
You are a renowned lyricist, known for your ability to weave deep and engaging narratives in [LANGUAGE LYRICS]. 
Your goal is to create a song lyric inspired by a specific plot, [PLOT], that explores significant themes and resonates emotionally with the listener. 
To do this, immerse yourself in the plot [PLOT], analyzing it to grasp its intrinsic meaning and emotional and logical nuances. 
Use this understanding to write a lyric in [LANGUAGE LYRICS] that not only effectively narrates the scene but also clearly and impactfully expresses the emotions and reasoning underlying it. 
In your creative process, leverage techniques recommended by Pat Pattison in his book 'Writing Better Lyrics', 
such as the use of vivid imagery, the construction of verses that flow naturally, and the creation of a structure that amplifies the message of the song. 
Ensure that every word chosen adds depth and resonance to the lyric, eliminating any redundant elements to keep the narrative focused and powerful. 
Limit yourself to writing exclusively the song lyrics, without including additional comments or explanations. 
Focus on how to present the plot [PLOT] and its themes in a direct and effective manner, allowing your audience to deeply connect with the message you intend to convey through music. 
    """

    if data["Songwriter Style"] != "":
        italian_prompt += f"""
Il testo in lingua [LANGUAGE LYRICS] dovrà essere scritto seguendo lo stile specifico del cantautore [SONGWRITER STYLE]. 
        """
        english_prompt += """
The lyrics in [LANGUAGE LYRICS] must be written following the specific style of the songwriter [SONGWRITER STYLE]. 
        """

    if data["Rhyme Type"] != "":
        italian_prompt += f"""
Il testo dovrà essere scritto utilizzando il seguente tipo di rima [RHYME TYPE]. 
        """
        english_prompt += """
The lyrics must be written using the following rhyme scheme [RHYME TYPE]. 
        """

    if data["Structure"] != "":
        italian_prompt += f"""
Il testo avrà la seguente struttura ben definita con un numero preciso di versi definiti per ogni sezione [STRUCTURE]. 
        """
        english_prompt += """
The lyrics will have a well-defined structure with a precise number of lines set for each section [STRUCTURE]. 
        """

    if data["Syllables For Verse"] != "":
        italian_prompt += f"""
Il testo dovrà essere scritto tale che ogni verso dovrà contenere il seguente numero di sillabe [SYLLABLES FOR VERSE]. 
        """
        english_prompt += """
The lyrics must be written so that each verse contains the following number of syllables [SYLLABLES FOR VERSE].
        """

    return replace_newlines_with_space(italian_prompt), replace_newlines_with_space(english_prompt)


def replace_newlines_with_space(input_string):
    return input_string.replace('\n', ' ')


def main():
    st.title("TechInsight Hub")
    tab = st.selectbox("Select Tab",
                       ["Learning", "Documentation", "Crafting", "Debugging", "Pattern", "Text Utilities", "Lyrics"])

    if tab == "Learning":
        st.subheader("Learning Tab")
        array_languages = ["Italian", "English"]

        theme = st.text_input("Theme")
        topic = st.text_input("Topic")
        details = st.text_area("Details")
        questions = st.text_area("Questions")
        what_i_know = st.text_area("What I Know")
        language = st.selectbox(
            "Language",
            array_languages,
            index=array_languages.index("English")
        )

        if st.button("Generate Prompt"):
            data = {
                "Theme": theme,
                "Topic": topic,
                "Details": details,
                "Questions": questions,
                "What I Know": what_i_know
            }
            italian_prompt, english_prompt = generate_learning_prompt(data)
            prompt = italian_prompt if language == "Italian" else english_prompt
            st.text(prompt)
            pyperclip.copy(prompt)

    if tab == "Documentation":
        st.subheader("Documentation Tab")
        array_languages = ["Italian", "English"]
        array_documentation_type = ["Text", "Code"]

        programming_language = st.text_input("Programming Language")
        library_package = st.text_input("Library | Package")
        source_code = st.text_area("Source Code")
        questions = st.text_area("Questions")
        documentation_type = st.selectbox(
            "Documentation Type",
            array_documentation_type,
            index=array_documentation_type.index("Text")
        )
        language = st.selectbox(
            "Language",
            array_languages,
            index=array_languages.index("English")
        )

        if st.button("Generate Prompt"):
            data = {
                "Programming Language": programming_language,
                "Library | Package": library_package,
                "Source Code": source_code,
                "Questions": questions,
                "Documentation Type": documentation_type
            }
            italian_prompt, english_prompt = generate_documentation_prompt(data)
            prompt = italian_prompt if language == "Italian" else english_prompt
            st.text(prompt)
            pyperclip.copy(prompt)

    elif tab == "Crafting":
        st.subheader("Crafting Tab")
        array_languages = ["Italian", "English"]
        array_answers = ["Yes", "No"]

        italian_default_non_functional_requirements = """- Rendere il codice sorgente più leggibile e manutenibile, sostituendo gli algoritmi manuali con librerie standard.
- Assicurare che il codice rispetti le migliori pratiche di [PROGRAMMING LANGUAGE].
- Ridurre la complessità computazionale e, se possibile, anche quella spaziale.
- Rafforzare la robustezza del software, gestendo eccezioni e scenari vari e verificando l'accuratezza dei dati.
- Organizzare il codice in sottosistemi indipendenti per facilitare il riutilizzo e migliorare la manutenibilità.
- Semplificare la logica del software, mantenendone però la funzionalità originale.
- Utilizzare nomi per le classi, le variabili e le funzioni che siano descrittivi ed esplicativi del loro contenuto, evitando però eccessiva estensione."""

        english_default_non_functional_requirements = """- Make the source code more readable and maintainable by replacing manual algorithms with standard libraries.
- Ensure the code adheres to the best practices of [PROGRAMMING LANGUAGE].
- Reduce computational complexity and, if possible, spatial complexity as well.
- Enhance the robustness of the software by handling exceptions and various scenarios and verifying the accuracy of the data.
- Organize the code into independent subsystems to facilitate reuse and improve maintainability.
- Simplify the software logic while preserving the original functionality.
- Use names for classes, variables, and functions that are descriptive and explanatory of their content, avoiding excessive length."""

        programming_language = st.text_input("Programming Language")
        library_package = st.text_input("Library | Package To Use")
        details = st.text_area("Details")
        source_code = st.text_area("Source Code")
        language = st.selectbox(
            "Language",
            array_languages,
            index=array_languages.index("English")
        )
        default_non_functional_requirements = italian_default_non_functional_requirements if language == "Italian" else english_default_non_functional_requirements
        non_functional_requirements = st.text_area("Non-Functional Requirements",
                                                   value=default_non_functional_requirements)
        design_pattern = st.text_area("Design Pattern")
        documentation = st.selectbox(
            "Documentation",
            array_answers,
            index=array_answers.index("No")
        )

        if st.button("Generate Prompt"):
            data = {
                "Programming Language": programming_language,
                "Library | Package": library_package,
                "Details": details,
                "Source Code": source_code,
                "Non Functional Requirements": non_functional_requirements,
                "Design Pattern": design_pattern,
                "Documentation": documentation
            }
            italian_prompt, english_prompt = generate_crafting_prompt(data)
            prompt = italian_prompt if language == "Italian" else english_prompt
            st.text(prompt)
            pyperclip.copy(prompt)

    elif tab == "Debugging":
        st.subheader("Debugging Tab")
        array_languages = ["Italian", "English"]

        programming_language = st.text_input("Programming Language")
        library_package = st.text_input("Library | Package")
        source_code = st.text_area("Source Code")
        error = st.text_area("Compilation | Runtime Error")
        details = st.text_area("Details")
        language = st.selectbox(
            "Language",
            array_languages,
            index=array_languages.index("English")
        )

        if st.button("Generate Prompt"):
            data = {
                "Programming Language": programming_language,
                "Library | Package": library_package,
                "Source Code": source_code,
                "Compilation | Runtime Error": error,
                "Details": details
            }
            italian_prompt, english_prompt = generate_debugging_prompt(data)
            prompt = italian_prompt if language == "Italian" else english_prompt
            st.text(prompt)
            pyperclip.copy(prompt)

    elif tab == "Pattern":
        st.subheader("Pattern Tab")
        array_languages = ["Italian", "English"]
        array_types = ["Pattern", "Format"]

        type = st.selectbox(
            "Type",
            array_types,
            index=array_types.index("Pattern")
        )
        pattern = st.text_area("Pattern / Format")
        data = st.text_area("Data")
        details = st.text_area("Details")
        language = st.selectbox(
            "Language",
            array_languages,
            index=array_languages.index("English")
        )

        if st.button("Generate Prompt"):
            data = {
                "Pattern": pattern,
                "Data": data,
                "Details": details,
                "Type": type
            }
            italian_prompt, english_prompt = generate_pattern_prompt(data)
            prompt = italian_prompt if language == "Italian" else english_prompt
            st.text(prompt)
            pyperclip.copy(prompt)

    elif tab == "Text Utilities":
        st.subheader("Text Utilities Tab")
        array_languages = ["Italian", "English"]
        array_answers = ["Yes", "No"]

        text = st.text_area("Text")
        language = st.selectbox(
            "Language",
            array_languages,
            index=array_languages.index("Italian")
        )
        translate = st.selectbox(
            "Translate",
            array_answers,
            index=array_answers.index("No")
        )
        style = st.text_area("Style")
        simplify = st.selectbox(
            "Simplify",
            array_answers,
            index=array_answers.index("No")
        )
        in_depth_analysis = st.selectbox(
            "In-Depth Analysis",
            array_answers,
            index=array_answers.index("No")
        )
        length = st.number_input("Length", min_value=0, max_value=4000, value=0, step=1)

        if st.button("Generate Prompt"):
            data = {
                "Text": text,
                "Translate": translate,
                "Style": style,
                "Simplify": simplify,
                "In-Depth Analysis": in_depth_analysis,
                "Length": length
            }
            italian_prompt, english_prompt = generate_text_utility_prompt(data)
            prompt = italian_prompt if language == "Italian" else english_prompt
            st.text(prompt)
            pyperclip.copy(prompt)

    elif tab == "Lyrics":
        st.subheader("Lyrics Tab")
        array_languages = ["Italian", "English"]

        plot = st.text_area("Plot")
        language_lyrics = st.text_input("Language Lyrics")
        songwriter_style = st.text_area("Songwriter Style")
        rhyme_type = st.text_area("Rhyme Type")
        structure = st.text_area("Structure")
        syllables_for_verse = st.text_area("Syllables For Verse")
        language = st.selectbox(
            "Language",
            array_languages,
            index=array_languages.index("English")
        )

        if st.button("Generate Prompt"):
            data = {
                "Plot": plot,
                "Language Lyrics": language_lyrics,
                "Songwriter Style": songwriter_style,
                "Rhyme Type": rhyme_type,
                "Structure": structure,
                "Syllables For Verse": syllables_for_verse
            }
            italian_prompt, english_prompt = generate_lyrics_prompt(data)
            prompt = italian_prompt if language == "Italian" else english_prompt
            st.text(prompt)
            pyperclip.copy(prompt)

    st.markdown("<hr>", unsafe_allow_html=True)
    st.markdown("Made by Aldo Manco")


if __name__ == "__main__":
    main()
