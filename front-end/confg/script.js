// Interation with page --> acording to data and structure reuse
// Objeto para Menu e Footer

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
    checkLogin: function() {
        const user = JSON.parse(localStorage.getItem("user"));
        if (!user) {
            window.location.href = "login.html";
        }
    },
    login: function(userData) {
        localStorage.setItem("user", JSON.stringify(userData));
        document.getElementById("access").innerText = `Olá, ${userData.nomePaciente}`;
        document.getElementById("change").innerHTML =`<a href="../view/userInformation.html">Minha conta</a>`;
    },
    logout: function() {
        localStorage.removeItem("user");
        window.location.href = "login.html";
    }
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
    showUpPsicologies: async function(){
        const profissionaisPsicologos = JSON.parse(localStorage.getItem("psicologos"));
        if (!profissionaisPsicologos){
            document.getElementById("psicologos").innerHTML = 
            `
            <h1 class="titlePsicologos">Nao há nenhum psicologo disponivel dentro da nova base de dados</h1>
            `
        }
        for (i = 0; i < length(profissionaisPsicologos); i++){
            // Colocar a estrutura da amostragem dos psicologos
            const psicologo = document.createElement("div");
            psicologo.innerHTML = 
            `
            `
            document.getElementById("psicologos").appendChild(psicologo)
        }
    }
}

// Inicializar Layout
document.addEventListener("DOMContentLoaded", () => {
    Layout.addHeader();
    Layout.addFooter();
})



// Interation with Data --> send data to the API Flask...
// Send data to put it on Data Base
document.querySelector('.form').addEventListener('submit', async (event) => {
    event.preventDefault();
    const email = document.querySelector('input[name="name"]').value;
    const password = document.querySelector('input[name="pass"]').value;

    const response = await fetch('/login', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ email, senha: password })
    });

    if (response.ok) {
        const user = await response.json();
        localStorage.setItem('user', JSON.stringify(user));
        window.location.href = '/';
    } else {
        alert('Login inválido');
    }
});

document.querySelector('#cadastroForms').addEventListener('submit', async (event) => {
    event.preventDefault();
    const formData = new FormData(event.target);
    const data = Object.fromEntries(formData.entries());

    const response = await fetch('/receberDados', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(data)
    });

    if (response.ok) {
        alert('Cadastro realizado com sucesso!');
        window.location.href = '/login-page';
    } else {
        alert('Erro ao realizar o cadastro.');
    }
});

async function loadPsychologists() {
    const response = await fetch('/psicologos');
    const psychologists = await response.json();
    const container = document.getElementById('psicologos');

    if (psychologists.length > 0) {
        psychologists.forEach(psychologist => {
            const card = document.createElement('div');
            card.innerHTML = `
                <div class="card">
                    <h3>${psychologist.nome}</h3>
                    <p>${psychologist.especialidade}</p>
                </div>
            `;
            container.appendChild(card);
        });
    } else {
        container.innerHTML = '<h1>Nenhum psicólogo disponível no momento.</h1>';
    }
}
document.addEventListener("DOMContentLoaded", loadPsychologists)