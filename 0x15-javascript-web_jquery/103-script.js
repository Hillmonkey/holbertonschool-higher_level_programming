$.when($.ready).then(function () {
  $('INPUT#btn_search').keypress(function () {
    let city = $('INPUT#city_search').val();
    $.getJSON('https://query.yahooapis.com/v1/public/yql?q=select%20wind%20from%20weather.forecast%20where%20woeid%20in%20(select%20woeid%20from%20geo.places(1)%20where%20text%3D%22:' + city + '%22)&format=json', function (data) {
      let windSpeed = data.query.results.channel.wind.speed;
      $('DIV#wind_speed').text(windSpeed);
    });
  });
});

$.when($.ready).then(function () {
  $('INPUT#city_search').keypress(function (e) {
    console.log(e.originalEvent.key);
    let key = e.which;
    if (key == 13) {
      let city = $('INPUT#city_search').val();
      $.getJSON('https://query.yahooapis.com/v1/public/yql?q=select%20wind%20from%20weather.forecast%20where%20woeid%20in%20(select%20woeid%20from%20geo.places(1)%20where%20text%3D%22:' + city + '%22)&format=json', function (data) {
        let windSpeed = data.query.results.channel.wind.speed;
        $('DIV#wind_speed').text(windSpeed);
      });
    }
  });
});
