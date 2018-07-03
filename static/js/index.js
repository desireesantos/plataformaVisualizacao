
function hideShowCols(tabId) {
   'use  strict';
    var tab, i, j, th, func = {}, cell ,first=true, startCol=0;

    th = (window.event.target) ? window.event.target : window.event.srcElement;
    if (th.tagName !== 'TH') {
        return;
    }
    tab = document.getElementById(tabId);
    function show(cell) {
        if (cell.hide) {
            cell.innerHTML = cell.innerHTML.slice(5, -3);
            cell.hide = !cell.hide;
        }
    }
    function hide(cell) {
        if (!cell.hide) {
            cell.innerHTML = '&#8203;<!--' + cell.innerHTML + '-->';
            cell.hide = !cell.hide;
            cell.style.backgroundColor = "lightgray";
        }
    }
    if (th.hide) {
        func = show;
    } else {
        func = hide;
    }
    for (i = 0; i < tab.rows.length; i++) {
        for (j = startCol; j < tab.rows[i].cells.length; j++) {
            cell = tab.rows[i].cells[j];
            if ((th.offsetLeft <= cell.offsetLeft && cell.offsetLeft <= th.offsetLeft + th.clientWidth)
                    && (th.colSpan >= cell.colSpan)) {
                func(cell);
                if(first){
                    first=false;
                    startCol=j;
                }
            } else if (cell.offsetLeft > th.offsetLeft + th.clientWidth) {
                break;
            }
        }
    }
}