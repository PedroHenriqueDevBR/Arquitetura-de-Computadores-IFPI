//      se A*B > C
//          então C <- C*3;
//      fim se

		lw 1,0,a
        lw 2,0,b
        lw 3,0,c

mult:	beq 7,1,reset
        add 4,4,2
        addi 7,7,1
        beq 0,0,mult

reset:	add 6,0,0
        add 7,0,0

more_t:	beq 7,4,done
		beq 7,3,pre_mc
        addi 7,7,1
        beq 0,0,more_t

pre_mc:	addi 7,0,1
		addi 4,0,3
		beq 0,0,mult_c

mult_c:	beq 7,4,done
		addi 3,3,c
        addi 7,7,1
        beq 0,0,mult_c

done:	halt
a: 		.fill 3
b: 		.fill 5
c: 		.fill 10