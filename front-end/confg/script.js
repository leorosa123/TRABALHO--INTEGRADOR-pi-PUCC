user = NaN
// Objeto para o menu
const Layout = {
    addHeader: function () {
        const headerElement = document.querySelector("header");
        if (headerElement) {
            headerElement.innerHTML = `
                <header style="background-color: #fff;">
                    <a href="${urls.index}" class="logo">
                        <img src="../confg/S.A.D.png" alt="S.A.D Logo" width="120">
                    </a>
                    <ul class="navbar">
                        <li><a href="${urls.index}" class="active">Home</a></li>
                        <li><a href="${urls.sobre}">Sobre Nós</a></li>
                        <li><a href="${urls.servicos}">Serviços</a></li>
                        <li><a href="${urls.contato}">Contato</a></li>
                        <li><a href="${urls.agendamento}"><button>Agendamentos</button></a></li>
                    </ul>
                    <div class="main-acessos" id="access">
                        <a href="${urls.loginPage}" class="login"><i class="ri-user-fill"></i>Login</a>
                        <a href="${urls.cadastro}" class="Cadastro">/ Cadastro</a>
                    </div>
                </header>
            `;
        }
    },
    addFooter: function() {
        document.querySelector("footer").innerHTML = `
            <!-- Footer -->
            <footer class="text-center text-lg-start bg-body-tertiary text-muted" id="Contato">
            <!-- Section: Social media -->
            <section class="d-flex justify-content-center justify-content-lg-between p-4 border-bottom">
                <!-- Left -->
                <div class="me-5 d-none d-lg-block fw-bold">
                <span>Meios de Contato e conexão</span>
                </div>
                <!-- Left -->
            </section>
            <!-- Section: Social media -->

            <!-- Section: Links  -->
            <section>
                <div class="container text-center text-md-start mt-5">
                <!-- Grid row -->
                <div class="row mt-3">
                    <!-- Grid column -->
                    <div class="col-md-3 col-lg-4 col-xl-3 mx-auto mb-4">
                    <!-- Content -->
                    <h6 class="text-uppercase fw-bold mb-4">
                        <i class="fas fa-gem me-3"></i>Agency S.A.D
                    </h6>
                    <p>
                        Buscamos soluções inteligêntes e humanizadas para melhorar a saúde mental e bem estar de pessoas com ploblemas cotidianos reais.
                    </p>
                    </div>
                    <!-- Grid column -->

                    <!-- Grid column -->
                    <div class="col-md-2 col-lg-2 col-xl-2 mx-auto mb-4 menu-footer">
                    <!-- Links -->
                    <h6 class="text-uppercase fw-bold mb-4">
                        Menu
                    </h6>
                    <p>
                        <a href="${urls.index}" class="text-reset">Home</a>
                    </p>
                    <p>
                        <a href="${urls.sobre}" class="text-reset">Quem Somos</a>
                    </p>
                    <p>
                        <a href="${urls.servicos}" class="text-reset">Serviços</a>
                    </p>
                    <p>
                        <a href="${urls.contato}" class="text-reset">Contato</a>
                    </p>
                    </div>
                    <!-- Grid column -->

                    <!-- Grid column -->
                    <div class="col-md-3 col-lg-2 col-xl-2 mx-auto mb-4 servicos-footer">
                    <!-- Links -->
                    <h6 class="text-uppercase fw-bold mb-4">
                        Soluções
                    </h6>
                    <p>
                        <a href="#!" class="text-reset">Reuniões</a>
                    </p>
                    <p>
                        <a href="#!" class="text-reset">Ligações</a>
                    </p>
                    <p>
                        <a href="#!" class="text-reset">Relatórios</a>
                    </p>
                    <p>
                        <a href="#!" class="text-reset">Jogos</a>
                    </p>
                    </div>
                    <!-- Grid column -->

                    <!-- Grid column -->
                    <div class="col-md-4 col-lg-3 col-xl-3 mx-auto mb-md-0 mb-4">
                    <!-- Links -->
                    <h6 class="text-uppercase fw-bold mb-4">Contato</h6>
                    <p><i class="fas fa-home me-3"></i> São Paulo, Nova paulista 10012, BR</p>
                    <p>
                        <i class="fas fa-envelope me-3"></i>
                        atendimentohope@gmail.com
                    </p>
                    <p><i class="fas fa-phone me-3"></i> + 55 19 9234 3333</p>
                    <p><i class="fas fa-print me-3"></i> + 55 19 2198 4422</p>
                    </div>
                    <!-- Grid column -->
                </div>
                <!-- Grid row -->
                </div>
            </section>
            <!-- Section: Links  -->

            <!-- Copyright -->
            <div class="text-center p-4" style="background-color: rgba(87, 87, 87, 0.05);">
            <b>  © 2024 Copyright alunos da Pontifícia Universidade Católica de Campinas </b>
            </div>
            <!-- Copyright -->
            </footer>
            <!-- Footer -->
        `;
    }
};

// Objeto para autenticação
const Auth = {
    login: function (userData) {
        localStorage.setItem("user", JSON.stringify(userData));
        Layout.addHeader();
        window.location.href = urls.index; 
    },
    logout: function () {
        localStorage.removeItem("user");
        Layout.addHeader();
        window.location.href = urls.loginPage; 
    },
};

// Objeto para gerenciar usuários
const Usuario = {
    saveFormDataAsJSON: function(form) {
        const formData = new FormData(form);
        const jsonData = {};
        formData.forEach((value, key) => jsonData[key] = value);
        return jsonData;
    },
    sendToFlask: async function(url, data) {
        const response = await fetch(url, {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify(data)
        });
        return response.json();
    }
};

// Exibindo os psicologos
const psicologos = {
    showUpPsicologies: async function() {
        try {
            const response = await fetch(urls.psicologos);
            const profissionais = await response.json();

            const container = document.getElementById("psicologos");
            if (profissionais.length === 0) {
                container.innerHTML = "<h1>Não há psicólogos disponíveis.</h1>";
            } else {
                profissionais.forEach((psicologo) => {
                    const card = `
                        <div class="psicologo-card">
                            <h3>${psicologo.nome}</h3>
                            <p>${psicologo.especialidade}</p>
                            
                        </div>`;
                    container.innerHTML += card;
                });
            }
        } catch (error) {
            console.error("Erro ao carregar psicólogos:", error);
        }
    }
};

// Inicializar Layout
document.addEventListener("DOMContentLoaded", () => {
    Layout.addHeader();
    Layout.addFooter();
})

// Enviando as informacoes dentro do forms de cadastro
// Função para validar os campos do formulário
function validateForm(formData) {
    const { nome, cpf, email, dataNascimento, senha, confirmarSenha } = formData;

    // Validação do nome
    if (!nome || nome.trim().length < 3) {
        return "O nome deve ter pelo menos 3 caracteres.";
    }

    // Validação do CPF (formato básico, sem verificação de dígitos verificadores)
    const cpfRegex = /^\d{11}$/;
    if (!cpfRegex.test(cpf)) {
        return "CPF inválido. Deve conter 11 números.";
    }

    // Validação do email
    const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
    if (!emailRegex.test(email)) {
        return "E-mail inválido.";
    }

    // Validação da data de nascimento
    const hoje = new Date();
    const dataNasc = new Date(dataNascimento);
    if (!dataNascimento || dataNasc >= hoje) {
        return "Data de nascimento inválida.";
    }

    // Validação da senha
    if (senha.length < 6) {
        return "A senha deve ter pelo menos 6 caracteres.";
    }

    // Verificar se as senhas coincidem
    if (senha !== confirmarSenha) {
        return "As senhas não coincidem.";
    }

    // Retorna null se tudo estiver válido
    return null;
}

// Função para enviar os dados para a API Flask
async function submitForm() {
    // Captura os dados do formulário
    const formData = {
        name: document.getElementById("nome").value,
        cpf: document.getElementById("cpf").value,
        email: document.getElementById("email").value,
        datanasc: document.getElementById("dataNascimento").value,
        pass: document.getElementById("senha").value,
    };

    // Valida os dados (a função validateForm deve ser usada antes)
    const validationError = validateForm(formData);
    if (validationError) {
        alert(validationError);
        return;
    }

    // Envia os dados para a API Flask
    try {
        const response = await fetch("http://localhost:5000/receberDados", {
            method: "POST",
            headers: {
                "Content-Type": "application/json",
            },
            body: JSON.stringify(formData),
        });

        if (response.ok) {
            const responseData = await response.json();
            alert(responseData.mensagem);
            console.log(responseData);
        } else if (response.status === 409) {
            alert("E-mail ou CPF já cadastrado.");
        } else {
            alert("Erro ao enviar o formulário. Tente novamente.");
        }
    } catch (error) {
        console.error("Erro na requisição:", error);
        alert("Erro ao conectar-se à API.");
    }
}

// validatecoesDeLogin
// Verifica se a variável `user` está vazia
function checkUserOnPageLoad() {
    const user = localStorage.getItem("user"); // Verifica o localStorage para o usuário
    return user ? 1 : 0;
}

// Função para autenticar usuário com servidor Flask
async function handleLogin(event) {
    // Captura os valores do formulário
    const email = document.getElementById("nameLogin").value;
    const senha = document.getElementById("passLogin").value;
    // Chama a função loginUser com os valores capturados
    await loginUser(email, senha);
}

async function loginUser(email, senha) {
    try {
        const url = urls.login;

        // Envia as credenciais para o servidor Flask
        const response = await fetch(url, {
            method: "POST",
            headers: {
                "Content-Type": "application/json",
            },
            body: JSON.stringify({ email, senha }),
        });

        // Trata a resposta
        if (response.ok) {
            const userData = response.json();
            console.log("Usuário autenticado:");

            // Salva o usuário no localStorage
            localStorage.setItem("user", JSON.stringify(userData));

            // Atualiza a interface ou redireciona
            document.getElementById('access').innerHTML = 
            `
            <a href="${urls.userInfo}"> Minha conta</a>
            `;
            window.location.href = urls.index;
        } else {
            const errorData = response.json();
            alert(errorData.error || "Erro ao autenticar.");
            window.location.href = urls.loginPage
        }
    } catch (error) {
        console.error("Erro na autenticação:", error);
        alert("Erro ao conectar ao servidor. Tente novamente.");
        window.location.href = urls.loginPage;
    }
}
// Exemplo de uso: Chamando a função de login
document.querySelector("#loginForm").addEventListener("submit", async (event) => {
    event.preventDefault(); // Previne o envio padrão do formulário

    const email = document.querySelector("#email").value;
    const senha = document.querySelector("#senha").value;

    await loginUser(email, senha);
});
