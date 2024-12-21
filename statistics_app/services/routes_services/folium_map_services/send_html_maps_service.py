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


def e_8(data):
    # Create a Folium map
    m = folium.Map(location=[20, 0], zoom_start=2)

    # Add data points to the map
    for row in data:
        # Check if latitude and longitude values are present
        if row.get('latitude') and row.get('longitude'):
            # Use CircleMarker to add a marker to the map
            folium.CircleMarker(
                location=(row['latitude'], row['longitude']),
                radius=5,  # Adjust radius if needed
                popup=folium.Popup(
                    f"Region: {row['region']}<br>"
                    f"Group: {row['groups']}<br>"
                    f"Attack Count: {row['attack_count']}",
                    max_width=300
                ),
                color='blue',  # Adjust marker color
                fill=True,
                fill_color='blue'
            ).add_to(m)

    return m._repr_html_()  # Render the map as HTML for embedding


def e_11(data):
    m = folium.Map(location=[20, 0], zoom_start=2)  # Initial map view

    # Iterate over your data
    for row in data:
        # Make sure there are latitude and longitude values
        if row['latitude'] and row['longitude']:
            # Create a CircleMarker for each data point
            folium.CircleMarker(
                location=(row['latitude'], row['longitude']),
                radius=5,  # Static radius or scale it based on another value
                popup=folium.Popup(
                    f"Targets: {row['targets']}<br>Groups: {', '.join(row['groups'])}",
                    max_width=300  # Set the maximum popup width
                ),
                color='red',  # Set the border color of the circle
                fill=True,
                fill_color='red'  # Set the fill color inside the circle
            ).add_to(m)

    return m._repr_html_()


def e_14(data):
    m = folium.Map(location=[20, 0], zoom_start=2)  # Initial map view

    # Iterate over your data
    for row in data:
        # Check if there are latitude and longitude values
        if row.get('latitude') and row.get('longitude'):
            # Prepare the popup content
            popup_content = ''
            if 'country' in row:
                popup_content += f"Country: {row['country']}<br>"
            elif 'region' in row:
                popup_content += f"Region: {row['region']}<br>"

            # Add attack type and groups information
            popup_content += f"Attack Type: {row['attack_types']}<br>Groups: {', '.join(row['groups'])}"

            # Create a CircleMarker for each data point
            folium.CircleMarker(
                location=(row['latitude'], row['longitude']),
                radius=5,  # Static radius or scale it based on another value
                popup=folium.Popup(popup_content, max_width=300),  # Set the maximum popup width
                color='red',  # Set the border color of the circle
                fill=True,
                fill_color='red'  # Set the fill color inside the circle
            ).add_to(m)

    return m._repr_html_()

def e_16(data):
    # Create the base map
    m = folium.Map(location=[20, 0], zoom_start=2)  # Initial map view

    # Iterate over your data
    for row in data:
        # Check if there are latitude and longitude values
        if row.get('latitude') and row.get('longitude'):
            # Determine whether the data is for a region or a country
            if 'region' in row:
                location_type = 'Region'
                location_value = row['region']
            elif 'country' in row:
                location_type = 'Country'
                location_value = row['country']
            else:
                continue  # Skip if neither 'region' nor 'country' is present

            # Prepare the popup content
            popup_content = f"{location_type}: {location_value}<br>Unique Groups: {row['unique_groups']}"

            # Create a CircleMarker for each data point
            folium.CircleMarker(
                location=(row['latitude'], row['longitude']),
                radius=5,  # Static radius or scale it based on unique_groups if needed
                popup=folium.Popup(popup_content, max_width=300),  # Set the maximum popup width
                color='blue' if location_type == 'Country' else 'green',  # Different colors for country/region
                fill=True,
                fill_color='blue' if location_type == 'Country' else 'green'  # Match fill color
            ).add_to(m)

    # Return the rendered map as HTML
    return m._repr_html_()


if __name__ == '__main__':
    e_6(get_attack_change_percentage_by_region())