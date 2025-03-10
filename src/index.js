/**
 * Checks for duplicates in an array using O(N)
 *
 * @param {Array} array array of number to be checked
 * @returns boolean value indicating whether an array has duplicates or not
 */
const hasDuplicates = (array) => {
  let existingNumbers = [];

  for (let i = 0; i < array.length; i++) {
    if (existingNumbers[array[i]] === 1) {
      return true;
    } else {
      existingNumbers[array[i]] = 1;
    }
  }
  return false;
};

const wordBuilder = (letters) => {
  let collections = [];
  for (let i = 0; i < letters.length; i++) {
    for (let j = 0; j < letters.length; j++) {
      if (i !== j) {
        collections.push(letters[i] + letters[j]);
      }
    }
  }

  return collections;
};

const intersection = (array1, array2) => {
  let smallerArray;
  let largerArray;

  if (array1.length > array2.length) {
    smallerArray = array2;
    largerArray = array1;
  } else {
    smallerArray = array1;
    largerArray = array2;
  }

  let hashTable = {};

  let result = [];

  for (const el1 of largerArray) {
    hashTable[el1] = true;
  }

  for (const el2 of smallerArray) {
    if (hashTable[el2]) {
      result.push(el2);
    }
  }

  return result;
};

// example of using recursion to print out numbers instead of forLoop
function countdown(number) {
  console.log(number);

  if (number === 0) {
    // this is the base case
    return;
  } else {
    countdown(number - 1);
  }
}

export default { hasDuplicates, wordBuilder, intersection, countdown };
