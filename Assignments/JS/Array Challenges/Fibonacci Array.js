function fibonacciArray(n) {
    var result = [];
    var first = 0;
    var second = 1;
    var nextFab;
    result.push(first);
    result.push(second);
    for (i = 0; i <n-2; i++){
        nextFab=first+second
        result.push(nextFab);    
        first = second;
        second= nextFab;

    }
  return result;
}

var result1 = fibonacciArray(10);
console.log(result1); // we expect back [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
