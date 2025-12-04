def main():
#    spacecraft = {"name": "Voyager 1", "distance": 163}
    spacecraft = {"name": "James Webb Space Telescope"}
    spacecraft.update({"distance": 0.01, "orbit": "Sun"})
    print(create_report(spacecraft))




def create_report(spacecraft):
    return f"""
    ========= REPORT =========

    Name: {spacecraft.get("name", "Unknown")}
    DISTANCE: {spacecraft.get("distance", "Unknown")} AU
    ORBIT: {spacecraft.get("orbit", "Unknown")}

    ==========================
    """


main()