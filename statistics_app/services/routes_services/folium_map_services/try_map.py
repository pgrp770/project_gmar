import folium


from statistics_app.services.routes_services.statistic_route_services.statistic_route_service import \
    get_average_casualties

data = get_average_casualties("region", limit=0)

def try_one(data):


# Initialize Folium map
    m = folium.Map(location=[20, 0], zoom_start=2)

    # Add data points
    for row in data:
        if row['latitude'] and row['longitude']:
            folium.CircleMarker(
                location=(row['latitude'], row['longitude']),
                radius=row['casualties_average'] / 10,  # Scale the radius
                popup=folium.Popup(f"{row['casualties']} casualties, {row['casualties_average']:.2f}% average"),
                color='red',
                fill=True,
                fill_color='red'
            ).add_to(m)

    return m._repr_html_()
