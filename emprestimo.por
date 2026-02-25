
  inteiro valorCasa, salario, prestacao, limite : real
   anos, meses : 

inicio

{
   escreva("Digite o valor da casa: R$ ")
   leia(valorCasa)

   escreva("Digite o salário do comprador: R$ ")
   leia(salario)

   escreva("Em quantos anos vai pagar? ")
   leia(anos)

   meses <- anos * 12
   prestacao <- valorCasa / meses
   limite <- salario * 0.3

   escreval("Valor da prestação mensal: R$ ", prestacao:0:2)
   escreval("30% do salário: R$ ", limite:0:2)

   se prestacao <= limite entao
      escreval("Empréstimo APROVADO!")
   senao
      escreval("Empréstimo NEGADO!")
}