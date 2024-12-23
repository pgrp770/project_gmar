columns = [
    "date",
    "country",
    "country_txt",
    "region",
    "region_txt",
    "city",
    "latitude",
    "longitude",
    "summary",
    "attacktype1_txt",
    "attacktype2_txt",
    "attacktype3_txt",
    "targtype1_txt",
    "targtype2_txt",
    "targtype3_txt",
    "targsubtype1_txt",
    "targsubtype2_txt",
    "targsubtype3_txt",
    "natlty1_txt",
    "natlty2_txt",
    "natlty3_txt",
    "gname",
    "gname2",
    "gname3",
    "nperps",
    "nkill",
    "nwound",
]

fillna_columns_with_empty_string = [
    "region_txt"
]

fillna_columns_with_unknown = {
    "targtype1_txt": "Unknown",
    "targtype2_txt": "Unknown",
    "targtype3_txt": "Unknown",
    "targsubtype1_txt": "Unknown",
    "targsubtype2_txt": "Unknown",
    "targsubtype3_txt": "Unknown",
    "attacktype1_txt": "Unknown",
    "attacktype2_txt": "Unknown",
    "attacktype3_txt": "Unknown",
    "gname": "Unknown",
    "gname2": "Unknown",
    "gname3": "Unknown",
    "natlty1_txt": "Unknown",
    "natlty2_txt": "Unknown",
    "natlty3_txt": "Unknown",
    "latitude": 0,
    "longitude": 0,
}

fillna_columns_with_zero = [
    "country",
    "region",
    "nkill",
    "nwound",
    "nperps"
]
