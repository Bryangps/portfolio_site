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
var containerPagamento = document.getElementById('container-pagamento');
var containerPendente = document.getElementById('container-pendente');
var containerEfetuado = document.getElementById('container-efetuado');
var containerBusca = document.getElementById('container-busca');
var containerTVendas = document.getElementById('container-tvendas');

function cadastroBebidas(){
    containerPrincipal.style.display = 'none';
    containerVendas.style.display = 'none';
    containerEstoque.style.display = 'none';
    containerPagamento.style.display = 'none';
    containerCadastro.style.display = 'block';
    containerPendente.style.display = 'none';
    containerEfetuado.style.display = 'none';
    containerBusca.style.display = 'none';
    containerTVendas.style.display = 'none';
}

function vendasBebidas(){
    containerPrincipal.style.display = 'none';
    containerVendas.style.display = 'block';
    containerEstoque.style.display = 'none';
    containerPagamento.style.display = 'none';
    containerCadastro.style.display = 'none';
    containerPendente.style.display = 'none';
    containerEfetuado.style.display = 'none';
    containerBusca.style.display = 'none';
    containerTVendas.style.display = 'none';
}

function Estoque(){
    containerPrincipal.style.display = 'none';
    containerVendas.style.display = 'none';
    containerEstoque.style.display = 'block';
    containerPagamento.style.display = 'none';
    containerCadastro.style.display = 'none';
    containerPendente.style.display = 'none';
    containerEfetuado.style.display = 'none';
    containerBusca.style.display = 'none';
    containerTVendas.style.display = 'none';
}

function Pagamento(){
    containerPrincipal.style.display = 'none';
    containerVendas.style.display = 'none';
    containerEstoque.style.display = 'none';
    containerPagamento.style.display = 'block';
    containerCadastro.style.display = 'none';
    containerPendente.style.display = 'none';
    containerEfetuado.style.display = 'none';
    containerBusca.style.display = 'none';
    containerTVendas.style.display = 'none';
}

function Pendente(){
    containerPrincipal.style.display = 'none';
    containerVendas.style.display = 'none';
    containerEstoque.style.display = 'none';
    containerPagamento.style.display = 'none';
    containerCadastro.style.display = 'none';
    containerPendente.style.display = 'block';
    containerEfetuado.style.display = 'none';
    containerBusca.style.display = 'none';
    containerTVendas.style.display = 'none';
}

function Efetuado(){
    containerPrincipal.style.display = 'none';
    containerVendas.style.display = 'none';
    containerEstoque.style.display = 'none';
    containerPagamento.style.display = 'none';
    containerCadastro.style.display = 'none';
    containerPendente.style.display = 'none';
    containerEfetuado.style.display = 'block';
    containerBusca.style.display = 'none';
    containerTVendas.style.display = 'none';
}

function Busca(){
    containerPrincipal.style.display = 'none';
    containerVendas.style.display = 'none';
    containerEstoque.style.display = 'none';
    containerPagamento.style.display = 'none';
    containerCadastro.style.display = 'none';
    containerPendente.style.display = 'none';
    containerEfetuado.style.display = 'none';
    containerBusca.style.display = 'block';
    containerTVendas.style.display = 'none';
}

function TVendas(){
    containerPrincipal.style.display = 'none';
    containerVendas.style.display = 'none';
    containerEstoque.style.display = 'none';
    containerPagamento.style.display = 'none';
    containerCadastro.style.display = 'none';
    containerPendente.style.display = 'none';
    containerEfetuado.style.display = 'none';
    containerBusca.style.display = 'none';
    containerTVendas.style.display = 'block';
}
//Alerta sair da conta
function alertLogout(){
    if (!confirm('Tem certeza que deseja sair da sua conta?')) {
        event.preventDefault();
    }
}

//funçao submete o formulário e limpa o formulário sem recarregar a página. Permitindo que o usuario continue cadastrando. Emite alerta de cadastro efetuado no cadastro de produtos e venda confirmada no formulario de vendas.
function submitForm(event) {
    event.preventDefault(); 
    document.getElementById("form-cadastrob").reset();
    alert('Cadastro efetuado com sucesso!')
}

function submitVenda(){
    event.preventDefault(); 
    document.getElementById("form-venda").reset();
    alert('Venda confirmada!');
}

