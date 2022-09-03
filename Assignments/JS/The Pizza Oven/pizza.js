function pizzaOven(crustType, sauceType, cheeses, toppings) {
  var pizza = {};
  pizza.curstType = crustType;
  pizza.sauceType = sauceType;
  pizza.cheeses = cheeses;
  pizza.toppings = toppings;
  return pizza;
}

var p1 = pizzaOven("deep dish", "traditional", "mozarella", [
  "pepperoni",
  "suasage",
]);
//console.log(p1);
var p2 = pizzaOven(
  "hand tossed",
  "marinara",
  ["mozarella", "feta"],
  ["mushrooms", "olives", "onions"]
);
//console.log(p2);
var p3 = pizzaOven("deep dish", "marinara", "fata", [
  "fried onions",
  "pepperoni",
]);
//console.log(p3);
var p4 = pizzaOven("hand tossed", "traditional", "mozarella", [
  "suasage",
  "mushrooms",
]);
//console.log(p4);


function randomPizza(p1, p2, p3, p4) {
    var random = Math.floor(Math.random() * 4) + 1;
    if (random == 1) {
        console.log(p1); 
    }
    else if (random == 2) {
        console.log(p2); 
    }
    else if (random == 3) {
        console.log(p3);
    }
    else {
        console.log(p4);
    }
    
}


randomPizza(p1, p2, p3, p4);