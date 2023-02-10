#!/usr/bin/node

const request = require('request');
const movieId = process.argv[2];

function getRequest (url) {
  return new Promise((resolve, reject) => {
    request(url, (error, response, body) => {
      if (error || response.statusCode !== 200) {
        reject(error);
      } else {
        resolve(body);
      }
    });
  });
}

async function getNames () {
  const url = `https://swapi-api.alx-tools.com/api/films/${movieId}/`;
  const movie = await getRequest(url);
  const characterUrls = JSON.parse(movie).characters;
  const characterPromises = characterUrls.map((val) => getRequest(val));
  const characters = await Promise.all(characterPromises);
  characters.forEach((val) => console.log(JSON.parse(val).name));
}

getNames();
