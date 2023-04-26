#!/usr/bin/node

const request = require('request');
const movieId = process.argv[2];
const url = `https://swapi-api.alx-tools.com/api/films/${movieId}/`;

request(url, function (error, response, body) {
  if (error) {
    console.log(error);
  } else {
    const characters = JSON.parse(body).characters;
    printCharacters(characters, 0); // start with the first character
  }
});

function printCharacters (characters, index) {
  if (index < characters.length) { // if the index is less than the length of the array
    request(characters[index], function (error, response, body) {
      if (error) {
        console.log(error);
      } else {
        const characterName = JSON.parse(body).name;
        console.log(characterName);
        printCharacters(characters, index + 1); // recursively print the next character
      }
    });
  }
}
