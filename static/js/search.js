function myFunction() {
var input, filter;
input = document.getElementsByClassName('myLinks');
filter = document.getElementById('myInput').value.toUpperCase();
// Loop through all list items, and hide those who don't match the search query
for (i = 0; i < input.length; i++) {
    var currentElem = input[i];
    var currentElemChild = input[i].children[0]
    if (currentElemChild.innerHTML.toUpperCase().indexOf(filter) > -1) {
        currentElem.style.display = "";
    } else {
        currentElem.style.display = "none";
    }
  }
}
document.getElementById('myInput').addEventListener('keyup', myFunction);