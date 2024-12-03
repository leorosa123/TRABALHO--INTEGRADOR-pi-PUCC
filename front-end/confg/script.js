// Interation with page --> acording to data and structure reuse
// Objeto para Menu e Footer
const urls = {
    index: "{{url_for('index')}}",
    sobre: "{{url_for('index')}}#Sobre",
    servicos: "{{url_for('index')}}#Servicos",
    contato: "{{url_for('index')}}#Contato",
    loginPage: "{{url_for('login_page')}}",
    cadastro: "{{url_for('cadastro')}}",
    agendamento: "{{url_for('agendamento')}}",
    userInfo: "{{url_for('informacoes')}}"
};

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
    addFooter: function () {
        const footerElement = document.querySelector("footer");
        if (footerElement) {
            footerElement.innerHTML = `
                <footer class="text-center text-lg-start bg-body-tertiary text-muted" id="Contato">
                    <div class="container text-center mt-4">
                        <h6 class="text-uppercase fw-bold mb-4">Agency H.O.P.E</h6>
                        <p>
                            Fornecendo suporte psicológico com soluções inteligentes para uma vida mais equilibrada.
                        </p>
                        <ul>
                            <li><a href="${urls.index}">Home</a></li>
                            <li><a href="${urls.sobre}">Sobre Nós</a></li>
                            <li><a href="${urls.servicos}">Serviços</a></li>
                            <li><a href="${urls.contato}">Contato</a></li>
                        </ul>
                        <p>Contato: atendimentohope@gmail.com | +55 19 9234 3333</p>
                    </div>
                </footer>
            `;
        }
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
