int *get_arr(int size);
void arr_add(int *a, int *b, int size);
void arr_sub(int *a, int *b, int size);
int arr_comp(int *a, int *b, int size);
int *arr_copy(int *a, int size);
void print_arr(int *a, int size);
int **get_matrix(int row, int col);
void matrix_sub(int **des, int **a, int **b, int row, int col);
int **matrix_init(int row, int col);
void print_table(int *avail,int **need, int **alloc, int **max,int row, int col);
int safety(int *avail, int **need, int **alloc, int proc_n, int res_n);

