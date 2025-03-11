var players = JSON.parse(document.getElementById('players').textContent);

countrySelected = document.getElementById("country-select");

countrySelected.addEventListener("change",()=>{
    tableBody = document.getElementById("body-table");
    tableBody.innerHTML="";
    for (let i=0; i<players.length ; i++){
        console.log(players[i]);
        if (players[i].country===countrySelected.value){
            tableBody.innerHTML+=`
            <tr>
            <td> ${players[i].rank} </td>
            <td><img src=${players[i].country_image} width='25'>  ${players[i].country} </td>
            <td> ${players[i].first_name} </td>
            <td> ${players[i].last_name} </td>
            <td> ${players[i].points} </td>
            <td> ${players[i].nb_tournaments} </td>
            </tr>
            `
        }
    }
})