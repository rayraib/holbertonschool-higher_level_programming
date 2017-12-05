#include "lists.h"
/**
* check_cycle - Checks if a singly linked list has a cycle in it.
* @list: Pointer to the singly linked list
* Return: 1 if there is cycle, else 0.
*/
int check_cycle(listint_t *list)
{
	int i, index;
	listint_t *loop_head, *tmp;

	i = index = 0;
	tmp = list;
	if (tmp == NULL)
		return (0); /*if initial header pointer is NULL */
	if (tmp->next == NULL)
		return (0);/*if first node points to NULL */
	tmp = tmp->next;
	while (tmp->next != NULL)
	{
		index++;
		loop_head = list;
		for (i = 0; i < index; i++)
		{
			if (tmp->next == loop_head)
				return (1);
			loop_head = loop_head->next;
		}
		tmp = tmp->next;
	}
	return (0);
}

