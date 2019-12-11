#include "lists.h"
/**
 * insert_node - function that inserts a node
 * @head: head of the list
 * @number: number to be inserted
 * Return: the address of the new node, or NULL if it failed
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *newnode = malloc(sizeof(listint_t));
	listint_t *tmp = *head;
	listint_t *tmp2;

	if (newnode == NULL)
		return (NULL);
	if (*head ==  NULL)
	{
		newnode->next = *head;
		*head = newnode;
	}
	else
	{
		while (tmp->next != NULL)
		{
			if (tmp->n > number)
			{
				tmp2->next = newnode;
				newnode->n = number;
				newnode->next = tmp;
				return (newnode);
			}
			tmp2 = tmp;
			tmp = tmp->next;
		}
	}
	return (NULL);
}
