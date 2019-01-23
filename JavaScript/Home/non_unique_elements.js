"use strict";

function nonUniqueElements(data) {
	const obj = {};
	var arr = [];
	
	for (const key of data){
		obj[key] = 0;
	}
	
	for (const key of data){
		obj[key] += 1;
	}
	
	for (const key of data){
		if (obj[key] > 1){
			arr.push(key);
		}
	}
	
	
	console.log(arr);

		
	
	
	
	
	
    return arr;
}

var assert = require('assert');

if (!global.is_checking) {
    assert.deepEqual(nonUniqueElements([1, 2, 3, 1, 3]), [1, 3, 1, 3], "1st example");
    assert.deepEqual(nonUniqueElements([1, 2, 3, 4, 5]), [], "2nd example");
    assert.deepEqual(nonUniqueElements([5, 5, 5, 5, 5]), [5, 5, 5, 5, 5], "3rd example");
    assert.deepEqual(nonUniqueElements([10, 9, 10, 10, 9, 8]), [10, 9, 10, 10, 9], "4th example");
    console.log("Coding complete? Click 'Check' to review your tests and earn cool rewards!");
}
