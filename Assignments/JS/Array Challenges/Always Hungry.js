
function alwaysHungry(arr) {
    var containsFood = false;
    for (i = 0; i < arr.length; i++){
        if (arr[i] == "food") {
            console.log("yummy"); 
            containsFood = true;
        }
        
    }

    if (containsFood == false) {
      console.log("I am hungry");
    }
}

alwaysHungry([4, 1, 5, 7, 2]);
alwaysHungry([3.14, "food", "pie", true, "food"]);