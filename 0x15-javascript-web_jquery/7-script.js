const URL = 'https://swapi-api.hbtn.io/api/people/5/?format=json';
$.get(URL, function (character) {
  const name = character.name;
  $('DIV#character').append(name);
});
