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
	while (slow->next != NULL && fast->next->next != NULL)
	{
		if (slow->next == fast->next->next)
			return (1);
		slow = slow->next;
		fast = fast->next->next;
	}
	return (0);
}
