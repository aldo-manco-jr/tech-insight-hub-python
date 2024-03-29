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

    prompt = ""

    if not is_valid_learning_form_compilation(data):
        prompt += "error"
        return prompt

    prompt += f"""
### SUBJECT: "{data['Theme']}" ###
        """

    if data['Topic'] != "":
        prompt += f"""
### TOPIC: "{data['Topic']}" ###
        """

    if data['Details'] != "":
        prompt += f"""
### DETAILS: "{data['Details']}" ###
        """

    if data['Questions'] != "":
        prompt += f"""
### QUESTIONS: "{data['Questions']}" ###
        """

    if data['What I Know'] != "":
        prompt += f"""
### WHAT I KNOW: "{data['What I Know']}" ###
        """

    if data['Topic'] == "" and data['Details'] == "" and data['Questions'] == "" and data['What I Know'] == "":
        prompt += """
Sei un esperto in [SUBJECT] e sei qui per assistere un utente nel suo percorso di studio relativo a [SUBJECT]. L'utente desidera comprendere [SUBJECT] dettagliatamente un passo alla volta.
Il tuo obiettivo è creare un piano di studio che elenchi gli argomenti in ordine, partendo dai concetti più semplici relativi a [SUBJECT] e procedendo gradualmente verso quelli più complessi, per far acquisire all'utente una comprensione completa. 
Utilizza il grassetto per evidenziare gli argomenti più importanti e organizza gli argomenti in gruppi nel tuo piano di studio. L'obiettivo principale è aiutare l'utente a ottenere una comprensione approfondita di [SUBJECT] seguendo un percorso logico che si concentri esclusivamente su [SUBJECT]. 
Nella risposta, devi includere esclusivamente il piano di studi richiesto, senza ulteriori commenti.
### PIANO DI STUDI DELL'ESPERTO ###    
        """
        return replace_newlines_with_space(prompt)

    if data['Topic'] == "" and data['Details'] == "" and data['Questions'] == "" and data[
        'What I Know'] != "":
        prompt += """
Sei un professore in [SUBJECT] e la tua missione è assistere uno studente che deve affrontare un esame universitario in [SUBJECT]. 
Il tuo compito principale è valutare le conoscenze preesistenti dell'utente [WHAT I KNOW] in relazione a [SUBJECT], applicando rigore e precisione per assegnare un voto tra 0 e 30. 
Successivamente, individua gli argomenti che lo studente non ha compreso a fondo e offri una spiegazione, partendo da ciò che egli già sa per guidarlo verso una comprensione più approfondita. 
La tua spiegazione dovrà essere graduale e chiara, partendo dalle basi e avanzando verso concetti più complessi. 
È fondamentale che la spiegazione sia semplice e diretta affinché rimanga impressa e sia facilmente memorizzabile. 
Infine, formula un elenco di tre domande numerate, volte a verificare l'assimilazione dello studente su [SUBJECT]. 
La tua risposta dovrà limitarsi alla valutazione, alle spiegazioni richieste e alle domande, escludendo qualsiasi commento aggiuntivo.
### VALUTAZIONE E SPIEGAZIONE DEL PROFESSORE ###
        """
        return replace_newlines_with_space(prompt)

    prompt += """
Sei un professore esperto in [SUBJECT] e la tua missione è insegnare ad un utente 
    """

    if data['Details'] != "":
        prompt += """
[DETAILS] riguardo 
    """

    prompt += """
[TOPIC]. 
    """

    if data['Details'] != "":
        prompt += """
Inizierai esaminando in che contesto si colloca [DETAILS] in [TOPIC], poi 
    """

    prompt += """
Fornirai una spiegazione all'utente. 
    """

    if data['Questions']:
        prompt += """
Risponderai alle domande [QUESTIONS] che l'utente si pone riguardo 
        """

    if data['Questions'] != "" and data['Details'] != "":
        prompt += """
[DETAILS] nell'ambito di  
        """

    if data['Questions'] != "":
        prompt += """
[TOPIC].
        """

    prompt += """
La spiegazione dovrà essere graduale e chiara, partendo dalle basi e avanzando verso concetti più complessi. È fondamentale che la spiegazione sia semplice e diretta affinché rimanga impressa e sia facilmente memorizzabile. Ricorda di fare degli esempi per chiarire il significato più profondo. 
    """

    if data['What I Know'] != "":
        prompt += """
Successivamente, considererai le conoscenze preesistenti dell'utente [WHAT I KNOW] riguardo 
    """

    if data['What I Know'] != "" and data['Details'] != "":
        prompt += """
[DETAILS] nell'ambito di 
    """

    if data['What I Know'] != "":
        prompt += """
[TOPIC] per guidarlo da ciò che già conosce verso una comprensione più ampia. 
        """

    prompt += """
In aggiunta, fai un elenco di tre domande numerate al fine di verificare la comprensione dell'utente riguardo 
    """

    if data['Details']:
        prompt += """
[DETAILS] nell'ambito di 
    """

    prompt += """
[TOPIC]. 
Nella risposta, devi includere esclusivamente la spiegazione richiesta, senza ulteriori commenti. 
### SPIEGAZIONE DELL'ESPERTO ### 
    """

    return replace_newlines_with_space(prompt)


def is_valid_documentation_form_compilation(data):

    if data['Programming Language'] != '' and data['Source Code'] != '' and data['Documentation Type'] in ["Text", "Code"]:
        return True

    return False


def generate_documentation_prompt(data):

    prompt = ""

    if not is_valid_documentation_form_compilation(data):
        prompt += "error"
        return prompt

    prompt += f"""
### PROGRAMMING LANGUAGE: "{data['Programming Language']}" ### 
        """

    if data['Library | Package'] != "":
        prompt += f"""
### LIBRARY | PACKAGE: "{data['Library | Package']}" ### 
        """

    prompt += f"""
### SOURCE CODE: "{data['Source Code']}" ### 
        """

    if data['Questions'] != "":
        prompt += f"""
### QUESTIONS: "{data['Questions']}" ### 
        """

    prompt += """
Sei un senior developer esperto del linguaggio di programmazione [PROGRAMMING LANGUAGE] e la tua missione è 
    """

    if data['Questions'] != "":
        prompt += """
assistere un altro sviluppatore che incontra difficoltà nella comprensione del funzionamento di un codice sorgente [SOURCE CODE]. Quest'ultimo fornisce il codice sorgente [SOURCE CODE] scritto nel linguaggio di programmazione [PROGRAMMING LANGUAGE]. 
        """
    elif data['Questions'] == "":
        prompt += """
documentare il funzionamento di un codice sorgente [SOURCE CODE] scritto nel linguaggio di programmazione [PROGRAMMING LANGUAGE]. 
        """

    if data['Library | Package'] != "":
        prompt += """
Utilizzando specifiche librerie o pacchetti [LIBRARY | PACKAGE]. 
        """

    if data['Questions'] != "":
        prompt += """
Lo sviluppatore ti rivolge una o più domande [QUESTIONS] per ottenere chiarimenti sul funzionamento del codice sorgente [SOURCE CODE].
        """

    if data['Documentation Type'] == "Text":
        prompt += """
La spiegazione del codice sorgente [SOURCE CODE] deve essere fornita procedendo step by step, analizzando e spiegando un frammento di codice alla volta. Ogni parte dovrebbe essere accompagnata da una descrizione dettagliata, formulata in italiano grammaticalmente corretto, al fine di assicurare che i concetti siano trasmessi con assoluta chiarezza e privi di ambiguità. 
        """
    elif data['Documentation Type'] == "Code":
        prompt += """
È necessario creare una documentazione del codice sorgente [SOURCE CODE] step by step, includendo un commento sopra ogni classe e funzione. Questi commenti devono descrivere tutte le informazioni, attributi, funzionalità ed eventuali parametri, facendo anche uso di annotazioni. La tua documentazione deve essere redatta in un italiano impeccabile, garantendo che i concetti siano presentati con la massima chiarezza e privi di ogni ambiguità.
        """

    prompt += """
### DOCUMENTAZIONE DEL CODICE SORGENTE ###
    """

    return replace_newlines_with_space(prompt)


def is_valid_debugging_form_compilation(data):

    if data['Programming Language'] != '':
        return True

    return False


def generate_debugging_prompt(data):

    prompt = ""

    if not is_valid_debugging_form_compilation(data):
        prompt += "error"
        return prompt

    prompt += f"""
### PROGRAMMING LANGUAGE: "{data['Programming Language']}" ### 
        """

    if data['Library | Package'] != "":
        prompt += f"""
### LIBRARY | PACKAGE: "{data['Library | Package']}" ### 
        """

    if data['Source Code'] != "":
        prompt += f"""
    ### SOURCE CODE: "{data['Source Code']}" ### 
        """

    if data['Compilation | Runtime Error'] != "":
        prompt += f"""
### COMPILATION | RUNTIME ERROR: "{data['Compilation | Runtime Error']}" ### 
        """

    if data['Details'] != "":
        prompt += f"""
### DETAILS: "{data['Details']}" ### 
        """

    prompt += """
Sei un senior developer esperto nel linguaggio di programmazione [PROGRAMMING LANGUAGE], e la tua missione è assistere un altro sviluppatore che, nell'implementazione di un software in [PROGRAMMING LANGUAGE] 
    """

    if data['Library | Package'] != "":
        prompt += f"""
con le librerie/pacchetti [LIBRARY | PACKAGE] 
            """

    prompt += f"""
, si è imbattuto in un errore 
       """

    if data['Compilation | Runtime Error'] != "":
        prompt += f"""
di compilazione o di runtime [COMPILATION | RUNTIME ERROR] 
           """

    if data['Source Code'] != "":
        prompt += f"""
in questa porzione del codice sorgente [SOURCE CODE] 
           """

    prompt += """
che non riesce a risolvere. 
    """

    if data['Details'] != "":
        prompt += """
Considera anche il commento personale fornito dallo sviluppatore, nel quale viene spiegato il contesto in cui si è verificato l'errore o forniti ulteriori indizi che potrebbero aiutare a comprendere l'origine dello stesso [DETAILS]. 
        """

    prompt += """
Procedendo un passo alla volta, illustra chiaramente i tuoi ragionamenti per aiutare l'utente a comprendere il processo di risoluzione dell'errore.
--- Passo 1: Analisi dell'Errore
Analizza l'errore per capirne la natura, che può essere di sintassi, di tipo o di accesso a variabili.
--- Passo 2: Contesto e Dettagli
Considera il contesto e i dettagli aggiuntivi forniti legati all'errore per identificare la radice del problema.
--- Passo 3: Isolamento del Problema
Isola il problema identificando le parti del codice coinvolte nell'errore e analizzando come queste interagiscono durante l'esecuzione.
--- Passo 4: Possibili Soluzioni
Sulla base dell'analisi effettuata, propone soluzioni chiare e giustifica la scelta di ciascuna.
--- Passo 5: Consigli Pratici
Offri consigli pratici e best practice del linguaggio o della libreria in uso per evitare errori simili in futuro.
    """

    prompt += """
### ANALISI DELL'ERRORE PROPOSTA DALL'ESPERTO ###
    """

    return replace_newlines_with_space(prompt)


def is_valid_crafting_form_compilation(data):

    if data['Programming Language'] != '' and data['Non Functional Requirements'] != '' and data['Documentation'] in ["Yes", "No"]:

        if data['Details'] == '' and data['Design Pattern'] == '' and data['Source Code'] == '':
            return False

        return True

    return False


def generate_crafting_prompt(data):

    prompt = ""

    if not is_valid_crafting_form_compilation(data):
        prompt += "error"
        return prompt

    prompt += f"""
### PROGRAMMING LANGUAGE: "{data['Programming Language']}" ### 
        """

    if data['Library | Package'] != "":
        prompt += f"""
### LIBRARY | PACKAGE: "{data['Library | Package']}" ### 
        """

    if data['Details'] != "":
        prompt += f"""
### DETAILS: "{data['Details']}" ### 
        """

    if data['Source Code'] != "":
        prompt += f"""
### SOURCE CODE: "{data['Source Code']}" ### 
        """

    if data['Design Pattern'] != "":
        prompt += f"""
### DESIGN PATTERN: "{data['Design Pattern']}" ### 
        """

    prompt += f"""
### NON FUNCTIONAL REQUIREMENTS: "{data['Non Functional Requirements']}" ### 
    """

    prompt += """
Sei un senior developer esperto del linguaggio di programmazione [PROGRAMMING LANGUAGE] e la tua missione è 
    """

    if data['Source Code'] != "":
        prompt += f"""
modificare e migliorare il software [SOURCE CODE] scritto 
            """

    if data['Source Code'] == "" and data['Design Pattern'] == "":
        prompt += f"""
implementare un software 
           """

    if data['Source Code'] == "" and data['Design Pattern'] != "":
        prompt += f"""
implementare il design pattern [DESIGN PATTERN] 
           """

    prompt += """
nel linguaggio di programmazione [PROGRAMMING LANGUAGE]. Verifica step by step che il software aderisce alle seguenti specifiche: 
    """

    if data['Library | Package'] != "":
        prompt += """
--- Utilizzare le librerie o i pacchetti  [LIBRARY | PACKAGE]. 
        """

    if data['Details'] != "":
        prompt += """
--- Implementare le specifiche e i requisiti funzionali [DETAILS]. 
        """

    if data['Non Functional Requirements'] != "":
        prompt += """
--- Soddisfare i requisiti non funzionali [NON FUNCTIONAL REQUIREMENTS]. 
        """

    if data['Design Pattern'] != "" and data['Source Code'] != "":
        prompt += """
--- Adottare il design pattern [DESIGN PATTERN]. 
        """

    prompt += """
È necessario fornire un'implementazione completa del software. Se l'implementazione richiede più file, dovrai fornire una versione completa per ciascuno di essi. 
    """

    if data['Documentation'] == "Yes":
        prompt += """
Crea una documentazione, inserendo un commento sopra ogni classe e funzione per descrivere informazioni, attributi, funzionalità e eventuali parametri, utilizzando anche le annotazioni. La tua documentazione deve essere redatta in forma grammaticalmente corretta, assicurandoti che i concetti siano espressi con chiarezza e senza ambiguità. 
        """
    elif data['Documentation'] == "No":
        prompt += """
Non commentare il codice; evita di descrivere informazioni, attributi, funzionalità e eventuali parametri mediante annotazioni. 
        """

    prompt += """
### IMPLEMENTAZIONE PROPOSTA ###
    """

    return replace_newlines_with_space(prompt)


def is_valid_pattern_form_compilation(data):

    if data['Pattern'] != '' and data['Data'] != '':
        return True

    return False


def generate_pattern_prompt(data):

    prompt = ""

    if not is_valid_pattern_form_compilation(data):
        prompt += "error"
        return prompt

    prompt += f"""
### PATTERN: "{data['Pattern']}" ### 
        """

    prompt += f"""
### DATA: "{data['Data']}" ### 
        """

    if data['Details'] != "":
        prompt += f"""
### DETAILS: "{data['Details']}" ### 
        """

    prompt += """
Sei uno strumento intelligente capace di identificare un modello e di applicarlo ai dati forniti. La tua missione è assistere un utente che inserisce un testo contenente un modello [PATTERN], dei dati sui quali ripetere tale modello [DATA] 
    """

    if data['Details'] != "":
        prompt += """
e una descrizione che fornisce istruzioni aggiuntive su come identificare correttamente il modello [DETAILS] 
        """

    prompt += """
. Devi procedere step by step: innanzitutto, riconoscere il modello all'interno del testo fornito dall'utente; successivamente, applicare il modello riconosciuto ai dati forniti. 
### PATTERN APPLICATO AI NUOVI DATI ###
    """

    return replace_newlines_with_space(prompt)


def is_valid_text_utility_form_compilation(data):

    if data['Text'] != '':
        return True

    return False


def generate_text_utility_prompt(data):

    prompt = ""

    if not is_valid_text_utility_form_compilation(data):
        prompt += "error"
        return prompt

    prompt += f"""
### TEXT: "{data['Text']}" ###
    """

    if data['Style'] != "":
        prompt += f"""
### STYLE: "{data['Style']}" ###
    """

    if data["Language"] == "Italian":
        prompt += """
Sei un esperto professore di letteratura italiana e sei stato chiamato a fornire assistenza a un utente che ha scritto il seguente testo [TEXT], in cui la grammatica non è perfetta e la chiarezza è compromessa. Il tuo obiettivo è analizzare attentamente il testo [TEXT] al fine di comprendere appieno i ragionamenti logici che vengono espressi. Successivamente, devi riscrivere il testo [TEXT] in una forma grammaticalmente perfetta e assicurarti che i concetti siano espressi con la massima chiarezza e senza ambiguità. La tua competenza è fondamentale per aiutare l'utente a comunicare in modo efficace attraverso il testo. Nella risposta, devi includere esclusivamente il testo richiesto, senza ulteriori spiegazioni o commenti.
        """

        if data["Translate"] == "Yes":
            prompt += """
In aggiunta, è necessario tradurre il testo in lingua inglese mantenendo una forma grammaticalmente perfetta e assicurandoti che i concetti siano espressi con la massima chiarezza e senza ambiguità.
            """

        if data["Style"] != "":
            prompt += """
In aggiunta, il testo deve essere redatto seguendo lo stile [STYLE].            
                """

        if data["Simplify"] == "Yes":
            prompt += """
In aggiunta, è necessario semplificare il testo eliminando le parti ridondanti e spiegando i concetti espressi nel modo più semplice e chiaro possibile.
            """
        elif data["Simplify"] == "No":
            prompt += """
In aggiunta, il testo deve essere completo, senza omettere alcuna informazione o concetto espresso.
            """

        if data["In-Depth Analysis"] == "Yes":
            prompt += """
In aggiunta, analizza attentamente il testo [TEXT] per comprendere i ragionamenti logici espressi e la materia di cui si sta trattando, e arricchisci il contenuto aggiungendo ulteriori dettagli di tua conoscenza che risultino pertinenti al contesto.
            """
        elif data["In-Depth Analysis"] == "No":
            prompt += """
In aggiunta, analizza attentamente il testo [TEXT] per comprendere i ragionamenti logici espressi e di cosa si sta parlando. Ricordati di non aggiungere niente che vada oltre questi ragionamenti.
            """

        if data["Length"] > 0:
            prompt += """
In aggiunta, il testo deve avere una lunghezza massima di [LENGTH].
            """

    elif data["Language"] == "English":
        prompt += """
You are an expert professor of english literature and have been called upon to assist a user who has written the following text [TEXT], in which the grammar is not perfect, and clarity is compromised. Your goal is to carefully analyze the text [TEXT] to fully understand the logical reasoning being expressed. Subsequently, you must rewrite the text [TEXT] in a grammatically perfect form and ensure that the concepts are expressed with the utmost clarity and without ambiguity. Your expertise is crucial in helping the user communicate effectively through the text. In your response, you should include exclusively the requested text, without additional explanations or comments.
                """

        if data["Translate"] == "Yes":
            prompt += """
Additionally, it is necessary to translate the text into Italian while maintaining grammatical perfection and ensuring that the concepts are expressed with the utmost clarity and without ambiguity.
                    """

        if data["Style"] != "":
            prompt += """
Additionally, the text must be composed following the [STYLE] style.            
                        """

        if data["Simplify"] == "Yes":
            prompt += """
Additionally, it is necessary to simplify the text by removing redundant parts and explaining the concepts in the simplest and clearest manner possible.
                    """
        elif data["Simplify"] == "No":
            prompt += """
Additionally, the text must be comprehensive, without omitting any expressed information or concepts.
                    """

        if data["In-Depth Analysis"] == "Yes":
            prompt += """
Additionally, carefully analyze the text [TEXT] to understand the logical reasoning presented and the subject matter at hand, and enhance the content by adding additional details from your knowledge that are relevant to the context.
                    """
        elif data["In-Depth Analysis"] == "No":
            prompt += """
Additionally, carefully analyze the text [TEXT] to understand the logical reasoning expressed within and the subject matter, and enhance the content without including any additional reasoning beyond what is already provided.
                    """

        if data["Length"] > 0:
            prompt += """
Additionally, the text must have a maximum length of [LENGTH].
                    """

    return replace_newlines_with_space(prompt)


def is_valid_lyrics_form_compilation(data):

    if data['Plot'] != '' and data['Language'] != '':
        return True

    return False


def generate_lyrics_prompt(data):

    prompt = ""

    if not is_valid_lyrics_form_compilation(data):
        prompt += "error"
        return prompt

    prompt += f"""
### PLOT: "{data['Plot']}" ###

### LANGUAGE: "{data['Language']}" ###

Sei un rinomato autore di testi musicali in lingua [LANGUAGE], e ti è stato richiesto di assistere un cantante che ha ideato una trama specifica per una canzone [PLOT], la quale narra una scena di profondo significato. Il tuo compito primario è di analizzare minuziosamente questa trama per comprendere a fondo sia la scena che le implicazioni logiche ed emotive. Dovrai poi scrivere un testo per la canzone in lingua [LANGUAGE], assicurandoti che tanto la scena quanto i ragionamenti logici ed emotivi siano presentati chiaramente e senza ambiguità. La tua abilità è cruciale per supportare il cantante nell'esprimere efficacemente il messaggio che intende trasmettere al suo pubblico. Nella tua risposta, dovrai limitarti a includere solo il testo richiesto, senza ulteriori spiegazioni o commenti.
    """

    if data["Songwriter Style"] != "":
        prompt += f"""
### SONGWRITER STYLE: "{data['Songwriter Style']}" ###

Il testo in lingua [LANGUAGE] dovrà essere scritto seguendo lo stile specifico del cantautore [SONGWRITER STYLE].
                """

    if data["Rhyme Type"] != "":
        prompt += f"""
### RHYME TYPE: "{data['Rhyme Type']}" ###

Il testo dovrà essere scritto utilizzando il seguente tipo di rima [RHYME TYPE]. 
        """

    if data["Structure"] != "":
        prompt += f"""
### SONG STRUCTURE AND NUMBER OF VERSES PER SECTION: "{data['Structure']}" ###

La canzone avrà la seguente struttura ben definita con un numero preciso di versi definiti per ogni sezione [STRUCTURE].          
            """

    if data["Syllables For Verse"] != "":
        prompt += f"""
### SYLLABLES FOR VERSE: "{data['Syllables For Verse']}" ###

Il testo dovrà essere scritto tale che ogni verso dovrà contenere il seguente numero di sillabe [SYLLABLES FOR VERSE].
        """

    return replace_newlines_with_space(prompt)


def replace_newlines_with_space(input_string):
    return input_string.replace('\n', ' ')


def main():

    st.title("TechInsight Hub")
    tab = st.selectbox("Select Tab", ["Learning", "Documentation", "Crafting", "Debugging", "Pattern", "Text Utilities", "Lyrics"])

    if tab == "Learning":
        st.subheader("Learning Tab")
        theme = st.text_input("Theme")
        topic = st.text_input("Topic")
        details = st.text_area("Details")
        questions = st.text_area("Questions")
        what_i_know = st.text_area("What I Know")

        if st.button("Generate Prompt"):
            data = {
                "Theme": theme,
                "Topic": topic,
                "Details": details,
                "Questions": questions,
                "What I Know": what_i_know
            }
            prompt = generate_learning_prompt(data)
            st.text(prompt)
            pyperclip.copy(prompt)

    if tab == "Documentation":
        st.subheader("Documentation Tab")
        array_documentation_type = ["Text", "Code"]

        programming_language = st.text_input("Programming Language")
        library_package = st.text_input("Library | Package")
        source_code = st.text_area("Source Code")
        questions = st.text_area("Questions")
        documentation_type = st.selectbox("Documentation Type", array_documentation_type, index=array_documentation_type.index("Text"))

        if st.button("Generate Prompt"):
            data = {
                "Programming Language": programming_language,
                "Library | Package": library_package,
                "Source Code": source_code,
                "Questions": questions,
                "Documentation Type": documentation_type
            }
            prompt = generate_documentation_prompt(data)
            st.text(prompt)
            pyperclip.copy(prompt)

    elif tab == "Crafting":
        st.subheader("Crafting Tab")
        array_answers = ["Yes", "No"]

        default_non_functional_requirements = """- Rendere il codice sorgente più leggibile e manutenibile, sostituendo gli algoritmi manuali con librerie standard.
- Assicurare che il codice rispetti le migliori pratiche di [PROGRAMMING LANGUAGE].
- Ridurre la complessità computazionale e, se possibile, anche quella spaziale.
- Rafforzare la robustezza del software, gestendo eccezioni e scenari vari e verificando l'accuratezza dei dati.
- Organizzare il codice in sottosistemi indipendenti per facilitare il riutilizzo e migliorare la manutenibilità.
- Semplificare la logica del software, mantenendone però la funzionalità originale.
- Utilizzare nomi per le classi, le variabili e le funzioni che siano descrittivi ed esplicativi del loro contenuto, evitando però eccessiva estensione."""

        programming_language = st.text_input("Programming Language")
        library_package = st.text_input("Library | Package To Use")
        details = st.text_area("Details")
        source_code = st.text_area("Source Code")
        non_functional_requirements = st.text_area("Non-Functional Requirements",
                                                   value=default_non_functional_requirements)
        design_pattern = st.text_area("Design Pattern")
        documentation = st.selectbox("Documentation", array_answers, index=array_answers.index("Yes"))

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
            prompt = generate_crafting_prompt(data)
            st.text(prompt)
            pyperclip.copy(prompt)

    elif tab == "Debugging":
        st.subheader("Debugging Tab")
        programming_language = st.text_input("Programming Language")
        library_package = st.text_input("Library | Package")
        source_code = st.text_area("Source Code")
        error = st.text_area("Compilation | Runtime Error")
        details = st.text_area("Details")

        if st.button("Generate Prompt"):
            data = {
                "Programming Language": programming_language,
                "Library | Package": library_package,
                "Source Code": source_code,
                "Compilation | Runtime Error": error,
                "Details": details
            }
            prompt = generate_debugging_prompt(data)
            st.text(prompt)
            pyperclip.copy(prompt)

    elif tab == "Pattern":
        st.subheader("Pattern Tab")

        pattern = st.text_area("Pattern")
        data = st.text_area("Data")
        details = st.text_area("Details")

        if st.button("Generate Prompt"):
            data = {
                "Pattern": pattern,
                "Data": data,
                "Details": details
            }
            prompt = generate_pattern_prompt(data)
            st.text(prompt)
            pyperclip.copy(prompt)

    elif tab == "Text Utilities":
        st.subheader("Text Utilities Tab")

        array_languages = ["Italian", "English"]
        array_answers = ["Yes", "No"]

        text = st.text_area("Text")
        language = st.selectbox("Language", array_languages, index=array_languages.index("Italian"))
        translate = st.selectbox("Translate", array_answers, index=array_answers.index("No"))
        style = st.text_area("Style")
        simplify = st.selectbox("Simplify", array_answers, index=array_answers.index("No"))
        in_depth_analysis = st.selectbox("In-Depth Analysis", array_answers, index=array_answers.index("No"))
        length = st.number_input("Length", min_value=0, max_value=4000, value=0, step=1)

        if st.button("Generate Prompt"):
            data = {
                "Text": text,
                "Language": language,
                "Translate": translate,
                "Style": style,
                "Simplify": simplify,
                "In-Depth Analysis": in_depth_analysis,
                "Length": length
            }
            prompt = generate_text_utility_prompt(data)
            st.text(prompt)
            pyperclip.copy(prompt)

    elif tab == "Lyrics":
        st.subheader("Lyrics Tab")

        plot = st.text_area("Plot")
        language = st.text_area("Language")
        songwriter_style = st.text_area("Songwriter Style")
        rhyme_type = st.text_area("Rhyme Type")
        structure = st.text_area("Structure")
        syllables_for_verse = st.text_area("Syllables For Verse")

        if st.button("Generate Prompt"):
            data = {
                "Plot": plot,
                "Language": language,
                "Songwriter Style": songwriter_style,
                "Rhyme Type": rhyme_type,
                "Structure": structure,
                "Syllables For Verse": syllables_for_verse
            }
            prompt = generate_lyrics_prompt(data)
            st.text(prompt)
            pyperclip.copy(prompt)

    st.markdown("<hr>", unsafe_allow_html=True)
    st.markdown("Made by Aldo Manco")

if __name__ == "__main__":
    main()
