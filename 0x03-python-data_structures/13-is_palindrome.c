#include "lists.h"
/**
 *is_palindrome - is palindrome
 *@head: head of the list
 *Return: return 1 if palindrome 0 otherwise
 */
int is_palindrome(listint_t **head)
{
	int len_list = 0, i;
	int *temp_list;
	listint_t *temp_head = *head, *temp_head_2 = *head;

	if (head == NULL || *head == NULL)
		return (1);
	while (temp_head != NULL)
	{
		len_list++;
		temp_head = temp_head->next;
	}
	temp_head = *head;
	temp_list = malloc(len_list * sizeof(int));
	for (i = 0; i < len_list; i++)
	{
		temp_list[i] = temp_head->n;
		temp_head = temp_head->next;
	}
	temp_list += i - 1;
	for (i = 0; i < len_list; i++)
	{
		if (*temp_list == temp_head_2->n)
		{
			if (i == len_list - 1)
				continue;
			else
			{
				--temp_list;
			}
			temp_head_2 = temp_head_2->next;
		}
		else
		{
			free(temp_list);
			return (0);
		}
	}
	free(temp_list);
	return (1);/*palindrome*/
}
