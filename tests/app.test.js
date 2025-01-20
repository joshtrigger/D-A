// import { hasDuplicates, wordBuilder } from '../src/index';
const { hasDuplicates, wordBuilder, intersection } = require('../src/index');

test('should build words', () => {
  const result = wordBuilder(['a', 'b', 'c', 'd']);
  const expectedResult = [
    'ab',
    'ac',
    'ad',
    'ba',
    'bc',
    'bd',
    'ca',
    'cb',
    'cd',
    'da',
    'db',
    'dc',
  ];

  expect(result).toEqual(expectedResult);
});

[
  { input: [1, 2, 4, 6, 2, 8], expectedResult: true },
  { input: [1, 2, 4, 6, 7, 9], expectedResult: false },
].forEach((element) => {
  it(`should check for duplicates - "${element.expectedResult
    .toString()
    .toUpperCase()}"`, () => {
    const result = hasDuplicates(element.input);
    expect(result).toEqual(element.expectedResult);
  });
});

[
  {
    array1: [1, 2, 3, 4, 5, 7],
    array2: [0, 2, 4, 6, 8],
    expectedResult: [2, 4],
  },
  {
    array1: [1, 2, 4],
    array2: [7, 5, 6, 3, 8],
    expectedResult: [],
  },
].forEach((element) => {
  it(`should check for intersecting numbers - "${
    element.expectedResult.length > 0
  }"`, () => {
    const result = intersection(element.array1, element.array2);
    expect(result).toEqual(element.expectedResult);
  });
});
