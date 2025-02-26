// Get all elements with the specified class and convert the collection to an array
var redirectButtons = Array.from(document.getElementsByClassName("nav-button"));

// Add a click event listener to each button in the array
redirectButtons.forEach(function(button) {
    button.addEventListener("click", function () {
        // Specify the URL you want to redirect to for each button
        var targetUrl = button.getAttribute("data-href");
        console.log('targetUrl')

        // Perform the redirection
        window.location.href = targetUrl;
    });
});

var redirectButtons = Array.from(document.getElementsByClassName("log-button"));
redirectButtons.forEach(function(button) {
    button.addEventListener("click", function () {
        // Specify the URL you want to redirect to for each button
        var targetUrl = button.getAttribute("data-href");
        console.log('targetUrl')

        // Perform the redirection
        window.location.href = targetUrl;
    });
});

