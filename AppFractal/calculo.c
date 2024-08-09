#include <stdio.h>

int mandelbrot(double real, double imag, int max_iter) {
    double zr = 0.0, zi = 0.0;
    int iter = 0;
    while (zr * zr + zi * zi < 4.0 && iter < max_iter) {
        double temp = zr * zr - zi * zi + real;
        zi = 2.0 * zr * zi + imag;
        zr = temp;
        iter++;
    }
    return iter;
}

void generate_mandelbrot(int width, int height, double x_min, double x_max, double y_min, double y_max, int max_iter, int *output) {
    double dx = (x_max - x_min) / (width - 1);
    double dy = (y_max - y_min) / (height - 1);
    for (int y = 0; y < height; y++) {
        for (int x = 0; x < width; x++) {
            double real = x_min + x * dx;
            double imag = y_min + y * dy;
            output[y * width + x] = mandelbrot(real, imag, max_iter);
        }
    }
}
