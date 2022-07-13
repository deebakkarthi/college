#include <stdio.h>
#include <stdlib.h>
#include "banker.h"

int request(int *avail, int *need, int *alloc, int *req, int res_n);

int request(int *avail, int *need, int *alloc, int *req, int res_n)
{
	if(!(arr_comp(req,need,res_n))){
		return 0;
	}else{
		if(!(arr_comp(req,avail,res_n))){
			return 0;
		}else{
			/*Simulating giving resources
			 * has to be claimed back if there are no
			 * safe sequences available*/
			arr_sub(avail,req,res_n);
			arr_add(alloc,req,res_n);
			arr_sub(need,req,res_n);
			return 1;
		}
	}
}

int main()
{
	int proc_n;
	int res_n;
	scanf("%d %d",&proc_n,&res_n);

	int **max;
	int **alloc;
	int **need = matrix_init(proc_n,res_n);
	int *avail;
	int *req;
	int pid;

	avail = get_arr(res_n);
	max = get_matrix(proc_n, res_n);
	alloc = get_matrix(proc_n, res_n);
	/*need = max - alloc*/
	matrix_sub(need,max,alloc,proc_n,res_n);

	print_table(avail,need,alloc,max,proc_n,res_n);

	/*request input*/
	scanf("%d",&pid);
	req = get_arr(res_n);
	printf("P%d requested ",pid);
	print_arr(req,res_n);

	if(request(avail,need[pid],alloc[pid],req,res_n)){
		if(safety(avail,need,alloc,proc_n,res_n)){
			printf("Safe\n");
			print_table(avail,need,alloc,max,proc_n,res_n);
		}else{
			printf("Unsafe\n");
			
			/*
			 * Reclaiming resources
			 * */
			arr_add(avail,req,res_n);
			arr_sub(alloc[pid],req,res_n);
			arr_add(need[pid],req,res_n);

			print_table(avail,need,alloc,max,proc_n,res_n);
		}
	}else{
		printf("Unsafe/Invalid request\n");
	}
}

