function noSpaces() {
    var username = document.querySelector('[name="username"]');
    var registerUsername = document.getElementById("registerUsername");
    var email = document.querySelector('[name="email"]');

    username.addEventListener('keypress', function (event) {
        var key = event.keyCode;
        if (key === 32) {
            event.preventDefault();
        }
    });
    
    email.addEventListener('keypress', function (event) {
        var key = event.keyCode;
        if (key === 32) {
            event.preventDefault();
        }
    });
    
    registerUsername.addEventListener('keypress', function (event) {
        var key = event.keyCode;
        if (key === 32) {
            event.preventDefault();
        }
    });
}
