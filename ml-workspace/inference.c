
#include <stdio.h>
#include "model_weights.h"
#include "model_bias.h"

int predict(float input[64])
{
    float scores[10];

    // Calculate score for each digit class
    for (int k = 0; k < 10; k++)
    {
        scores[k] = bias[k];

        for (int i = 0; i < 64; i++)
        {
            scores[k] += weights[k][i] * input[i];
        }
    }

    // Find class with maximum score
    int predicted_digit = 0;

    for (int k = 1; k < 10; k++)
    {
        if (scores[k] > scores[predicted_digit])
        {
            predicted_digit = k;
        }
    }

    return predicted_digit;
}

int main()
{
    float input[64];

    printf("Enter 64 pixel values (0-16):\n");

    for (int i = 0; i < 64; i++)
    {
        if (scanf("%f", &input[i]) != 1)
        {
            printf("Invalid input!\n");
            return 1;
        }
    }

    int result = predict(input);

    printf("\nPredicted digit: %d\n", result);

    return 0;
}
