       	addi 3,0,0
        addi 4,0,1
        beq 0,0,loop

loop: 	lw 1,3,vetor
        lw 2,4,vetor
        movi 0,zero
        beq 0,0,smal

smal:	beq 0,2,change
        beq 0,1,save
        addi 0,0,1
        beq 0,0,smal

change:	addi 7,1,zero
	addi 1,2,zero
        addi 2,7,zero
        movi 6,noend
        beq 0,0,save

save:	sw 1,3,vetor
	sw 2,4,vetor
        movi 0,4
        beq 0,4,reset
        addi 3,3,1
	addi 4,3,1
        movi 6,0
	beq 0,0,loop

reset:	movi 0,zero
        beq 0,6,done
	movi 3,zero
        movi 4,one
        beq 0,0,loop

done:	movi 0,zero
	lw 1,0,vetor
        addi 0,0,1
        lw 2,0,vetor
        addi 0,0,1
        lw 3,0,vetor
        addi 0,0,1
        lw 4,0,vetor
        addi 0,0,1
        lw 5,0,vetor
        beq 0,0,end
        
aux:	.fill 0
zero:	.fill 0
one:	.fill 1
noend:	.fill 1
vetor:	.fill 5
 	.fill 2
 	.fill 4
 	.fill 3
 	.fill 1
end:	halt
