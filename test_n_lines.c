/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   test_n_lines.c                                     :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: dboyer <dboyer@student.42.fr>              +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2019/11/19 15:22:06 by dboyer            #+#    #+#             */
/*   Updated: 2019/11/22 15:02:06 by dboyer           ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "get_next_line.h"
#include <stdio.h>

int		main(int ac, char **av)
{
	char	*line;
	int		fd;
	int 	i;

	i = 0;
	line = "\0";
	fd = ac > 1 ? open(av[1], O_RDONLY) : 0;
	while (get_next_line(fd, &line) > 0)
	{
		i++;
		free(line);
	}
	printf("%d", i);
	close(fd);
	return (0);
}
