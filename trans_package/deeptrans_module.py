from deep_translator import GoogleTranslator
from langdetect import detect, detect_langs

def TransLate(text: str, src: str, dest: str) -> str:
    """Translate the text from source language to destination language using deep_translator."""
    try:
        translated = GoogleTranslator(source=src, target=dest).translate(text)
        return translated
    except Exception as e:
        return str(e)

def LangDetect(text: str, set: str="all") -> str:
    """Detect the language of the text and return its name, confidence or both using langdetect."""
    try:
        if set == "lang":
            return detect(text)
        else:
            detections = detect_langs(text)
            if set == "confidence":
                return str(detections[0].prob)
            else:  # "all"
                return detections[0].lang, str(detections[0].prob)
    except Exception as e:
        return str(e)

def CodeLang(lang: str) -> str:
    """Return language code from its name or vice-versa using deep_translator's supported languages."""
    translator = GoogleTranslator(source='auto', target='en')  # create an instance of GoogleTranslator
    supported_languages = translator.get_supported_languages(as_dict=True)
    reversed_languages = {value: key for key, value in supported_languages.items()}

    if lang in supported_languages:
        return supported_languages[lang]
    elif lang in reversed_languages:
        return reversed_languages[lang]
    else:
        return "Error: Invalid language or code."


def LanguageList(out: str, text: str=None) -> str:
    """Display a table of all supported languages and their codes, along with text translated to that language."""
    translator = GoogleTranslator(source='auto', target='en')  # create an instance of GoogleTranslator
    supported_languages = translator.get_supported_languages(as_dict=True)

    header = "N   Language       ISO-639 code   Text"
    separator = "-" * 60
    result = [header, separator]

    for idx, (code, lang_name) in enumerate(supported_languages.items(), 1):
        try:
            translated_text = GoogleTranslator(source='en', target=code).translate(text) if text else ""
            line = f"{idx:<4} {lang_name:<15} {code:<15} {translated_text}"
            result.append(line)
        except Exception as e:
            result.append(f"Error translating to {lang_name} ({code}): {e}")
            continue

    if out == "screen":
        return "\n".join(result)
    elif out == "file":
        with open("languages.txt", "w", encoding="utf-8") as f:
            f.write("\n".join(result))
        return "Ok"
    else:
        return "Error: Invalid output method."
