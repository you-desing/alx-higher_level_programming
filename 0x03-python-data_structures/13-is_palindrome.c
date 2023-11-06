#include <stdio.h>
#include <stdlib.h>
#include "lists.h"
/**
 * is_palindrome - function to call check_pal to see if list is palindrome
 * @head: ptr to the beginning of the list
 * Return: 0 if not palindrome else 1
 */
int is_palindrome(listint_t **head)
{
	listint_t *current = *head;
	listint_t *temp = NULL;
	listint_t *prev = NULL;

	if (*head == NULL || (*head)->next == NULL)
		return (1);
	while (current != NULL)
	{
		temp = current->next;
		current->next = prev;
		prev = current;
		current = temp;
	}
	while (prev != NULL && *head != NULL)
	{
		if (prev->n != (*head)->n)
			return (0);
		prev = prev->next;
		*head = (*head)->next;
	}
	return (1);
}
