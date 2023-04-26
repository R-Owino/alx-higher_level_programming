#!/usr/bin/node

const request = require('request');

const filmId = process.argv[2];
const apiUrl = `https://swapi-api.hbtn.io/api/films/${filmId}`;

request(apiUrl, (error, response, body) => {
  if (error) {
    console.error(error);
    return;
  }

  const characters = JSON.parse(body).characters;
  displayCharacterNames(characters);
});

function displayCharacterNames (characters) {
  let currentIndex = 0;

  function getNextCharacter () {
    if (currentIndex >= characters.length) {
      return;
    }

    const currentCharacterUrl = characters[currentIndex];
    request(currentCharacterUrl, (error, response, body) => {
      if (error) {
        console.error(error);
      } else {
        const currentCharacter = JSON.parse(body);
        console.log(currentCharacter.name);
      }

      currentIndex++;
      getNextCharacter();
    });
  }

  getNextCharacter();
}
