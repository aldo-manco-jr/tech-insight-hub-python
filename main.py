import streamlit as st
import pyperclip

import documentation_prompt
import learning_prompt
import debugging_prompt
import crafting_prompt



st.set_page_config(
    page_title="TechInsight Hub",
    page_icon="icon/rocket_ship.png",
)

def generate_learning_prompt(data):

    # Print values one by one
    if data['Theme'] != "":
        if data['Topic'] != "":
            if data['Details'] != "":
                prompt = generate_learning_details_prompt(data)
            else:
                prompt = generate_learning_topic_prompt(data)
        else:
            prompt = generate_learning_theme_prompt(data)
    else:
        prompt = 'error'

    return prompt


def generate_learning_theme_prompt(data):

    prompt = f"""
    ### SUBJECT: "{data['Theme']}" ###

    {learning_prompt.learning_theme_prompt}
            """

    return prompt


def generate_learning_topic_prompt(data):

    if data['What I Know'] != "":
        prompt = f"""
### SUBJECT: "{data['Theme']}" ###

### TOPIC: "{data['Topic']}" ###

### WHAT I KNOW: "{data['What I Know']}" ###

{learning_prompt.learning_topic_prompt_with_knowledge}
            """
    else:
        prompt = f"""
### SUBJECT: "{data['Theme']}" ###

### TOPIC: "{data['Topic']}" ###

{learning_prompt.learning_topic_prompt}
            """

    return prompt


def generate_learning_details_prompt(data):

    if data['What I Know'] != "":
        prompt = f"""
### SUBJECT: "{data['Theme']}" ###

### TOPIC: "{data['Topic']}" ###

### DETAILS: "{data['Details']}" ###

### WHAT I KNOW: "{data['What I Know']}" ###

{learning_prompt.learning_details_prompt_with_knowledge}
            """
    else:
        prompt = f"""
### SUBJECT: "{data['Theme']}" ###

### TOPIC: "{data['Topic']}" ###

### DETAILS: "{data['Details']}" ###

{learning_prompt.learning_details_prompt}
            """

    return prompt


def generate_documentation_prompt(data):

    # Print values one by one
    if data['Source Code'] != "":
        if data['Question'] != "":
            if data['Programming Language'] != "":
                prompt = generate_documentation_explained_known_doubt_prompt(data)
            else:
                prompt = generate_documentation_explained_doubt_prompt(data)
        else:
            if data['Programming Language']:
                prompt = generate_documentation_documented_known_code_prompt(data)
            else:
                prompt = generate_documentation_documented_code_prompt(data)
    else:
        prompt = 'error'

    if prompt != "error":
        if data['Documentation Type'] == "Text":
            prompt += "La spiegazione del codice sorgente [SOURCE CODE] deve essere articolata ragionando passo dopo passo, seguendo una logica precisa. È importante mostrare a video e spiegare un frammento di codice alla volta, accompagnando ciascuna parte con una spiegazione dettagliata. Questa spiegazione deve essere redatta in un italiano grammaticalmente impeccabile, garantendo che i concetti siano espressi con la massima chiarezza e privi di ogni ambiguità. La tua expertise è cruciale per guidare l'utente nella comprensione efficace del codice sorgente [SOURCE CODE]."
            prompt += "### SPIEGAZIONE DEL CODICE SORGENTE ###"
        else:
            prompt += "Crea una documentazione del codice sorgente [SOURCE CODE] con un commento sopra ogni classe e funzione, descrivendo tutte le informazioni, attributi, funzionalità ed eventuali parametri utilizzando anche le annotazioni. La tua documentazione deve essere scritta in una forma grammaticalmente perfetta, e assicurati che i concetti siano espressi con la massima chiarezza e senza ambiguità. La tua competenza è fondamentale per aiutare l'utente a comprendere in modo efficace il codice sorgente [SOURCE CODE]."
            prompt += "### DOCUMENTAZIONE DEL CODICE SORGENTE ###"

    return prompt


def generate_documentation_explained_known_doubt_prompt(data):

    if data['Library | Package'] != "" and data['Programming Language'] != "":
        prompt = f"""
### PROGRAMMING LANGUAGE: "{data['Programming Language']}" ###

### LIBRARY | PACKAGE: "{data['Library | Package']}" ###

### SOURCE CODE: "{data['Source Code']}" ###

### QUESTION: "{data['Question']}" ###

{documentation_prompt.documentation_explained_known_doubt_prompt_with_library}
            """
    else:
        prompt = f"""
### PROGRAMMING LANGUAGE: "{data['Programming Language']}" ###

### SOURCE CODE: "{data['Source Code']}" ###

### QUESTION: "{data['Question']}" ###

{documentation_prompt.documentation_explained_known_doubt_prompt}
            """

    return prompt


def generate_documentation_explained_doubt_prompt(data):

    prompt = f"""
### SOURCE CODE: "{data['Source Code']}" ###

### QUESTION: "{data['Question']}" ###

{documentation_prompt.documentation_explained_doubt_prompt}
                """

    return prompt


def generate_documentation_documented_known_code_prompt(data):

    if data['Library | Package'] != "" and data['Programming Language'] != "":
        prompt = f"""
### PROGRAMMING LANGUAGE: "{data['Programming Language']}" ###

### LIBRARY | PACKAGE: "{data['Library | Package']}" ###

### SOURCE CODE: "{data['Source Code']}" ###

{documentation_prompt.documentation_documented_known_code_prompt_with_library}
            """
    else:
        prompt = f"""
### PROGRAMMING LANGUAGE: "{data['Programming Language']}" ###

### SOURCE CODE: "{data['Source Code']}" ###

{documentation_prompt.documentation_documented_known_code_prompt}
            """

    return prompt


def generate_documentation_documented_code_prompt(data):

    prompt = f"""
    ### SOURCE CODE: "{data['Source Code']}" ###

    {documentation_prompt.documentation_documented_code_prompt}
                """

    return prompt


def generate_debugging_prompt(data):

    if data['Programming Language'] != "":
        if data['Details'] != "":
            if data['Compilation | Runtime Error'] != "":
                if data['Source Code'] != "":
                    prompt = generate_debugging_located_detailed_runtime_prompt(data)
                else:
                    prompt = generate_debugging_detailed_runtime_prompt(data)
            else:
                if data['Source Code'] != "":
                    prompt = generate_debugging_detailed_correction_prompt(data)
                else:
                    prompt = generate_debugging_syntactic_prompt(data)
        else:
            if data['Compilation | Runtime Error'] != "":
                if data['Source Code'] != "":
                    prompt = generate_debugging_located_runtime_prompt(data)
                else:
                    prompt = generate_debugging_runtime_prompt(data)
            else:
                if data['Source Code'] != "":
                    prompt = generate_debugging_correction_prompt(data)
                else:
                    prompt = "error"
    else:
        prompt = "error"

    return prompt


def generate_debugging_detailed_runtime_prompt(data):

    if data['Library | Package'] != "":
        prompt = f"""
### PROGRAMMING LANGUAGE: "{data['Programming Language']}" ###

### LIBRARY | PACKAGE: "{data['Library | Package']}" ###

### DETAILS: "{data['Details']}" ###

### COMPILATION | RUNTIME ERROR: "{data['Compilation | Runtime Error']}" ###

{debugging_prompt.debugging_detailed_runtime_prompt_with_library}
            """
    else:
        prompt = f"""
### PROGRAMMING LANGUAGE: "{data['Programming Language']}" ###

### DETAILS: "{data['Details']}" ###

### COMPILATION | RUNTIME ERROR: "{data['Compilation | Runtime Error']}" ###

{debugging_prompt.debugging_detailed_runtime_prompt}
            """

    return prompt


def generate_debugging_located_runtime_prompt(data):

    if data['Library | Package'] != "":
        prompt = f"""
### PROGRAMMING LANGUAGE: "{data['Programming Language']}" ###

### LIBRARY | PACKAGE: "{data['Library | Package']}" ###

### SOURCE CODE: "{data['Source Code']}" ###

### COMPILATION | RUNTIME ERROR: "{data['Compilation | Runtime Error']}" ###

{debugging_prompt.debugging_located_runtime_prompt_with_library}
            """
    else:
        prompt = f"""
### PROGRAMMING LANGUAGE: "{data['Programming Language']}" ###

### SOURCE CODE: "{data['Source Code']}" ###

### COMPILATION | RUNTIME ERROR: "{data['Compilation | Runtime Error']}" ###

{debugging_prompt.debugging_located_runtime_prompt}
            """

    return prompt


def generate_debugging_detailed_correction_prompt(data):

    if data['Library | Package'] != "":
        prompt = f"""
### PROGRAMMING LANGUAGE: "{data['Programming Language']}" ###

### LIBRARY | PACKAGE: "{data['Library | Package']}" ###

### SOURCE CODE: "{data['Source Code']}" ###

### DETAILS: "{data['Details']}" ###

{debugging_prompt.debugging_detailed_correction_prompt_with_library}
            """
    else:
        prompt = f"""
### PROGRAMMING LANGUAGE: "{data['Programming Language']}" ###

### SOURCE CODE: "{data['Source Code']}" ###

### DETAILS: "{data['Details']}" ###

{debugging_prompt.debugging_detailed_correction_prompt}
            """

    return prompt


def generate_debugging_correction_prompt(data):

    if data['Library | Package'] != "":
        prompt = f"""
### PROGRAMMING LANGUAGE: "{data['Programming Language']}" ###

### LIBRARY | PACKAGE: "{data['Library | Package']}" ###

### SOURCE CODE: "{data['Source Code']}" ###

{debugging_prompt.debugging_correction_prompt_with_library}
            """
    else:
        prompt = f"""
### PROGRAMMING LANGUAGE: "{data['Programming Language']}" ###

### SOURCE CODE: "{data['Source Code']}" ###

{debugging_prompt.debugging_correction_prompt}
            """

    return prompt


def generate_debugging_located_detailed_runtime_prompt(data):

    if data['Library | Package'] != "":
        prompt = f"""
### PROGRAMMING LANGUAGE: "{data['Programming Language']}" ###

### LIBRARY | PACKAGE: "{data['Library | Package']}" ###

### DETAILS: "{data['Details']}" ###

### SOURCE CODE: "{data['Source Code']}" ###

### COMPILATION | RUNTIME ERROR: "{data['Compilation | Runtime Error']}" ###

{debugging_prompt.debugging_located_detailed_runtime_prompt_with_library}
            """
    else:
        prompt = f"""
### PROGRAMMING LANGUAGE: "{data['Programming Language']}" ###

### DETAILS: "{data['Details']}" ###

### SOURCE CODE: "{data['Source Code']}" ###

### COMPILATION | RUNTIME ERROR: "{data['Compilation | Runtime Error']}" ###

{debugging_prompt.debugging_located_detailed_runtime_prompt}
            """

    return prompt


def generate_debugging_syntactic_prompt(data):

    if data['Library | Package'] != "":
        prompt = f"""
### PROGRAMMING LANGUAGE: "{data['Programming Language']}" ###

### LIBRARY | PACKAGE: "{data['Library | Package']}" ###

### DETAILS: "{data['Details']}" ###

{debugging_prompt.debugging_syntactic_prompt_with_library}
            """
    else:
        prompt = f"""
### PROGRAMMING LANGUAGE: "{data['Programming Language']}" ###

### DETAILS: "{data['Details']}" ###

{debugging_prompt.debugging_syntactic_prompt}
            """

    return prompt


def generate_debugging_runtime_prompt(data):

    if data['Library | Package'] != "":
        prompt = f"""
### PROGRAMMING LANGUAGE: "{data['Programming Language']}" ###

### LIBRARY | PACKAGE: "{data['Library | Package']}" ###

### COMPILATION | RUNTIME ERROR: "{data['Compilation | Runtime Error']}" ###

{debugging_prompt.debugging_runtime_prompt_with_library}
            """
    else:
        prompt = f"""
### PROGRAMMING LANGUAGE: "{data['Programming Language']}" ###

### COMPILATION | RUNTIME ERROR: "{data['Compilation | Runtime Error']}" ###

{debugging_prompt.debugging_runtime_prompt}
            """

    return prompt


def generate_crafting_prompt(data):

    if data['Programming Language'] != "":
        if data['Details'] != "":
            if data['Design Pattern'] != "":
                if data['Source Code'] != "":
                    prompt = generate_crafting_edited_structured_implementation_prompt(data)
                else:
                    prompt = generate_crafting_structured_implementation_prompt(data)
            else:
                if data['Source Code'] != "":
                    prompt = generate_crafting_edited_implementation_prompt(data)
                else:
                    prompt = generate_crafting_implementation_prompt(data)
        else:
            if data['Design Pattern'] != "":
                if data['Source Code'] != "":
                    prompt = generate_crafting_designed_implementation_prompt(data)
                else:
                    prompt = generate_crafting_structure_prompt(data)
            else:
                if data['Source Code'] != "":
                    prompt = generate_crafting_improved_implementation_prompt(data)
                else:
                    prompt = "error"
    else:
        prompt = "error"

    if prompt != "error":
        if data["Documentation"] == "Yes":
            prompt += """
Crea una documentazione con un commento sopra ogni classe e funzione, descrivendo tutte le informazioni, attributi, funzionalità ed eventuali parametri utilizzando anche le annotazioni. La tua documentazione deve essere scritta in una forma grammaticalmente perfetta, e assicurati che i concetti siano espressi con la massima chiarezza e senza ambiguità. La tua competenza è fondamentale per aiutare l'utente a comunicare in modo efficace la tua implementazione.
            """
        elif data["Documentation"] == "No":
            prompt += """
Non commentare il codice, evita di descrivere le informazioni, attributi, funzionalità ed eventuali parametri utilizzando annotazioni.
            """
        prompt += """
        
### IMPLEMENTAZIONE PROPOSTA ###
        """

    return prompt


def generate_crafting_structure_prompt(data):

    if data['Library | Package'] != "":
        prompt = f"""
### PROGRAMMING LANGUAGE: "{data['Programming Language']}" ###

### LIBRARY | PACKAGE: "{data['Library | Package']}" ###

### DESIGN PATTERN: "{data['Design Pattern']}" ###

{crafting_prompt.crafting_structure_prompt_with_library}
            """
    else:
        prompt = f"""
### PROGRAMMING LANGUAGE: "{data['Programming Language']}" ###

### DESIGN PATTERN: "{data['Design Pattern']}" ###

{crafting_prompt.crafting_structure_prompt}
            """

    return prompt


def generate_crafting_implementation_prompt(data):

    if data['Library | Package'] != "":
        prompt = f"""
### PROGRAMMING LANGUAGE: "{data['Programming Language']}" ###

### LIBRARY | PACKAGE: "{data['Library | Package']}" ###

### DETAILS: "{data['Details']}" ###

{crafting_prompt.crafting_implementation_prompt_with_library}
            """
    else:
        prompt = f"""
### PROGRAMMING LANGUAGE: "{data['Programming Language']}" ###

### DETAILS: "{data['Details']}" ###

{crafting_prompt.crafting_implementation_prompt}
            """

    return prompt


def generate_crafting_structured_implementation_prompt(data):

    if data['Library | Package'] != "":
        prompt = f"""
### PROGRAMMING LANGUAGE: "{data['Programming Language']}" ###

### LIBRARY | PACKAGE: "{data['Library | Package']}" ###

### DETAILS: "{data['Details']}" ###

### DESIGN PATTERN: "{data['Design Pattern']}" ###

{crafting_prompt.crafting_structured_implementation_prompt_with_library}
            """
    else:
        prompt = f"""
### PROGRAMMING LANGUAGE: "{data['Programming Language']}" ###

### DETAILS: "{data['Details']}" ###

### DESIGN PATTERN: "{data['Design Pattern']}" ###

{crafting_prompt.crafting_structured_implementation_prompt}
            """

    return prompt


def generate_crafting_edited_structured_implementation_prompt(data):

    if data['Library | Package'] != "":
        prompt = f"""
### PROGRAMMING LANGUAGE: "{data['Programming Language']}" ###

### LIBRARY | PACKAGE: "{data['Library | Package']}" ###

### DESIGN PATTERN: "{data['Design Pattern']}" ###

### DETAILS: "{data['Details']}" ###

### SOURCE CODE: "{data['Source Code']}" ###

{crafting_prompt.crafting_edited_structured_implementation_prompt_with_library}
            """
    else:
        prompt = f"""
### PROGRAMMING LANGUAGE: "{data['Programming Language']}" ###

### DESIGN PATTERN: "{data['Design Pattern']}" ###

### DETAILS: "{data['Details']}" ###

### SOURCE CODE: "{data['Source Code']}" ###

{crafting_prompt.crafting_edited_structured_implementation_prompt}
            """

    return prompt


def generate_crafting_designed_implementation_prompt(data):

    if data['Library | Package'] != "":
        prompt = f"""
### PROGRAMMING LANGUAGE: "{data['Programming Language']}" ###

### LIBRARY | PACKAGE: "{data['Library | Package']}" ###

### DESIGN PATTERN: "{data['Design Pattern']}" ###

### SOURCE CODE: "{data['Source Code']}" ###

{crafting_prompt.crafting_designed_implementation_prompt_with_library}
            """
    else:
        prompt = f"""
### PROGRAMMING LANGUAGE: "{data['Programming Language']}" ###

### DESIGN PATTERN: "{data['Design Pattern']}" ###

### SOURCE CODE: "{data['Source Code']}" ###

{crafting_prompt.crafting_designed_implementation_prompt}
            """

    return prompt


def generate_crafting_improved_implementation_prompt(data):

    if data['Library | Package'] != "":
        prompt = f"""
### PROGRAMMING LANGUAGE: "{data['Programming Language']}" ###

### LIBRARY | PACKAGE: "{data['Library | Package']}" ###

### SOURCE CODE: "{data['Source Code']}" ###

{crafting_prompt.crafting_improved_implementation_prompt_with_library}
            """
    else:
        prompt = f"""
### PROGRAMMING LANGUAGE: "{data['Programming Language']}" ###

### SOURCE CODE: "{data['Source Code']}" ###

{crafting_prompt.crafting_improved_implementation_prompt}
            """

    return prompt


def generate_crafting_edited_implementation_prompt(data):

    if data['Library | Package'] != "":
        prompt = f"""
### PROGRAMMING LANGUAGE: "{data['Programming Language']}" ###

### LIBRARY | PACKAGE: "{data['Library | Package']}" ###

### DETAILS: "{data['Details']}" ###

### SOURCE CODE: "{data['Source Code']}" ###

{crafting_prompt.crafting_edited_implementation_prompt_with_library}
            """
    else:
        prompt = f"""
### PROGRAMMING LANGUAGE: "{data['Programming Language']}" ###

### DETAILS: "{data['Details']}" ###

### SOURCE CODE: "{data['Source Code']}" ###

{crafting_prompt.crafting_edited_implementation_prompt}
            """

    return prompt


def generate_text_utility_prompt(data):
    prompt = f"""
### TEXT: "{data['Text']}" ###

### LANGUAGE: "{data['Language']}" ###

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

        if data["Length"] > 0:
            prompt += """
Additionally, the text must have a maximum length of [LENGTH].
                    """

    return prompt


def generate_lyrics_prompt(data):
    prompt = f"""
### PLOT: "{data['Plot']}" ###

### LANGUAGE: "{data['Language']}" ###
            """

    if data["Plot"] != "" and data["Language"] != "":
        prompt += f"""
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
    else:
        prompt = 'error'

    return prompt

def main():

    st.title("TechInsight Hub")
    tab = st.selectbox("Select Tab", ["Learning", "Documentation", "Debugging", "Crafting", "Text Utilities", "Lyrics"])

    if tab == "Learning":
        st.subheader("Learning Tab")
        theme = st.text_input("Theme")
        topic = st.text_input("Topic")
        details = st.text_area("Details")
        what_i_know = st.text_area("What I Know")

        if st.button("Generate Prompt"):
            data = {
                "Theme": theme,
                "Topic": topic,
                "Details": details,
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
        question = st.text_area("Question")
        documentation_type = st.selectbox("Documentation Type", array_documentation_type, index=array_documentation_type.index("Text"))

        if st.button("Generate Prompt"):
            data = {
                "Programming Language": programming_language,
                "Library | Package": library_package,
                "Source Code": source_code,
                "Question": question,
                "Documentation Type": documentation_type
            }
            prompt = generate_documentation_prompt(data)
            st.text(prompt)
            pyperclip.copy(prompt)

    elif tab == "Debugging":
        st.subheader("Debugging Tab")
        programming_language = st.text_input("Programming Language")
        library_package = st.text_input("Library | Package")
        details = st.text_area("Details")
        error = st.text_area("Compilation | Runtime Error")
        source_code = st.text_area("Source Code")

        if st.button("Generate Prompt"):
            data = {
                "Programming Language": programming_language,
                "Library | Package": library_package,
                "Details": details,
                "Compilation | Runtime Error": error,
                "Source Code": source_code
            }
            prompt = generate_debugging_prompt(data)
            st.text(prompt)
            pyperclip.copy(prompt)

    elif tab == "Crafting":
        st.subheader("Crafting Tab")
        array_answers = ["Yes", "No"]

        programming_language = st.text_input("Programming Language")
        library_package = st.text_input("Library | Package To Use")
        design_pattern = st.text_input("Design Pattern")
        details = st.text_area("Details")
        source_code = st.text_area("Source Code")
        documentation = st.selectbox("Documentation", array_answers, index=array_answers.index("Yes"))

        if st.button("Generate Prompt"):
            data = {
                "Programming Language": programming_language,
                "Library | Package": library_package,
                "Design Pattern": design_pattern,
                "Details": details,
                "Source Code": source_code,
                "Documentation": documentation
            }
            prompt = generate_crafting_prompt(data)
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
