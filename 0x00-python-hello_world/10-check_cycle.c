#include "lists.h"
/**
* check_cycle - Checks if a singly linked list has a cycle in it.
* @list: Pointer to the singly linked list
* Return: 1 if there is cycle, else 0.
*/
int check_cycle(listint_t *list)
{
	int i, index;
	listint_t *loop_head, *temp;

	i = index = 0;
	temp = list;
	if (list == NULL)
		return (0); /*if initial header pointer is NULL */
	if (list->next == NULL)
		return (0);/*if first node points to NULL */
	while (1)
	{
		index++;
		loop_head = temp;
		list = list->next;
		if (list->next == NULL)
			return (0);
		for (i = 0; i < index; i++)
		{
			if (list->next == loop_head)
				return (1);
			loop_head = loop_head->next;
		}
	}
}

