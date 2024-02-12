#include <stdio.h>

void generate_sequence(int x0, int d, int n) {
    FILE *fp;
    fp = fopen("sequence_points.txt", "w");

    if (fp == NULL) {
        printf("Error opening file.\n");
        return;
    }

    for (int i = 0; i < n; i++) {
        int point = (i + 1) / 2 * (2 * x0 + i * d);
        fprintf(fp, "%d\n", point);
    }

    fclose(fp);
}

int main() {
    int x0 = 200;  // initial value
    int d = 50;    // common difference
    int n = 30;    // number of terms

    generate_sequence(x0, d, n);

    printf("Sequence points generated and saved in 'sequence_points.txt'\n");

    return 0;
}
