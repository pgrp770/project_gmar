import folium


def e_2(data):

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

    [
        folium.Marker(
            location=(row['latitude'], row['longitude']),
            popup=folium.Popup(
                f"Region: {row['region']}<br>"
                f"Most Active Group: {row['top_5_groups'][0]['group']}<br>"
                f"Attack Count: {row['top_5_groups'][0]['count']}<br>"
                f"<br>Click to see all groups." if row['top_5_groups'] else "No active groups",
                max_width=300
            ),
            icon=folium.Icon(color='blue')
        ).add_to(m)
        .add_child(
            folium.Popup(f" Region: {row['region']}"
                '<br>'.join(
                    [
                        f"Group: {group['group']} - Attacks: {group['count']}"
                        for group in row['top_5_groups']
                    ]
                ) if row['top_5_groups'] else "No group information available",
                max_width=300
            )
        )
        for row in data
        if row.get('latitude') and row.get('longitude')
    ]

    return m._repr_html_()


def e_11(data):
    location_type = 'region' if 'region' in data[0] else 'country'
    m = folium.Map(location=[20, 0], zoom_start=2)

    [
        folium.Marker(
            location=(row['latitude'], row['longitude']),
            radius=5,
            popup=folium.Popup(
                f"locations: {row[location_type]}, <br>Groups: {row['groups']}",
                max_width=300
            ),
            color='red',
            fill=True,
            fill_color='red'
        ).add_to(m)
        for row in data
        if row['latitude'] and row['longitude']
    ]

    return m._repr_html_()


def e_14(data):
    m = folium.Map(location=[20, 0], zoom_start=2, prefer_canvas=True)

    [
        folium.Marker(
            location=(row['latitude'], row['longitude']),
            radius=5,
            popup=folium.Popup(
                ''.join([
                    f"Country: {row['country']}<br>" if 'country' in row else '',
                    f"Attack Type: {row['attack_type']}<br>" if 'attack_type' in row else '',
                    f"Groups: {', '.join(row['group'])}" if 'group' in row else ''
                ]),
                max_width=300
            ),
            color='red',
            fill=True,
            fill_color='red'
        ).add_to(m)
        for row in data
        if 'latitude' in row and 'longitude' in row
    ]

    return m._repr_html_()

def e_16(data):
    m = folium.Map(location=[20, 0], zoom_start=2)

    [
        folium.Marker(
            location=(row['latitude'], row['longitude']),
            radius=10,
            color='blue',
            fill=True,
            fill_color='blue',
            fill_opacity=0.6,
            popup=f"{('Region' if 'region' in row else 'Country')}: {row.get('region', row.get('country', ''))}<br>Unique Groups: {row['unique_group_count']}"
        ).add_to(m)
        for row in data
        if row.get('latitude') and row.get('longitude') and ('region' in row or 'country' in row)
    ]

    return m._repr_html_()

