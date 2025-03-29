# Easy Bible Format (EBF)
Version 1.x.y

## Introduction
- **TODO:** why a new format
- **TODO:** why over JSON and not XML
- **TODO:** other formats that this one will be based on

## Versioning
This specification will be versioned according to [semantic versioning](https://semver.org/).

On the header of this document will be displayed the major number associated with the current text.

Only git-tagged versions of the specification are in compliance to semantic version, intermediate commits are not necessarily in compliance too.

## Extension
The suggested extension of file is `.ebx.json`, where x is the major number of the file format.

Example for major 1:
```
bible.ebf1.json
```

## Structure
JSON file with following key structure:

- bible
    - name (string): Name of the bible translation
    - language (string): Bible language according to [ISO 639-1](https://en.wikipedia.org/wiki/List_of_ISO_639_language_codes) (2 letters)
    - books (list): 
        - name (string): Name of the book according to the current translation
        - abbreviation (string): Name of the book according to the current translation
        - usfm_id (string): Identifier according to the [USFM book identifier](https://ubsicap.github.io/usfm/v3.0.2/identification/books.html)
        - chapters (list): List of chapters already in the correct display order
            - comment (string): Comment about the chapter at all
            - verses (list): List of verses already in the correct display order
                - text (string): The text content of the verse
                - section_title (string): Title of a section of verses, starting on this one
                - comment (string): Comment about the specific verse
                - references (list):
                    - **TODO:** create a structure for cross references (use ufsm_id)
- metadata
    - **TODO:** create a structure for some computational metadata link input file hash
