#include <stdio.h>
#include <stdlib.h>
#include "lists.h"

/**
 * check_cycle - Checks if a singly-linked list contains a cycle
 * @list: A singly-linked list
 *
 * Return: If there is no cycle - 0
 *         If there is a cycle - 1
 */
int check_cycle(listint_t *list)
{
	listint_t *load1, *load2;
	
	load1 = list;
	load2 = list;

	while (load1 && load2 && load2->next)
	{
		load1 = load1->next;
		load2 = load2->next->next;

		if (load1 == load2)
		{
			printf("There is a cycle.");
			return (1);
		}
	}
	return (0);
}
