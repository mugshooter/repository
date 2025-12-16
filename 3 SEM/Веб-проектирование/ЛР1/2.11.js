function isPalindrome(str) {
    var cleanedStr = str.replace(/[\W_]/g, '').toLowerCase();
    var reversedStr = cleanedStr.split('').reverse().join('');
    return cleanedStr === reversedStr;
}

console.log(isPalindrome("Da Ad")); 
console.log(isPalindrome("Ne palindrome")); 