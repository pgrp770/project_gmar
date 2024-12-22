import folium


def e_2(data):
    print("Preparing the HTML map...")

    m = folium.Map(location=[20, 0], zoom_start=2)

    def get_color(average):
        if average < 10:
            return 'green'
        elif average < 30:
            return 'orange'
        return 'red'

    location_type = 'region' if 'region' in data[0] else 'country'

    [
        folium.Marker(
            location=(row['latitude'], row['longitude']),
            icon=folium.Icon(
                color=get_color(row['casualties_average']),
                icon='info-sign'
            ),
            popup=folium.Popup(
                f"Location: {row.get(location_type, 'Unknown')}<br>"
                f"Casualties: {row['casualties']}<br>"
                f"Average: {row['casualties_average']:.2f}%",
                max_width=300
            ),
        ).add_to(m)
        for row in data if row.get('latitude') and row.get('longitude')  # Ensure valid coordinates
    ]

    return m._repr_html_()



def e_6(data):
    m = folium.Map(location=[20, 0], zoom_start=2)

    [
        folium.Marker(
            location=(row['latitude'], row['longitude']),
            popup=folium.Popup(
                f"Region: {row['region']}<br>Attack Change: {row['attack_change_percentage']:.2f}%",
                max_width=300
            ),
            icon=folium.Icon(color="blue", icon="info-sign")
        ).add_to(m)
        for row in data if row.get('latitude') and row.get('longitude')
    ]

    return m._repr_html_()


def e_8(data):
    m = folium.Map(location=[20, 0], zoom_start=2)

    for row in data:
        if row.get('latitude') and row.get('longitude'):
            folium.Marker(
                location=(row['latitude'], row['longitude']),
                popup=folium.Popup(
                    f"Region: {row['region']}<br>"
                    f"Group: {row['group']}<br>"  
                    f"Attack Count: {row['attack_count']}",
                    max_width=300
                ),
                icon=folium.Icon(color='blue')
            ).add_to(m)

    return m._repr_html_()


def e_11(data):
    location_type = 'region' if 'region' in data[0] else 'country'
    m = folium.Map(location=[20, 0], zoom_start=2)
    for row in data:
        if row['latitude'] and row['longitude']:
            flattened_groups = [group for sublist in row['groups'] for group in sublist]

            folium.Marker(
                location=(row['latitude'], row['longitude']),
                radius=5,
                popup=folium.Popup(
                    f"locations: {row[location_type]}, <br>Groups: {', '.join(flattened_groups)}",
                    max_width=300
                ),
                color='red',
                fill=True,
                fill_color='red'
            ).add_to(m)

    return m._repr_html_()


def e_14(data):
    m = folium.Map(location=[20, 0], zoom_start=2, prefer_canvas=True)
    for row in data:
        if 'latitude' in row and 'longitude' in row:
            popup_content = ''

            if 'country' in row:
                popup_content += f"Country: {row['country']}<br>"

            if 'attack_type' in row:
                popup_content += f"Attack Type: {row['attack_type']}<br>"

            if 'group' in row:
                popup_content += f"Groups: {', '.join(row['group'])}"

            folium.Marker(
                location=(row['latitude'], row['longitude']),
                radius=5,
                popup=folium.Popup(popup_content, max_width=300),
                color='red',
                fill=True,
                fill_color='red'
            ).add_to(m)

    return m._repr_html_()

def e_16(data):
    m = folium.Map(location=[20, 0], zoom_start=2)

    for row in data:
        if row.get('latitude') and row.get('longitude'):
            if 'region' in row:
                location_type = 'Region'
                location_value = row['region']
            elif 'country' in row:
                location_type = 'Country'
                location_value = row['country']
            else:
                continue

            popup_content = f"{location_type}: {location_value}<br>Unique Groups: {row['unique_group_count']}"

            folium.Marker(
                location=(row['latitude'], row['longitude']),
                radius=10,
                color='blue',
                fill=True,
                fill_color='blue',
                fill_opacity=0.6,
                popup=popup_content
            ).add_to(m)

    return m._repr_html_()

