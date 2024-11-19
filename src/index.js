/**
 * Checks for duplicates in an array using O(N) 
 * 
 * @param {Array} array array of number to be checked
 * @returns boolean value indicating whether an array has duplicates or not
 */
function hasDuplicates(array) {
  let existingNumbers = [];

  for (let i = 0; i < array.length; i++) {
    if (existingNumbers[array[i]] === 1) {
      return true;
    } else {
      existingNumbers[array[i]] = 1;
    }
  }
  return false;
}

console.log(hasDuplicates([1, 2, 4, 6, 2, 8]));
console.log(hasDuplicates([1, 2, 4, 6, 7, 9]));
