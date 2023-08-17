import { signup } from "./signup.js";

const signup_form = document.querySelector("#signup-form");

signup_form.addEventListener("submit", async event => {
    event.preventDefault();
    signup(signup_form);
});