// app.js

$(document).ready(function() {
    // Generate game board dynamically
    var boardHtml = "";
    for (var i = 0; i < 3; i++) {
        for (var j = 0; j < 3; j++) {
            boardHtml += "<div class='cell' data-row='" + i + "' data-col='" + j + "'></div>";
        }
    }
    $("#board").append(boardHtml);

    // Add click event handler for cells
    $(".cell").click(function() {
        var row = $(this).data("row");
        var col = $(this).data("col");
        alert("Clicked cell at row " + row + ", column " + col);
    });
});
