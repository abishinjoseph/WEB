from flask import Flask, render_template_string
import folium
import os

# Create a Flask application
app = Flask(__name__)

# Create a base map centered at India
m = folium.Map(location=[20.5937, 78.9629], zoom_start=5)  # Centered on India

# Define the locations with images, details, latitude, and longitude
locations = [
    {
        'name': 'Ajanta Caves',
        'coordinates': [20.5654, 75.7100],
        'image': 'https://www.tutorialspoint.com/ajanta_caves/images/monasteries.jpg',
        'details': 'Ajanta Caves: Ancient Buddhist cave temples with exquisite frescoes and sculptures.',
        'url': 'https://en.wikipedia.org/wiki/Ajanta_Caves'
    },
    {
        'name': 'Ellora Caves',
        'coordinates': [20.0185, 75.2197],
        'image': 'https://whc.unesco.org/uploads/thumbs/site_0243_0001-750-750-20151104152442.jpg',
        'details': 'Ellora Caves: Rock-cut temples representing Hindu, Buddhist, and Jain traditions.',
        'url': 'https://en.wikipedia.org/wiki/Ellora_Caves'
    },
    {
        'name': 'Khajuraho',
        'coordinates': [24.8578, 79.9311],
        'image': 'https://plus.unsplash.com/premium_photo-1697730370661-51bf72769ff6?q=80&w=2574&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D',
        'details': 'Khajuraho: Temples with intricate and erotic sculptures from the Chandela dynasty.',
        'url': 'https://en.wikipedia.org/wiki/Khajuraho'
    },
    {
        'name': 'Hampi',
        'coordinates': [15.3356, 76.4602],
        'image': 'https://upload.wikimedia.org/wikipedia/commons/4/4b/Hampi_virupaksha_temple.jpg',
        'details': 'Hampi: Ruins from the Vijayanagara Empire, including the Virupaksha Temple and the Stone Chariot.',
        'url': 'https://en.wikipedia.org/wiki/Hampi'
    },
    {
        'name': 'Konark',
        'coordinates': [19.8870, 86.0941],
        'image': 'https://upload.wikimedia.org/wikipedia/commons/4/47/Konarka_Temple.jpg',
        'details': 'Konark: Home to the Sun Temple, an architectural marvel known for its intricate stone carvings.',
        'url': 'https://en.wikipedia.org/wiki/Konark'
    }
]

# URL of the custom paper pin icon
paper_pin_icon_url = 'pin.png'

# Add pins to the map with hoverable images and details
for location in locations:
    html = f"""
    <div style="width: 320px; height: 300px; overflow: hidden; position: relative;">
        <h4>{location['name']}</h4>
        <a href="{location['url']}" target="_blank">
            <img src="{location['image']}" style="width: 100%; height: 150px; object-fit: cover; margin-bottom: 10px;">
        </a>
        <p style="margin: 0; padding: 5px; box-sizing: border-box; height: calc(100% - 150px - 10px); overflow: auto; position: absolute; bottom: 0; left: 0; width: 100%; background: white;">
            {location['details']}
        </p>
    </div>
    """
    iframe = folium.IFrame(html, width=320, height=300)
    popup = folium.Popup(iframe, max_width=320)
    
    # Add marker with custom paper pin icon
    folium.Marker(
        location=location['coordinates'],
        popup=popup,
        icon=folium.CustomIcon(icon_image=paper_pin_icon_url, icon_size=(30, 30))  # Customize size as needed
    ).add_to(m)

# Save the map to an HTML file
file_path = 'map.html'
m.save(file_path)

# Serve the HTML map via Flask
@app.route('/')
def index():
    with open(file_path, 'r') as f:
        return render_template_string(f.read())

if __name__ == '__main__':
    app.run(debug=True)
