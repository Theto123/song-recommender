import requests
import random

print("Welcome to Song recommender\n ".upper())

Song_type = ["Happy", "Sad", "Chill", "Groovy", "Romantic", "Nostalgic"]
uppercase_items = [types.upper() for types in Song_type]

print("Enter song type from this list:\n ")
print(Song_type)
print()

while True:
    user_input = input("\n").upper()
    if user_input not in uppercase_items:
        print("Sorry, you have entered an incorrect song type or maybe misspelt it.")
        print("Try again.")
        continue

    else:
        while True:
            try:
                user_search_limit = input("Enter a search limit:\n ")
                break

            except ValueError:
                print("Incorrect data type! Retry entry.")

        if user_input == uppercase_items[0]:
            print("Happiness is always key.😁\n")
            happy_song_urls = [
                f"https://itunes.apple.com/search?term=PharrellWilliams&limit={user_search_limit}",
                f"https://itunes.apple.com/search?term=JasonMraz&limit={user_search_limit}",
                f"https://itunes.apple.com/search?term=MeghanTrainor&limit={user_search_limit}",
            ]

            random_url = random.choice(happy_song_urls)
            n = random_url.split("=")
            artist_name = n[1].split("&")[0]
            response = requests.get(random_url)
            data = response.json()

            print(
                f"We have recommended {user_search_limit} songs by {artist_name} for you.\n"
            )
            print("Hope you enjoy them!\n")

            for i, result in enumerate(data["results"], start=1):
                print(i, result["trackName"])

        elif user_input == uppercase_items[1]:
            print("You need some healing, hey?😭\n")
            sad_songs_urls = [
                f"https://itunes.apple.com/search?term=Adele&limit={user_search_limit}",
                f"https://itunes.apple.com/search?term=LewisCapaldi&limit={user_search_limit}",
                f"https://itunes.apple.com/search?term=SYML&limit={user_search_limit}",
            ]

            random_url = random.choice(sad_songs_urls)
            n = random_url.split("=")
            artist_name = n[1].split("&")[0]
            response = requests.get(random_url)
            data = response.json()

            print(
                f"We have recommended {user_search_limit} songs by {artist_name} for you.\n"
            )
            print("Hope you enjoy them!\n")

            for i, result in enumerate(data["results"], start=1):
                print(i, result["trackName"])

        elif user_input == uppercase_items[2]:
            print("Nothing like a hot day under a coconut tree.😎\n ")
            chill_songs_urls = [
                f"https://itunes.apple.com/search?term=Joji&limit={user_search_limit}",
                f"https://itunes.apple.com/search?term=DanielCaesar&limit={user_search_limit}",
                f"https://itunes.apple.com/search?term=CigarattesAfterSex&limit={user_search_limit}",
            ]

            random_url = random.choice(chill_songs_urls)
            n = random_url.split("=")
            artist_name = n[1].split("&")[0]
            response = requests.get(random_url)
            data = response.json()

            print(
                f"We have recommended {user_search_limit} songs by {artist_name} for you.\n"
            )
            print("Hope you enjoy them!\n")

            for i, result in enumerate(data["results"], start=1):
                print(i, result["trackName"])

        elif user_input == uppercase_items[3]:
            print("Urging to shake what your mama gave ya?🕺")
            groovy_songs_urls = [
                f"https://itunes.apple.com/search?term=Anderson.Paak&limit={user_search_limit}",
                f"https://itunes.apple.com/search?term=Anderson.Paak&limit={user_search_limit}",
                f"https://itunes.apple.com/search?term=Jamiroquai&limit={user_search_limit}",
            ]

            random_url = random.choice(groovy_songs_urls)
            n = random_url.split("=")
            artist_name = n[1].split("&")[0]
            response = requests.get(random_url)
            data = response.json()

            print(
                f"We have recommended {user_search_limit} songs by {artist_name} for you.\n"
            )
            print("Hope you enjoy them!\n")

            for i, result in enumerate(data["results"], start=1):
                print(i,result["trackName"])

        elif user_input == uppercase_items[4]:
            print("Feeling some love?😏")
            romance_songs_urls = [
                f"https://itunes.apple.com/search?term=EdSheeran&limit={user_search_limit}",
                f"https://itunes.apple.com/search?term=PatrickWatson&limit={user_search_limit}",
                f"https://itunes.apple.com/search?term=Giveon&limit={user_search_limit}",
            ]

            random_url = random.choice(romance_songs_urls)
            n = random_url.split("=")
            artist_name = n[1].split("&")[0]
            response = requests.get(random_url)
            data = response.json()

            print(
                f"We have recommended {user_search_limit} songs by {artist_name} for you.\n"
            )
            print("Hope you enjoy them!\n")

            for i, result in enumerate(data["results"], start=1):
                print(i, result["trackName"])

        elif user_input == uppercase_items[5]:
            print("Memories, huh?🥹")
            nostalgia_songs_urls = [
                f"https://itunes.apple.com/search?term=Coldplay&limit={user_search_limit}",
                f"https://itunes.apple.com/search?term=MacMiller&limit={user_search_limit}",
                f"https://itunes.apple.com/search?term=LanaDelRey&limit={user_search_limit}",
            ]

            random_url = random.choice(nostalgia_songs_urls)
            n = random_url.split("=")
            artist_name = n[1].split("&")[0]
            response = requests.get(random_url)
            data = response.json()

            print(
                f"We have recommended {user_search_limit} songs by {artist_name} for you.\n"
            )
            print("Hope you enjoy them!\n")

            for i, result in enumerate(data["results"], start=1):
                print(i, result["trackName"])

