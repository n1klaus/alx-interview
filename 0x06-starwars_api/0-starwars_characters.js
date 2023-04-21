#!/usr/bin/node

const request = require('request');

const URL = 'https://swapi-api.alx-tools.com/api';

function getCharacters () {
  if (process.argv.length !== 3) return Promise.reject(new Error());
  const filmId = process.argv[2];
  const characterResolver = [];
  if (isNaN(filmId)) return Promise.reject(new Error());
  request(`${URL}/films/${filmId}`, function (err, response, body) {
    if (err) return Promise.reject(err);
    if (body && response.statusCode === 200) {
      const info = JSON.parse(body);
      const characters = info.characters;
      if (characters) {
        Array.from(characters).map((charLink) => {
          let characterName = new Promise((resolve, reject) => {
            request(`${charLink}`, (err, response, body) => {
              if (err) return reject(err);
              if (body && response.statusCode === 200) {
                const characterResponse = JSON.parse(body);
                characterName = characterResponse.name;
                return resolve(characterName);
              }
            });
          });
          characterResolver.push(characterName);
          return Promise.resolve(characterName);
        });

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
