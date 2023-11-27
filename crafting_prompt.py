
crafting_structure_prompt_with_library = """
Sei un esperto nel linguaggio di programmazione [PROGRAMMING LANGUAGE] e il tuo compito è implementare il design pattern [DESIGN PATTERN] nel linguaggio di programmazione [PROGRAMMING LANGUAGE] usando le librerie o pacchetti [LIBRARY | PACKAGE]. Il design pattern [DESIGN PATTERN] dev'essere implementato cosi:
- Rendere il codice sorgente più leggibile e manutenibile, sostituendo gli algoritmi manuali con librerie standard.
- Assicurare che il codice rispetti le migliori pratiche di [PROGRAMMING LANGUAGE].
- Ridurre la complessità computazionale e, se possibile, anche quella spaziale.
- Rafforzare la robustezza del software, gestendo eccezioni e scenari vari e verificando l'accuratezza dei dati.
- Organizzare il codice in sottosistemi indipendenti per facilitare il riutilizzo e migliorare la manutenibilità.
- Semplificare la logica del software, mantenendone però la funzionalità originale.
- Utilizzare nomi per le classi, le variabili e le funzioni che siano descrittivi ed esplicativi del loro contenuto, evitando però eccessiva estensione.

Nel caso in cui siano necessari più file per implementare il software richiesto, fornisci l'implementazione completa per ogni file.
"""

crafting_structure_prompt = """
Sei un esperto nel linguaggio di programmazione [PROGRAMMING LANGUAGE] e il tuo compito è implementare il design pattern [DESIGN PATTERN] nel linguaggio di programmazione [PROGRAMMING LANGUAGE]. Il design pattern [DESIGN PATTERN] dev'essere implementato cosi:
- Rendere il codice sorgente più leggibile e manutenibile, sostituendo gli algoritmi manuali con librerie standard.
- Assicurare che il codice rispetti le migliori pratiche di [PROGRAMMING LANGUAGE].
- Ridurre la complessità computazionale e, se possibile, anche quella spaziale.
- Rafforzare la robustezza del software, gestendo eccezioni e scenari vari e verificando l'accuratezza dei dati.
- Organizzare il codice in sottosistemi indipendenti per facilitare il riutilizzo e migliorare la manutenibilità.
- Semplificare la logica del software, mantenendone però la funzionalità originale.
- Utilizzare nomi per le classi, le variabili e le funzioni che siano descrittivi ed esplicativi del loro contenuto, evitando però eccessiva estensione.

Nel caso in cui siano necessari più file per implementare il software richiesto, fornisci l'implementazione completa per ogni file.
"""

crafting_implementation_prompt_with_library = """
Sei un esperto nel linguaggio di programmazione [PROGRAMMING LANGUAGE] e il tuo compito è implementare un software nel linguaggio di programmazione [PROGRAMMING LANGUAGE] usando le librerie o pacchetti [LIBRARY | PACKAGE]. Il software deve implementare le specifiche e i requisiti funzionali in [DETAILS]. Il software dev'essere implementato cosi:
- Rendere il codice sorgente più leggibile e manutenibile, sostituendo gli algoritmi manuali con librerie standard.
- Assicurare che il codice rispetti le migliori pratiche di [PROGRAMMING LANGUAGE].
- Ridurre la complessità computazionale e, se possibile, anche quella spaziale.
- Rafforzare la robustezza del software, gestendo eccezioni e scenari vari e verificando l'accuratezza dei dati.
- Organizzare il codice in sottosistemi indipendenti per facilitare il riutilizzo e migliorare la manutenibilità.
- Semplificare la logica del software, mantenendone però la funzionalità originale.
- Utilizzare nomi per le classi, le variabili e le funzioni che siano descrittivi ed esplicativi del loro contenuto, evitando però eccessiva estensione.

Nel caso in cui siano necessari più file per implementare il software richiesto, fornisci l'implementazione completa per ogni file.
"""

crafting_implementation_prompt = """
Sei un esperto nel linguaggio di programmazione [PROGRAMMING LANGUAGE] e il tuo compito è implementare un software nel linguaggio di programmazione [PROGRAMMING LANGUAGE]. Il software deve implementare le specifiche e i requisiti funzionali in [DETAILS]. Il software dev'essere implementato cosi:
- Rendere il codice sorgente più leggibile e manutenibile, sostituendo gli algoritmi manuali con librerie standard.
- Assicurare che il codice rispetti le migliori pratiche di [PROGRAMMING LANGUAGE].
- Ridurre la complessità computazionale e, se possibile, anche quella spaziale.
- Rafforzare la robustezza del software, gestendo eccezioni e scenari vari e verificando l'accuratezza dei dati.
- Organizzare il codice in sottosistemi indipendenti per facilitare il riutilizzo e migliorare la manutenibilità.
- Semplificare la logica del software, mantenendone però la funzionalità originale.
- Utilizzare nomi per le classi, le variabili e le funzioni che siano descrittivi ed esplicativi del loro contenuto, evitando però eccessiva estensione.

Nel caso in cui siano necessari più file per implementare il software richiesto, fornisci l'implementazione completa per ogni file.
"""

crafting_structured_implementation_prompt_with_library = """
Sei un esperto nel linguaggio di programmazione [PROGRAMMING LANGUAGE] e il tuo compito è implementare un software nel linguaggio di programmazione [PROGRAMMING LANGUAGE] usando le librerie o pacchetti [LIBRARY | PACKAGE]. Il software deve implementare le specifiche e i requisiti funzionali in [DETAILS] e utilizzando il design pattern [DESIGN PATTERN]. Il software dev'essere implementato cosi:
- Rendere il codice sorgente più leggibile e manutenibile, sostituendo gli algoritmi manuali con librerie standard.
- Assicurare che il codice rispetti le migliori pratiche di [PROGRAMMING LANGUAGE].
- Ridurre la complessità computazionale e, se possibile, anche quella spaziale.
- Rafforzare la robustezza del software, gestendo eccezioni e scenari vari e verificando l'accuratezza dei dati.
- Organizzare il codice in sottosistemi indipendenti per facilitare il riutilizzo e migliorare la manutenibilità.
- Semplificare la logica del software, mantenendone però la funzionalità originale.
- Utilizzare nomi per le classi, le variabili e le funzioni che siano descrittivi ed esplicativi del loro contenuto, evitando però eccessiva estensione.

Nel caso in cui siano necessari più file per implementare il software richiesto, fornisci l'implementazione completa per ogni file.
"""

crafting_structured_implementation_prompt = """
Sei un esperto nel linguaggio di programmazione [PROGRAMMING LANGUAGE] e il tuo compito è implementare un software nel linguaggio di programmazione [PROGRAMMING LANGUAGE]. Il software deve implementare le specifiche e i requisiti funzionali in [DETAILS] e utilizzando il design pattern [DESIGN PATTERN]. Il software dev'essere implementato cosi:
- Rendere il codice sorgente più leggibile e manutenibile, sostituendo gli algoritmi manuali con librerie standard.
- Assicurare che il codice rispetti le migliori pratiche di [PROGRAMMING LANGUAGE].
- Ridurre la complessità computazionale e, se possibile, anche quella spaziale.
- Rafforzare la robustezza del software, gestendo eccezioni e scenari vari e verificando l'accuratezza dei dati.
- Organizzare il codice in sottosistemi indipendenti per facilitare il riutilizzo e migliorare la manutenibilità.
- Semplificare la logica del software, mantenendone però la funzionalità originale.
- Utilizzare nomi per le classi, le variabili e le funzioni che siano descrittivi ed esplicativi del loro contenuto, evitando però eccessiva estensione.

Nel caso in cui siano necessari più file per implementare il software richiesto, fornisci l'implementazione completa per ogni file.
"""

crafting_improved_implementation_prompt_with_library = """
Sei un esperto nel linguaggio di programmazione [PROGRAMMING LANGUAGE] e il tuo compito è migliorare il software [SOURCE CODE]. Le modifiche da apportare includono:
- Rendere il codice sorgente più leggibile e manutenibile, sostituendo gli algoritmi manuali con librerie standard.
- Assicurare che il codice rispetti le migliori pratiche di [PROGRAMMING LANGUAGE].
- Ridurre la complessità computazionale e, se possibile, anche quella spaziale.
- Rafforzare la robustezza del software, gestendo eccezioni e scenari vari e verificando l'accuratezza dei dati.
- Organizzare il codice in sottosistemi indipendenti per facilitare il riutilizzo e migliorare la manutenibilità.
- Semplificare la logica del software, mantenendone però la funzionalità originale.
- Utilizzare nomi per le classi, le variabili e le funzioni che siano descrittivi ed esplicativi del loro contenuto, evitando però eccessiva estensione.

Devi fornire un'implementazione completa del software migliorato, utilizzando le librerie o i pacchetti [LIBRARY | PACKAGE].

Nel caso in cui siano necessari più file per implementare il software richiesto, fornisci l'implementazione completa per ogni file.
"""

crafting_improved_implementation_prompt = """
Sei un esperto nel linguaggio di programmazione [PROGRAMMING LANGUAGE] e il tuo compito è migliorare il software [SOURCE CODE]. Le modifiche da apportare includono:
- Rendere il codice sorgente più leggibile e manutenibile, sostituendo gli algoritmi manuali con librerie standard.
- Assicurare che il codice rispetti le migliori pratiche di [PROGRAMMING LANGUAGE].
- Ridurre la complessità computazionale e, se possibile, anche quella spaziale.
- Rafforzare la robustezza del software, gestendo eccezioni e scenari vari e verificando l'accuratezza dei dati.
- Organizzare il codice in sottosistemi indipendenti per facilitare il riutilizzo e migliorare la manutenibilità.
- Semplificare la logica del software, mantenendone però la funzionalità originale.
- Utilizzare nomi per le classi, le variabili e le funzioni che siano descrittivi ed esplicativi del loro contenuto, evitando però eccessiva estensione.

Devi fornire un'implementazione completa del software migliorato.

Nel caso in cui siano necessari più file per implementare il software richiesto, fornisci l'implementazione completa per ogni file.
"""

crafting_edited_implementation_prompt_with_library = """
Sei un esperto nel linguaggio di programmazione [PROGRAMMING LANGUAGE] e il tuo compito è modificare il software [SOURCE CODE] scritto nel linguaggio di programmazione [PROGRAMMING LANGUAGE]. Il software dev'essere modificato utilizzando le librerie o i pacchetti [LIBRARY | PACKAGE] e integrando le specifiche e i requisiti funzionali in [DETAILS]. Il software dev'essere implementato cosi:
- Rendere il codice sorgente più leggibile e manutenibile, sostituendo gli algoritmi manuali con librerie standard.
- Assicurare che il codice rispetti le migliori pratiche di [PROGRAMMING LANGUAGE].
- Ridurre la complessità computazionale e, se possibile, anche quella spaziale.
- Rafforzare la robustezza del software, gestendo eccezioni e scenari vari e verificando l'accuratezza dei dati.
- Organizzare il codice in sottosistemi indipendenti per facilitare il riutilizzo e migliorare la manutenibilità.
- Semplificare la logica del software, mantenendone però la funzionalità originale.
- Utilizzare nomi per le classi, le variabili e le funzioni che siano descrittivi ed esplicativi del loro contenuto, evitando però eccessiva estensione.

Devi fornire un'implementazione completa del software modificato.

Nel caso in cui siano necessari più file per implementare il software richiesto, fornisci l'implementazione completa per ogni file.
"""

crafting_edited_implementation_prompt = """
Sei un esperto nel linguaggio di programmazione [PROGRAMMING LANGUAGE] e il tuo compito è modificare il software [SOURCE CODE] scritto nel linguaggio di programmazione [PROGRAMMING LANGUAGE]. Il software dev'essere modificato integrando le specifiche e i requisiti funzionali in [DETAILS]. Il software dev'essere implementato cosi:
- Rendere il codice sorgente più leggibile e manutenibile, sostituendo gli algoritmi manuali con librerie standard.
- Assicurare che il codice rispetti le migliori pratiche di [PROGRAMMING LANGUAGE].
- Ridurre la complessità computazionale e, se possibile, anche quella spaziale.
- Rafforzare la robustezza del software, gestendo eccezioni e scenari vari e verificando l'accuratezza dei dati.
- Organizzare il codice in sottosistemi indipendenti per facilitare il riutilizzo e migliorare la manutenibilità.
- Semplificare la logica del software, mantenendone però la funzionalità originale.
- Utilizzare nomi per le classi, le variabili e le funzioni che siano descrittivi ed esplicativi del loro contenuto, evitando però eccessiva estensione.

Devi fornire un'implementazione completa del software modificato.

Nel caso in cui siano necessari più file per implementare il software richiesto, fornisci l'implementazione completa per ogni file.
"""

crafting_designed_implementation_prompt_with_library = """
Sei un esperto nel linguaggio di programmazione [PROGRAMMING LANGUAGE] e il tuo compito è modificare il software [SOURCE CODE] scritto nel linguaggio di programmazione [PROGRAMMING LANGUAGE]. Il software dev'essere modificato utilizzando le librerie o i pacchetti [LIBRARY | PACKAGE] e utilizzando il design pattern [DESIGN PATTERN]. Il software dev'essere implementato cosi:
- Rendere il codice sorgente più leggibile e manutenibile, sostituendo gli algoritmi manuali con librerie standard.
- Assicurare che il codice rispetti le migliori pratiche di [PROGRAMMING LANGUAGE].
- Ridurre la complessità computazionale e, se possibile, anche quella spaziale.
- Rafforzare la robustezza del software, gestendo eccezioni e scenari vari e verificando l'accuratezza dei dati.
- Organizzare il codice in sottosistemi indipendenti per facilitare il riutilizzo e migliorare la manutenibilità.
- Semplificare la logica del software, mantenendone però la funzionalità originale.
- Utilizzare nomi per le classi, le variabili e le funzioni che siano descrittivi ed esplicativi del loro contenuto, evitando però eccessiva estensione.

Devi fornire un'implementazione completa del software modificato.

Nel caso in cui siano necessari più file per implementare il software richiesto, fornisci l'implementazione completa per ogni file.
"""

crafting_designed_implementation_prompt = """
Sei un esperto nel linguaggio di programmazione [PROGRAMMING LANGUAGE] e il tuo compito è modificare il software [SOURCE CODE] scritto nel linguaggio di programmazione [PROGRAMMING LANGUAGE]. Il software dev'essere modificato utilizzando il design pattern [DESIGN PATTERN]. Il software dev'essere implementato cosi:
- Rendere il codice sorgente più leggibile e manutenibile, sostituendo gli algoritmi manuali con librerie standard.
- Assicurare che il codice rispetti le migliori pratiche di [PROGRAMMING LANGUAGE].
- Ridurre la complessità computazionale e, se possibile, anche quella spaziale.
- Rafforzare la robustezza del software, gestendo eccezioni e scenari vari e verificando l'accuratezza dei dati.
- Organizzare il codice in sottosistemi indipendenti per facilitare il riutilizzo e migliorare la manutenibilità.
- Semplificare la logica del software, mantenendone però la funzionalità originale.
- Utilizzare nomi per le classi, le variabili e le funzioni che siano descrittivi ed esplicativi del loro contenuto, evitando però eccessiva estensione.

Devi fornire un'implementazione completa del software modificato.

Nel caso in cui siano necessari più file per implementare il software richiesto, fornisci l'implementazione completa per ogni file.
"""

crafting_edited_structured_implementation_prompt_with_library = """
Sei un esperto nel linguaggio di programmazione [PROGRAMMING LANGUAGE] e il tuo compito è modificare il software [SOURCE CODE] scritto nel linguaggio di programmazione [PROGRAMMING LANGUAGE]. Il software dev'essere modificato utilizzando le librerie o i pacchetti [LIBRARY | PACKAGE], integrando le specifiche e i requisiti funzionali in [DETAILS] e utilizzando il design pattern [DESIGN PATTERN]. Il software dev'essere implementato cosi:
- Rendere il codice sorgente più leggibile e manutenibile, sostituendo gli algoritmi manuali con librerie standard.
- Assicurare che il codice rispetti le migliori pratiche di [PROGRAMMING LANGUAGE].
- Ridurre la complessità computazionale e, se possibile, anche quella spaziale.
- Rafforzare la robustezza del software, gestendo eccezioni e scenari vari e verificando l'accuratezza dei dati.
- Organizzare il codice in sottosistemi indipendenti per facilitare il riutilizzo e migliorare la manutenibilità.
- Semplificare la logica del software, mantenendone però la funzionalità originale.
- Utilizzare nomi per le classi, le variabili e le funzioni che siano descrittivi ed esplicativi del loro contenuto, evitando però eccessiva estensione.

Devi fornire un'implementazione completa del software modificato.

Nel caso in cui siano necessari più file per implementare il software richiesto, fornisci l'implementazione completa per ogni file.
"""

crafting_edited_structured_implementation_prompt = """
Sei un esperto nel linguaggio di programmazione [PROGRAMMING LANGUAGE] e il tuo compito è modificare il software [SOURCE CODE] scritto nel linguaggio di programmazione [PROGRAMMING LANGUAGE]. Il software dev'essere modificato integrando le specifiche e i requisiti funzionali in [DETAILS] e utilizzando il design pattern [DESIGN PATTERN]. Il software dev'essere implementato cosi:
- Rendere il codice sorgente più leggibile e manutenibile, sostituendo gli algoritmi manuali con librerie standard.
- Assicurare che il codice rispetti le migliori pratiche di [PROGRAMMING LANGUAGE].
- Ridurre la complessità computazionale e, se possibile, anche quella spaziale.
- Rafforzare la robustezza del software, gestendo eccezioni e scenari vari e verificando l'accuratezza dei dati.
- Organizzare il codice in sottosistemi indipendenti per facilitare il riutilizzo e migliorare la manutenibilità.
- Semplificare la logica del software, mantenendone però la funzionalità originale.
- Utilizzare nomi per le classi, le variabili e le funzioni che siano descrittivi ed esplicativi del loro contenuto, evitando però eccessiva estensione.

Devi fornire un'implementazione completa del software modificato.

Nel caso in cui siano necessari più file per implementare il software richiesto, fornisci l'implementazione completa per ogni file.
"""