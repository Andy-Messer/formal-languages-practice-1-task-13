"""! @brief Python Library - Solve for homework: 'Formal Languages, Practice 1, task 13' """

##
# @mainpage Homework: 'Formal Languages, Practice 1, task 13'
#
# @section description_main Description
# Task: Даны α и слово u ∈ {a, b, c}∗ . Найти длину самого длинного подслова u, при-
# надлежащего L. Аргументами являются строка в алфавите {a, b, c, 1, ., +, ∗}.
# Предполагается, что первым компонентом входа является регулярное
# выражение α в обратной польской записи, задающее язык L.
#
# Copyright (c)2021 Andrey Krotov. All rights reserved.
__all__ = ['nfa', 'solve', 'dump']
__author__ = "Krotov Andrey <krotov.ai@phystech.edu>"
__version__ = "0.1"
__date__ = "18 October 2021"

import logging
import io
import sys

from practice1.nfa import NFA


def solve(istream=sys.stdin, ostream=sys.stdout):
    """! Solution for the task
    
     Корректность: воспользуемся тем, что любая регулярка задаёт НКА.
     А значит если подслово может быть прочитано НКА,
     то оно принадлежит установленному языку.
     Более точно, переберем все подстроки данной нам строки и попытаемся их прочитать,
     длина наибольшей прочитанной строки будет ответом.
     Верность построения НКА доказывается самим алгоритмом построения.
    """
    logging.info(f'Redirecting input and output streams')

    cp_stdin = sys.stdin
    cp_stout = sys.stdout
    if isinstance(istream, type(io.StringIO())):
        sys.stdin = istream
    if isinstance(ostream, type(io.StringIO())):
        sys.stdout = ostream
    logging.info(f'Done...')

    try:
        input_split = input().split()
        string = input_split[-1]
        reg = "".join(input_split[:len(input_split) - 1])
        logging.info(f'Submitted to the entrance: "{reg}", "{string}"')
        try:
            logging.info(f'Start building NFA...')
            try:
                nfa_global = NFA(reg)
            except IndexError as e:
                return e
            logging.debug(f'Dumping NFA... (to see dumpfile go to "./logs/dump.log" or "./snapshots"')
            nfa_global._make_dump()

            logging.info(f'Start solving the task.')
            ans = 0
            for i in range(len(string)):
                for j in range(i + 1, len(string) + 1):
                    logging.info(f'------------------------------------------------')

                    substring = string[i:j]
                    logging.info(f'"{substring}" has been passed to NFA for reading')

                    if nfa_global.read(substring):
                        logging.info(f'the Line was read!')

                        logging.info(f'Checking the length of substring')
                        if len(substring) > ans:
                            logging.info(f'New answer!!! {len(substring)}')

                        ans = max(len(substring), ans)

                        logging.info(f'Checked.')
                    else:
                        logging.info(f'the Line wasn\'t read')
            print(ans)
            if isinstance(istream, type(io.StringIO())):
                sys.stdin = cp_stdin
            if isinstance(ostream, type(io.StringIO())):
                sys.stdout = cp_stout

            logging.info('Exiting from "solve"')
            return ans

        except IndexError as e:
            logging.error('failed to build the NFA')
            raise IndexError

    except Exception as e:
        logging.error('Wrong input...')
        return e
