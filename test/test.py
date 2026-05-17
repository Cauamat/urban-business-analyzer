

if __name__ == "__main__":
    local = "Vila Mariana, São Paulo"
    tipo = "cafe"

    coords = get_coordinates(local)

    if coords:
        lat, lng = coords
        lugares = search_places(lat, lng, tipo)

        print(lugares[:3])