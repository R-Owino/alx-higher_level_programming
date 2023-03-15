#!/usr/bin/node

const SquareFrom5 = require('./5-square');

class Square extends SquareFrom5 {
  charPrint (c) {
    if (c === undefined) {
      c = 'X';
    }
    for (let i = 0; i < this.height; i++) {
      let sqr = '';
      for (let j = 0; j < this.width; j++) {
        sqr += c;
      }
      console.log(sqr);
    }
  }
}

module.exports = Square;
