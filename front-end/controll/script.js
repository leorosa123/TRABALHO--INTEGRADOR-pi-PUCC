section = new Map()

// Recebendo post do python -> Validacao dos dados e admissao do client
function searchData(){
    fetch("/api/data")
    .then(response => response.json)
    .then(dados => {
        const client = new Map();
        dados.array.forEach(dado => {
            client.set(dado.key, dado.value);
        });
    })
    .catch(error => console.error('Erro:',error));
}

// Restricoes de login
function setUpPriviledges(){



}
// Reabilitacao das restricoes
// Mudanca de pagina com o login
// Post para o python -> inserir dados
// Post para o python -> transformar dados