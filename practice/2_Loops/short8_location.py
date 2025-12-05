""" TUPLES"""

# ===== FIRST WAY TO STORE DATA AS SINGLE VALUES =====
# def main():
#     latitude = 42.376                   # One way to store data as a single value
#     longitude = -71.115                 # One way to store data as a single value
   
#     print(f"Latitude: ", latitude)
#     print(f"Longitude: ", longitude)
    
# ===== SECOND WAY TO STORE DATA AS A TUPLE =====
# def main():
#     coordinates = (42.376, -71.115)      # Another way to store data as a tuple
#     print(f"Latitude: {coordinates[0]}")
#     print(f"Longitude: {coordinates[1]}")

# ===== ANOTHER WAY TO WORK WITH TUPLES - UNPACKING THEM =====
# IMPORTANT! TUPLES CANNOT BE CHANGED ONCE ASSIGNED, WHILE A LIST CAN
# def main():
#     coordinates = (42.376, -71.115)
#     latitude, longitude = coordinates
#     print(f"Latitude: {latitude}")
#     print(f"Longitude: {longitude}")

import sys

def main():
    coordinate_tuple = (42.376, -71.115)
    coordinate_list = [42.376, -71.115]
    print(f"{sys.getsizeof(coordinate_tuple)} bytes")
    print(f"{sys.getsizeof(coordinate_list)} byttes")


main()