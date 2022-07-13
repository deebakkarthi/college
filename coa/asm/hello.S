# Hello world
.data
	str: .asciiz "hello, world\n"
.text
.globl main
main:
	# 4 - sycall for print string
	li $v0, 4
	# $a0 contains address of the string to be printed
	la $a0, str
	syscall

	j exit
exit:
	# 10 - syscall to halt
	li $v0, 10
	syscall
