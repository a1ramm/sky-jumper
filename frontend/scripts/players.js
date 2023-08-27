const table_listing = document.querySelector("#table-listing");

function get_all_players() {
    fetch("http://127.0.0.1:5000/players", {
        method: "GET"
    })
    .then(response => response.json())
    .then(json => list_in_table(json))
    .catch(error => console.log(error.message));
}

function list_in_table(json) {
    json.data.forEach(player => {
        let table_row = document.createElement("tr");
        let id = document.createElement("td");
        let username = document.createElement("td");
        let email = document.createElement("td");
        let coins = document.createElement("td");

        id.innerText = player.id;
        username.innerText = player.username;
        email.innerText = player.email;
        coins.innerText = player.coins;

        table_row.appendChild(id);
        table_row.appendChild(username);
        table_row.appendChild(email);
        table_row.appendChild(coins);

        table_listing.appendChild(table_row);
    });
}

get_all_players()