# learning_prompt_handler.py

import utils


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
        return utils.replace_newlines_with_space(italian_prompt), utils.replace_newlines_with_space(english_prompt)

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
        return utils.replace_newlines_with_space(italian_prompt), utils.replace_newlines_with_space(english_prompt)

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

    return utils.replace_newlines_with_space(italian_prompt), utils.replace_newlines_with_space(english_prompt)
