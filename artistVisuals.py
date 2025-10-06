from collections import Counter
import matplotlib.pyplot as plt
from jsonReader import JsonReader
import os

def analyze_top_artists(json_reader, top_n: int):
    data = json_reader.get_data()

    if not data:
        return []

    artists = [
        item["track"]["artistName"]
        for playlist in data.get("playlists", [])
        for item in playlist.get("items", [])
        if item.get("track") and item["track"].get("artistName")
    ]

    return Counter(artists).most_common(top_n)


def plot_top_artists(top_artists):

    if not top_artists:
        print("No artist data to plot.")
        return

    names, counts = zip(*top_artists)

    plt.figure(figsize=(10, 6))
    plt.bar(names, counts, color='green')
    plt.xlabel('Artists')
    plt.ylabel('Number of Appearances')
    plt.title('Top Artists in Playlists')
    plt.xticks(rotation=45)
    plt.tight_layout()

    os.makedirs("plots", exist_ok=True)
    plt.savefig('plots/top_artists.png')
    plt.show()


if __name__ == "__main__":
    json_reader = JsonReader('dataFiles/Playlist1.json')
    top_artists = analyze_top_artists(json_reader, top_n=10)
    print(f"Found {len(top_artists)} top artists: {top_artists}.")
    plot_top_artists(top_artists)