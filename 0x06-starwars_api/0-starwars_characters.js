#!/usr/bin/node

const request = require('request');
const movieId = process.argv[2];
const apiUrl = `https://swapi-api.alx-tools.com/api/films/${movieId}/`;

if (!movieId) {
  process.exit(1);
}

request(apiUrl, (error, response, body) => {
  if (error) {
    return;
  }

  if (response.statusCode !== 200) {
    return;
  }

  const movieData = JSON.parse(body);
  const characters = movieData.characters;

  characters.forEach((characterUrl) => {
    request(characterUrl, (error, response, body) => {
      if (error) {
        return;
      }

      const characterData = JSON.parse(body);
      console.log(characterData.name);
    });
  });
});
