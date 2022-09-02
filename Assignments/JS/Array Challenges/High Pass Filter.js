function highPass(arr, cutoff) {
  var filteredArr = [];
  for (i = 0; i < arr.length; i++){
    if (arr[i]>cutoff) {
      filteredArr.push(arr[i])
    }
    
  }
  return filteredArr
}

console.log(highPass([6, 8, 3, 10, -2, 5, 9],6))