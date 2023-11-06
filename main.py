import streamlit as st
import pyperclip
import learning_prompt
import debugging_prompt
import crafting_prompt



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

    if data['What I Know'] != "":
        prompt = f"""
### SUBJECT: {data['Theme']} ###

### WHAT I KNOW: {data['What I Know']} ###

{learning_prompt.learning_theme_prompt_with_knowledge}
        """
    else:
        prompt = f"""
### SUBJECT: {data['Theme']} ###

{learning_prompt.learning_theme_prompt}
        """

    return prompt


def generate_learning_topic_prompt(data):

    if data['What I Know'] != "":
        prompt = f"""
### SUBJECT: {data['Theme']} ###

### TOPIC: {data['Topic']} ###

### WHAT I KNOW: {data['What I Know']} ###

{learning_prompt.learning_topic_prompt_with_knowledge}
            """
    else:
        prompt = f"""
### SUBJECT: {data['Theme']} ###

### TOPIC: {data['Topic']} ###

{learning_prompt.learning_topic_prompt}
            """

    return prompt


def generate_learning_details_prompt(data):

    if data['What I Know'] != "":
        prompt = f"""
### SUBJECT: {data['Theme']} ###

### TOPIC: {data['Topic']} ###

### DETAILS: {data['Details']} ###

### WHAT I KNOW: {data['What I Know']} ###

{learning_prompt.learning_details_prompt_with_knowledge}
            """
    else:
        prompt = f"""
### SUBJECT: {data['Theme']} ###

### TOPIC: {data['Topic']} ###

### DETAILS: {data['Details']} ###

{learning_prompt.learning_details_prompt}
            """

    return prompt


def generate_debugging_prompt(data):

    if data['Programming Language'] != "":
        if data['Details'] != "":
            if data['Compilation | Runtime Error'] != "":
                prompt = generate_debugging_detailed_runtime_prompt(data)
            else:
                prompt = generate_debugging_syntactic_prompt(data)
        else:
            if data['Compilation | Runtime Error'] != "":
                prompt = generate_debugging_runtime_prompt(data)
            else:
                prompt = 'error'
    else:
        prompt = 'error'

    return prompt


def generate_debugging_detailed_runtime_prompt(data):

    if data['Library | Package'] != "":
        prompt = f"""
### PROGRAMMING LANGUAGE: {data['Programming Language']} ###

### LIBRARY | PACKAGE: {data['Library | Package']} ###

### DETAILS: {data['Details']} ###

### COMPILATION | RUNTIME ERROR: {data['Compilation | Runtime Error']} ###

{debugging_prompt.debugging_detailed_runtime_prompt_with_library}
            """
    else:
        prompt = f"""
### PROGRAMMING LANGUAGE: {data['Programming Language']} ###

### DETAILS: {data['Details']} ###

### COMPILATION | RUNTIME ERROR: {data['Compilation | Runtime Error']} ###

{debugging_prompt.debugging_detailed_runtime_prompt}
            """

    return prompt


def generate_debugging_syntactic_prompt(data):

    if data['Library | Package'] != "":
        prompt = f"""
### PROGRAMMING LANGUAGE: {data['Programming Language']} ###

### LIBRARY | PACKAGE: {data['Library | Package']} ###

### DETAILS: {data['Details']} ###

{debugging_prompt.debugging_syntactic_prompt_with_library}
            """
    else:
        prompt = f"""
### PROGRAMMING LANGUAGE: {data['Programming Language']} ###

### DETAILS: {data['Details']} ###

{debugging_prompt.debugging_syntactic_prompt}
            """

    return prompt


def generate_debugging_runtime_prompt(data):

    if data['Library | Package'] != "":
        prompt = f"""
### PROGRAMMING LANGUAGE: {data['Programming Language']} ###

### LIBRARY | PACKAGE: {data['Library | Package']} ###

### COMPILATION | RUNTIME ERROR: {data['Compilation | Runtime Error']} ###

{debugging_prompt.debugging_runtime_prompt_with_library}
            """
    else:
        prompt = f"""
### PROGRAMMING LANGUAGE: {data['Programming Language']} ###

### COMPILATION | RUNTIME ERROR: {data['Compilation | Runtime Error']} ###

{debugging_prompt.debugging_runtime_prompt}
            """

    return prompt


def generate_crafting_prompt(data):

    if data['Programming Language'] != "":
        if data['Details'] != "":
            if data['Design Pattern'] != "":
                prompt = generate_crafting_structured_implementation_prompt(data)
            else:
                prompt = generate_crafting_implementation_prompt(data)
        else:
            if data['Design Pattern'] != "":
                prompt = generate_crafting_structure_prompt(data)
            else:
                prompt = "error"
    else:
        prompt = "error"

    return prompt


def generate_crafting_structure_prompt(data):

    if data['Library | Package'] != "":
        prompt = f"""
### PROGRAMMING LANGUAGE: {data['Programming Language']} ###

### LIBRARY | PACKAGE: {data['Library | Package']} ###

### DESIGN PATTERN: {data['Design Pattern']} ###

{crafting_prompt.crafting_structure_prompt_with_library}
            """
    else:
        prompt = f"""
### PROGRAMMING LANGUAGE: {data['Programming Language']} ###

### DESIGN PATTERN: {data['Design Pattern']} ###

{crafting_prompt.crafting_structure_prompt}
            """

    return prompt


def generate_crafting_implementation_prompt(data):

    if data['Library | Package'] != "":
        prompt = f"""
### PROGRAMMING LANGUAGE: {data['Programming Language']} ###

### LIBRARY | PACKAGE: {data['Library | Package']} ###

### DETAILS: {data['Details']} ###

{crafting_prompt.crafting_implementation_prompt_with_library}
            """
    else:
        prompt = f"""
### PROGRAMMING LANGUAGE: {data['Programming Language']} ###

### DETAILS: {data['Details']} ###

{crafting_prompt.crafting_implementation_prompt}
            """

    return prompt


def generate_crafting_structured_implementation_prompt(data):

    if data['Library | Package'] != "":
        prompt = f"""
### PROGRAMMING LANGUAGE: {data['Programming Language']} ###

### LIBRARY | PACKAGE: {data['Library | Package']} ###

### DETAILS: {data['Details']} ###

### DESIGN PATTERN: {data['Design Pattern']} ###

{crafting_prompt.crafting_structured_implementation_prompt_with_library}
            """
    else:
        prompt = f"""
### PROGRAMMING LANGUAGE: {data['Programming Language']} ###

### DETAILS: {data['Details']} ###

### DESIGN PATTERN: {data['Design Pattern']} ###

{crafting_prompt.crafting_structured_implementation_prompt}
            """

    return prompt


def main():
    st.title("TechInsight Hub")
    tab = st.selectbox("Select Tab", ["Learning", "Debugging", "Crafting"])

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
            st.text("Generated Prompt:")
            st.text(prompt)
            pyperclip.copy(prompt)

    elif tab == "Debugging":
        st.subheader("Debugging Tab")
        programming_language = st.text_input("Programming Language")
        library_package = st.text_input("Library | Package")
        details = st.text_area("Details")
        error = st.text_area("Compilation | Runtime Error")

        if st.button("Generate Prompt"):
            data = {
                "Programming Language": programming_language,
                "Library | Package": library_package,
                "Details": details,
                "Compilation | Runtime Error": error
            }
            prompt = generate_debugging_prompt(data)
            st.text("Generated Prompt:")
            st.text(prompt)
            pyperclip.copy(prompt)

    elif tab == "Crafting":
        st.subheader("Crafting Tab")
        programming_language = st.text_input("Programming Language")
        library_package = st.text_input("Library | Package To Use")
        design_pattern = st.text_input("Design Pattern")
        details = st.text_area("Details")

        if st.button("Generate Prompt"):
            data = {
                "Programming Language": programming_language,
                "Library | Package": library_package,
                "Design Pattern": design_pattern,
                "Details": details
            }
            prompt = generate_crafting_prompt(data)
            st.text("Generated Prompt:")
            st.text(prompt)
            pyperclip.copy(prompt)


if __name__ == "__main__":
    main()
