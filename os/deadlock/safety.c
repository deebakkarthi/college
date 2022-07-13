#include <stdio.h>
#include <stdlib.h>
#include "banker.h"

int main()
{
	int proc_n;
	int res_n;
	scanf("%d %d",&proc_n,&res_n);

	int **max;
	int **alloc;
	int **need = matrix_init(proc_n,res_n);
	int *avail;

	avail = get_arr(res_n);
	max = get_matrix(proc_n, res_n);
	alloc = get_matrix(proc_n, res_n);
	/*Calculate need
	 * need = max - alloc
	 * */
	matrix_sub(need,max,alloc,proc_n,res_n);

	print_table(avail,need,alloc,max,proc_n,res_n);

	if(safety(avail,need,alloc,proc_n,res_n))
		printf("Safe\n");
	else
		printf("Unsafe\n");
}
