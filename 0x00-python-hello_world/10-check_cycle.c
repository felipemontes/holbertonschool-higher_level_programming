#include "lists.h"
/**
 * check_cycle - checks if there is a loop in the nodes
 * @list: head
 * Return: 1 if there is a cycle or 0 if there is no cycle
 */
int check_cycle(listint_t *list)
{
	listint_t *slow = list;
	listint_t *fast = list;

	if (list == NULL)
		return (0);
	fast = fast->next;
	while (fast->next != NULL && slow != NULL)
	{
		if (fast == slow)
		{
			return (1);
		}
		fast = fast->next->next;
		slow = slow->next;
	}
	return (0);
}
