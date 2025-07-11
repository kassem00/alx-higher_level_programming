#include "lists.h"
#include <stdlib.h>

/**
 * insert_node - Inserts a number into a sorted singly linked list.
 * @head: A pointer to the head of the listint_t list.
 * @number: The integer to insert.
 *
 * Return: If the function fails - NULL.
 *         Otherwise - a pointer to the new node.
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new;
	listint_t *current;
	char flag;

	current = *head;

	new = malloc(sizeof(listint_t));
	if (new == NULL)
		return (NULL);

	new->n = number;
	new->next = NULL;

	if (*head == NULL)
		*head = new;
	else
	{
		while (current->next != NULL)
		{
			if (current->next->n >= number)
			{
				new->next = current->next;
				current->next = new;
				flag = 1;
				break;
			}
			current = current->next;
		}
		if (flag != 1)
			current->next = new;
	}

	return (new);
}