#!/usr/bin/node

const $ = window.$;
$.getJSON('https://swapi-api.alx-tools.com/api/films/?format=json', function (data) {
  $.each(data.results, function (i, movie) {
    $('ul#list_movies').append('<li>' + movie.title + '</li>');
  });
});
