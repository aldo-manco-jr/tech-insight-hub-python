import streamlit as st
import pyperclip

from prompt_generation_handlers import learning_prompt_handler
from prompt_generation_handlers import documentation_prompt_handler
from prompt_generation_handlers import crafting_prompt_handler
from prompt_generation_handlers import debugging_prompt_handler
from prompt_generation_handlers import pattern_prompt_handler
from prompt_generation_handlers import text_utilities_prompt_handler
from prompt_generation_handlers import lyrics_prompt_handler

st.set_page_config(
    page_title="TechInsight Hub",
    page_icon="icon/rocket_ship.png",
)


def main():
    st.title("TechInsight Hub")

    tabs = [
        "Learning",
        "Documentation",
        "Crafting",
        "Debugging",
        "Pattern",
        "Text Utilities",
        "Lyrics"
    ]
    tab = st.selectbox("Select Tab", tabs)

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
            italian_prompt, english_prompt = learning_prompt_handler.generate_learning_prompt(data)
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
            italian_prompt, english_prompt = documentation_prompt_handler.generate_documentation_prompt(data)
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
            italian_prompt, english_prompt = crafting_prompt_handler.generate_crafting_prompt(data)
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
            italian_prompt, english_prompt = debugging_prompt_handler.generate_debugging_prompt(data)
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
            italian_prompt, english_prompt = pattern_prompt_handler.generate_pattern_prompt(data)
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
            italian_prompt, english_prompt = text_utilities_prompt_handler.generate_text_utility_prompt(data)
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
            italian_prompt, english_prompt = lyrics_prompt_handler.generate_lyrics_prompt(data)
            prompt = italian_prompt if language == "Italian" else english_prompt
            st.text(prompt)
            pyperclip.copy(prompt)

    st.markdown("<hr>", unsafe_allow_html=True)
    st.markdown("Made by Aldo Manco")


if __name__ == "__main__":
    main()
