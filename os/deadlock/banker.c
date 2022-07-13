/*
 * Auxillary funcs used in both safety and request
 * */
#include <stdio.h>
#include <stdlib.h>
/*Return a pointer to a copy of the given array*/
int *arr_copy(int *a, int size)
{
	int *copy;
	copy = (int *)calloc(size,sizeof(int));
	for(int i = 0; i < size; i++)
		copy[i] = a[i];
	return copy;
}
void print_arr(int *a, int size)
{
	for(int i = 0; i < size; i++)
		printf("%d ",a[i]);
	printf("\n");
}
int *get_arr(int size)
{
	int *arr;
	arr = (int *)calloc(size,sizeof(int));
	for(int i = 0; i < size; i++)
		scanf("%d",arr+i);
	return arr;
}

/*
 * a = a + b
 * */
void arr_add(int *a, int *b, int size)
{
	for(int i = 0; i < size; i++)
		a[i] = a[i] + b[i];
}

/*
 * a = a - b
 * */
void arr_sub(int *a, int *b, int size)
{
	for(int i = 0; i < size; i++)
		a[i] = a[i] - b[i];
}

/*
 * Returns 1 if x <= y for all x in a and corresponding y in b
 * */
int arr_comp(int *a, int *b, int size)
{
	int ret = 1;
	for(int i = 0; i < size; i++)
		ret = ret && ( a[i] <= b[i] );
	return ret;
}

/*return a pointer to a matrix after getting input*/
int **get_matrix(int row, int col)
{
	int **mat;
	mat = (int **)calloc(row,sizeof(int *));
	for(int i = 0; i < row; i++){
		mat[i] = get_arr(col);
	}
	return mat;
}
/*
 * des = a - b
 * */
void matrix_sub(int **des, int **a, int **b, int row, int col)
{
	for(int i = 0; i < row; i++){
		for(int j = 0; j < col; j++)
			des[i][j] = a[i][j] - b[i][j];
	}
}
/*returns a pointer to a matrix with row rows and col columns initialized to 0*/
int **matrix_init(int row, int col)
{
	int **mat;
	mat = (int **)calloc(row,sizeof(int *));
	for(int i = 0; i < row; i++){
		mat[i] = (int*)calloc(col,sizeof(int));
	}
	return mat;
}

/*Prints the Resource Allocation Table*/
void print_table(int *avail,int **need, int **alloc, int **max,int row, int col)
{
	printf("AVAIL: ");
	print_arr(avail,col);
	printf("PID\tNEED\tALLOC\tMAX\n");
	for(int i = 0; i < row; i++){
		printf("P%d\t",i);
		for(int j = 0; j < col; j++){
			printf("%d ",need[i][j]);
		}
		printf("\t");
		for(int j = 0; j < col; j++){
			printf("%d ",alloc[i][j]);
		}
		printf("\t");
		for(int j = 0; j < col; j++){
			printf("%d ",max[i][j]);
		}
		printf("\n");
	}
}

/*returns 1 if there a safe sequence available*/

int safety(int *avail, int **need, int **alloc, int proc_n, int res_n)
{
	/*Temporary copy of avail*/
	int *work = arr_copy(avail,res_n);
	/*Using calloc to get preinitialized array*/
	int *finish = (int *)calloc(proc_n,sizeof(int));

	/*flag to indicate completion of ALL processes*/
	int completed;
	/*Atleast 1 process that can be finished*/
	int legal = 1;

	while(legal){
		legal = 0;
		completed = 1;
		for(int i = 0; i < proc_n; i++){
			if ( finish[i] == 0 && arr_comp(need[i], work,res_n)){
				finish[i] = 1;

				/* Reclaiming resources
				 * work = work + alloc[i]
				 * */

				arr_add(work,alloc[i],res_n);
				printf("P%d ",i);
				legal = 1;
			}
			/*atleast one 0 in finish[] will make completed 0*/
			/*Has to be after if incase the process can be finished*/
			completed = completed && finish[i];
		}
		if(completed){
			return 1;
		}
	}
	return 0;
}

