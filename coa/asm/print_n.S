# variables
# $t0 - n
# $t1 - loop cond and offset in words
# $t2 - base addr
# $t3 - offset in bytes
# $t4 - final addr
.data
	arr: .word 69, 420, 13, 15, 24, 12, 100, 99, 21, 23, 24, 45
	prompt: .asciiz "Enter the number of numbers to be printed:\n"
	newline: .asciiz "\n"
.text
.globl main
main:
	# print prompt
	li $v0, 4
	la $a0, prompt
	syscall
	
	# get input for n
	li $v0, 5
	syscall

	# move n to $t0
	or $t0, $v0, $zero

	# $t1 loop cond var
	li $t1, 0
	la $t2, arr # $t2 = base_addr

	loop:
		beq $t1, $t0, exit
	 	# $t3  = 4*word_offset
		sll $t3, $t1, 2
	 	# $t2 = base + byte_offset
		add $t4, $t2, $t3

		#Printing num
		lw $a0, 0($t4)
		li $v0, 1
		syscall

		# printing newline
		li $v0, 4
		la $a0, newline
		syscall

		addi $t1, $t1, 1
		j loop
	j exit
exit:
	li $v0, 10
	syscall
