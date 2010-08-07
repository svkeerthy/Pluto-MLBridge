#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include <unistd.h>
#include <sys/time.h>

#include <omp.h>

#include "decls.h"
#include "util.h"

int main()
{
	int i, j, k;
    double t_start, t_end;

	init_array() ;

	IF_TIME(t_start = rtclock());

#pragma scop
    for (k=0; k<N; k++) {
        for (j=k+1; j<N; j++)   {
            a[k][j] = a[k][j]/a[k][k];
        }
        for(i=k+1; i<N; i++)    {
            for (j=k+1; j<N; j++)   {
                a[i][j] = a[i][j] - a[i][k]*a[k][j];
            }
        }
    }
#pragma endscop

	IF_TIME(t_end = rtclock());
	IF_TIME(fprintf(stderr, "%0.6lfs\n", t_end - t_start));

    if (fopen(".test", "r")) {
        print_array();
    }
    return 0;
}
