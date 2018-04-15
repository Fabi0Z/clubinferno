function showPassword() {
    document.getElementById("showPassword").addEventListener("click", function (e) {
        var pwd = document.getElementById("passwordLogin");
        var eye = document.getElementById("showPassword")
        if (pwd.getAttribute("type") == "password") {
            pwd.setAttribute("type", "text");
            eye.className = "fa fa-eye-slash"
        } else {
            pwd.setAttribute("type", "password");
            eye.className = "fa fa-eye"
        }
    });
    document.getElementById("showPassword2").addEventListener("click", function (e) {
        var pwd = document.getElementById("passwordRegister");
        var eye = document.getElementById("showPassword2")
        if (pwd.getAttribute("type") == "password") {
            pwd.setAttribute("type", "text");
            eye.className = "fa fa-eye-slash"
        } else {
            pwd.setAttribute("type", "password");
            eye.className = "fa fa-eye"
        }
    });
}