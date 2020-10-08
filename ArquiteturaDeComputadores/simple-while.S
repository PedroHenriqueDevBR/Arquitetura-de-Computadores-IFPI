	    lw 1,0,a
        lw 2,0,b
        lw 3,0,c
        beq 0,0,start
start: 	add 4,1,2
	    beq 4,3,stop
        addi 1,1,1
        addi 2,2,2
        addi 3,3,-1
        beq 0,0,start
stop: 	halt
a:	    .fill 10
b: 	    .fill 12
c: 	    .fill 30