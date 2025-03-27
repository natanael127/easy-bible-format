# Easy Bible Format (EBF)

# Introduction
- **TODO:** why a new format
- **TODO:** why over JSON and not XML
- **TODO:** other formats that this one will be based on

# Structure
JSON file with following key structure:

- bible
    - name (string): Name of the bible translation
    - language (string): Bible language according to [ISO 639-1](https://en.wikipedia.org/wiki/List_of_ISO_639_language_codes) (2 letters)
    - books (list): 
        - name (string): Name of the book according to the current translation
        - abbreviation (string): Name of the book according to the current translation
        - ufsm_id (string): Identifier according to the [UFSM book identifier](https://ubsicap.github.io/usfm/v3.0.2/identification/books.html)
        - chapters (list): List of chapters already in the correct display order
            - comments (string): Comments about the chapter at all
            - verses (list): List of verses already in the correct display order
                - text (string): The text content of the verse
                - comment (string): Comments about the specific verse
                - references (list):
                    - **TODO:** create a structure for cross references (use ufsm_id)
- metadata
    - **TODO:** create a structure for some computational metadata link input file hash
