import matplotlib.pyplot as plt
import os
from collections import Counter, defaultdict
from jsonReader import JsonReader



def analyze_song_amount_per_month(song_data):
    data = song_data.get_data()

    if not data:
        return []

    playlist_date_counts = {}

    for playlist in data['playlists']:
        name = playlist['name']
        date_counter = defaultdict(int)
        print(date_counter)
        for item in playlist.get('items', []):
            date = item.get('addedDate')
            if date:
                date_counter[date] += 1
        playlist_date_counts[name] = dict(date_counter)

    return playlist_date_counts



def plot_song_amount_per_month(dates):
    if not dates:
        print("No date data to plot.")
        return



    plt.figure(figsize=(12, 8))
    plt.barh(dates_to_plot, counts, color="green")
    plt.xlabel("Number of Songs Added")
    plt.ylabel("Dates")
    plt.xticks(rotation=90)
    plt.tight_layout()

    os.makedirs("plots", exist_ok=True)
    plt.savefig("plots/song_amount_per_month.png")
    plt.show()


if __name__ == "__main__":
    song_data = JsonReader("dataFiles/Playlist1.json")
    song_amount_per_month = analyze_song_amount_per_month(song_data)
    print(f"Found {len(song_amount_per_month)} unique dates.")
    plot_song_amount_per_month(song_amount_per_month)