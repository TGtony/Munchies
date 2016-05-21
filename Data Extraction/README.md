DATA EXTRACTION

1. Pull out desired products.
    - The main meta data contains all grocery and gourmet foods but we only need a small subset (the snacks).
    - Done by using meta_parser.cpp
        - finalist.txt contains keywords of the products we wanted
        - A search is done through the entire meta data
        - The title of each product is treated as a string as tested if it contains any of the keywords
        - If yes, output to new file (final_meta_data.txt)

2. Pull out reviews of desired products.
    - Done by using getreviews.cpp
        - First find and store ASIN (Amazon product id) in a vector from final_meta_data.txt.
        - Find ASIN of each review and see if it matches one of the ASIN in vector.
        - If yes, output the review to new file (final_review_data.txt)

3. Parse reviews for desired parts.
    - Done by using reviewparser.cpp
        - What we needed: ASIN and the actual review.
        - Searches each line, pull ASIN and review and output to (data.txt)

4. Combine review into 1 for each product.
    - Done by using reviewparser2.cpp

5. Pull adjectives out of reviews.
    - Done by using adjectiveExtractor.py
        - Uses NLTK
