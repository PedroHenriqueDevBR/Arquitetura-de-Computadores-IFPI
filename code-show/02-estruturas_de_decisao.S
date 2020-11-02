# Estruturas de decisão

# if
# A implementação da instrução if, requer a utilização de uma 
# instrução capaz de fazer verificações entre valores e retornar true ou false
# A instrução disponível no RISC16 capaz de realizar essa veririfcação 
# é a instrução "beq"

# beq a,b,c
# beq -> instrução
# a -> registrador 1 (um) na comparação
# b -> registrador 2 (um) na comparação
# c -> Ação executada caso os valores de "a" e "b" forem iguais


# else if
# A instrução else if basicamente é a proxima instrução caso o primeiro if
# seja false

# else
# O else é o proceguimento das instruções caso o "if" e o "else if" forem false


# Código de exemplo
        movi 1,10
        movi 2,9
        movi 3,11
        
start:	beq 1,2,done
        beq 1,3,done
        beq 0,0,sum
        
sum:	add 4,1,2
        add 4,4,3

done: 	halt
