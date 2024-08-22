// Get the modal
var modal = document.getElementById("shortenModal");

// Get the button that opens the modal
var btn = document.getElementById("btn");

// Get the <span> element that closes the modal
var span = document.getElementsByClassName("close")[0];

// Function to show the modal with the short link
function showModal(shortLink) {
    var shortenedLink = document.getElementById("shortenedLink");
    shortenedLink.href = shortLink;
    shortenedLink.innerHTML = shortLink;
    modal.style.display = "block";
}

// When the user clicks the shorten button, generate the short link and show it
btn.onclick = function() {
    var shortCode = "X1ShEF"; // Replace this with your logic to generate the short link
    var shortLink = "https://shortify-nine.vercel.app/" + shortCode;
    showModal(shortLink);
}

// When the user clicks on <span> (x), close the modal
span.onclick = function() {
    modal.style.display = "none";
}

// When the user clicks anywhere outside of the modal, close it
window.onclick = function(event) {
    if (event.target == modal) {
        modal.style.display = "none";
    }
}
