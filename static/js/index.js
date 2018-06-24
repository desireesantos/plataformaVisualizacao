
function toggle() {
   alert("Hello World");
}


var table = document.getElementById("mstrTable");
var thead = table.getElementsByTagName("thead")[0];
var tbody = table.getElementsByTagName("tbody")[0];

tbody.onclick = function (e) {
   e = e || window.event;
   var td = e.target || e.srcElement;
   var row = td.parentNode;
   row.className = row.className==="highlighted" ? "" : "highlighted";
}

thead.onclick = function (e) {
   e = e || window.event;
   var th = e.target || e.srcElement;
   alert(th.innerHTML);
}
