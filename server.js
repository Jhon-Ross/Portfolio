const express = require("express");
const path = require("path");

const app = express();
const PORT = process.env.PORT || 3000;

// Servir arquivos estáticos da raiz e da pasta "src"
app.use(express.static(__dirname));
app.use(express.static(path.join(__dirname, "src")));

// Rota para servir o index.html corretamente
app.get("/", (req, res) => {
    res.sendFile(path.join(__dirname, "index.html"));
});

// Inicia o servidor
app.listen(PORT, () => {
    console.log(`Servidor rodando na porta ${PORT}`);
});
