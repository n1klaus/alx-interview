#!/usr/bin/node

const request = require('request');

const URL = 'https://swapi-api.alx-tools.com/api';

// function to get all characters in a film id specified
// from the node arguments
function getCharacters () {
  if (process.argv.length !== 3) return Promise.reject(new Error());
  const filmId = process.argv[2];
  const characterResolver = [];
  if (isNaN(filmId)) return Promise.reject(new Error());
  // make a GET request for the film data
  request(`${URL}/films/${filmId}`, function (err, response, body) {
    if (err) return Promise.reject(err);
    if (body && response.statusCode === 200) {
      // parse the body content and extract the characters from the object
      const info = JSON.parse(body);
      const characters = info.characters;
      // if characters were found create an iteration of the array of links
      // to the character to get their names
      if (characters) {
        Array.from(characters).map((charLink) => {
          let characterName = new Promise((resolve, reject) => {
            // make another GET request using the link to get the character
            request(`${charLink}`, (err, response, body) => {
              if (err) return reject(err);
              if (body && response.statusCode === 200) {
                // parse the recived body and extract the name from the object
                const characterResponse = JSON.parse(body);
                characterName = characterResponse.name;
                // return the character name as a promise to be resolved
                return resolve(characterName);
              }
            });
          });
          // when the request is done add our character name to our array
          characterResolver.push(characterName);
          return Promise.resolve(characterName);
        });
        // wait until all promise objects in the array are fulfilled then
        // print to the standard output in the order inserted
        Promise.all(characterResolver)
          .then((characters) => {
            for (const character of characters) {
              console.log(character);
            }
          });
      }
    }
  });
}
getCharacters();
