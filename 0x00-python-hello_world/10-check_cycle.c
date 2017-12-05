#include "lists.h"
/**
* check_cycle - Checks if a singly linked list has a cycle in it.
* @list: Pointer to the singly linked list
* Return: 1 if there is cycle, else 0.
*/
int check_cycle(listint_t *list)
{
	listint_t *slow;
	listint_t *fast;

	fast = list;
	slow = list;
	while (slow->next != NULL && fast->next != NULL && fast->next->next != NULL)
	{
		slow = slow->next;
		fast = fast->next->next;
		if (slow == fast)
			return (1);
	}
	return (0);
}
