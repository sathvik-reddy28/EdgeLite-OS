
#include <stdio.h>
#include <string.h>
#include <time.h>
#include "model_weights.h"
#include "model_bias.h"

int predict(float input[64])
{
    float scores[10];

    for (int k = 0; k < 10; k++)
    {
        scores[k] = bias[k];

        for (int i = 0; i < 64; i++)
            scores[k] += weights[k][i] * input[i];
    }

    int predicted_digit = 0;

    for (int k = 1; k < 10; k++)
    {
        if (scores[k] > scores[predicted_digit])
            predicted_digit = k;
    }

    return predicted_digit;
}

int main(int argc, char *argv[])
{
    float input[64] = {0};

    if (argc == 2 && strcmp(argv[1], "--benchmark") == 0)
    {
        volatile int result_sink = 0;
        int last_prediction = 0;

        clock_t start = clock();

        for (int i = 0; i < 100000; i++)
        {
            input[i % 64] = (float)(i % 17);
            last_prediction = predict(input);
            result_sink += last_prediction;
        }

        clock_t end = clock();

        double total_ms =
            (double)(end - start) * 1000.0 / CLOCKS_PER_SEC;

        printf("Iterations: 100000\n");
        printf("Last predicted digit: %d\n", last_prediction);
        printf("Result checksum: %d\n", result_sink);
        printf("Total time: %.3f ms\n", total_ms);
        printf("Average inference latency: %.6f ms\n",
               total_ms / 100000.0);

        return 0;
    }

    if (argc == 2 && strcmp(argv[1], "--demo") == 0)
    {
        printf("\nEdgeLite OS - Automatic Digit Inference Demo\n");
        printf("Running inference on a predefined 8x8 input...\n");
    }
    else
    {
        printf("Enter 64 pixel values (0-16):\n");

        for (int i = 0; i < 64; i++)
        {
            if (scanf("%f", &input[i]) != 1)
            {
                printf("Invalid input!\n");
                return 1;
            }
        }
    }

    int result = predict(input);

    printf("Predicted digit: %d\n", result);

    return 0;
}
