#!/usr/bin/node
const request = require('request');
const apiUrl = process.argv[2];

request(apiUrl, function (err, response, body) {
  if (err) {
    console.error('Error:', err);
    return; // Exit the function if an error occurs
  }

  try {
    const films = JSON.parse(body).results;
    let counter = 0;

    for (let result = 0; result < films.length; result++) {
      const characters = films[result].characters;

      // Check if Wedge Antilles is present in the characters array
      const wedgeAntilles = characters.find(character => 
        character === 'https://swapi-api.alx-tools.com/api/people/18/' || 
        character === 'http://swapi-api.alx-tools.com/api/people/18/'
      );

      // Increment the counter if Wedge Antilles is found
      if (wedgeAntilles) {
        counter++;
      }
    }

    console.log('Count of movies where Wedge Antilles is present:', counter);
  } catch (error) {
    console.error('Error parsing response:', error);
  }
});
