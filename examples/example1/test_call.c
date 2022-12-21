/*
File:       test_call.c
Written by: Niranjan Bhujel
*/

#include "test.h"
#include "test_Call.h"

void test_call_func(casadi_real *a, casadi_real *x, casadi_real *y)
{
    const casadi_real *arg[21];
    casadi_real *res[12];
    casadi_int iw[15];
    casadi_real w[112];      // Size should be printed arg_size + size of input + size of output = 109 + 1 + 2 = 112

    /* 
    w stores input and output (and other variables).
    arg stores address of input (and other variables).
    res stores sddress of output (and other variables)

    Thus, addresses should be assigned for input and output.
    */
    arg[0] = w + 0;

    res[0] = w + 1;
    res[1] = w + 2;
    

    // Assign input
    w[0] = a[0];

    // Call solver function. w+3 is passed here. Always pass w + (size of input + size of output) = w + 1 + 2 = w+3.
    solver_func(arg, res, iw, w + 3, 0);

    // Assign output
    x[0] = w[1];
    y[0] = w[2];
}