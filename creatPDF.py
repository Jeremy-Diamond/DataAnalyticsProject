from fpdf import FPDF
import matplotlib.pyplot as plt
import plotly.express as px
import kaleido as kaleido

from musicQueries import top_5_songs_streams,most_popular_artist, plot_top_5_songs, spotify_data 


Width = 210
Height = 297

# Create variables for the charting data
top_5_songs_streams = top_5_songs_streams(spotify_data)
most_popular_artist = most_popular_artist(spotify_data)
#print(most_popular_artist)

# Convert the DataFrame to a string
top_5_songs_streams_str = top_5_songs_streams.to_string()
most_popular_artist_name_str = most_popular_artist.index[0]

#print(most_popular_artist_name_str)

# Create base PDF and set basic parameters
pdf = FPDF()
pdf.add_page()
pdf.set_font("Arial", size=12)
pdf.cell(200, 10, txt="2023 Spotify Analasys", ln=1, align='C') # Title

#add spotify logo at the top
pdf.image('images/spotify-logo.png', x=10, w=30)

# Add top 5 streamed songs
pdf.cell(200, 10, txt="Top 5 most streamed songs", ln=2, align='L') # Subtitle

# Add a table header
pdf.set_font("Arial", 'B', size=12)
pdf.cell(40, 10, txt="Times Played", border=1, align='C')
pdf.cell(80, 10, txt="Song", border=1, align='C')
pdf.cell(70, 10, txt="Artist", border=1, align='C')
pdf.ln()

# Add table content
pdf.set_font("Arial", size=12)
for index, row in top_5_songs_streams.iterrows():
    pdf.cell(40, 10, txt=f"{row['streams']:,}", border=1, align='C')
    pdf.cell(80, 10, txt=row['track_name'], border=1, align='L')
    pdf.cell(70, 10, txt=row['artist(s)_name'], border=1, align='L')
    pdf.ln()

# Add most popular artist
pdf.set_font("Arial", 'B', size=12)
pdf.cell(200, 20, txt=f"The most popular artist was {most_popular_artist_name_str} with {most_popular_artist['streams'].values[0]:,} total streams!", ln=2, align='L')
pdf.set_font("Arial", size=12)


# Define the platforms and their corresponding chart titles and image filenames
platforms = [
    ('in_apple_playlists', 'Top 5 Most Played Songs in Apple Playlists', 'images/top_5_songs_in_apple_playlists.png'),
    ('in_deezer_playlists', 'Top 5 Most Played Songs in Deezer Playlists', 'images/top_5_songs_in_deezer_playlists.png'),
    ('in_spotify_playlists', 'Top 5 Most Played Songs in Spotify Playlists', 'images/top_5_songs_in_spotify_playlists.png')
]

# Loop through each platform and add the corresponding chart to the PDF
for platform, title, image_path in platforms:
    plot_top_5_songs(spotify_data, platform)
    pdf.cell(200, 10, txt=title, ln=1, align='C')  # Center the title
    pdf.image(image_path, x=(Width - 180) / 2, w=180, h=60)  # Center the image and set height to fit three charts
    pdf.ln(5)  # Add some space after the image

# Save the PDF
pdf.output("SpotifyDataAnalysis.pdf")

