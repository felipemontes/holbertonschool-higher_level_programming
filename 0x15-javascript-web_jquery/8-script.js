const URL = 'https://swapi-api.hbtn.io/api/films/?format=json';

$.get(URL, function (movies) {
  const movie = movies.results;
  for (let i = 0; i < movie.length; i++) {
    $('UL#list_movies').append('<li>' + movie[i].title + '</li>');
  }
});
