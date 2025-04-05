# Based on https://github.com/scrollmapper/bible_databases/blob/a228a19a29099a41c196c2a310cd93e50a390e30/scripts/sword_to_json.py

from pysword.modules import SwordModules
import argparse
import json


USFM_ID_LOOKUP_TABLE = [
    {
        "name": "Genesis",
        "abbreviation": "Gen",
        "usfm_id": "GEN"
    },
    {
        "name": "Exodus",
        "abbreviation": "Exod",
        "usfm_id": "EXO"
    },
    {
        "name": "Leviticus",
        "abbreviation": "Lev",
        "usfm_id": "LEV"
    },
    {
        "name": "Numbers",
        "abbreviation": "Num",
        "usfm_id": "NUM"
    },
    {
        "name": "Deuteronomy",
        "abbreviation": "Deut",
        "usfm_id": "DEU"
    },
    {
        "name": "Joshua",
        "abbreviation": "Josh",
        "usfm_id": "JOS"
    },
    {
        "name": "Judges",
        "abbreviation": "Judg",
        "usfm_id": "JDG"
    },
    {
        "name": "Ruth",
        "abbreviation": "Ruth",
        "usfm_id": "RUT"
    },
    {
        "name": "I Samuel",
        "abbreviation": "1Sam",
        "usfm_id": "1SA"
    },
    {
        "name": "II Samuel",
        "abbreviation": "2Sam",
        "usfm_id": "2SA"
    },
    {
        "name": "I Kings",
        "abbreviation": "1Kgs",
        "usfm_id": "1KI"
    },
    {
        "name": "II Kings",
        "abbreviation": "2Kgs",
        "usfm_id": "2KI"
    },
    {
        "name": "I Chronicles",
        "abbreviation": "1Chr",
        "usfm_id": "1CH"
    },
    {
        "name": "II Chronicles",
        "abbreviation": "2Chr",
        "usfm_id": "2CH"
    },
    {
        "name": "Ezra",
        "abbreviation": "Ezra",
        "usfm_id": "EZR"
    },
    {
        "name": "Nehemiah",
        "abbreviation": "Neh",
        "usfm_id": "NEH"
    },
    {
        "name": "Tobit",
        "abbreviation": "Tob",
        "usfm_id": "TOB"
    },
    {
        "name": "Judith",
        "abbreviation": "Jdt",
        "usfm_id": "JDT"
    },
    {
        "name": "Esther",
        "abbreviation": "Esth",
        "usfm_id": "EST"
    },
    {
        "name": "Job",
        "abbreviation": "Job",
        "usfm_id": "JOB"
    },
    {
        "name": "Psalms",
        "abbreviation": "Ps",
        "usfm_id": "PSA"
    },
    {
        "name": "Proverbs",
        "abbreviation": "Prov",
        "usfm_id": "PRO"
    },
    {
        "name": "Ecclesiastes",
        "abbreviation": "Eccl",
        "usfm_id": "ECC"
    },
    {
        "name": "Song of Solomon",
        "abbreviation": "Song",
        "usfm_id": "SNG"
    },
    {
        "name": "Wisdom",
        "abbreviation": "Wis",
        "usfm_id": "WIS"
    },
    {
        "name": "Sirach",
        "abbreviation": "Sir",
        "usfm_id": "SIR"
    },
    {
        "name": "Isaiah",
        "abbreviation": "Isa",
        "usfm_id": "ISA"
    },
    {
        "name": "Jeremiah",
        "abbreviation": "Jer",
        "usfm_id": "JER"
    },
    {
        "name": "Lamentations",
        "abbreviation": "Lam",
        "usfm_id": "LAM"
    },
    {
        "name": "Baruch",
        "abbreviation": "Bar",
        "usfm_id": "BAR"
    },
    {
        "name": "Ezekiel",
        "abbreviation": "Ezek",
        "usfm_id": "EZK"
    },
    {
        "name": "Daniel",
        "abbreviation": "Dan",
        "usfm_id": "DAN"
    },
    {
        "name": "Hosea",
        "abbreviation": "Hos",
        "usfm_id": "HOS"
    },
    {
        "name": "Joel",
        "abbreviation": "Joel",
        "usfm_id": "JOL"
    },
    {
        "name": "Amos",
        "abbreviation": "Amos",
        "usfm_id": "AMO"
    },
    {
        "name": "Obadiah",
        "abbreviation": "Obad",
        "usfm_id": "OBA"
    },
    {
        "name": "Jonah",
        "abbreviation": "Jonah",
        "usfm_id": "JON"
    },
    {
        "name": "Micah",
        "abbreviation": "Mic",
        "usfm_id": "MIC"
    },
    {
        "name": "Nahum",
        "abbreviation": "Nah",
        "usfm_id": "NAM"
    },
    {
        "name": "Habakkuk",
        "abbreviation": "Hab",
        "usfm_id": "HAB"
    },
    {
        "name": "Zephaniah",
        "abbreviation": "Zeph",
        "usfm_id": "ZEP"
    },
    {
        "name": "Haggai",
        "abbreviation": "Hag",
        "usfm_id": "HAG"
    },
    {
        "name": "Zechariah",
        "abbreviation": "Zech",
        "usfm_id": "ZEC"
    },
    {
        "name": "Malachi",
        "abbreviation": "Mal",
        "usfm_id": "MAL"
    },
    {
        "name": "I Maccabees",
        "abbreviation": "1Macc",
        "usfm_id": "1MA"
    },
    {
        "name": "II Maccabees",
        "abbreviation": "2Macc",
        "usfm_id": "2MA"
    },
    {
        "name": "Matthew",
        "abbreviation": "Matt",
        "usfm_id": "MAT"
    },
    {
        "name": "Mark",
        "abbreviation": "Mark",
        "usfm_id": "MRK"
    },
    {
        "name": "Luke",
        "abbreviation": "Luke",
        "usfm_id": "LUK"
    },
    {
        "name": "John",
        "abbreviation": "John",
        "usfm_id": "JHN"
    },
    {
        "name": "Acts",
        "abbreviation": "Acts",
        "usfm_id": "ACT"
    },
    {
        "name": "Romans",
        "abbreviation": "Rom",
        "usfm_id": "ROM"
    },
    {
        "name": "I Corinthians",
        "abbreviation": "1Cor",
        "usfm_id": "1CO"
    },
    {
        "name": "II Corinthians",
        "abbreviation": "2Cor",
        "usfm_id": "2CO"
    },
    {
        "name": "Galatians",
        "abbreviation": "Gal",
        "usfm_id": "GAL"
    },
    {
        "name": "Ephesians",
        "abbreviation": "Eph",
        "usfm_id": "EPH"
    },
    {
        "name": "Philippians",
        "abbreviation": "Phil",
        "usfm_id": "PHP"
    },
    {
        "name": "Colossians",
        "abbreviation": "Col",
        "usfm_id": "COL"
    },
    {
        "name": "I Thessalonians",
        "abbreviation": "1Thess",
        "usfm_id": "1TH"
    },
    {
        "name": "II Thessalonians",
        "abbreviation": "2Thess",
        "usfm_id": "2TH"
    },
    {
        "name": "I Timothy",
        "abbreviation": "1Tim",
        "usfm_id": "1TI"
    },
    {
        "name": "II Timothy",
        "abbreviation": "2Tim",
        "usfm_id": "2TI"
    },
    {
        "name": "Titus",
        "abbreviation": "Titus",
        "usfm_id": "TIT"
    },
    {
        "name": "Philemon",
        "abbreviation": "Phlm",
        "usfm_id": "PHM"
    },
    {
        "name": "Hebrews",
        "abbreviation": "Heb",
        "usfm_id": "HEB"
    },
    {
        "name": "James",
        "abbreviation": "Jas",
        "usfm_id": "JAS"
    },
    {
        "name": "I Peter",
        "abbreviation": "1Pet",
        "usfm_id": "1PE"
    },
    {
        "name": "II Peter",
        "abbreviation": "2Pet",
        "usfm_id": "2PE"
    },
    {
        "name": "I John",
        "abbreviation": "1John",
        "usfm_id": "1JN"
    },
    {
        "name": "II John",
        "abbreviation": "2John",
        "usfm_id": "2JN"
    },
    {
        "name": "III John",
        "abbreviation": "3John",
        "usfm_id": "3JN"
    },
    {
        "name": "Jude",
        "abbreviation": "Jude",
        "usfm_id": "JUD"
    },
    {
        "name": "Revelation of John",
        "abbreviation": "Rev",
        "usfm_id": "REV"
    },
    {
        "name": "Prayer of Manasses",
        "abbreviation": "PrMan",
        "usfm_id": "MAN"
    },
    {
        "name": "I Esdras",
        "abbreviation": "1Esd",
        "usfm_id": "1ES"
    },
    {
        "name": "II Esdras",
        "abbreviation": "2Esd",
        "usfm_id": "2ES"
    },
    {
        "name": "Additional Psalm",
        "abbreviation": "AddPs",
        "usfm_id": "PS2"
    },
    {
        "name": "Laodiceans",
        "abbreviation": "EpLao",
        "usfm_id": "LAO"
    }
]

def generate_dict(source_file):
    modules = SwordModules(source_file)
    found_modules = modules.parse_modules()
    bible_version = list(found_modules.keys())[0]
    bible_metadata = found_modules[bible_version]
    bible = modules.get_bible_from_module(bible_version)

    books = bible.get_structure()._books.get('ot',[]) + bible.get_structure()._books.get('nt',[])

    bib = {'bible': {}}
    bib['bible']['name'] = bible_metadata.get('description', bible_version)
    bib['bible']['language'] = bible_metadata.get('lang', '')
    bib['bible']['books'] = []
    books_out_list = bib['bible']['books']

    for book in books:
        print(f"Processing book: {book.name}")
        all_verses_empty = True
        chapters = []
        for chapter in range(1, book.num_chapters + 1):
            verses = []
            for verse in range(1, len(book.get_indicies(chapter)) + 1):
                verse_text = bible.get(
                    books=[book.name],
                    chapters=[chapter],
                    verses=[verse]
                )
                if verse_text:
                    all_verses_empty = False
                verses.append({"text": verse_text,})
            chapters.append({"verses": verses})
        if not all_verses_empty:
            # Find the USFM ID based on abbreviation
            usfm_id = next(
                (item['usfm_id'] for item in USFM_ID_LOOKUP_TABLE 
                if item['abbreviation'] == book.preferred_abbreviation),
                None
            )
            books_out_list.append({
                'names': [book.name],
                'usfm_id': usfm_id,
                'abbreviation': book.preferred_abbreviation,
                'chapters': chapters
            })
        else:
            print(f"Book {book.name} is empty, skipping.")

    return bib

def write_json(bible_dict, output_file):
    with open(output_file, 'w') as outfile:
        json.dump(bible_dict, outfile, indent=4)

def converter(input_path, output_path):
    bible_dict = generate_dict(input_path)
    write_json(bible_dict, output_path)

    print(f"Arquivo JSON gerado: {output_path}")


def main():
    parser = argparse.ArgumentParser(
        description='Conversor de módulo Bíblia SWORD para formato JSON',
    )
    parser.add_argument('--input', required=True, help='Caminho para o arquivo do módulo SWORD da Bíblia')
    parser.add_argument('--output', required=False, help='Caminho para o arquivo JSON de saída (opcional, padrão: mesmo nome do input com extensão .json)')
    args = parser.parse_args()

    # Se output não foi fornecido, usa o mesmo nome do arquivo de entrada com extensão .json
    output_file = args.output
    if not output_file:
        splited_path = args.input.split('.')
        base_name = "".join(splited_path[:-1])
        output_file = base_name + '.json'
        print(f"Saída padrão: {output_file}")

    converter(args.input, output_file)

if __name__ == "__main__":
    main()
