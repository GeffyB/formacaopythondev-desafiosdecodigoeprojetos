# Criando um sitema Bancário com Python

#
## Desafio v1:

Fomos contratados por um grande banco para desenvolver o seu novo sistema. Esse banco deseja modernizar suas operações e para isso escolheu a linguagem Python. Para a primeira versão do sistema foi implementado apenas 3 operações: depósito, saque e extrato.  
   
Operação de depósito:  
    
Deve ser possível depositar valores positivos para a minha conta bancária. A v1 do projeto trabalha apenas com 1 usuário, dessa forma não foi necessário se preocupar em identificar qual é o número da agência e conta bancária. Todos os depósitos devem ser armazenados em uma variável e exibidos na operação de extrato.
    
Operação de Saque:
    
O sistema deve permitir realizar 3 saques diários com limite máximo de R$ 500,00 por saque. Caso o usuário não tenha saldo em conta, o sistema deve exibir uma mensagem informando que não será possível sacar o dinheiro por falta de saldo. Todos os saques devem ser armazenados em uma variável e exibidos na operação de extrato.

Operação de extrato:

Essa operação deve listar todos os depósitos e saques realizados na conta. No fim da listagem deve ser exibido o saldo atual da conta. Se o extrato estiver em branco, exibir a mensagem: Não foram realizadas movimentações.
Os valores devem ser exibidos utilizando o formato R$ xxx.xx, exemplo:
1500.45 = R$ 1500.45

#
## Desafio v2:

Separar as funções existentes de saque, depósito e extrato em funções e criar duas novas funções: cadastrar usuário (cliente) e cadastrar conta bancária.

Deixar o código mais modularizado com funções para os operações existentes.

#
## Desafio v3:

Reprodução das novas implementações no código propostas no desafio.  

Atualizar a implementação do sistema bancário, para armazenar os dados de clientes e contas bancárias em objetos ao invés de dicionários. O código deve seguir o modelo de classes UML anexado na imagem no repositório -> [Imagem](https://github.com/GeffyB/formacaopythondev-desafiosdecodigoeprojetos/blob/master/DesafiosDeProjeto/ProjetoSistemaBancario/UML_sistema_bancario.png)


