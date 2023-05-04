#!/usr/bin/node

const $ = window.$;
$(document).ready(function () {
  function translateHello () {
    const langCode = $('#language_code').val();
    const apiUrl = `https://www.fourtonfish.com/hellosalut/hello/${langCode}`;

    $.get(apiUrl, function (data) {
      $('#hello').html(data.hello);
    });
  }

  $('#btn_translate').click(translateHello);

  $('#language_code').keypress(function (event) {
    if (event.keyCode === 13) {
      translateHello();
    }
  });
});
