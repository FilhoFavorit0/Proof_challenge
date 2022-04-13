document.getElementById('botao1').addEventListener('click', loadText);

function loadText() {
    fetch("https://www.dan.me.uk/torlist/?exit")
    .then (function(response){
        return response.text();
    })
    .then (function(data){
        console.log(data);
        document.getElementById('lista').innerHTML = data;
    })
}