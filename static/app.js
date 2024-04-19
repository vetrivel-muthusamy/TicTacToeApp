// app.js

$(document).ready(function() {
    // Add click event handler for cells
    $(".cell").click(function() {
        var row = $(this).parent().index(); // Get the row index of the clicked cell
        var col = $(this).index(); // Get the column index of the clicked cell
        alert("Clicked cell at row " + row + ", column " + col);
    });
});
