"""
Module 4 Project — Part 1: API Exploration
Explore 3 public APIs and document what you find.

Instructions:
- Fill in each TODO section
- Run the script to verify your code works
- Document your findings in comments and print statements
"""

import os
import requests

REST_COUNTRIES_KEY = os.getenv("REST_COUNTRIES_API_KEY")

BASE_URLS = {
    "jsonplaceholder": "https://jsonplaceholder.typicode.com",
    "pokeapi": "https://pokeapi.co/api/v2",
    "restcountries": "https://api.restcountries.com/countries/v5",
}

# ============================================================
# API 1: JSONPlaceholder
# Documentation: https://jsonplaceholder.typicode.com/guide/
# ============================================================

def explore_jsonplaceholder():
    print("\n=== API 1: JSONPlaceholder ===")


# GET /users retrieves a collection of resources because we want all the users.
    try:
        response = requests.get(BASE_URLS["jsonplaceholder"] + "/users", timeout=10)
        print(f"\nMethod: {response.request.method}")
        print(f"URL: {response.url}")
        print(f"Status: {response.status_code} {response.reason}")
        print(f"Content-Type: {response.headers.get('Content-Type')}")
        print()

        if response.status_code == 200:
            users = response.json()
            
            for user in users:
                user_name = user["name"]
                user_email = user["email"]
                print(f"User Name: {user_name}, User Email: {user_email}")
        else: 
            print("Request Failed.")

    except requests.RequestException:
        print("JSONPlaceholder API is unavailable.")

    # TODO 2: GET posts by a specific user
    # Endpoint: GET /posts?userId=<number>
    # Print the count and first post title


# Query parameters filter the posts collection to only those belonging to userId 1. 


    try:
        response = requests.get(
            "https://jsonplaceholder.typicode.com/posts", timeout=10, 
            params={"userId": 1,}
        )

        print(f"\nMethod: {response.request.method}")
        print(f"URL: {response.url}")
        print(f"Status: {response.status_code} {response.reason}")
        print(f"Content-Type: {response.headers.get('Content-Type')}")
        print()   
        print()

        if response.status_code == 200:
            posts = response.json()
            print(f"First Post Title: {posts[0]['title']}")

            print(f"Status Code: {response.status_code}")
            print(f"User 1 posts: {len(posts)}")
        else:
            print(f"GET posts failed: {response.status_code}")
    except requests.RequestException:
        print("GET posts request failed due to a connection error.")


    # TODO 3: POST a new post
    # Endpoint: POST /posts
    # Body: {"title": "...", "body": "...", "userId": 1}
    # Print the status code and returned id

    new_post = {
        "title": "My First API Post",
        "body": "This was created by sending a POST request!",
        "userId": 1,
    }


# POST creates a new resource on the server. Status 201 confirms successful creation.

    try:
        response = requests.post(BASE_URLS["jsonplaceholder"] + "/posts", json=new_post, timeout=10)

        print(f"\nMethod: {response.request.method}")
        print(f"URL: {response.url}")
        print(f"Status: {response.status_code} {response.reason}")
        print(f"Content-Type: {response.headers.get('Content-Type')}")
        print()

        if response.status_code == 201:
            posts = response.json()
            print(f"Status Code: {response.status_code}")
            print(f"ID: {posts['id']}")

        else:
            print(f"Post Response Failed: {response.status_code}")
    except requests.RequestException:
        print("POST request failed due to a connection error.")

# A nested resource retrieves posts belonging to a specific user.
    try:
        response = requests.get(
            BASE_URLS["jsonplaceholder"] + "/users/1/posts",
            timeout=10
        )

        print(f"\nMethod: {response.request.method}")
        print(f"URL: {response.url}")
        print(f"Status: {response.status_code} {response.reason}")
        print(f"Content-Type: {response.headers.get('Content-Type')}")
        print()

        if response.status_code == 200:
            posts = response.json()
            print(f"User 1 has {len(posts)} posts.")

            if posts:
                print(f"First post: {posts[0]['title']}")
        else:
            print(f"Nested resource request failed: {response.status_code}")

    except requests.RequestException:
        print("Nested resource API request failed.")     


# ============================================================
# API 2: PokeAPI
# Documentation: https://pokeapi.co/docs/v2
# ============================================================

def explore_pokeapi():
    print("\n=== API 2: PokeAPI ===")

    # TODO 4: GET a specific Pokémon (try ID 1 = Bulbasaur, or 25 = Pikachu)
    # Endpoint: GET /pokemon/<id>
    # Print: name, height, weight, list of abilities

    try:

        pokemon_response = requests.get(BASE_URLS["pokeapi"] + "/pokemon/25", timeout=10)

        print(f"\nMethod: {pokemon_response.request.method}")
        print(f"URL: {pokemon_response.url}")
        print(f"Status: {pokemon_response.status_code} {pokemon_response.reason}")
        print(f"Content-Type: {pokemon_response.headers.get('Content-Type')}")
        print()


        if pokemon_response.status_code == 200:
            pokemon_data = pokemon_response.json()
            pokemon_name =  pokemon_data["name"]
            pokemon_height = pokemon_data["height"]
            pokemon_weight = pokemon_data["weight"]

            print(f"Name: {pokemon_name}, Height: {pokemon_height}, Weight: {pokemon_weight}")
                  
            pokemon_abilities = pokemon_data["abilities"]

            for ability in pokemon_abilities:
                name = ability["ability"]["name"]
                print(name)
                
    # TODO 5: Follow the first type URL from the Pokémon response
        # The URL is at pokemon["types"][0]["type"]["url"]
        # Print: type name, first 5 Pokémon of that type
    
            pokemon_types = pokemon_data["types"]
            type = pokemon_types[0]["type"]
            type_url = type["url"]

            try:

                type_response = requests.get(type_url, timeout=10)

                print(f"\nMethod: {type_response.request.method}")
                print(f"URL: {type_response.url}")
                print(f"Status: {type_response.status_code} {type_response.reason}")
                print(f"Content-Type: {type_response.headers.get('Content-Type')}")
                print()

                if type_response.status_code == 200:
                    type_data = type_response.json()
                    type_name = type_data["name"]

                    print(f"Name: {type_name}")
                    type_pokemon = type_data["pokemon"][0:5]

                    for pokemon in type_pokemon:
                        name = pokemon["pokemon"]["name"]
                        print(name)
                else: 
                    print(f"Type Response Failed: {type_response.status_code}")

            except requests.RequestException:
                print("API is unavailable. ")
        else: 
            print(f"Pokemon Request Failed: {pokemon_response.status_code}")
    except requests.RequestException:
        print("Pokemon API is unavailable")

    # GET a specific resource: Bulbasaur (ID 1)
    
    try:
        bulbasaur_response = requests.get(
            BASE_URLS["pokeapi"] + "/pokemon/1",
            timeout=10
        )
        print(f"\nMethod: {bulbasaur_response.request.method}")
        print(f"URL: {bulbasaur_response.url}")
        print(f"Status: {bulbasaur_response.status_code} {bulbasaur_response.reason}")
        print(f"Content-Type: {bulbasaur_response.headers.get('Content-Type')}")
        print()
        print("Specific Resource Test: ")

        if bulbasaur_response.status_code == 200:
            bulbasaur_data = bulbasaur_response.json()
            bulbasaur_name = bulbasaur_data["name"]
            bulbasaur_type = bulbasaur_data["types"][0]["type"]["name"]

            print(f"Name: {bulbasaur_name}")
            print(f"Type: {bulbasaur_type}")
        else:
            print("Request Failed.")
    except requests.RequestException:
        print("Pokemon API is unavailable. ")

    # TODO 6: Document the response structure in a comment below:
    # Top-level keys in the /pokemon response:
        # name
        # height
        # weight
        # abilities
        # types

    # Nested structures:
        # abilities: list of dictionaries containing ability information
        # types: list of dictionaries containing type information
        # types[0]["type"]: dictionary containing name and url

# ============================================================
# API 3: REST Countries
# Documentation: https://restcountries.com/#endpoints
# ============================================================

def explore_restcountries():
    print("\n=== API 3: REST Countries ===")

    # TODO 7: GET a country by name (try "Japan" or any country you like)
    # Endpoint: GET /name/<country_name>
    # Print: official name, capital, population, region

    headers = {
        "Authorization": f"Bearer {REST_COUNTRIES_KEY}"
    }

    
    try:
        country_response = requests.get(BASE_URLS["restcountries"] + "?q=Japan", headers=headers, timeout=10)

        print(f"\nMethod: {country_response.request.method}")
        print(f"URL: {country_response.url}")
        print(f"Status: {country_response.status_code} {country_response.reason}")
        print(f"Content-Type: {country_response.headers.get('Content-Type')}")
        print()

        if country_response.status_code == 200:
            country_data = country_response.json()
            country_name = country_data["data"]["objects"][0]["names"]["official"]


            country_capital = country_data["data"]["objects"][0]["capitals"][0]["name"]
            country_population = int(country_data["data"]["objects"][0]["population"])
            country_region = country_data["data"]["objects"][0]["region"] 

            print("\n=== REST COUNTRY: ===")
            print(f"Official Name: {country_name.title()}")
            print(f"Capital: {country_capital.title()}")
            print(f"Population: {country_population:,}")
            print(f"Region: {country_region.title()}")
            
        else:
            print(f"Country Name Request Failed: {country_response.status_code}")
    except requests.RequestException:
        print("API is unavailable. ")

            
    # TODO 8: GET all countries in a region (try "Europe" or "Asia")
    # Endpoint: GET /region/<region_name>
    # Print: count, first 10 country names alphabetically
    try:
        region_response = requests.get(BASE_URLS["restcountries"] + "?region=Asia&limit=100", headers=headers, timeout=10)

        print(f"\nMethod: {region_response.request.method}")
        print(f"URL: {region_response.url}")
        print(f"Status: {region_response.status_code} {region_response.reason}")
        print(f"Content-Type: {region_response.headers.get('Content-Type')}")
        print()

        if region_response.status_code == 200:
            region_data = region_response.json()
            countries = region_data["data"]["objects"]
            country_count = len(countries)

            country_names = []

            for country in countries: 
                common_name = country["names"]["common"]
                country_names.append(common_name)

            country_names.sort()
            first_ten = country_names[0:10]

            print("\nFirst Ten Countries:")
            for name in first_ten:
                print(name)
        
            print(f"\nTotal countries in Asia: {country_count}")
        else:
            print("Request Failed.")
    except requests.RequestException:
        print("Asia region request failed due to a connection error.")
        

    # TODO 9: Handle an error
    # Try a country name that doesn't exist
    # Handle the response gracefully (don't crash)
    try:
        error_response = requests.get(BASE_URLS["restcountries"] + "?q=Narnia", headers=headers, timeout=10)

        print(f"\nMethod: {error_response.request.method}")
        print(f"URL: {error_response.url}")
        print(f"Status: {error_response.status_code} {error_response.reason}")
        print(f"Content-Type: {error_response.headers.get('Content-Type')}")
        print()



        error_data = error_response.json()
        countries_found = error_data["data"]["objects"] 

        print()
        if not countries_found:
            print("No matching country found.") 
        else: 
            print("Country Found.")
    except requests.RequestException:
        print("Error request failed due to a connection error.")

# ============================================================
# Run all explorations
# ============================================================

if __name__ == "__main__":
    explore_jsonplaceholder()
    explore_pokeapi()
    explore_restcountries()
    print("\n=== Exploration complete! ===")
