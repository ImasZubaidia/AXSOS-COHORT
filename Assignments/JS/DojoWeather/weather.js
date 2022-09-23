function acceptCookie() {
    var cookieAlert = document.getElementById("cookie-section");
    cookieAlert.remove();
}

function navigate(cityElement) {
    alert("Loading weather report of "  + cityElement.innerText);
}

function convertTempUnit() {

    var degrees = document.querySelectorAll('.temp')

    if (document.getElementById("tempSelector").selectedIndex == 0)
    {
        for (let i = 0; i < degrees.length; i++){
            var FahrenheitValues = fromCelciusToFahrenheit(parseInt(degrees[i].innerText));
            changeTempretureinHTML(degrees[i], FahrenheitValues);
        }
        

    } else if (document.getElementById("tempSelector").selectedIndex == 1) {

        for (let i = 0; i < degrees.length; i++) {
          var celciusValues = fromFahrenheitToCelcius(parseInt(degrees[i].innerText));
          changeTempretureinHTML(degrees[i], celciusValues);
        }        
    }
	
}

function fromCelciusToFahrenheit(degree) {
    var FahTemp = degree * 1.8 + 32;
    return Math.floor(FahTemp);
}

function fromFahrenheitToCelcius(degree) {
    var celsius = (degree - 32) / 1.8;
  return Math.floor(celsius);
}

function changeTempretureinHTML(element, value) {
  element.innerHTML = value;
}