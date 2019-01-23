"use strict";

function countNeighbours(data, row, col) {
	
	var count = 0;
	var len_row = data.length;
	var len_col = data[0].length;
	for (var i = -1; i < 2; i++){
		for (var j = -1; j < 2; j++){
			
			let dummy_row = row + i;
			let dummy_col = col + j;
			if (dummy_row >= 0 && dummy_col >= 0 && dummy_row < len_row && dummy_col < len_col) {
					count += data[dummy_row][dummy_col];
			}
		}
	}
	count -= data[row][col];
    return count;
}

var assert = require('assert');

if (!global.is_checking) {
    assert.equal(countNeighbours([[1, 0, 0, 1, 0],
                                  [0, 1, 0, 0, 0],
                                  [0, 0, 1, 0, 1],
                                  [1, 0, 0, 0, 0],
                                  [0, 0, 1, 0, 0]], 1, 2), 3, "1st example");

    assert.equal(countNeighbours([[1, 0, 0, 1, 0],
                                  [0, 1, 0, 0, 0],
                                  [0, 0, 1, 0, 1],
                                  [1, 0, 0, 0, 0],
                                  [0, 0, 1, 0, 0]], 0, 0), 1, "2nd example");

    assert.equal(countNeighbours([[1, 1, 1],
                                  [1, 1, 1],
                                  [1, 1, 1]], 0, 2), 3, "Dense corner");

    assert.equal(countNeighbours([[0, 0, 0],
                                  [0, 1, 0],
                                  [0, 0, 0]], 1, 1), 0, "Single");
	assert.equal(countNeighbours([[1,0,1,0,1],
	[0,1,0,1,0],
	[1,0,1,0,1],
	[0,1,0,1,0],
	[1,0,1,0,1],
	[0,1,0,1,0]]
	,5,4), 2,"Unsymmetrical");
    console.log("Coding complete? Click 'Check' to review your tests and earn cool rewards!");
}
