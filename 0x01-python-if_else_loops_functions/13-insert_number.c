#include "lists.h"
#include <stdio.h>
/**
 *insert_node - add node in the end of linked list
 *@head: head of the list
 *@number: number to insert
 *Return: return node
 */

listint_t *insert_node(listint_t **head, int number)
{
	listint_t *tmp = *head, *node;

	if (head == NULL || *head == NULL)
		return (NULL);
	while (tmp && tmp->next)
	{
		if (number <= tmp->next->n)
			break;
		tmp = (tmp)->next;
	}
	node = malloc(sizeof(listint_t));
	if (node == NULL)
		return (NULL);
	node->n = number;
	node->next = tmp->next;
	tmp->next = node;
	return (node);
}
