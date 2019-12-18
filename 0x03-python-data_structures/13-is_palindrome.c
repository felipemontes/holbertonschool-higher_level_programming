#include "lists.h"
/**
 * is_palindrome - function to check if a list is palindrome
 * @head: start of the list
 * Return: 0 if it is not a palindrome, 1 if it is a palindrome
 */
int is_palindrome(listint_t **head)
{
	listint_t *node1 = *head;
	listint_t *last_node = *head;
	listint_t *tmp = *head;
	int i = 0;
	int ct;

	if (!head && !*head)
		return (1);
	while (node1 != NULL)
	{
		node1 = node1->next;
		i++;
	}
	while (i--)
	{
		ct = 0;
		last_node = *head;
		while (last_node != NULL)
		{
			if (ct == i)
				break;
			ct++;
			last_node = last_node->next;
		}
		if (last_node->n != tmp->n)
			return (0);
		tmp = tmp->next;
	}
	return (1);
}
