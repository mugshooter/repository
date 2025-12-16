let str1 = 'I learn JavaScript!';
let length1 = str1.length;
console.log(length1); 

let removed1 = str1.substr(0, 1) + str1.substr(-1);

let removed2 = str1.substring(0, 1) + str1.substring(18, 19);

let removed3 = str1.slice(0, 1) + str1.slice(-1);

console.log(removed1); 
console.log(removed2); 
console.log(removed3); 


let str3 = 'I learn JavaScript!';
let position3 = str3.indexOf('learn');
console.log(position3); 

let str4 = 'Очень длинный текст, который нужно, к сожалению, обрезать.';
let n = 10;
let result4 = str4.length > n ? str4.substr(0, n) + '...' : str4;
console.log(result4); 