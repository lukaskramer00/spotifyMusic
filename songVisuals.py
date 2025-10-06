import matplotlib.pyplot as plt
import os
from collections import defaultdict
from jsonReader import JsonReader
from datetime import datetime
import pandas as pd



def analyze_song_amount_per_date(song_data):
    data = song_data.get_data()

    if not data:
        return []

    date_counter = defaultdict(int)
    for playlist in data['playlists']:
        for item in playlist.get('items', []):
            date = datetime.strptime(item.get('addedDate'), "%Y-%m-%d")
            date_month_convertion = date.strftime("%Y-%m")
            if date_month_convertion:
                date_counter[date_month_convertion] += 1

    print(date_counter)
    return dict(date_counter)




def plot_song_amount_per_date(dates: dict):
    dates = dict(sorted(dates.items()))
    if not dates:
        print("No date data to plot.")
        return

    df = pd.DataFrame(list(dates.items()), columns=['Date', 'Song Count'])
    df["year"] = df["Date"].str[:4]

    colors = {
        "2020": "red",
        "2021": "blue",
        "2022": "green",
        "2023": "purple",
        "2024": "orange",
        "2025": "brown",
    }

    bar_colors = df["year"].map(colors)

    plt.figure(figsize=(9, 30))
    plt.barh(df["Date"], df["Song Count"], color=bar_colors, height=0.8)

    plt.xlabel("Number of Songs Added")
    plt.ylabel("Dates")
    plt.yticks(range(len(df["Date"])), df["Date"])
    plt.xticks(rotation=90)
    plt.tight_layout()

    os.makedirs("plots", exist_ok=True)
    plt.savefig("plots/song_amount_per_date.png")
    plt.show()


if __name__ == "__main__":
    song_data = JsonReader("dataFiles/Playlist1.json")
    song_amount_per_date = analyze_song_amount_per_date(song_data)
    print(f"Found {len(song_amount_per_date)} unique dates.")
    plot_song_amount_per_date(song_amount_per_date)