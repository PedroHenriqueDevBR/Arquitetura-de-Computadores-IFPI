# Instruções
add     -> Adição entre registradores                           # (X) add 1,0,3
addi    -> Adição entre um registrador e um valor imediato      # (X) addi 1,0,10 -> número
nand    -> Negação do regA com o regB                           # (X) nand 1,2,2
lui	    -> Aplica um valor imediato AND 0Xffc0                  #     lui 1,0
sw	    -> Armazena um valor de um registrador em uma variável  # (X) sw 1,0,n
lw	    -> Carrega valor de uma variável no registrador         # (X) lw 1,0,n
beq	    -> Verifica simularidade entre dois valores, se forem   # (X) beq 0,0,done
            iguais executa uma ação
jalr    -> Armazena o point counter no regA                     #     jarl 1,0

# Pseudo-instruções
nop	    -> Não faz nada                                         #      nop
halt    -> Parar o processo                                     # (X)  halt
lli	    -> Adição de (um valor imediato + 0x3f) com um          #      lli 1,n
            registrador e atribui a valor ao mesmo registrador
movi    -> Atribui um valor imediato a um registrador           # (X)  movi 1,n
.fill   -> Cria variáveis                                       # (X)  .fill
.space  -> Inicializa um array com N valores 0                  # (X)  .space 5
