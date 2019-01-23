"use strict";

function mostWanted(data) {    
	var result = {};
	
	for (let i = 0; i < data.length; i++)
	{
		let letter = data[i].toLowerCase();
		if ('abcdefghijklmnopqrstuvwxyz'.includes(letter))
			{
			if (!result[letter])
			{
				result[letter] = 1
			}
			else
			{
				++result[letter];
			}
		}
	}
	
	let array_of_object = []
	let max = 0;
	for (let key in result)
	{
		array_of_object.push([key, result[key]])
		if(result[key] > max)
		{
			max = result[key];
		}
		
	}
	array_of_object.sort();	// Get letters in right order
	var return_elem = '';
	for (let i = 0; i<array_of_object.length; i++)
	{
		let elem = array_of_object[i]
		if (elem[1] === max)
		{
			return_elem = elem[0];
			break;
		}
	}

    return return_elem;
}

var assert = require('assert');

if (!global.is_checking) {
    assert.equal(mostWanted("Hello World!"), "l", "1st example");
    assert.equal(mostWanted("How do you do?"), "o", "2nd example");
    assert.equal(mostWanted("One"), "e", "3rd example");
    assert.equal(mostWanted("Oops!"), "o", "4th example");
    assert.equal(mostWanted("AAaooo!!!!"), "a", "Letters");
	mostWanted("Lorem ipsum dolor sit amet");
    console.log("Coding complete? Click 'Check' to review your tests and earn cool rewards!");
}
