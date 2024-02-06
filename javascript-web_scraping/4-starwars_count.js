#!/usr/bin/node
const request = require('request');
const apiUrl = process.argv[2];

request(apiUrl, function (err, response, body) {
  if (err) {
    console.error(err);
  } else {
    let counter = 0;
    const films = JSON.parse(body).results;

    for (let result = 0; result < films.length; result++) {
      const characters = films[result].characters;

      const wedgeAntilles = characters.find(character => character === 'https://swapi-api.alx-tools.com/api/people/18/' || character === 'http://swapi-api.alx-tools.com/api/people/18/');

      if (wedgeAntilles) {
        counter += 1;
      }
    }

    console.log(counter);
  }
});
