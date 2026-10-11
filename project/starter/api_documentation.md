

# Module 4 Project — API Documentation

## API 1: JSONPlaceholder

### Base URL
https://jsonplaceholder.typicode.com

### Authentication
None required. JSONPlaceholder is a public API that allows requests without an API key or authentication token.

### Endpoints Tested

### 1. GET /users

    Description: Retrieves a collection of users.

    Example response:
    '''json
    [
        {
            "name": "Leanne Graham",
            "email": "Sincere@april.biz"
        }
    ]
    '''
#### 2. GET /posts?userId=1

    Description: Retrieves posts belonging to user ID 1 using a query parameter.

    Example response:
    '''json
    [
        {
            "userId": 1,
            "id": 1,
            "title": "My First Post",
            "body": "This is an example post."
        }
    ]
    '''

#### 3. POST /posts

    Description: Simulates creating a new post.

    Example response:
    '''json
    [
        {
            "userId": 1,
            "id": 101,
            "title": "My First API Post",
            "body": "This was created by sending a POST request!"
        }
    ]
    '''


#### 4. GET /users/1/posts

    Description: Retrieves posts belonging to user 1 through a nested resource endpoint.

    Example response (abbreviated):

    ```json
    [
    {
    "userId": 1,
    "id": 1,
    "title": "sunt aut facere repellat provident occaecati excepturi optio reprehenderit"
    }
    ]
    ```

Status: 200 OK

Result: Returned 10 posts belonging to user 1.


### Rate Limits
No rate-limit errors (HTTP 429) were encountered during testing.
The exact rate limit was not verified.

### Challenges and Observations
JSONPlaceholder simulates POST requests. The API returned
201 Created and assigned ID 101, but the new post was
not permanently saved to the server.



## API 2: PokeAPI

### Base URL
https://pokeapi.co/api/v2/

### Authentication
None required. PokeAPI is a public API that allows GET requests without an API key or authentication token.

### Endpoints Tested

#### 1. GET /pokemon/25

Description: Retrieves information about Pikachu, including its name, height, weight, and abilities.

Example response:
```json
{
  "name": "pikachu",
  "height": 4,
  "weight": 60,
  "abilities": [
    {
      "ability": {
        "name": "static"
      }
    },
    {
      "ability": {
        "name": "lightning-rod"
      }
    }
  ]
}
```

Status: 200 OK

#### 2. GET /type/13/

Description: Retrieves information about the Electric type, including Pokémon belonging to that type. This URL was obtained from the nested types data in Pikachu's response.

Example response:
```json
{
  "name": "electric",
  "pokemon": [
    {
      "pokemon": {
        "name": "pikachu"
      }
    },
    {
      "pokemon": {
        "name": "raichu"
      }
    },
    {
      "pokemon": {
        "name": "magnemite"
      }
    },
    {
      "pokemon": {
        "name": "magneton"
      }
    },
    {
      "pokemon": {
        "name": "voltorb"
      }
    }
  ]
}
```

#### 3. GET /pokemon/1

    Description: Retrieves information about Bulbasaur using its Pokémon ID. The script extracts its name and first type from the JSON response.

    Example response:

    ```json
    {
    "name": "bulbasaur",
    "types": [
        {
        "type": {
            "name": "grass"
        }
        },
        {
        "type": {
            "name": "poison"
        }
        }
    ]
    }
    ```
    Status: 200 OK


### Rate Limits
No HTTP 429 errors were encountered during testing. The exact rate limit was not verified.

### Challenges and Observations
PokeAPI uses nested JSON structures. To retrieve Pokémon abilities, the script needed to access dictionaries inside a list.

The Pokémon response also contained a URL for its type. Following that URL allowed the script to make another GET request and retrieve Electric-type Pokémon.

This demonstrated how related API resources can be connected through URLs.


## API 3: REST Countries

### Base URL
https://api.restcountries.com/countries/v5

### Authentication
The API requests used an Authorization header containing a Bearer token loaded from an environment variable named REST_COUNTRIES_API_KEY.

### Endpoints Tested

#### 1. GET /countries/v5?q=Japan

Description: Searches for Japan and retrieves its official name, capital, population, and region.

Example response:
```json
{
  "data": {
    "objects": [
      {
        "names": {
          "official": "Japan"
        },
        "capitals": [
          {
            "name": "Tokyo"
          }
        ],
        "population": 122650000,
        "region": "Asia"
      }
    ]
  }
}
```

Status: 200 OK

#### 2. GET /countries/v5?region=Asia&limit=100

Description: Retrieves countries belonging to Asia. The script sorts their common names alphabetically and prints the first ten.

Example response:
```json
{
  "data": {
    "objects": [
      {
        "names": {
          "common": "Afghanistan"
        }
      },
      {
        "names": {
          "common": "Japan"
        }
      }
    ],
    "meta": {
      "total": 52
    }
  }
}
```

Status: 200 OK

Total countries returned: 52

#### 3. GET /countries/v5?q=Narnia

Description: Tests error handling by searching for a country that does not exist.

Example response:
```json
{
  "data": {
    "objects": []
  },
  "meta": {
    "total": 0,
    "count": 0
  }
}
```

Status: 200 OK

Result: No matching country found.

### Rate Limits
No HTTP 429 errors were encountered during testing. The exact rate limit was not verified.

### Challenges and Observations
REST Countries returned nested JSON objects, requiring multiple dictionary and list accesses to extract country information.

The region request initially returned only 25 countries because of pagination. Adding the limit=100 query parameter allowed the script to retrieve all 52 countries in Asia.

Searching for a nonexistent country returned HTTP 200 OK with an empty objects list rather than HTTP 404.

The script handled this by checking whether the returned list was empty and displaying "No matching country found."

This demonstrated that a successful HTTP response does not always mean the requested data exists.




## API 3: REST Countries

### Base URL
https://api.restcountries.com/countries/v5

### Authentication
Bearer token authentication was used.

The API key was stored in an environment variable named `REST_COUNTRIES_API_KEY` and accessed using `os.getenv()`.

The token was included in the request headers:

```python
headers = {
    "Authorization": f"Bearer {REST_COUNTRIES_KEY}"
}
```

This keeps the API key out of the source code.

### Endpoints Tested

#### 1. GET /countries/v5?q=Japan

Description: Retrieves information about Japan using a country-name query parameter.

Example response:
```json
{
  "data": {
    "objects": [
      {
        "names": {
          "official": "Japan",
          "common": "Japan"
        },
        "capitals": [
          {
            "name": "Tokyo"
          }
        ],
        "population": 122650000,
        "region": "Asia"
      }
    ]
  }
}
```

Status: 200 OK

#### 2. GET /countries/v5?region=Asia&limit=100

Description: Retrieves countries in Asia using query parameters to filter by region and limit the results.

The script extracts the common names, sorts them alphabetically, and prints the first 10 countries.

Example response:
```json
{
  "data": {
    "objects": [
      {
        "names": {
          "common": "Afghanistan"
        },
        "region": "Asia"
      },
      {
        "names": {
          "common": "Armenia"
        },
        "region": "Asia"
      }
    ]
  }
}
```

Status: 200 OK

Results:
- Total countries returned: 52
- First 10 names displayed alphabetically
- The response was filtered to countries in Asia

#### 3. GET /countries/v5?q=Narnia

Description: Tests how the API handles a search for a country that does not exist.

Example response:
```json
{
  "data": {
    "objects": []
  }
}
```

Status: 200 OK

Result:
No matching country found.

The script checked whether the returned list was empty and printed a message instead of crashing.

### Rate Limits

No HTTP 429 rate-limit errors were encountered during testing.

The exact rate limit was not verified.

### Challenges and Observations

REST Countries required Bearer token authentication, unlike JSONPlaceholder and PokeAPI.

The API returned nested JSON data. To retrieve Japan's official name, capital, population, and region, the script needed to access dictionaries and lists inside the response.

Query parameters were used to search for Japan and filter countries by region.

One surprising result was that searching for a nonexistent country such as Narnia returned HTTP 200 OK with an empty list rather than HTTP 404 Not Found.

The script handled this by checking whether the list contained any countries before attempting to display the results.

This demonstrated that a successful HTTP status code does not always mean the requested information was found.
