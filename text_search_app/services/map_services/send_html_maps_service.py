import folium


def create_map(data):
    m = folium.Map(location=[20, 0], zoom_start=2)

    for row in data:
        if row.get('latitude') and row.get('longitude'):
            folium.Marker(
                location=(row['latitude'], row['longitude']),
                popup=(
                    f"<b>Content:</b> {row.get('content', 'N/A')}<br>"
                    f"<b>Country:</b> {row.get('country', 'N/A')}<br>"
                    f"<b>Region:</b> {row.get('region', 'N/A')}<br>"
                    f"<b>Date:</b> {row.get('date', 'N/A')}"
                    f"<b>Category:</b> {row.get('category', 'N/A')}<br>"
                )
            ).add_to(m)

    return m._repr_html_()
