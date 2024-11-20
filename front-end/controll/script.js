// Modify this to search for any type of data
// Função para buscar os dados da API
async function carregarClientes() {
    try {
        const response = await fetch('/api/clientes');
        const clientes = await response.json();

        // Atualizar o DOM com as informações do cliente
        const listaClientes = document.getElementById('lista-clientes');
        listaClientes.innerHTML = '';

        clientes.forEach(cliente => {
            const item = document.createElement('div');
            item.className = 'cliente';
            item.innerHTML = `
                <h3>${cliente.nome}</h3>
                <p>CPF: ${cliente.cpf}</p>
                <p>Data de Nascimento: ${cliente.dataNascimento}</p>
                <p>Email: ${cliente.email}</p>
                <img src="${cliente.foto}" alt="Foto do Cliente">
            `;
            listaClientes.appendChild(item);
        });
    } catch (error) {
        console.error('Erro ao carregar os clientes:', error);
    }
}

// Chamar a função ao carregar a página
//document.addEventListener('DOMContentLoaded', carregarClientes);

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

async function showUpPsicologies(){

}
// Reabilitacao das restricoes
// Mudanca de pagina com o login
// Post para o python -> inserir dados
// Post para o python -> transformar dados