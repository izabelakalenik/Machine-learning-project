# Predicting Film Popularity and Resampling Techniques for Rare Target Values

W pierwszym pliku: **01_data_preprocessing**, zrobiłam jakieś basic operacje data preprocessing i wybrałam wstępnie cechy, które możemy analizować (wydają się najbardziej sensowne).

Później data frame jest przekazywany do drugiego pliku: **02_experiment_goal**, i tam ogólnie miało być tylko to:
![image](https://github.com/user-attachments/assets/77576cd9-8724-44f1-a990-cf7609accbbe)

Ale potem byłoby ciężko przenosić te df, tworzyć zbiory testowe i treningowe, żeby trenować modele, bo nie importuje się tak łatwo struktur z jednego notebooka do drugiego. Więc ostatecznie wszystko zostawiłam w tym pliku.

W tym fragmencie:

<img width="511" alt="image" src="https://github.com/user-attachments/assets/0ce84a39-16a2-447d-88e7-6dc3c4d2247c" />

To tego zaznaczonego kodu nie musiałoby być, ale jak się nie zresetuje tych indeksów, to wywala błąd - nie wiem dlaczego do końca, coś mi może umknęło właśnie przez przekazywanie danych między tymi modułami 
(albo są jakieś problemy z wartoścami nienumeryczniemi - może z *orginal_language* feature). Już nie mam trochę siły tego sprawdzać.
