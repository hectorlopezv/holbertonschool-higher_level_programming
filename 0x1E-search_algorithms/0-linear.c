#include "search_algos.h"

/**
 * linear_search - linear search
 *@array: array of intergers
 *@size: size of the array
 *@value: value to search
 *Return: -1 if not found else value
 */


int linear_search(int *array, size_t size, int value)
{
	int i;

	if (array == NULL)
		return (-1);

	for (i = 0; (size_t)i < size; i++)
	{
		printf("Value checked array[%d] = [%d]\n", i, array[i]);
		if (array[i] == value)
			return (i);
	}
	return (-1);
}
