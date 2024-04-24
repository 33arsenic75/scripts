var r = document.querySelectorAll('input[type=radio]');
for(var i = 0; i < r.length; i++){
  r[i].click();
}
var t = document.getElementsByTagName('textarea')
for(var i = 0; i < t.length; i++){
  t[i].value = "No Opinion";
  t[i].click();
}