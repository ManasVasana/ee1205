#include <stdio.h>

#define X0 200   // initial value
#define D 50     // common difference
#define N_MAX 30 // maximum number of terms

void generate_sequence() {
    FILE *fp;
    fp = fopen("sequence_points.txt", "w");

    if (fp == NULL) {
        printf("Error opening file.\n");
        return;
    }

    for (int n = 0; n < N_MAX; n++) {
        int point = ((n + 1) / 2) * (2 * X0 + n * D);
        fprintf(fp, "%d\n", point);
    }

    fclose(fp);
}

int main() {
    generate_sequence();

    printf("Sequence points generated and saved in 'sequence_points.txt'\n");

    return 0;
}
