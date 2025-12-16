// Найти количество символов в строке
let str1 = 'I learn JavaScript!';
let length1 = str1.length;
console.log(length1); // Выводит 20

let removed1 = str1.substr(0, 1) + str1.substr(-1);

let removed2 = str1.substring(0, 1) + str1.substring(18, 19);

let removed3 = str1.slice(0, 1) + str1.slice(-1);

console.log(removed1); 
console.log(removed2); 
console.log(removed3); 