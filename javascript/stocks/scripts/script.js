
function getUserSelectedStock() { 
  let userValue = searchInput.value;

  if (userValue)
  {
    getStockData(userValue);  
  }
}

function displayInitialStocks() {
  let initalStocks = ["GOOGL", "AAPL", "MSFT", "AMZN"];

  initalStocks.forEach(getStockData);
}

async function getStockData(symbol) {
  let tableBody = document.getElementById("stock-table-body");

  let url = 'https://finnhub.io/api/v1/quote?symbol=' + symbol + '&token=d8jcn99r01qh6g3phoq0d8jcn99r01qh6g3phoqg';

  const data = await fetch(`${url}`).then(response => response.json());
      
  if(data.cod === `404`){

      not_found.style.display = "flex";
      display.style.display = "none";

      return;
  }

    console.log(data);
    let price = data["c"];

    // Check the price > 0 to make sure it is a valid stock price and add as a new row to the table

    if (price > 0) {
      let time = data["t"] * 1000; // Need to convert seconds to milliseconds
      let date = new Date(time);
      var dateTextVal = date.toLocaleDateString(); // gives date in local Format eg 04/07/2026
      var timeTextVal = date.toLocaleTimeString(); // gives time in local Format eg: 09:00:00

      addAnotherRow(symbol, price, dateTextVal);
  }
}

function addAnotherRow(symbol, price, dateTextVal) {
  var table = document.getElementById("stock-table");
  var row = table.insertRow(1);
  var cell1 = row.insertCell(0);
  var cell2 = row.insertCell(1);
  var cell3 = row.insertCell(2);
  cell1.innerHTML = symbol;
  cell2.innerHTML = price;
  cell3.innerHTML = dateTextVal;
}


