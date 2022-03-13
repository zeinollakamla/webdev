"use strict"
//The name of JavaScript

let name = prompt("What is the “official” name of JavaScript?", "");

if (name == "ECMAScript") {
    alert("Right!");
}
else {
    alert("You don’t know? ECMAScript!");
}

//Show the sign

let num = prompt("What is the “official” name of JavaScript?", 0);

if (num > 0) {
    alert(1);
}
else if (num < 0){
    alert(-1);
}
else {
    alert(0);
}

//Rewrite 'if' into '?'

let result;

result = (a + b < 4) ? "Below" : "Over";

//Rewrite 'if..else' into '?'

let message;

message = (login == "Employee") ? "Hello" :
  (login == "Director") ? "Greeting":
  (login == "") ? "No login" :
  "";