import folium


def create_map(data):
    m = folium.Map(location=[20, 0], zoom_start=2)
    for row in data:
        if row.get('latitude') and row.get('longitude'):
            popup_content = (
                f"<div style='max-height: 300px; overflow-y: auto;'>"
                f"<b>Content:</b> {row.get('content', 'N/A')}<br>"
                f"<b>Country:</b> {row.get('country', 'N/A')}<br>"
                f"<b>Region:</b> {row.get('region', 'N/A')}<br>"
                f"<b>Date:</b> {row.get('date', 'N/A')}<br>"
                f"<b>Category:</b> {row.get('category', 'N/A')}<br>"
                f"</div>"
            )
            folium.Marker(
                location=(row['latitude'], row['longitude']),
                popup=folium.Popup(popup_content, max_width=250)
            ).add_to(m)

    return m._repr_html_()
