import matplotlib.pyplot as plt
import os
from collections import defaultdict
from jsonReader import JsonReader



def analyze_song_amount_per_date(song_data):
    data = song_data.get_data()

    if not data:
        return []

    date_counter = defaultdict(int)
    for playlist in data['playlists']:
        for item in playlist.get('items', []):
            date = item.get('addedDate')
            if date:
                date_counter[date] += 1

    print(date_counter)
    return dict(date_counter)




def plot_song_amount_per_date(dates: dict):
    dates = dict(sorted(dates.items()))
    if not dates:
        print("No date data to plot.")
        return

    x_values = list(dates.values())
    y_values = list(dates.keys())

    plt.figure(figsize=(9, 30))
    plt.barh(range(len(y_values)), x_values, color="green", height=0.8)
    plt.xlabel("Number of Songs Added")
    plt.ylabel("Dates")
    plt.yticks(range(len(y_values)), y_values)
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