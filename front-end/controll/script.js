// Arquivo: main.js

// Objeto para Menu e Footer
const Layout = {
    addHeader: function() {
        document.querySelector("header").innerHTML = `
            <nav>
                <a href="index.html">Home</a>
                <a href="psicologos.html">Psicólogos</a>
                <a href="agendamento.html">Agendamento</a>
                <a href="login.html" id="userLink">Login</a>
            </nav>
        `;
    },
    addFooter: function() {
        document.querySelector("footer").innerHTML = `
            <p>&copy; 2024 Hope. Todos os direitos reservados.</p>
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
        document.getElementById("userLink").innerText = `Olá, ${userData.nomePaciente}`;
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

// Inicializar Layout
document.addEventListener("DOMContentLoaded", function() {
    Layout.addHeader();
    Layout.addFooter();
    const user = JSON.parse(localStorage.getItem("user"));
    if (user) {
        document.getElementById("userLink").innerText = `Olá, ${user.nomePaciente}`;
    }
});

