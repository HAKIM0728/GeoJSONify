from flask import Flask, render_template
import folium

app = Flask(__name__)

@app.route('/')
def index():
    # Create a Folium map
    m = folium.Map(location=[40, -100], zoom_start=4)

    # Add a marker to the map
    folium.Marker(location=[40, -100], popup='Marker').add_to(m)

    # Convert the Folium map to HTML
    map_html = m._repr_html_()

    # Render the HTML template with the map content
    return render_template('index.html', map_html=map_html)


if __name__ == "__main__":
  app.run(host='0.0.0.0',debug=True)
