#include "lists.h"
/**
 *check_cycle - check for a loop in a linked list
 *@list: list
 *Return: return 1 for loop ,0 otherwise
 */

int check_cycle(listint_t *list)
{
	listint_t *tortoise = list, *hare = list;

	if (list == NULL)
		return (0);

	while ( tortoise && hare && hare != NULL)
	{
		tortoise = tortoise->next;
		hare = hare->next->next;
		if (tortoise == hare)
			return (1);
	}
	return (0);
}
