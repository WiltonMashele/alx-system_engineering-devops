#include <stdio.h>
#include <stdlib.h>
#include <sys/types.h>
#include <sys/wait.h>
#include <unistd.h>

/**
 * infinite_while - Executes a loop that continues indefinitely.
 *
 * Return: Always returns 0.
 */

int infinite_while(void)
{
	while (1)
	{
		sleep(1);
	}
	return (0);
}

/**
 * main - Generates and initiates five zombie processes.
 *
 * Return: Always EXIT_SUCCESS (0).
 */

int main(void)
{
	pid_t processID;
	char counter = 0;

	for(; counter < 5; counter++)
	{
		processID = fork();
		if (processID > 0)
		{
			printf("Created zombie process, PID: %d\n", processID);
			sleep(1);
		}
		else
			exit(0);
	}

	infinite_while();

	return (EXIT_SUCCESS);
}
