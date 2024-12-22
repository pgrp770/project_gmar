import folium


from statistics_app.services.routes_services.statistic_route_services.statistic_route_service import \
    get_average_casualties, get_attack_change_percentage_by_region

# data = get_average_casualties("region", limit=0)

def e_2(data):
    print("prepering the html maps")

    m = folium.Map(location=[20, 0], zoom_start=2)

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

    for row in data:
        if row['latitude'] and row['longitude']:
            folium.CircleMarker(
                location=(row['latitude'], row['longitude']),
                radius=5,
                popup=folium.Popup(
                    f"Region: {row['region']}<br>Attack Change: {row['attack_change_percentage']:.2f}%",
                    max_width=300
                ),
                color='red',
                fill=True,
                fill_color='red'
            ).add_to(m)

    return m._repr_html_()


def e_8(data):
    # Create a Folium map
    m = folium.Map(location=[20, 0], zoom_start=2)


    for row in data:

        if row.get('latitude') and row.get('longitude'):
            folium.CircleMarker(
                location=(row['latitude'], row['longitude']),
                radius=5,
                popup=folium.Popup(
                    f"Region: {row['region']}<br>"
                    f"Group: {row['groups']}<br>"
                    f"Attack Count: {row['attack_count']}",
                    max_width=300
                ),
                color='blue',
                fill=True,
                fill_color='blue'
            ).add_to(m)

    return m._repr_html_()


def e_11(data):
    m = folium.Map(location=[20, 0], zoom_start=2)  # Initial map view

    for row in data:
        if row['latitude'] and row['longitude']:
            folium.CircleMarker(
                location=(row['latitude'], row['longitude']),
                radius=5,
                popup=folium.Popup(
                    f"Targets: {row['targets']}<br>Groups: {', '.join(row['groups'])}",
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
        if row.get('latitude') and row.get('longitude'):
            popup_content = ''
            if 'country' in row:
                popup_content += f"Country: {row['country']}<br>"
            elif 'region' in row:
                popup_content += f"Region: {row['region']}<br>"

            popup_content += f"Attack Type: {row['attack_types']}<br>Groups: {', '.join(row['groups'])}"

            folium.CircleMarker(
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

            popup_content = f"{location_type}: {location_value}<br>Unique Groups: {row['unique_groups']}"

            folium.CircleMarker(
                location=(row['latitude'], row['longitude']),
                fill=True,
            ).add_to(m)

    return m._repr_html_()


# if __name__ == '__main__':
    # e_6(get_attack_change_percentage_by_region())