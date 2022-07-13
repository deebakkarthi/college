#include <stdio.h>
#include <semaphore.h>
#include <stdlib.h>
#include <unistd.h>
#include <pthread.h>

sem_t empty;
sem_t full;
sem_t mutex;
int *buf;
int max_buf;

void usage();
void buf_init();
void semaphore_init();
void thread_init();
void destroy_sem();
void *producer();
void *consumer();
void print_buf();

void usage()
{
	fprintf(stderr,"Usage: pc [MAX_BUF]\n");
	exit(1);
}

void buf_init()
{
	buf = (int *)calloc(max_buf,sizeof(int));
}

void semaphore_init()
{
	/*Delete previous semaphores as semaphores are not
	 * released automatically when a process dies
	 * */
	destroy_sem();
	sem_init(&full,0,0);
	sem_init(&empty,0,max_buf);
	sem_init(&mutex,0,1);
}

void destroy_sem()
{
	sem_destroy(&full);
	sem_destroy(&empty);
	sem_destroy(&mutex);
}

void thread_init()
{
	/*Creating and joining producer and consumer threads*/
	pthread_t ptid, ctid;
	pthread_create(&ptid,NULL,producer,NULL);
	pthread_create(&ctid,NULL,consumer,NULL);
	pthread_join(ptid,NULL);
	pthread_join(ctid,NULL);
}

void *producer()
{
	int ind = 0;
	for(int i = 0 ; i < 5*max_buf; i++){
		sem_wait(&empty);
		sem_wait(&mutex);

		/*Critical Section*/
		buf[ind] = (random() % 100) + 1;
		ind = (ind + 1) % max_buf;
		print_buf("P");

		sem_post(&mutex);
		sem_post(&full);
	}
}

void *consumer()
{
	int ind = 0;
	for(int i = 0 ; i < 5*max_buf; i++){
		sem_wait(&full);
		sem_wait(&mutex);

		/*Critical section*/
		buf[ind] = 0;
		ind = (ind + 1) % max_buf;
		print_buf("C");

		sem_post(&mutex);
		sem_post(&empty);
	}
}

void print_buf(char *caller)
{
	printf("%s:",caller);
	for(int i = 0; i < max_buf; i++)
		if(buf[i] != 0)
			printf("%d ",buf[i]);
	printf("\n");
}

int main(int argc, char **argv)
{
	if (argc < 2)
		usage();

	max_buf = atoi(argv[1]);

	buf_init();
	semaphore_init();
	thread_init();
	destroy_sem();
	return 0;
}
