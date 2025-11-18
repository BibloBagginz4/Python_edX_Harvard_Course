shows = [
    " Avatar: the last airbender",
    "Ben 10",
    "Arthur",
    " Spongebob Squarepants",
    "Phineas and ferb",
    "Kim possible",
    "Kimmy neutron ",
    "the Proud family "
]

def main():
    cleaned_shows = []
    for show in shows:
        cleaned_shows.append(show.strip().title())
    print("\n".join(cleaned_shows))

main()