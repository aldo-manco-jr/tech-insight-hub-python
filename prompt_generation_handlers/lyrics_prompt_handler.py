# lyrics_prompt_handler.py

import utils


def is_valid_lyrics_form_compilation(data):
    if (data['Plot'] != '' and
            data['Language Lyrics'] != ''
    ):
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

    return utils.replace_newlines_with_space(italian_prompt), utils.replace_newlines_with_space(english_prompt)
