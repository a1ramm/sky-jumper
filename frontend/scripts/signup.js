export function signup(form) {
        //var form_data = new FormData(signup_form);
    
        var form_data = {
            "username": document.querySelector("#username").value,
            "email": document.querySelector("#email").value,
            "password": document.querySelector("#password").value
        }
    
        //form_data = JSON.stringify(form_data)

        console.log(form_data)

        fetch("http://127.0.0.1:5000/player/register", {
            method: "POST",
            dataType: "json",
            contentType: "application/json",
            body: form_data
        });
}
