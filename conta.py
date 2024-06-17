from main import Conta

minha_conta = Conta(1)
minha_conta.creditar(100)
print(minha_conta.exibir_saldo())
minha_conta.render(10)
print(minha_conta.exibir_saldo())