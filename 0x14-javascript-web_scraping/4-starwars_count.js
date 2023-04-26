#!/usr/bin/node

const request = require('request');
const url = process.argv[2];

request(url, (error, response, body) => {
  if (error) {
    console.log(error);
  } else {
    let count = 0;
    const films = JSON.parse(body).results;
    for (let i = 0; i < films.length; i++) {
      let j = 0;
      const character = films[i].characters;
      while (j < character.length) {
        if (character[j].includes('18')) {
          count++;
        }
        j++;
      }
    }
    console.log(count);
  }
});
