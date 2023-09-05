from googletrans import Translator, LANGUAGES

def TransLate(text: str, src: str, dest: str) -> str:
    """Translate the text from source language to destination language."""
    translator = Translator()

    try:
        translated = translator.translate(text, src=src, dest=dest)
        return translated.text
    except Exception as e:
        return str(e)

def LangDetect(text: str, set: str="all") -> str:
    """Detect the language of the text and return its name, confidence or both."""
    translator = Translator()

    try:
        detected = translator.detect(text)
        if set == "lang":
            return detected.lang
        elif set == "confidence":
            return str(detected.confidence)
        else:
            return detected.lang, str(detected.confidence)
    except Exception as e:
        return str(e)

def CodeLang(lang: str) -> str:
    """Return language code from its name or vice-versa."""
    reversed_languages = {value: key for key, value in LANGUAGES.items()}

    if lang in LANGUAGES:
        return LANGUAGES[lang]
    elif lang in reversed_languages:
        return reversed_languages[lang]
    else:
        return "Error: Invalid language or code."

def LanguageList(out: str, text: str=None) -> str:
    """Display a table of all supported languages and their codes, along with text translated to that language."""
    translator = Translator()

    header = "N   Language       ISO-639 code   Text"
    separator = "-" * 60
    result = [header, separator]

    for idx, (code, lang_name) in enumerate(LANGUAGES.items(), 1):
        try:
            translated_text = translator.translate(text, dest=code).text if text else ""
            line = f"{idx:<4} {lang_name:<15} {code:<15} {translated_text}"
            result.append(line)
        except Exception as e:
            # Якщо сталася помилка під час перекладу, додамо повідомлення про це
            result.append(f"Error translating to {lang_name} ({code}): {e}")

    if out == "screen":
        return "\n".join(result)
    elif out == "file":
        with open("languages.txt", "w", encoding="utf-8") as f:
            f.write("\n".join(result))
        return "Ok"
    else:
        return "Error: Invalid output method."
