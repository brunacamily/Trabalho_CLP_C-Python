#include <stdio.h>
#include <stdlib.h>

#define WIDTH 800
#define HEIGHT 800
#define MAX_ITER 1000

int mandelbrot(double real, double imag) {
    double z_real = 0.0;
    double z_imag = 0.0;
    int iter;

    for (iter = 0; iter < MAX_ITER; iter++) {
        double z_real2 = z_real * z_real;
        double z_imag2 = z_imag * z_imag;

        if (z_real2 + z_imag2 > 4.0) {
            break; // Diverge
        }

        z_imag = 2.0 * z_real * z_imag + imag;
        z_real = z_real2 - z_imag2 + real;
    }

    return iter;
}
