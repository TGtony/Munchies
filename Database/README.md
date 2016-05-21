DATABASE

1. Pull out necessary parts for our database.
    - What we needed: ASIN, title, description, URL (image of product)
    - Uses final_meta_data.txt as input
    - Done using getdatabasefile.cpp
        - Runs through final_meta_data.txt with each iteration extraction a part we need.
        - Parts are stored inside a struct object.
        - Each individual product gets a struct.
        - A vector holds all the structs.
        - Once every part has been found, output to file (database.csv)

2. Convert csv to json.
    - Done by using csvtojson.py
