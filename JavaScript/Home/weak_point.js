"use strict";

function weakPoint(matrix){
	let row_sums = matrix.map(x => x.reduce((y,z) => y+z));
	let col_sums = matrix[0];
	
	for (let i = 1; i < matrix.length; i++)
	{
		for (let j = 0; j < matrix[i].length; j++)
		{
			col_sums[j] += matrix[i][j];
		}
	}
		
	var min_row_i = 0;
	var min_row = Infinity;
	for (let i = 0; i < row_sums.length; i++)
	{
		if (row_sums[i] < min_row)
		{
			min_row = row_sums[i];
			min_row_i = i;
		}
	}
	
	var min_col_i = 0;
	var min_col = Infinity;
	for (let i = 0; i < col_sums.length; i++)
	{
		if (col_sums[i] < min_col)
		{
			min_col = col_sums[i];
			min_col_i = i;
		}
	}
	
    return [min_row_i, min_col_i]
}

var assert = require('assert');

if (!global.is_checking) {
    assert.deepEqual(weakPoint([[7, 2, 7, 2, 8],
                                [2, 9, 4, 1, 7],
                                [3, 8, 6, 2, 4],
                                [2, 5, 2, 9, 1],
                                [6, 6, 5, 4, 5]]
                                ), [3, 3], "Example");
    assert.deepEqual(weakPoint([[7, 2, 4, 2, 8],
                                [2, 8, 1, 1, 7],
                                [3, 8, 6, 2, 4],
                                [2, 5, 2, 9, 1],
                                [6, 6, 5, 4, 5]]
                                ), [1, 2], "Two weak point");

    assert.deepEqual(weakPoint([[1, 1, 1],
                                [1, 1, 1],
                                [1, 1, 1]]
                                ), [0, 0], "Top left");
    console.log("Coding complete? Click 'Check' to review your tests and earn cool rewards!");
}