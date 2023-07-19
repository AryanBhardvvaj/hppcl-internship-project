// Get references to the predict buttons
const predictButtons = document.querySelectorAll('.predict_btn');

// Add click event listener to each predict button
predictButtons.forEach((button) => {
  button.addEventListener('click', () => {
    const cardId = button.parentNode.parentNode.id; // Get the ID of the parent card

    // Perform different actions based on the card ID
    if (cardId === 'card1') {
      // Code for card 1
      // Set the new URL for card 1
      // Make an AJAX request to fetch the kashang.html template
      function loadKashangHTML() {
        var xhr = new XMLHttpRequest();
        xhr.onreadystatechange = function () {
          if (xhr.readyState === 4 && xhr.status === 200) {
            var responseHTML = xhr.responseText;
            // Use the responseHTML as needed
            // For example, you can insert it into a specific element on your page
            document.getElementById('kashang').innerHTML = responseHTML;
          }
        };
        xhr.open('GET', '/kashang', true);
        xhr.send();
      }
      // Call the function to load the kashang.html template
      loadKashangHTML();
    }
    if (cardId === 'card2') {
      // Code for card 2
      // Set the new URL for card 2
      // Make an AJAX request to fetch the sainj.html template
      function loadSainjHTML() {
        var xhr = new XMLHttpRequest();
        xhr.onreadystatechange = function () {
          if (xhr.readyState === 4 && xhr.status === 200) {
            var responseHTML = xhr.responseText;
            // Use the responseHTML as needed
            // For example, you can insert it into a specific element on your page
            document.getElementById('sainj').innerHTML = responseHTML;
          }
        };
        xhr.open('GET', '/sainj', true);
        xhr.send();
      }
      // Call the function to load the sainj.html template
      loadSainjHTML();
    }
    if (cardId === 'card3') {
      // Code for card 3
      // Set the new URL for card 3
      // Make an AJAX request to fetch the sk.html template
      function loadSkHTML() {
        var xhr = new XMLHttpRequest();
        xhr.onreadystatechange = function () {
          if (xhr.readyState === 4 && xhr.status === 200) {
            var responseHTML = xhr.responseText;
            // Use the responseHTML as needed
            // For example, you can insert it into a specific element on your page
            document.getElementById('sk').innerHTML = responseHTML;
          }
        };
        xhr.open('GET', '/sk', true);
        xhr.send();
      }
      // Call the function to load the sk.html template
      loadSkHTML();
    }
  });
});

// Add click event listener to the redirect button
const redirectButton = document.getElementById('redirectButton');
redirectButton.addEventListener('click', () => {
  // Set the new URLs
  window.location.href = '/kashang';
  // Add additional URLs if needed
  window.location.href = '/sainj';
  window.location.href = '/sk';
});

window.addEventListener('scroll', function() {
  var navbar = document.querySelector('.navbar');
  navbar.classList.toggle('sticky', window.scrollY > 0);
});