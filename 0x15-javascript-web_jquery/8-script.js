$.getJSON('https://swapi.co/api/films/?format=json', function (data) {
  console.log(data);
  for (let i = 0; i < data.count; i++) {
    $('UL#list_movies').append('<li>' + data.results[i].title + '</li>');
  }
});
