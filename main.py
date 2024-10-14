from fnmatch import translate

import requests
from bs4 import BeautifulSoup
from googletrans import Translator


def get_english_words():
    url = "https://randomword.com/"
    try:
        response = requests.get(url)

        soup = BeautifulSoup(response.content, "html.parser")
        english_words = soup.find("div", id="random_word").text.strip()
        word_definition = soup.find("div", id="random_word_definition").text.strip()

        return {
            "english_words": english_words,
            "word_definition": word_definition
        }
    except:
        print("Произошла ошибка")

def word_game():
    translator = Translator()
    print("Добро пожаловать в игру!")
    while True:
        word_dict = get_english_words()
        word = word_dict.get("english_words")
        word_definition = word_dict.get("word_definition")
        result = translator.translate(word_definition, dest="ru").text.strip()
        trans_word = translator.translate(word, dest="ru").text.strip()

        print(f"Значение слова - {result}")
        user = input("Что это за слово? ")
        if user == trans_word:
            print("Все верно!")
        else:
            print(f"Ответ неверный, правильное слово -{trans_word}")
        play_again = input("Хотите сыграть еще? y/n")
        if play_again != "y":
            print("Спасибо за игру!")
            break
word_game()
