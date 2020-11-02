# Rotinas

# As rotinas no RISC16 são essensiais para manter um código que seja 
# possível de ser entendido e modificado, gerando menos erros e dor de cabeça.

# A implementação de uma rotina utiliza a mesma estrutura da implementação 
# de uma variável, sendo que, na variável o valor é atribuido utilizando o .fill
# e na rotina nós podemos atribuir diretamente as instruções, sem o uso do .fill.


# Exemplo do código apresentado
		lw 1,0,a
        lw 2,0,b
        
start:	add 3,1,2
		beq 0,0,done

done:	halt

a: .fill 10
b: .fill 20