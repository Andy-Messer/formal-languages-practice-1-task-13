"""! @brief module - Implementation of NFA. """

##
# @file nfa.py
#
# @brief A module for building nondeterministic finite automaton
#
# @section description_main Description
# Building an automaton based on a regular expression written in reverse Polish notation.
# With some additional functionality to solve the problem.
#
# @section libraries_main Libraries/Modules
# - dump - module makes it possible
# - logging - module
# - os - module
# - json - module
# to unload information about nondeterministic finite automaton to a file

# @section author Author(s)
# - Created by Andrey Krotov on 17/10/2021
# - Modified by Andrey Krotov on 17/10/2021
#
# Copyright (c) 2021 Andrey Krotov. All rights reserved.

# Imports
from os import path, remove
from practice1.dump import __dump__
import json
import logging.config

# Logging, setup config file
if path.isfile("./logs/logs.log"):
    remove("./logs/logs.log")
with open("./practice1/logging_configuration.json", 'r') as logging_configuration_file:
    config_dict = json.load(logging_configuration_file)

logging.config.dictConfig(config_dict)

# Constants
__alphabet_of_letters = ['a', 'b', 'c']


def _is_letter(symbol: str) -> bool:
    """! Checks for the presence of a character in the alphabet.
    @param symbol user-supplied character
    @return True if symbol in alphabet
    @return False if symbol not in alphabet
    """
    logging.debug(f'Check for the letter in alphabet: %s', symbol)
    if symbol in __alphabet_of_letters:
        logging.debug(f"It's letter from alphabet!")
        return True
    logging.debug(f"It isn't letter from alphabet(")
    return False


#####################################
# Section: Working with states of NFA
##########
class _Node:
    """! Node - state of NKA """
    # Dictionary of transitions, where you can go by adding
    # a letter to your word - a key from the dictionary
    transitions = dict()
    # Label that indicates whether the automaton terminates when it enters this state
    final = False

    def __init__(self, transitions=None, final=False):
        logging.debug('Node initialization...')
        self.transitions = transitions
        self.final = final
        logging.debug('Node initialization completed.')


def _is_way_to(state: _Node, letter: str) -> bool:
    """! Checks for the presence letter in possible transitions
    @param state state of NFA
    @param letter letter from preset alphabet
    @return True if ways exist
    @return False if ways don't exist
    """
    if letter in state.transitions:
        if len(state.transitions[letter]) > 0:
            return True
    return False


def _get_ways(state: _Node, letter: str) -> list:
    """! Returns a list of states that can be entered by a given letter
    @param state state of NFA
    @param letter letter from preset alphabet
    @return list list of states that can be entered by a given letter
    """
    if letter in state.transitions:
        return state.transitions[letter]
    return []


#####################################
# Section: Working with NFA
##########
class NFA:
    """! Nondeterministic finite automaton
     It consists of a list of states, in which, inside each state,
     all possible transitions to other states are stored, allowed by
     a regular expression specified by the user in reverse Polish notation.
    """

    # The starting state of nondeterministic finite automaton
    initial = _Node()
    # List of states of nondeterministic finite automaton
    nodes = []
    # The final state of nondeterministic finite automaton
    final = _Node()

    def __init__(self, reg_exp: str = None):
        """! Initialize method from a regExp in reverse Polish notation
        @param reg_exp: regular expression given in reverse Polish notation
        """
        # To hide unnecessary functionality, we will use an additional class
        new_nfa = _CreateNFA(reg_exp).nfa

        # Initialization
        self.initial = new_nfa.initial
        self.nodes = new_nfa.nodes
        self.final = new_nfa.final
        self.state = self.initial

    def _make_dump(self):
        """! Take a snapshot of a nondeterministic finite automaton using the dump library """
        __dump__(self, filename='dump.log')

    def read(self, string: str) -> bool:
        """! Answers the question whether the string can be read by the NFA
        This method uses the breadth-first search algorithm
        @param string the string passed by the user
        @return True if the string can be read by an automaton
        @return False if the string can't be read by an automaton
        """
        # Putting the starting state in the queue
        index = 0
        q = [[self.initial, index]]
        while len(q) > 0:
            # Take out the current state
            state = q[0][0]
            ind = q[0][1]
            q.pop(0)
            # Processing eps transitions
            for next_state in _get_ways(state, 'eps'):
                q.append([next_state, ind])
            if ind < len(string):
                # Put in the queue all states reachable by a given letter
                if _is_way_to(state, string[ind]):
                    for next_state in _get_ways(state, string[ind]):
                        q.append([next_state, ind + 1])
            elif state.final:
                return True
        return False


#####################################
# Section: Creating NFA
##########
class _CreateNFA:
    """! Functor for creating NFA """

    #################################
    # Section: Architecture of NFA
    ##########
    # The starting state of nondeterministic finite automaton
    initial = _Node()
    # List of states of nondeterministic finite automaton
    nodes = []
    # The final state of nondeterministic finite automaton
    final = _Node()
    ########

    # Created NFA
    nfa = None

    # Log info
    logger = logging.getLogger(__name__)

    #################################
    # Section:    Working with stack,
    #         reverse polish notation
    #                      processing
    ##########
    # Stack for processing input
    stack = []

    def reg_concatenation(self):
        """! Regex concatenation
        This method takes the last two elements in stack and concatenates.
        """
        try:
            first_nfa, second_nfa = self.stack[-2], self.stack[-1]
            self.stack.pop(), self.stack.pop()

            # Supplementing the automaton with vertices from the second automaton
            first_nfa.final.final = False
            first_nfa.nodes += second_nfa.nodes

            # Throw 'eps' the transition between the end of the first and the beginning of the second
            if "eps" not in first_nfa.final.transitions:
                first_nfa.final.transitions.setdefault("eps", [])
            first_nfa.final.transitions['eps'].append(second_nfa.initial)

            first_nfa.final = second_nfa.final

            self.stack.append(first_nfa)
        except IndexError as e:
            self.logger.error(e)
            raise e

    def reg_iteration(self):
        """! Regex iteration
        This method takes the last element and applies the Kleene star
        """
        # Throw 'eps' the transition between the end of the first and the beginning of the first
        if "eps" not in self.stack[-1].final.transitions:
            self.stack[-1].final.transitions.setdefault("eps", [])
        self.stack[-1].final.transitions["eps"].append(self.stack[-1].initial)
        # we replace the end of the automaton
        self.stack[-1].final.final = False
        self.stack[-1].final = self.stack[-1].initial
        self.stack[-1].final.final = True

    def reg_or(self):
        """! boolean 'or' for regular expressions
        This method takes the last two elements in stack and forks them into one block
        with the help of two additional states.
        """

        first_nfa, second_nfa = self.stack[-2], self.stack[-1]
        self.stack.pop(), self.stack.pop()

        new_nfa = _CreateNFA()

        first_nfa.final.final = False
        second_nfa.final.final = False

        # Epsilon transitions collecting a new automaton
        if "eps" not in new_nfa.final.transitions:
            new_nfa.final.transitions.setdefault("eps", [])
        if "eps" not in new_nfa.initial.transitions:
            new_nfa.initial.transitions.setdefault("eps", [])
        if "eps" not in first_nfa.final.transitions:
            first_nfa.final.transitions.setdefault("eps", [])
        if "eps" not in second_nfa.initial.transitions:
            second_nfa.final.transitions.setdefault("eps", [])

        new_nfa.initial.transitions["eps"].append(first_nfa.initial)
        new_nfa.initial.transitions["eps"].append(second_nfa.initial)

        first_nfa.final.transitions["eps"].append(new_nfa.final)
        second_nfa.final.transitions["eps"].append(new_nfa.final)

        new_nfa.initial = new_nfa.initial
        new_nfa.final = new_nfa.final
        new_nfa.nodes += first_nfa.nodes
        new_nfa.nodes += second_nfa.nodes
        self.stack.append(new_nfa)

    def __init__(self, reg_exp=None):
        """! Constructing NFA instance """
        if reg_exp is not None:
            logging.info("Constructing NFA from regExpr")
            logging.info("Initialize some basic variables")
            self.initial = _Node()
            self.nodes = []
            self.final = _Node()
            self.nfa = None
            self.stack = []
            logging.info("Trying to parse regExpr")
            try:
                logging.info("Parse regExpr letter by letter")
                for i in range(len(reg_exp)):
                    if _is_letter(reg_exp[i]):
                        logging.info("Creating some basic NFA for one letter")
                        new_nfa = _CreateNFA()
                        if reg_exp[i] not in new_nfa.initial.transitions:
                            new_nfa.initial.transitions.setdefault(reg_exp[i], [])
                        new_nfa.initial.transitions[reg_exp[i]].append(new_nfa.final)
                        self.stack.append(new_nfa)
                        logging.info("Created.")
                    elif reg_exp[i] == '.':
                        self.reg_concatenation()
                    elif reg_exp[i] == '*':
                        self.reg_iteration()
                    elif reg_exp[i] == '+':
                        self.reg_or()
                    elif reg_exp[i] == ' ':
                        pass
                    else:
                        raise ValueError(f'No such operation or letter: {reg_exp[i]}')
                self.nfa = self.stack[-1]
                logging.info("NFA Constructed.")
            except ValueError as e:
                self.logger.error(e)
                raise e
        else:
            self.nodes = [_Node(dict()), _Node(dict(), final=True)]
            self.initial = self.nodes[0]
            self.final = self.nodes[1]
