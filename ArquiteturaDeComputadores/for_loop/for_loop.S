//      para i de A até B faça
//          C <- C – A;
//     fim para

		lw 1,0,a
        lw 2,0,b
        lw 3,0,c
        lw 4,0,a

neg:	nand 4,4,4
		addi 4,4,1

loop:	beq 1,2,done
		add 3,3,4
        addi 1,1,1
        beq 0,0,loop

done:	halt
a: 		.fill 1
b: 		.fill 5
c: 		.fill 15
