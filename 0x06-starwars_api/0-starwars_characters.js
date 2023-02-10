#!/usr/bin/node

const movieId = process.argv[2];
const url = `https://swapi-api.alx-tools.com/api/films/${movieId}/`;

const request = require('request');
request(url, (error, response, body) => {
  if (error) {
    console.error(error);
    return;
  }
  body = JSON.parse(response.body);
  const charactersUrls = body.characters;
  charactersUrls.forEach((val) => {
    request(val, (error, response, body) => {
      if (error) {
        console.error(error);
        return;
      }
      const name = JSON.parse(response.body).name;
      console.log(name);
    });
  });
});
