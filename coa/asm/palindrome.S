# $s0 - size of string
# $s1 - base addr of string
# $s2 - last addr of string

# $t0 - loop cond
# $t1 - n/2

# $t2 - L char
# $t3 - R char
.data
	size_prompt: .asciiz "Enter the size of string:\n"
	str_prompt: .asciiz "Enter the string:\n"
	succ_prompt: .asciiz "It is a palindrome\n"
	fail_prompt: .asciiz "It is not a palindrome\n"
	newline: .asciiz "\n"
.text
.globl main
main:
	# print size prompt
	li $v0, 4
	la $a0, size_prompt
	syscall

	# get input for n
	li $v0, 5
	syscall

	# store size in $t0 and allocate n+1 bytes
	or $s0, $v0, $zero
	or $a0, $v0, $zero
	addi $a0, $a0, 1
	li $v0, 9
	syscall
	
	# move the memory address to $t1
	or $s1, $v0, $zero

	# print string input prompt
	li $v0, 4
	la $a0, str_prompt
	syscall

	# get input string
	or $a1, $s0, $zero
	# Only gets input of size n-1 to accomodate \0
	# But we have already allocated extra space for \0
	# So we can increment this by one to get input of size n
	addi $a1, $a1, 1
	or $a0, $s1, $zero
	li $v0, 8
	syscall

	# print newline
	li $v0, 4
	la $a0, newline
	syscall

	# last addr
	or $t0, $s0, $zero
	addi $t0, $t0, -1
	add $s2, $s1, $t0

	# loop var
	li $t0, 0
	# n/2
	li $t1, 2
	div $s0, $t1
	mflo $t1
	loop:
		beq $t0, $t1, loop_exit

		# Palindrome check  = a[i] != a[n-i]
		# a[n] is in $s2
		# Getting forward part of the string
		add $t2, $s1, $t0
		lb $t2, 0($t2)

		# Getting backward part of the string
		sub $t3, $s2, $t0
		lb $t3, 0($t3)

		bne $t2, $t3, fail
		addi $t0, $t0, 1
		j loop
	loop_exit:
		# print success string
		li $v0, 4
		la $a0, succ_prompt
		syscall
		j exit
	fail:
		# print success string
		li $v0, 4
		la $a0, fail_prompt
		syscall
		j exit

exit:
	li $v0, 10
	syscall
