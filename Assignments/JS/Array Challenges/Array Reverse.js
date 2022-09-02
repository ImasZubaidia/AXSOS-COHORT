function reverse1(arr) {

  var reversed = [];
  for (let index = arr.length-1; index >= 0; index--) {
    reversed.push(arr[index]);
  }

  return reversed;
}

var result = reverse1(["a", "b", "c", "d", "e"]);
console.log(result); 



//in place
function reverse2(arr) {
  
  var start = 0;
  var end = arr.length - 1;
  while (start < end) {
    swap(start, end, arr);
    start++;
    end--;
  }
  return arr;
}

function swap(i, j,arr) {
  var temp = arr[i];
  arr[i] = arr[j]
  arr[j]= temp
}
var result = reverse2(["a", "b", "c", "d", "e"]);
console.log(result); 