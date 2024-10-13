import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Path to the CSV file
file_path = './data/spotify-2023.csv'

# Read the CSV file into a DataFrame with specified encoding
spotify_data = pd.read_csv(file_path, encoding='ISO-8859-1')

# Display the first few rows of the DataFrame to inspect the data
# print("First few rows of the DataFrame:")
# print(spotify_data.head())

# function to create a list of the top 5 song streams
def top_5_songs_streams(data):
    # Filter the DataFrame to include only the relevant columns
    streams = data[['track_name', 'artist(s)_name', 'in_apple_playlists', 'in_deezer_playlists', 'streams']]
    
    # Sort the data based on the number of times played in Apple playlists
    top_5_songs_streams = streams.sort_values(by='streams', ascending=False).head(5)
    
    return top_5_songs_streams

#print(top_5_songs_streams(spotify_data))

#function to list the most popular artist in 2023
def most_popular_artist(data):
    # Filter the DataFrame to include only the relevant columns
    artist_streams = data[['artist(s)_name', 'streams']]
    
    # Group the data by artist and sum the streams
    artist_streams = artist_streams.groupby('artist(s)_name').sum()
    
    # Sort the data based on the total streams
    most_popular_artist = artist_streams.sort_values(by='streams', ascending=False).head(1)
    
    return most_popular_artist

#function that returns a chart of playlist data for the top 5 songs
def plot_top_5_songs(data, playlist_name):
  
    # Filter the DataFrame to include only the relevant columns and top 5 most streamed songs
    top_5_streamed_songs = data[['track_name', 'artist(s)_name', 'streams', 'in_apple_playlists', 'in_deezer_playlists', 'in_spotify_playlists']].sort_values(by='streams', ascending=False).head(5)

    # Create new list of the top 5 songs
    top_5_songs = top_5_streamed_songs[['track_name', playlist_name]].sort_values(by=playlist_name, ascending=False)
    #print('Top 5 songs:', top_5_songs)

    # Plot the data
    plt.figure(figsize=(15, 6), tight_layout=True)
    plt.barh(top_5_songs['track_name'], top_5_songs[playlist_name], color='skyblue')
    plt.xlabel('Number of Plays')
    plt.ylabel('Track Name')
    plt.gca().invert_yaxis()  # Invert y-axis to have the highest value on top
    #plt.show()

    #create a png file of the chart
    plt.savefig(f'./images/top_5_songs_{playlist_name}.png')

#plot_top_5_songs(spotify_data, 'in_apple_playlists')
#plot_top_5_songs(spotify_data, 'in_deezer_playlists')
#plot_top_5_songs(spotify_data, 'in_spotify_playlists')






