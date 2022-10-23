from collections import defaultdict

import nltk
import sys

import argparse

from nltk.corpus import stopwords

# nltk.download('punkt')
# nltk.download('pl196x')
# nltk.download('wordnet')
# nltk.download('omw-1.4')
# nltk.download('averaged_perceptron_tagger')



def ntlk():
    gracz_counter: int = 0
    kostka_counter: int = 0
    karta_counter: int = 0
    logiczna_counter: int = 0
    czas_counter: int = 0
    rozgrywka_counter: int = 0
    mechanika_counter: int = 0
    gra_counter: int = 0
    plansza_counter: int = 0
    zasady_counter: int = 0
    wiek_counter: int = 0
    partner_counter: int = 0

    sequence: str = ""
    text: str = ""
    result: str = ""
    words = defaultdict(int)

    try:
        text_file = open("tekst1.txt", encoding="UTF-8")
    except FileNotFoundError as e:
        print(e, file=sys.stderr)
        sys.exit(1)
    else:
        for line in text_file:
            sequence += line
        text = nltk.word_tokenize(sequence)
        text_file.close()
    tagged_text = nltk.pos_tag(text)

    for pair in tagged_text:
        word: str = pair[0]
        word = word.lower()

        if word == (
                "gracze" or "graczy" or "graczowi" or "gracza" or "graczem" or "graczu" or "graczami" or "graczach" or "gracze"):
            gracz_counter += 1
        elif word == (
                "kostki" and "kostka" or "kostce" or "kostkę" or "kostką" or "kostce	"):
            kostka_counter += 1
        elif word == (
                "karty" or "karty" or "karcie" or "kartę" or "kartą" or "taktyk" or "karcie" or "kartom" or "kartami"):
            karta_counter += 1
        elif word == ("logicznego" or "logicznej" or "logiczną" or "logiczna"):
            logiczna_counter += 1
        elif word == ("czas" or "czasu" or "czasowi" or "czas" or "czasem"):
            czas_counter += 1
        elif word == ("rozgrywka" or "rozgrywki" or "rozgrywce" or "rozgrywkę" or "rozgrywką" or "rozgrywce" or "rozgrywko"):
            rozgrywka_counter += 1
        elif word == (
                "mechaniki" or "mechaniki" or "mechanice" or "mechanikę" or "mechaniką" or "mechanice" or "mechaniko"):
            mechanika_counter += 1
        elif word == (
                "gra" or "gry" or "grze" or "grę" or "błędzie" or "grą" or "grze" or "gro"):
            gra_counter += 1
        elif word == (
                "plansza" or "planszy" or "planszę" or "planszą" or "planszo" or "planszach" or "plansze" or "planszom"):
            plansza_counter += 1
        elif word == (
                "zasady" or "zasady" or "zasadzie" or "zasadę" or "zasadą" or "zasadzie" or "zasado" or "zasadach" or "zasadami"):
            zasady_counter += 1
        elif word == ("wieków" or "wieku" or "wiekowi" or "wiek" or "wiekiem"):
            wiek_counter += 1
        elif word == (
                "partner" or "partnera" or "partnerowi" or "partnerem" or "partnerze" or "partnerami" or "partnerach"):
            partner_counter += 1

    print("Gracz: {}\n".format(gracz_counter))
    print("Kostka: {}\n".format(kostka_counter))
    print("Karta: {}\n".format(karta_counter))
    print("Logiczna: {}\n".format(logiczna_counter))
    print("Czas: {}\n".format(czas_counter))
    print("Rozgrywka: {}\n".format(rozgrywka_counter))
    print("Mechanika: {}\n".format(mechanika_counter))
    print("Gra: {}\n".format(gra_counter))
    print("Plansza: {}\n".format(plansza_counter))
    print("Zasady: {}\n".format(zasady_counter))
    print("Wiek: {}\n".format(wiek_counter))
    print("Partner: {}\n".format(partner_counter))


ntlk()
