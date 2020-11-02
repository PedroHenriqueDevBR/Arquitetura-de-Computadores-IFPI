# Loop

# Um loop é basicamente a implementação de uma rotina que se repete 
# enquando um valor de parada não for alcançado, caso o valor de parada 
# não seja alcançado nunca, então, teremos um loop infinito

# Para implementar um loop, vamos precisar de uma estrutura e uma 
# instrução já apresentada, que são elas, a implementação de uma rotina
# e a utilização da instrução "beq" que vai servir de verificador para
# causar o fim do loop.

# Exemplo de código

		movi 1,10
        movi 2,0
        
start:	beq 0,0,loop

loop:	beq 1,2,done
		addi 2,2,1
        beq 0,0,loop

done:	halt