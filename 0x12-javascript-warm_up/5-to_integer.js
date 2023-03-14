#!/usr/bin/node

const arg = process.argv[2];

if (!isNaN(arg)) {
  const num = parseInt(arg);
  console.log(`My number: ${num}`);
} else {
  console.log('Not a number');
}
