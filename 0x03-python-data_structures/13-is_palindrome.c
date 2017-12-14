#include "lists.h"
/**
* is_palindrome - Checks if a singly linked list is a palindrome
* @head: Double pointer to the first node of the singly linked list
* Return: 1 if palindrome, 0 if not a palindrome
*/
int is_palindrome(listint_t **head)
{
	listint_t *current, *next, *previous, *sec_head;
	int length, i, mid_idx;

	next = current = *head;
	if (head == NULL || *head == NULL || (*head)->next == NULL)
		return (1);
	for (length = 0; next->next != NULL; length++)
		next = next->next;
	length -= 1;
	mid_idx = length / 2;
	for (i = 0; i < mid_idx; i++)
		current = current->next;
	if (length % 2 == 0)
		next = current->next;
	else
		next = current->next->next;
	current->next = NULL;
	current = next;
	previous = NULL;
	while (current != NULL)
	{
		next = current->next;
		current->next = previous;
		previous = current;
		current = next;
	}
	sec_head = previous;
	while (*head != NULL)
	{
		if ((*head)->n == sec_head->n)
		{
			*head = (*head)->next;
			sec_head = sec_head->next;
		}
		else
			return (0);
	}
	return (1);
}
