
let init_amount = 500;

function increase_one(){
    init_amount += 1;
    document.getElementById('amount').innerHTML = init_amount;
}
function increase_ten(){
    init_amount += 10;
    document.getElementById('amount').innerHTML = init_amount;
}
function increase_hundred(){
    init_amount += 100
    document.getElementById('amount').innerHTML = init_amount;
}
function increase_fivehundred(){
    init_amount += 500;
    document.getElementById('amount').innerHTML = init_amount;
}
function api_test(){
    var request = new XMLHttpRequest();
 
    request.open('GET', 'https://jsonplaceholder.typicode.com/users/1', true);
    request.responseType = 'json';
    
    var data
    request.onload = function () {
      data = this.response;
      console.log(data);
    };
 
    request.send();
    //return data;
}