
function addItem() {
  const item = document.getElementById("inputItem").value;
  const list = document.getElementById("list");
  const li = document.getElementById("li");
  li.appendChild(document.createTextNode("- " + item));
  list.appendChild(li);
  document.getElementById("input").value = "";
  li.onclick = removeItem;
}
document.body.onkeyup = function(e) {
  if (e.keyCode == 13) {
    newItem();
  }
}

function removeItem(e) {
  e.target.parentElement.removeChild(e.target);
}
