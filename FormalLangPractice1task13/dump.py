##
# @file dump.py
#
# @brief auxiliary module for uploading information about NFA
#
# @section description_main Description
# Collects a textual description of the state of the automaton
# in '/logs' and takes snapshots of the state of the machine, puts them to '/snapshots'
#
# @section libraries_main Libraries/Modules
# - graphviz - module for visualisation
# - os - module for communication with the system

# @section author Author(s)
# - Created by Andrey Krotov on 17/10/2021
# - Modified by Andrey Krotov on 18/10/2021
#
# Copyright (c) 2021 Andrey Krotov. All rights reserved.

# Imports
import graphviz
import os
import logging
import inspect
import os.path

dot = graphviz.Digraph(format='png', comment='dump of NFA')
dump_file = None

states = dict()


def make_new_state(num):
    if num not in states:
        states[num] = 'q' + str(len(states))
    return states[num]


def __print_brief__(node):
    dump_file.write("\t\t\tNode id: " + make_new_state(node) + ", is final: " + str(node.final) + '\n')


def get_transitions_size(node):
    sz = 0
    for nodes in node.transitions:
        sz += len(node.transitions[nodes])
    return sz


def __print_node__(node):
    dump_file.write("Node id: " + make_new_state(node) + ", is final: " + str(node.final) + ', ')
    dump_file.write("Count of transitions: " + str(get_transitions_size(node)) + '\n')
    if get_transitions_size(node) > 0:
        for key in node.transitions:
            for _node_ in node.transitions[key]:
                dump_file.write("\t\tby: " + str(key) + " to: \n")
                # dot.node(str(id(node)))
                # dot.node(str(id(_node_)))
                dot.edge(make_new_state(node), make_new_state(_node_), label=key)
                __print_brief__(_node_)
    dump_file.write("\t\tIt's all transitions...\n")


def __print__(nfa):
    dump_file.write("||******************************************************************************||\n")
    dump_file.write(
        "\tNFA id: " + str(id(nfa)) + ", initial: " + make_new_state(nfa.initial) + ", final: " + make_new_state(
            nfa.final) + '\n')
    dump_file.write("\tCount of Nodes: " + str(len(nfa.nodes)) + '\n')
    for node in nfa.nodes:
        if node == nfa.initial:
            dot.node(make_new_state(node), style='filled', color='lightgrey')
        if node == nfa.final:
            dot.node(make_new_state(node), shape='doublecircle')
        dump_file.write("\n\tDumping ")
        __print_node__(node)
    dump_file.write("||******************************************************************************||\n\n")


def _tree_remove(top: str):
    """! Removes all files in the current directory.
    @param top Name of initial directory.
    """
    for root, dirs, files in os.walk(top, topdown=False):
        for name in files:
            os.remove(os.path.join(root, name))
        for name in dirs:
            os.rmdir(os.path.join(root, name))


def __dump_stack__(nfa, filename):
    global dump_file
    if os.path.isfile('./logs' + filename):
        _tree_remove('./logs')
    if not os.path.isdir('./logs'):
        os.mkdir('./logs')
    os.chdir('./logs')
    dump_file = open(filename, 'w')
    dump_file.write("Dumping started...\n")
    dump_file.write("Dumping NFA...\n")
    __print__(nfa)
    os.chdir('..')
    if os.path.isdir('./snapshots/' + filename):
        _tree_remove('./snapshots')
    if not os.path.isdir('./snapshots'):
        os.mkdir('./snapshots')
    os.chdir('./snapshots')

    if not os.path.isdir('./' + filename):
        os.mkdir('./' + filename)
    else:
        _tree_remove('./' + filename)
        os.rmdir('./' + filename)
        os.mkdir('./' + filename)
    os.chdir('./' + filename)
    dot.render('./' + filename)
    dot.clear()
    os.chdir('..')
    os.chdir('..')
    dump_file.close()
