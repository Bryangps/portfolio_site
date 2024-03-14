function validatePassword(){
    var password = document.getElementById("password").value;
    var confirmPassword = document.getElementById("confirm-password").value;

        if (password != confirmPassword) {
            alert("As senhas não correspondem!");
            return false;

        }
        else {
            return true;
        }
}


