from model import *

class DaoCategoria:
    @classmethod
    def salvar(cls, categoria):
        with open ('categoria.txt', 'a') as arq:
            arq.writelines(categoria)
            arq.writelines('\n')

# @classmethod indica que o método pertence a classe e não a instancia e por isso...
# eu preciso receber a classe em si que é o parametro 'cls'
# o self aponta para a instancia e o cls aponta para a classe
# estrutura with facilita a abertura e fechamento de arquivos
# o "as" está dizendo que o arquivo "categoria.txt" deve ser referenciado como "arq"
# a função writelines() grava o conteúdo de uma lista em um arquivo

    @classmethod
    def ler(cls):
        with open('categoria.txt', 'r') as arq:
            cls.categoria = arq.readlines()

        cls.categoria = list(map(lambda x: x.replace('\n', ''), cls.categoria))

        cat = []
        for i in cls.categoria:
            cat.append(Categoria(i))

        return cat

# quando a função readlines le o arquivo, ela não retira o \n do final, para retirar esse \n do final usamos o map
# o map vai fazer uma alteração, contudo precisamos utilizar o list para converter para uma lista
# se não ele vai devolver um objeto do tipo map
# abrimos o arquivo texto, pegamos tudo que tem dentro desse arquivo texto e jogamos para dentro de categoria
# tiramos o \n, retornando apenas a string, contudo não queremos retornar a string em si e sim uma instancia do nosso model
# o model Categoria recebe um parametro que é categoria
# dentro da lista cat estou adicionando uma nova categoria que é uma instancia de Categoria
# e passamos como parametro o que está dentro do arquivo categoria

class DaoVenda:
    @classmethod
    def salvar(cls, venda: Venda):
        with open('venda.txt', 'a') as arq:
            arq.writelines(venda.itensVendido.nome + "|" + venda.itensVendido.preco + "|" +
                           venda.itensVendido.categoria + "|" + venda.vendedor + "|" +
                           venda.comprador + "|" + str(venda.quantidadeVendida) + "|" + venda.data)
            arq.writelines('\n')

# venda tem o parametro itensVendido, itensVendido é um Produto (class), e Produto tem preco, nome e categoria

    @classmethod
    def ler(cls):
        with open('venda.txt', 'r') as arq:
            cls.venda = arq.readlines()

        cls.venda = list(map(lambda x: x.replace('\n', ''), cls.venda))
        cls.venda = list(map(lambda x: x.split('|'), cls.venda))
        vend = []
        for i in cls.venda:
            vend.append(Venda(Produtos(i[0], i[1], i[2]), i[3], i[4], i[5], i[6]))
        return vend

# o split separa strings em substrings e retorna listas

class DaoEstoque:
    @classmethod
    def salvar(cls, produto: Produtos, quantidade):
        with open('estoque.txt', 'a') as arq:
            arq.writelines(produto.nome + "|" + produto.preco + "|" + produto.categoria + "|" + str(quantidade))
            arq.writelines('\n')

#recebe uma variável produto que é do tipo Produtos(da model) e recebe também a quantidade
# ela abre um arquivo "estoque.txt" e salva os dados dentro desse arquivo.

    @ classmethod
    def ler(cls):
        with open('estoque.txt', 'r') as arq:
            cls.estoque = arq.readlines()

        cls.estoque = list(map(lambda x: x.replace('\n', ''), cls.estoque))
        cls.estoque = list(map(lambda x: x.split('|'), cls.estoque))
        est = []
        if len(cls.estoque) > 0:
            for i in cls.estoque:
                est.append(Estoque(Produtos(i[0], i[1], i[2]), int(i[3])))

        return est

# método ler vai abri o arquivo "estoque", vai jogar tudo pra dentro de estoque


class DaoFornecedor:
    @classmethod
    def salvar(cls, fornecedor: Fornecedor):
        with open('fornecedores.txt', 'a') as arq:
            arq.writelines(fornecedor.nome + "|" + fornecedor.cnpj + "|" + fornecedor.telefone
                           + "|" + fornecedor.categoria)
            arq.writelines('\n')

    @classmethod
    def ler(cls):
        with open('fornecedores.txt', 'r') as arq:
            cls.fornecedores = arq.readlines()

        cls.fornecedores = list(map(lambda x: x.replace('\n', ''), cls.fornecedores))
        cls.fornecedores = list(map(lambda x: x.split('|'), cls.fornecedores))
        forn = []
        if len(cls.fornecedores) > 0:
            for i in cls.fornecedores:
                forn.append(Fornecedor(i[0], i[1], i[2], i[3]))

        return forn


class DaoPessoa:
    @classmethod
    def salvar(cls, pessoas: Pessoa):
        with open('clientes.txt', 'a') as arq:
            arq.writelines(pessoas.nome + "|" + pessoas.telefone + "|" + pessoas.cpf
                           + "|" + pessoas.email + "|" + pessoas.endereco)
            arq.writelines('\n')

    @classmethod
    def ler(cls):
        with open('clientes.txt', 'r') as arq:
            cls.clientes = arq.readlines()

        cls.clientes = list(map(lambda x: x.replace('\n', ''), cls.clientes))
        cls.clientes = list(map(lambda x: x.split('|'), cls.clientes))

        cli = []
        if len(cls.clientes) > 0:
            for i in cls.clientes:
                cli.append(Pessoa(i[0], i[1], i[2], i[3], i[4]))

        return cli


class DaoFuncionario:
    @classmethod
    def salvar(cls, funcionario: Funcionario):
        with open('funcionarios.txt', 'a') as arq:
            arq.writelines(funcionario.clt + "|" + funcionario.nome + "|" + funcionario.telefone
                           + "|" + funcionario.cpf + "|" + funcionario.email + "|" + funcionario.endereco)
            arq.writelines('\n')

    @classmethod
    def ler(cls):
        with open('funcionarios.txt', 'r') as arq:
            cls.funcionarios = arq.readlines()

        cls.funcionarios = list(map(lambda x: x.replace('\n', ''), cls.funcionarios))
        cls.funcionarios = list(map(lambda x: x.split('|'), cls.funcionarios))

        funcionario = []
        for i in cls.funcionarios:
            funcionario.append(Funcionario(i[0], i[1], i[2], i[3], i[4], i[5]))

        return funcionario

