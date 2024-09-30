
#include <cs50.h>
#include <stdio.h>

int main(void)
{
    // Prompt the user for their name
    string name = get_string("What's your name? ");

    // Prompt the user for their age
    int age = get_int("How old are you? ");

    // Print a greeting message
    printf("Hello, %s! You are %d years old.\n", name, age);

    return 0;
}
