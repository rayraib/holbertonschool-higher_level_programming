#include "lists.h"
int compare_list(listint_t *sec_head, listint_t **head);
listint_t *reverse_list(listint_t **head, listint_t *current);
listint_t *split_list(listint_t **head, int len);
int get_length(listint_t **head);
/**
* is_palindrome - Checks if a singly linked list is a palindrome
* @head: Double pointer to the first node of the singly linked list
* Return: 1 if palindrome, 0 if not a palindrome
*/

int is_palindrome(listint_t **head)
{
	listint_t *current, *sec_head;
	int length;

	if (head == NULL || *head == NULL || (*head)->next == NULL)
		return (1);
	length = get_length(&(*head));
	current = split_list(&(*head), length);
	sec_head = reverse_list(&(*head), current);
	return (compare_list(sec_head, &(*head)));
}
/**
* get_length - Calculate length of a singly linked list
* @head: Double pointer to initial node of a singly linked list
* Return: Length of the linked list
*/
int get_length(listint_t **head)
{
	int length;
	listint_t *tmp;

	tmp = *head;
	for (length = 0; tmp->next != NULL; length++)
		tmp = tmp->next;
	return (length);
}
/**
* split_list - Finds the mid index of singly linked list
* @head: Double pointer to initial node of a singly linked list
* @len: Length of the linked list
* Return: Address of the mid idx of the list
*/
listint_t *split_list(listint_t **head, int len)
{
	int mid_pt, i;
	listint_t *current;

	mid_pt = len / 2;
	current = *head;
	for (i = 0; i <= mid_pt; i++)
		current = current->next;
	return (current);
}
/**
* reverse_list - reverses a singly linked list
* @head: Double pointer to initial node of a singly linked list
* @current: Pointer to the initial node in a list to be reversed
* Return: Pointer to the initial node of the reversed linked list
*/
listint_t *reverse_list(listint_t **head, listint_t *current)
{
	listint_t *next, *previous, *sec_head;

	(void) head;
	next = previous = NULL;
	next = current->next;
	current->next = NULL;
	current = next;
	while (current != NULL)
	{
		next = current->next;
		current->next = previous;
		previous = current;
		current = next;
	}
	sec_head = previous;
	return (sec_head);
}
/**
* compare_list - Compares two linked list to check if they are palindrome
* @sec_head: Pointer to the head of the first list to compare
* @head: Double pointer to the headnode of the second list to compare
* Return: 1 if palindrome, 0 otherwise
*/
int compare_list(listint_t *sec_head, listint_t **head)
{
	while (sec_head != NULL)
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
