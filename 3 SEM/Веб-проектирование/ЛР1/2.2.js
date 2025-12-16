let str = 'aaa bbb ccc';

let removed1 = str.substr(0, 4) + str.substr(7);

let removed2 = str.substring(0, 4) + str.substring(7);

let removed3 = str.slice(0, 4) + str.slice(7);

console.log(removed1); 
console.log(removed2); 
console.log(removed3); 