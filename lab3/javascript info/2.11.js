"use strict"

//Check the range between
let age;
if (age>=14 && age<=90){

}
//Check the range outside
if (!(age >= 14 && age <= 90)){

}
if (age < 14 || age > 90){

}
//Check the login
let userName = prompt("Кто там?", '');

if (userName === 'Админ') {

  let pass = prompt('Пароль?', '');

  if (pass === 'Я главный') {
    alert( 'Здравствуйте!' );
  } else if (pass === '' || pass === null) {
    alert( 'Отменено' );
  } else {
    alert( 'Неверный пароль' );
  }

} else if (userName === '' || userName === null) {
  alert( 'Отменено' );
} else {
  alert( "Я вас не знаю" );
}