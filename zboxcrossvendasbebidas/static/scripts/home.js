//Formataçao dinheiro
function formatarDinheiro(input) {
   
    let valor = input.value.replace(/\D/g, '');
    valor = (Number(valor) / 100).toLocaleString('pt-BR', { style: 'currency', currency: 'BRL' });
    input.value = valor;
}

//navegação
var containerPrincipal = document.getElementById('container-principal');
var containerCadastro = document.getElementById('container-cadastro');
var containerVendas = document.getElementById('container-vendas');
var containerEstoque = document.getElementById('container-estoque');
var containerVCliente = document.getElementById('container-vcliente');

function cadastroBebidas(){
    containerPrincipal.style.display = 'none';
    containerVendas.style.display = 'none';
    containerEstoque.style.display = 'none';
    containerVCliente.style.display = 'none';
    containerCadastro.style.display = 'block';
}

function vendasBebidas(){
    containerPrincipal.style.display = 'none';
    containerVendas.style.display = 'block';
    containerEstoque.style.display = 'none';
    containerVCliente.style.display = 'none';
    containerCadastro.style.display = 'none';
}

function Estoque(){
    containerPrincipal.style.display = 'none';
    containerVendas.style.display = 'none';
    containerEstoque.style.display = 'block';
    containerVCliente.style.display = 'none';
    containerCadastro.style.display = 'none';
}

function vendasCliente(){
    containerPrincipal.style.display = 'none';
    containerVendas.style.display = 'none';
    containerEstoque.style.display = 'none';
    containerVCliente.style.display = 'block';
    containerCadastro.style.display = 'none';
}