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

int main() {
    FILE *fp = fopen("mandelbrot.ppm", "w");
    if (!fp) {
        fprintf(stderr, "Erro ao abrir o arquivo.\n");
        return 1;
    }

    fprintf(fp, "P3\n%d %d\n255\n", WIDTH, HEIGHT);

    for (int y = 0; y < HEIGHT; y++) {
        for (int x = 0; x < WIDTH; x++) {
            double real = (x - WIDTH / 2.0) * 4.0 / WIDTH;
            double imag = (y - HEIGHT / 2.0) * 4.0 / HEIGHT;

            int iter = mandelbrot(real, imag);
            int color = (iter == MAX_ITER) ? 0 : (iter * 255 / MAX_ITER);

            fprintf(fp, "%d %d %d ", color, color, color); // Grayscale
        }
        fprintf(fp, "\n");
    }

    fclose(fp);
    printf("Imagem do conjunto de Mandelbrot gerada como mandelbrot.ppm\n");
    return 0;
}
