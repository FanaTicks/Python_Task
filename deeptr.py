# Імпортуємо потрібні функції з модуля deeptrans_module
from trans_package.deeptrans_module import TransLate, LangDetect, CodeLang, LanguageList

def main():
    # Демонстрація функції TransLate
    translated_text = TransLate("Hello", "en", "fr")
    print(f"Translated text: {translated_text}\n")

    # Демонстрація функції LangDetect
    language, confidence = LangDetect("Hello")
    print(f"Detected language: {language} with confidence: {confidence}\n")

    # Демонстрація функції CodeLang
    language_code = CodeLang("english")
    print(f"Language code for 'english': {language_code}\n")

    # Демонстрація функції LanguageList
    languages_list = LanguageList("screen", "Good day")
    print(languages_list)

if __name__ == "__main__":
    main()
