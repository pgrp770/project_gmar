import folium


from statistics_app.services.routes_services.statistic_route_services.statistic_route_service import \
    get_average_casualties, get_attack_change_percentage_by_region

data = get_average_casualties("region", limit=0)

def e_2(data):


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


def e_6(data):
    m = folium.Map(location=[20, 0], zoom_start=2)

    # Add data points to the map
    for row in data:
        if row['latitude'] and row['longitude']:
            # Use CircleMarker to add a marker to the map
            folium.CircleMarker(
                location=(row['latitude'], row['longitude']),
                radius=5,  # Static radius, or you can scale based on another value
                popup=folium.Popup(
                    f"Region: {row['region']}<br>Attack Change: {row['attack_change_percentage']:.2f}%",
                    max_width=300
                ),
                color='red',  # Marker color
                fill=True,
                fill_color='red'
            ).add_to(m)

    return m._repr_html_()  # Render the map as HTML for embedding


if __name__ == '__main__':
    e_6(get_attack_change_percentage_by_region())