from collections import Counter
import matplotlib.pyplot as plt
from jsonReader import JsonReader

def analyze_top_artists(json_reader, top_n=5):
    data = json_reader.get_data()

    if not data:
        return []

    artists = [
        artist["name"]
        for playlist in data.get("playlists", [])
        for track in playlist.get("tracks", [])
        for artist in track.get('track', {}).get("artists", [])
        if artist.get("name")
    ]

    return Counter(artists).most_common(top_n)


def plot_top_artists(top_artists):

    if not top_artists:
        print("No artist data to plot.")
        return

    names, counts = zip(*top_artists)

    plt.figure(figsize=(10, 6))
    plt.bar(names, counts, color='skyblue')
    plt.xlabel('Artists')
    plt.ylabel('Number of Appearances')
    plt.title('Top Artists in Playlists')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    json_reader = JsonReader('dataFiles/Playlist1.json')
    top_artists = analyze_top_artists(json_reader, top_n=5)
    plot_top_artists(top_artists)