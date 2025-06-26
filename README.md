# 🎵 Song Recommender App

A fun and interactive Python project that recommends songs based on your mood using the iTunes API.

---

## 🚀 What It Does

This app lets you choose a mood from a predefined list:
- Happy 😁
- Sad 😭
- Chill 😎
- Groovy 🕺
- Romantic 😏
- Nostalgic 🥹

It then randomly selects an artist that matches that mood and uses the [iTunes Search API](https://itunes.apple.com/) to fetch real song titles for you to enjoy.

---

## 🧠 How It Works

- Prompts the user for a mood and a search limit.
- Validates input and gives helpful feedback if anything goes wrong.
- Fetches song data from iTunes using the `requests` library.
- Randomly selects from a list of matching artists for each mood.
- Displays the song titles directly in the terminal.

---

## 💻 Tech Stack

- Python 3
- `requests` for API calls
- `random` for artist selection
- iTunes Public API

---

## 📦 How to Run

1. Make sure Python is installed.
2. Install `requests` if not already:
3. Run the script:

---

## ✨ Example Output

Enter song type from this list:
['Happy', 'Sad', 'Chill', 'Groovy', 'Romantic', 'Nostalgic']

happy
Enter a search limit:
5

We have selected 5 songs by PharrellWilliams for you.
Hope you enjoy them!

-Happy

-Freedom

-Come Get It Bae

-Marilyn Monroe

-Gust of Wind


---

## 🧑‍💻 Made by

**Theto Praise Mamabolo**  
Inspired by curiosity, music, and the joy of creating useful tools with code.

---

## 🙏 Acknowledgements

- [iTunes Search API](https://affiliate.itunes.apple.com/resources/documentation/itunes-store-web-service-search-api/)
- Python docs
- God, for the gift of creativity and code

---


