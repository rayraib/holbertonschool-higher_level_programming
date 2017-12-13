#include "lists.h"
/**
* is_palindrome - Checks if a singly linked list is a palindrome
* @head: Double pointer to the first node of the singly linked list
* Return: 1 if palindrome, 0 if not a palindrome
*/
int is_palindrome(listint_t **head)
{
	listint_t *tmp, *beg, *mid, *end;
	int i, num_node, mid_idx;

	if (head == NULL || *head == NULL)
		return (0);
	tmp = beg = mid = end = *head;
	num_node = 1;
	while (end->next != NULL)
	{
		end = end->next;
		num_node++;
	}
	if (beg == end)
		return (1);
	mid_idx = num_node / 2;
	for (i = 0; i < mid_idx; i++)
		mid = mid->next;
	if (beg->n == end->n)
	{
		if (end == mid)
			return (1);
		tmp = mid;
		while (1)
		{
			while (mid->next != end && mid != end)
				mid = mid->next;
			beg = beg->next;
			if (beg == tmp)
				return (1);
			if (beg->n != mid->n)
				return (0);
			end = mid;
			mid = tmp;
		}
	}
	return (0);
}
