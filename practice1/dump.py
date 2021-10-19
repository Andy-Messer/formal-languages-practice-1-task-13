"""! @brief module - Dump utility of NFA. """

##
# @file dump.py
#
# @brief auxiliary module for uploading debugrmation about NFA
#
# @section description_main Description
# Collects a textual description of the state of the automaton
# in '/logs' and takes snapshots of the state of the machine, puts them to '/snapshots'
#
# @section libraries_main Libraries/Modules
# - graphviz - module for visualisation
# - os - module for communication with the system
# - logging - module for logging
#
# @section author Author(s)
# - Created by Andrey Krotov on 17/10/2021
# - Modified by Andrey Krotov on 18/10/2021
#
# Copyright (c) 2021 Andrey Krotov. All rights reserved.

# Imports
import graphviz
import os
import logging

# New digraph for NFA visualization
logging.debug('creating digraph variable...')
dot = graphviz.Digraph(format='png', comment='dump of NFA')

# File where NFA will be dumped
dump_file = None

# Dictionary of nodes id and their names.
states = dict()


def make_new_state(node) -> str:
    """! Generate new name for id(node) in format: f'q + {id}'
    @param node: node
    @return name: new name of node
    """
    id_node = id(node)
    logging.debug('making new name for id of Node')
    if id_node not in states:
        states[id_node] = 'q' + str(len(states))
        logging.debug(f'new name created! {id_node} - {states[id_node]}')
    logging.debug(f'Exiting, return value: {states[id_node]}')
    return states[id_node]


def __print_brief__(node):
    """! Print a summary of the NFA node

    Short output format: 'node.name node.final'
    @param node: node the debugrmation about which should be output
    """
    logging.debug(f'printing brief debugrmation about node {id(node)}')
    dump_file.write("\t\t\tNode id: " + make_new_state(node) + ", is final: " + str(node.final) + '\n')


def __get_transitions_count(node):
    """! Counts the number of possible transitions
    @param node: node that number of transitions is being searched for
    @return count: number of transitions
    """
    logging.debug(f'Starting count transitions {id(node)}')
    count = 0
    for nodes in node.transitions:
        count += len(node.transitions[nodes])

    logging.debug(f"Transitions counted (exiting), returned value: {count}")
    return count


def __print_node__(node):
    """! Printing node of NFA

    Output the name of the node, its final and a list of neighbors with their number
    @param node: printing node
    """
    logging.debug(f'dump main debugrmation about the node {id(node)}')
    dump_file.write("Node id: " + make_new_state(node) + ", is final: " + str(node.final) + ', ')
    dump_file.write("Count of transitions: " + str(__get_transitions_count(node)) + '\n')

    logging.debug('dump all transitions about last node')
    if __get_transitions_count(node) > 0:
        for key in node.transitions:
            for _node_ in node.transitions[key]:
                dump_file.write("\t\tby: " + str(key) + " to: \n")
                dot.edge(make_new_state(node), make_new_state(_node_), label=key)
                __print_brief__(_node_)

    dump_file.write("\t\tIt's all transitions...\n")
    logging.debug('end of dump last node')


def __print__(nfa):
    """! Dump NFA

    Make notes about nodes and their connections
    @param nfa: nondeterministic finite automaton that need to be print
    """
    logging.debug(f'Dump main debugrmation about NFA {nfa}')
    dump_file.write("||******************************************************************************||\n")
    dump_file.write(
        "\tNFA id: " + str(id(nfa)) + ", initial: " + make_new_state(nfa.initial) + ", final: " + make_new_state(
            nfa.final) + '\n')
    dump_file.write("\tCount of Nodes: " + str(len(nfa.nodes)) + '\n')

    logging.debug(f'Dump all nodes')
    for node in nfa.nodes:
        if node == nfa.initial:
            dot.node(make_new_state(node), style='filled', color='lightgrey')
        if node == nfa.final:
            dot.node(make_new_state(node), shape='doublecircle')
        dump_file.write("\n\tDump ")
        __print_node__(node)

    logging.debug('End of dump NFA')
    dump_file.write("||******************************************************************************||\n\n")


def _tree_remove(top: str):
    """! Removes all files in the current directory.
    @param top Name of initial directory.
    """
    logging.debug(f'remove files and dirs in {top}')
    for root, dirs, files in os.walk(top, topdown=False):
        for name in files:
            os.remove(os.path.join(root, name))
        for name in dirs:
            os.rmdir(os.path.join(root, name))
    logging.debug('removing completed')


def __dump__(nfa, filename):
    """! Dump the information about NFA
    @param nfa: NFA
    @param filename: output file
    """
    logging.debug('Starting dump process...')
    global dump_file

    logging.debug('Creating logs dir')
    if os.path.isfile('./logs' + filename):
        _tree_remove('./logs')
    if not os.path.isdir('./logs'):
        os.mkdir('./logs')

    logging.debug('chdir to logs')
    os.chdir('./logs')

    logging.debug('Dump started...')
    dump_file = open(filename, 'w')
    dump_file.write("Dump started...\n")
    dump_file.write("Dump NFA...\n")
    __print__(nfa)
    dump_file.write('Map of Names:\n')
    for key in states:
        dump_file.write(str(key) + ' - ' + str(states[key]) + '\n')

    logging.debug('Dump process ended, exiting from logs')
    os.chdir('..')

    logging.debug('Creating snapshots dir')
    if os.path.isdir('./snapshots/' + filename):
        _tree_remove('./snapshots')
    if not os.path.isdir('./snapshots'):
        os.mkdir('./snapshots')

    os.chdir('./snapshots')
    logging.debug('chdir to snapshots')

    logging.debug(f'Creating {filename} dir')
    if not os.path.isdir('./' + filename):
        os.mkdir('./' + filename)
    else:
        _tree_remove('./' + filename)
        os.rmdir('./' + filename)
        os.mkdir('./' + filename)

    logging.debug(f'chdir to {filename}')
    os.chdir('./' + filename)

    dot.render('./' + filename)
    dot.clear()

    os.chdir('..')
    os.chdir('..')
    logging.debug('exiting to root')

    logging.debug('Dump fully ended')
    dump_file.close()
