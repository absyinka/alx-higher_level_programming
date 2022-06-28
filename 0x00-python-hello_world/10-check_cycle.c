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

	if (list == NULL || list->next == NULL)
		return (0);

	load1 = list->next;
	load2 = list->next->next;

	while (load1 && load2 && load2->next)
	{
		if (load1 == load2)
			return (1);

		load1 = load1->next;
		load2 = load2->next->next;
	}

	return (0);
}
