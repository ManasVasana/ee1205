#include <stdio.h>

void generate_sequence_recursive(int x0, int d, int n, int current, FILE *fp) {
    if (current >= n) {
        fclose(fp);
        return;
    }

    // Calculate the value at position current using the arithmetic sequence formula
    // y(current) = ((current + 1) / 2) * (2 * x0 + (current - 1) * d)
    int point = ((current + 1) / 2) * (2 * x0 + (current - 1) * d);

    if (point > 27750) {
        fprintf(fp, "%d *\n", point);
    } else {
        fprintf(fp, "%d\n", point);
    }

    generate_sequence_recursive(x0, d, n, current + 1, fp);
}

void generate_sequence(int x0, int d, int n) {
    FILE *fp;
    fp = fopen("sequence_points.txt", "w");

    if (fp == NULL) {
        printf("Error opening file.\n");
        return;
    }

    generate_sequence_recursive(x0, d, n, 0, fp);

    printf("Sequence points generated and saved in 'sequence_points.txt'\n");
}

int main() {
    int x0 = 200;  // initial value
    int d = 50;    // common difference
    int n = 30;    // number of terms

    generate_sequence(x0, d, n);

    return 0;
}
