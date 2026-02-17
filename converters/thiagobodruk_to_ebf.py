import json
import argparse
import os

# Mapeamento de abreviações do formato thiagobodruk para USFM IDs
ABBREV_TO_USFM = {
    # Antigo Testamento
    "gn": "GEN",
    "gen": "GEN",
    "ex": "EXO",
    "exo": "EXO",
    "lv": "LEV",
    "lev": "LEV",
    "nm": "NUM",
    "num": "NUM",
    "dt": "DEU",
    "deu": "DEU",
    "js": "JOS",
    "jos": "JOS",
    "jz": "JDG",
    "jdg": "JDG",
    "jud": "JDG",
    "rt": "RUT",
    "rut": "RUT",
    "1sm": "1SA",
    "1sa": "1SA",
    "2sm": "2SA",
    "2sa": "2SA",
    "1rs": "1KI",
    "1ki": "1KI",
    "1kgs": "1KI",
    "2rs": "2KI",
    "2ki": "2KI",
    "2kgs": "2KI",
    "1cr": "1CH",
    "1ch": "1CH",
    "2cr": "2CH",
    "2ch": "2CH",
    "ed": "EZR",
    "ezr": "EZR",
    "ne": "NEH",
    "neh": "NEH",
    "et": "EST",
    "est": "EST",
    "job": "JOB",
    "jó": "JOB",
    "sl": "PSA",
    "ps": "PSA",
    "psa": "PSA",
    "pv": "PRO",
    "pro": "PRO",
    "prv": "PRO",
    "ec": "ECC",
    "ecc": "ECC",
    "ct": "SNG",
    "sng": "SNG",
    "so": "SNG",
    "is": "ISA",
    "isa": "ISA",
    "jr": "JER",
    "jer": "JER",
    "lm": "LAM",
    "lam": "LAM",
    "ez": "EZK",
    "ezk": "EZK",
    "dn": "DAN",
    "dan": "DAN",
    "os": "HOS",
    "hos": "HOS",
    "ho": "HOS",
    "jl": "JOL",
    "jol": "JOL",
    "joel": "JOL",
    "am": "AMO",
    "amo": "AMO",
    "ob": "OBA",
    "oba": "OBA",
    "jn": "JON",
    "jon": "JON",
    "mq": "MIC",
    "mic": "MIC",
    "mi": "MIC",
    "na": "NAM",
    "nam": "NAM",
    "nah": "NAM",
    "hc": "HAB",
    "hab": "HAB",
    "hk": "HAB",
    "sf": "ZEP",
    "zep": "ZEP",
    "zp": "ZEP",
    "ag": "HAG",
    "hag": "HAG",
    "hg": "HAG",
    "zc": "ZEC",
    "zec": "ZEC",
    "ml": "MAL",
    "mal": "MAL",
    
    # Novo Testamento
    "mt": "MAT",
    "mat": "MAT",
    "mc": "MRK",
    "mrk": "MRK",
    "mk": "MRK",
    "lc": "LUK",
    "luk": "LUK",
    "lk": "LUK",
    "jo": "JHN",
    "jhn": "JHN",
    "at": "ACT",
    "act": "ACT",
    "atos": "ACT",
    "rm": "ROM",
    "rom": "ROM",
    "1co": "1CO",
    "2co": "2CO",
    "gl": "GAL",
    "gal": "GAL",
    "ef": "EPH",
    "eph": "EPH",
    "fp": "PHP",
    "php": "PHP",
    "ph": "PHP",
    "cl": "COL",
    "col": "COL",
    "1ts": "1TH",
    "1th": "1TH",
    "2ts": "2TH",
    "2th": "2TH",
    "1tm": "1TI",
    "1ti": "1TI",
    "2tm": "2TI",
    "2ti": "2TI",
    "tt": "TIT",
    "tit": "TIT",
    "fm": "PHM",
    "phm": "PHM",
    "hb": "HEB",
    "heb": "HEB",
    "tg": "JAS",
    "jas": "JAS",
    "jm": "JAS",
    "1pe": "1PE",
    "2pe": "2PE",
    "1jo": "1JN",
    "1jn": "1JN",
    "2jo": "2JN",
    "2jn": "2JN",
    "3jo": "3JN",
    "3jn": "3JN",
    "jd": "JUD",
    "jud": "JUD",
    "ap": "REV",
    "re": "REV",
    "rev": "REV",
    
    # Apócrifos/Deuterocanônicos
    "tb": "TOB",
    "tob": "TOB",
    "jt": "JDT",
    "jdt": "JDT",
    "sb": "WIS",
    "wis": "WIS",
    "eclo": "SIR",
    "sir": "SIR",
    "br": "BAR",
    "bar": "BAR",
    "1mc": "1MA",
    "1ma": "1MA",
    "2mc": "2MA",
    "2ma": "2MA",
}

# Mapeamento de códigos de idioma (pelos nomes de arquivo)
LANGUAGE_MAP = {
    "ar_svd": "ar",
    "de_schlachter": "de",
    "el_greek": "el",
    "en_bbe": "en",
    "en_kjv": "en",
    "eo_esperanto": "eo",
    "es_rvr": "es",
    "fi_finnish": "fi",
    "fi_pr": "fi",
    "fr_apee": "fr",
    "ko_ko": "ko",
    "pt_aa": "pt",
    "pt_acf": "pt",
    "pt_nvi": "pt",
    "ro_cornilescu": "ro",
    "ru_synodal": "ru",
    "vi_vietnamese": "vi",
    "zh_cuv": "zh",
    "zh_ncv": "zh",
}

# Nomes completos para versões de Bíblia
VERSION_NAMES = {
    "ar_svd": "The Arabic Bible",
    "de_schlachter": "Schlachter",
    "el_greek": "Modern Greek",
    "en_bbe": "Basic English Bible",
    "en_kjv": "King James Version",
    "eo_esperanto": "Esperanto",
    "es_rvr": "Reina Valera",
    "fi_finnish": "Finnish Bible",
    "fi_pr": "Pyhä Raamattu",
    "fr_apee": "Le Bible de I'Épée",
    "ko_ko": "Korean Version",
    "pt_aa": "Almeida Revisada Imprensa Bíblica",
    "pt_acf": "Almeida Corrigida e Revisada Fiel",
    "pt_nvi": "Nova Versão Internacional",
    "ro_cornilescu": "Versiunea Dumitru Cornilescu",
    "ru_synodal": "Синодальный перевод",
    "vi_vietnamese": "Tiếng Việt",
    "zh_cuv": "Chinese Union Version",
    "zh_ncv": "New Chinese Version",
}


def detect_language_from_filename(filename):
    """Detecta o idioma com base no nome do arquivo."""
    basename = os.path.basename(filename)
    name_without_ext = os.path.splitext(basename)[0]
    return LANGUAGE_MAP.get(name_without_ext, "en")


def detect_version_name(filename):
    """Detecta o nome da versão com base no nome do arquivo."""
    basename = os.path.basename(filename)
    name_without_ext = os.path.splitext(basename)[0]
    return VERSION_NAMES.get(name_without_ext, name_without_ext)


def convert_thiagobodruk_to_ebf(input_file, output_file=None):
    """
    Converte um arquivo JSON do formato thiagobodruk para o formato EBF1.
    
    Formato de entrada (thiagobodruk):
    [
        {
            "abbrev": "gn",
            "name": "Genesis",
            "chapters": [
                ["Verse 1", "Verse 2", ...],
                ["Verse 1", "Verse 2", ...],
                ...
            ]
        },
        ...
    ]
    
    Formato de saída (EBF1):
    {
        "bible": {
            "name": "Bible Version Name",
            "language": "pt",
            "books": [
                {
                    "names": ["Genesis"],
                    "abbreviation": "gn",
                    "usfm_id": "GEN",
                    "chapters": [
                        {
                            "verses": [
                                {"text": "Verse 1"},
                                {"text": "Verse 2"},
                                ...
                            ]
                        },
                        ...
                    ]
                },
                ...
            ]
        }
    }
    """
    
    # Ler o arquivo JSON de entrada
    print(f"Lendo arquivo: {input_file}")
    with open(input_file, 'r', encoding='utf-8-sig') as f:
        thiagobodruk_data = json.load(f)
    
    # Detectar idioma e nome da versão
    language = detect_language_from_filename(input_file)
    version_name = detect_version_name(input_file)
    
    # Criar estrutura EBF
    ebf_data = {
        "bible": {
            "name": version_name,
            "language": language,
            "books": []
        }
    }
    
    # Converter cada livro
    for book_data in thiagobodruk_data:
        abbrev = book_data.get("abbrev", "").lower()
        book_name = book_data.get("name", "Unknown")
        chapters_data = book_data.get("chapters", [])
        
        # Mapear abreviação para USFM ID
        usfm_id = ABBREV_TO_USFM.get(abbrev)
        
        if not usfm_id:
            print(f"Aviso: USFM ID não encontrado para abreviação '{abbrev}'. Pulando livro '{book_name}'.")
            continue
        
        # Converter capítulos
        ebf_chapters = []
        for chapter_verses in chapters_data:
            ebf_verses = []
            for verse_text in chapter_verses:
                ebf_verses.append({"text": verse_text})
            ebf_chapters.append({"verses": ebf_verses})

        # Maiúscula apenas na primeira letra para o EBF
        for i, char in enumerate(abbrev):
            if char.isalpha():
                abbrev = abbrev[:i] + char.upper() + abbrev[i+1:]
                break

        # Adicionar livro ao EBF
        ebf_book = {
            "names": [book_name],
            "abbreviation": abbrev,
            "usfm_id": usfm_id,
            "chapters": ebf_chapters
        }
        
        ebf_data["bible"]["books"].append(ebf_book)
        print(f"Convertido: {book_name} ({abbrev}) - {len(ebf_chapters)} capítulos")
    
    # Determinar arquivo de saída
    if not output_file:
        base_name = os.path.splitext(input_file)[0]
        output_file = f"{base_name}.ebf1.json"
    
    # Salvar arquivo de saída
    print(f"Salvando arquivo: {output_file}")
    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(ebf_data, f, ensure_ascii=False, indent=4)
    
    print(f"Conversão concluída! Total de livros: {len(ebf_data['bible']['books'])}")
    return output_file


def main():
    parser = argparse.ArgumentParser(
        description='Converte Bíblias do formato JSON thiagobodruk para o formato EBF1',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Exemplos de uso:
  python thiagobodruk_to_ebf.py --input pt_acf.json
  python thiagobodruk_to_ebf.py --input pt_acf.json --output biblia_acf.ebf1.json
  python thiagobodruk_to_ebf.py --input ../thiagobodruk-bibles/json/en_kjv.json

Créditos:
  Este conversor processa Bíblias do repositório de Thiago Bodruk:
  https://github.com/thiagobodruk/bible
        """
    )
    
    parser.add_argument(
        '--input',
        required=True,
        help='Caminho para o arquivo JSON de entrada no formato thiagobodruk'
    )
    
    parser.add_argument(
        '--output',
        required=False,
        help='Caminho para o arquivo JSON de saída no formato EBF1 (opcional, padrão: <input>.ebf1.json)'
    )
    
    args = parser.parse_args()
    
    # Verificar se o arquivo de entrada existe
    if not os.path.exists(args.input):
        print(f"Erro: Arquivo de entrada não encontrado: {args.input}")
        return 1
    
    # Converter
    try:
        convert_thiagobodruk_to_ebf(args.input, args.output)
        return 0
    except Exception as e:
        print(f"Erro durante a conversão: {e}")
        import traceback
        traceback.print_exc()
        return 1


if __name__ == "__main__":
    exit(main())
