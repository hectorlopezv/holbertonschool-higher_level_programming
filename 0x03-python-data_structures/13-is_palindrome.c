#include "lists.h"
/**
 *is_palindrome - is palindrome
 *@head: head of the list
 *Return: return 1 if palindrome 0 otherwise
 */
int is_palindrome(listint_t **head)
{
	listint_t *low, *fast, *prev, *temp;

	fast = *head;
	low = *head;
	prev = NULL, temp = NULL;
	if (head == NULL || *head == NULL)
		return (1);
	while (fast && fast->next)
	{/* loop until middle and reverse*/
		temp = low->next;
		fast = fast->next->next;
		low->next = prev;
		prev = low;
		low = temp;
	}
	low = fast != NULL ? low->next : low;
	while (low)
	{
		if (low->n != prev->n)
			return (0);
		low = low->next;
		prev = prev->next;
	}
	return (1);
}

