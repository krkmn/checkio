"use strict";

function longRepeat(line) {
	if (line ==="")
	{
		return 0;
	}
	let array = [];
	
	for (let sIndex = 0; sIndex < line.length; sIndex++)
	{
		for (let eIndex = sIndex + 1; eIndex < line.length+1; eIndex++)
		{
			let newLine = line.substring(sIndex,eIndex);
			let uniqueCharacters = new Set(newLine);
			//console.log(uniqueCharacters);
			if (uniqueCharacters.size === 1)
			{
				array.push(newLine);
				//console.log(newLine.substr(startIndex,endIndex+1));
			}
		}
	}
	array.sort(); //Sort alphabetically first
	array.sort((a,b) => b.length - a.length)
	console.log(array);
    return array[0].length;
}

var assert = require('assert');

if (!global.is_checking) {
    assert.equal(longRepeat('sdsffffse'), 4, "First")
    assert.equal(longRepeat('ddvvrwwwrggg'), 3, "Second")
    console.log('"Run" is good. How is "Check"?');
}