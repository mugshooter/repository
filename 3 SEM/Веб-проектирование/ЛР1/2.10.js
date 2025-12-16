let snakeCase = 'var_test_text';
let camelCase = snakeCase.replace(/_([a-z])/g, function(match, letter) {
  return letter.toUpperCase();
});

console.log(camelCase); 