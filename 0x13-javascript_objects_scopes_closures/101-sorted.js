#!/usr/bin/node

const dict = require('./101-data').dict;

const dKeys = Object.keys(dict);
const values = Object.values(dict);
let matched;
const usersByOccurrence = {};

// Iterate over the original dictionary and populate the new dictionary
for (let i = 0; i < values.length; i++) {
  usersByOccurrence[JSON.stringify(values[i])] = [];
  matched = dKeys.filter(key => dict[key] === values[i]);
  matched.forEach(item => usersByOccurrence[JSON.stringify(values[i])].push(item));
}
console.log(usersByOccurrence);
