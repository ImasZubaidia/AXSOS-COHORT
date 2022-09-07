function acceptCookie() {
    var cookieAlert = document.getElementById("cookie-section");
    cookieAlert.remove();
}

function navigate(cityElement) {
    alert("Loading weather report of "  + cityElement.innerText);
}

function convertTempUnit() {

	var tempArray=createTempreturesArray();

    if (document.getElementById("tempSelector").selectedIndex == 0)
    {
        var FahrenheitValues = fromCelciusToFahrenheit(tempArray);
        changeTempretureinHTML(FahrenheitValues);

    } else if (document.getElementById("tempSelector").selectedIndex == 1) {

        var celciusValues = fromFahrenheitToCelcius(tempArray);
        changeTempretureinHTML(celciusValues);
        
    }
	
}

function createTempreturesArray() {
    var AlltempsValues = [];

    AlltempsValues[0] = parseInt(document.getElementById("tempMax1").innerHTML);
    AlltempsValues[1] = parseInt(document.getElementById("tempMax2").innerHTML);
    AlltempsValues[2] = parseInt(document.getElementById("tempMax3").innerHTML);
    AlltempsValues[3] = parseInt(document.getElementById("tempMax4").innerHTML);
    AlltempsValues[4] = parseInt(document.getElementById("tempLowest1").innerHTML);
    AlltempsValues[5] = parseInt(document.getElementById("tempLowest2").innerHTML);
    AlltempsValues[6] = parseInt(document.getElementById("tempLowest3").innerHTML);
    AlltempsValues[7] = parseInt(document.getElementById("tempLowest4").innerHTML);

    return AlltempsValues;
}

function fromCelciusToFahrenheit(array) {
    for (let index = 0; index < array.length; index++) {
        var celsius=array[index];
        var FahTemp= (celsius * 1.8) + 32
        array[index]=Math.floor(FahTemp);    
    }

    return array;
}


function fromFahrenheitToCelcius(array){
    for (let index = 0; index < array.length; index++) {
        var FahTemp = array[index];
        var celsius = (FahTemp - 32) / 1.8;
        array[index] = Math.floor(celsius);
        
    }
    return array;
}

function changeTempretureinHTML(array) {
     document.getElementById("tempMax1").innerHTML = array[0];
     document.getElementById("tempMax2").innerHTML = array[1];
     document.getElementById("tempMax3").innerHTML = array[2];
     document.getElementById("tempMax4").innerHTML = array[3];
     document.getElementById("tempLowest1").innerHTML = array[4];
     document.getElementById("tempLowest2").innerHTML = array[5];
     document.getElementById("tempLowest3").innerHTML = array[6];
     document.getElementById("tempLowest4").innerHTML = array[7];
    
}