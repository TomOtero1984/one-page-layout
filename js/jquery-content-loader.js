// About
$(document).ready(function () {
    $("#about").load("content/about.html");
});

// Projects
$(document).ready(function () {
    $("#projects").load("content/projects.html");
});

// Contact
// $(document).ready(function () {
//     $("#contact").load("content/contact.html");
// });

// Check for element
// $(document).ready(function () {
//     $("#contact").on(" load", function () {
//         if ($("#email").length) {
//             console.log("Email Found")
//         }
//         else {
//             console.log("Email Missing")
//             console.log(`${$("#email").length}`)
//         }
//     });
// });

// GetJSON
$.getJSON("../data/engineering_quotes.json", function (json) {
    console.log(json);
})