
let table = document.getElementById("containerTable");
let thead = table.getElementsByTagName("thead")[0];

thead.onclick = function (e) {
   e = e || window.event;
   var th = e.target || e.srcElement;

   alert(th.innerHTML);
}
