#include "lists.h"
/**
* insert_node - inserts a number into a sorted singly linked list
* @head: Pointer to a pointer to the singly linked list
* @number: number to be inserted
* Return: Address of the new node, or NULL if failure
*/
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *tmp, *prev_tmp, *new_node;

	tmp = *head;
	prev_tmp = NULL;
	if (head == NULL)
		return (NULL);
	new_node = malloc(sizeof(listint_t));
	if (new_node == NULL)
		return (NULL);
	new_node->n = number;
	if (tmp == NULL)
	{
		new_node->next = NULL;
		*head = new_node;
		return (new_node);
	}
	while (tmp != NULL && tmp->n < number)
	{
		prev_tmp = tmp;
		tmp = tmp->next;
	}
	if (tmp == NULL)
	{
		new_node->next = NULL;
		prev_tmp->next =  new_node;
		return (new_node);
	}
	else if (prev_tmp == NULL)
	{
		new_node->next = tmp;
		*head = new_node;
		return (new_node);
	}
	new_node->next = tmp;
	prev_tmp->next = new_node;
	return (new_node);
}
