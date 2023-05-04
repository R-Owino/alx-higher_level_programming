#!/usr/bin/node

const $ = window.$;
$(document).ready(function () {
  // Add item
  $('#add_item').click(function () {
    $('UL.my_list').append('<li>Item</li>');
  });

  // Remove item
  $('#remove_item').click(function () {
    $('UL.my_list li:last-child').remove();
  });

  // Clear list
  $('#clear_list').click(function () {
    $('UL.my_list').empty();
  });
});
