let getWind = function (city) {
  return ($.getJSON('https://query.yahooapis.com/v1/public/yql?q=select%20wind%20from%20weather.forecast%20where%20woeid%20in%20(select%20woeid%20from%20geo.places(1)%20where%20text%3D%22:' + city + '%22)&format=json', function (data) {
    console.log(data.query.results.channel.wind.speed);
    return (data.query.results.channel.wind.speed);
  }));
};

// console.log(getWind('Dallas'), 'woot');

$.when($.ready).then(function () {
  $('INPUT#btn_search').click(function () {
    let city = $('INPUT#city_search').val();
    $('DIV#wind_speed').text(getWind(city));
  });
});

$.when($.ready).then(function () {
  $('INPUT#city_search').keypress(function (e) {
    console.log(e.originalEvent.key);
    let key = e.which;
    if (key == 13) {
      let city = $('INPUT#city_search').val();
      $('DIV#wind_speed').text(getWind(city));
    }
  });
});
