import json
import re
from trans_package.deeptrans_module import TransLate, LangDetect

def main():
    # Зчитуємо конфігураційний файл
    with open("config.json", "r") as config_file:
        config = json.load(config_file)

    filename = config["filename"]
    try:
        with open(filename, "r", encoding="utf-8") as file:
            content = file.read()
    except FileNotFoundError:
        print(f"File {filename} not found!")
        return

    # Визначення мови тексту
    detected_language = LangDetect(content, set="lang")

    print(f"File Name: {filename}")
    print(f"File Size: {len(content)} bytes")
    print(f"Symbols: {len(content)}")
    print(f"Words: {len(content.split())}")
    print(f"Sentences: {len(re.split('[.!?]', content)) - 1}")
    print(f"Language: {detected_language}")

    # Обрізаємо текст згідно конфігурації
    content = content[:config["max_symbols"]]
    content = " ".join(content.split()[:config["max_words"]])
    content = re.split('[.!?]', content)[:config["max_sentences"]]
    content = ".".join(content)



    # Переклад тексту
    translated_text = TransLate(content, 'auto', config["translation_language"])

    # Виводимо результат
    if config["output"] == "screen":
        print(f"Translated to {config['translation_language']}: {translated_text}")
    elif config["output"] == "file":
        output_filename = f"{filename.split('.')[0]}_{config['translation_language']}.txt"
        with open(output_filename, "w", encoding="utf-8") as out_file:
            out_file.write(translated_text)
        print("Ok")
    else:
        print("Error: Invalid output method.")

if __name__ == "__main__":
    main()
