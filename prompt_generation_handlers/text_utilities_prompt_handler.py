# text_utilities_prompt_handler.py

import utils


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
Sei un esperto professore di letteratura 
    """
    english_prompt += """
You are an expert professor of 
    """

    if data['Translate'] == 'Yes':
        italian_prompt += """
italiana e inglese 
        """
        english_prompt += """
english and italian 
        """
    elif data['Translate'] == 'No':
        italian_prompt += """
italiana 
        """
        english_prompt += """
english 
        """

    italian_prompt += """
e sei stato chiamato a fornire assistenza a un utente che ha scritto il seguente testo [TEXT], in cui la grammatica non è perfetta e la chiarezza è compromessa. Il tuo obiettivo è analizzare attentamente il testo [TEXT] al fine di comprendere appieno i ragionamenti logici che vengono espressi. Successivamente, devi riscrivere il testo [TEXT] in una forma grammaticalmente perfetta e assicurarti che i concetti siano espressi con la massima chiarezza e senza ambiguità. La tua competenza è fondamentale per aiutare l'utente a comunicare in modo efficace attraverso il testo. Nella risposta, devi includere esclusivamente il testo richiesto, senza ulteriori spiegazioni o commenti. 
    """
    english_prompt += """
literature and have been called upon to assist a user who has written the following text [TEXT], in which the grammar is not perfect, and clarity is compromised. Your goal is to carefully analyze the text [TEXT] to fully understand the logical reasoning being expressed. Subsequently, you must rewrite the text [TEXT] in a grammatically perfect form and ensure that the concepts are expressed with the utmost clarity and without ambiguity. Your expertise is crucial in helping the user communicate effectively through the text. In your response, you should include exclusively the requested text, without additional explanations or comments. 
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

    return utils.replace_newlines_with_space(italian_prompt), utils.replace_newlines_with_space(english_prompt)
