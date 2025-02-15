import requests
from bs4 import BeautifulSoup
from collections import Counter

url = input(print("Введіте посилання:")) # Укажите нужную страницу
word_to_count = input(print("Введіть слово:"))  # Слово, которое нужно подсчитать

response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")
text = soup.get_text()

words = text.lower().split()
word_count = Counter(words)

print(f"Слово '{word_to_count}' зустрічається {word_count[word_to_count]} раз(а).")










