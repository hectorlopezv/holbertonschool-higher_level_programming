#include "lists.h"
#include <stdio.h>
/**
 *insert_node - add node in the end of linked list
 *@head: head of the list
 *@number: number to insert
 *Return: return NULL if failed , node otherwise
 */

listint_t *insert_node(listint_t **head, int number)
{
	listint_t *tmp = *head, *node;

	if (head == NULL)
		return (NULL);
	node = malloc(sizeof(listint_t));
	if (node == NULL)
		return (NULL);
	node->n = number;
	node->next = NULL;
	if (*head == NULL)
		*head = node;
	if ((*head)->n > number)
	{
		node->next = *head;
		*head = node;
		return (node);
	}
	while (tmp && tmp->next)
	{
		if (number <= tmp->next->n)
			break;
		tmp = (tmp)->next;
	}
	node->next = tmp->next;
	tmp->next = node;
	return (node);
}
