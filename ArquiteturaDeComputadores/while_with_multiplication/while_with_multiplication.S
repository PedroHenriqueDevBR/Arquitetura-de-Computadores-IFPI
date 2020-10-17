//      enquanto A < B faça
//          C <- C + 1
//          se 3*C > 10
//              então A <- B + 1;
//          fim se
//      fim enquanto

		lw 1,0,a
        lw 2,0,b
        lw 3,0,c

loop:	beq 1,2,done
		addi 3,3,1
        addi 4,3,0
        addi 6,0,1
        addi 7,0,3

mult_v:	beq 6,7,reset
		add 4,4,3
		addi 6,6,1
        beq 0,0,mult_v

reset: 	addi 5,0,10
		addi 6,0,0
		addi 7,0,0

verify:	beq 7,4,loop
		beq 7,5,sum
        addi 7,7,1
        beq 0,0,verify
        
sum:	addi 1,2,1
		beq 0,0,done

done:	halt
a: 		.fill 3
b: 		.fill 5
c: 		.fill 1
