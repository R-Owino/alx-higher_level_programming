#!/usr/bin/node

const fs = require('fs');

// Get the file paths from the command line arguments
const [, , file1, file2, dest] = process.argv;

// Read the contents of the first file
const data1 = fs.readFileSync(file1, 'utf8');

// Read the contents of the second file
const data2 = fs.readFileSync(file2, 'utf8');

// Concatenate the contents of the two files
const result = data1 + data2;

// Write the result to the destination file
fs.writeFileSync(dest, result);
