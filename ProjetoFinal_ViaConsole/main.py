'''Faça um programa que realize o cadastro das seguintes telas:
-Login
-Cadastro de Imóveis
-Cadastro de Aluguel (Imóvel x Inquilino)
-Cadastro do Inquilino
-Cadastro do Proprietário (Opcional)
Os campos são:
Para Imóvel:
-ID / Logradouro / CEP / Bairro / Cidade
Para Aluguel
-ID / ID Imóvel / ID Inquilino
Para Inquilino e/ou Proprietário
-ID / Nome / Data Nascimento
Use a criatividade para criar o programa, utilize tudo que
 você aprendeu na trilha. Listas, Dicionários, Funções, Classes e
Condicionais, Loops e etc '''

from src.usuario import Usuario
from src.function_login import escolha


print("Seja Bem-Vindo(a)!")
print("Para iniciar, informe a opção desejada: ")
escolha()