
function calculate(){

let calls = document.getElementById('calls').value;
let value = document.getElementById('value').value;
let close = document.getElementById('close').value;

let jobs = calls * (close/100);
let revenue = jobs * value;
let monthly = revenue * 4;

document.getElementById('result').innerText =
"Estimated lost revenue: $" + monthly.toLocaleString() + " per month";

}
