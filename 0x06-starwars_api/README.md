#  Star Wars Characters

# Problem
Write a script that prints all characters of a Star Wars movie:

The first positional argument passed is the Movie ID - example: 3 = “Return of the Jedi”
Display one character name per line in the same order as the “characters” list in the /films/ endpoint
You must use the Star wars API
You must use the request module

# Requirements
1. Use a List to preserve sequential ordering of characters when fetching from the star wars api
2. Use promises to make sure all pending operations are correctly handled when printing the names

# [Solution](./0-starwars_characters.js)
1. Validate movie id provided from argument is an integer
2. Fetch the film using the id with `https://swapi-api.alx-tools.com/api/films/<id>`
3. Access the characters attribute from the response object to load all characters links
    and for each character link extract the character name which is added to a local variable list all_characters
3. for each name in the variable list print the name of the character

Time complexity => O(n) # dependent on number of characters in a film
Space complexity => O(n) # dependent on number of characters in a film
