/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   test_wrong_input.c                                 :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: dboyer <dboyer@student.42.fr>              +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2019/11/19 15:22:06 by dboyer            #+#    #+#             */
/*   Updated: 2019/11/22 17:28:42 by dboyer           ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "get_next_line.h"
#include <stdio.h>

int		main(int ac, char **av)
{
	char	*line;
	int 	i;

	(void)ac;
	i = 0;
	line = "\0";
	printf("%d", get_next_line(atoi(av[1]), &line));
	return (0);
}
