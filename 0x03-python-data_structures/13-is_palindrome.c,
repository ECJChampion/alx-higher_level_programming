#include <stdio.h>
#include <stdlib.h>
#include "lists.h"

/**
 * is_palindrome - function in C that checks if a linked list is a palindrome
 * @head: pointer to the linked list
 * Return: 0 if it is not a palindrome, 1 if it is a palindrome
 */

int is_palindrome(listint_t **head)
{
	listint_t *p, *q, *prev = NULL;
	listint_t *slow, *fast;

	fast = *head;
	slow = *head;

	while (fast != NULL && fast->next != NULL)
	{
		fast = fast->next->next;
		p = slow;
		slow = slow->next;
		p->next = prev;
		prev = p;
	}
	if (fast != NULL)
	{
		slow = slow->next;
	}
	q = prev;

	while (q != NULL && slow != NULL)
	{
		if (q->n != slow->n)
			return (0);
		q = q->next;
		slow = slow->next;
	}
	return (1);
}
