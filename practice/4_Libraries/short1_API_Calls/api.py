import requests


def main():
    print("Search the Art Institute of Chicago!")
    artist = input("Artist: ").strip().upper()
        
    try:
        response = requests.get(
            "https://api.artic.edu/api/v1/artworks/search",
            {"q": artist}
        )
        response.raise_for_status()
        # print(response)
    except requests.HTTPError:
        print("Couldn't complete request!")
        return
    
    content = response.json()
    # print(content)
    for artwork in content["data"]:
        print(f"*{artwork['title']}")


if __name__ == "__main__":
    main()