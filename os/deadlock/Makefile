all: safety request

safety: safety.o banker.o
	gcc -o safety safety.o banker.o

safety.o: safety.c
	gcc -c safety.c

banker.o: banker.c
	gcc -c banker.c

request: request.o banker.o
	gcc -o request request.o banker.o

request.o: request.c
	gcc -c request.c

