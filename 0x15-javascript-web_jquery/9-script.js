#!/usr/bin/node

const $ = window.$;
$(document).ready(function () {
  $.getJSON('https://fourtonfish.com/hellosalut/?lang=fr', function (data) {
    $('#hello').text(data.hello);
  });
});
