#!/usr/bin/node

const request = require('request');

const filmUrl = 'https://swapi-api.alx-tools.com/api/films/';

try {
  if (process.argv.length === 3) {
    const filmId = process.argv[2];
    if (!isNaN(filmId)) {
      let characters;
      request
        .get(`${filmUrl}${filmId}`)
        .on('response', function (response) {
        //   console.log(response.statusCode);
        //   console.log(response.headers['content-type']);
          if (response.statusCode === 200) {
            const respData = response.toJSON();
            console.log(respData);
            characters = respData.characters;
            // console.log(characters);
            if (characters) {
              const characterNames = [];
              characters.forEach(charLink => {
                let characterResponse;
                request
                  .get(`${charLink}`)
                  .on('response', function (response) {
                    // console.log(response.statusCode);
                    // console.log(response.headers['content-type']);
                    characterResponse = response.toJSON();
                  })
                  .on('error', function (err) {
                    console.error(err);
                  });
                characterNames.push(characterResponse.name);
              });
              console.log(characterNames.join('\n'));
            }
          }
        })
        .on('error', function (err) {
          console.error(err);
        });
    }
  }
} catch (e) {
  console.error(e);
} finally {
  process.exit();
}
