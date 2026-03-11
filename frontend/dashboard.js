function loadChart(symbol){

document.getElementById("chart").innerHTML = `

<iframe
width="100%"
height="600"
src="https://www.tradingview.com/chart/?symbol=NSE:${symbol}&interval=1D">
</iframe>

`;

}
