# Summary

 Members                        | Descriptions                                
--------------------------------|---------------------------------------------
`namespace `[`practice1`](#namespacepractice1) | Python Library - Solve for homework: 'Formal Languages, Practice 1, task 13'.
`namespace `[`practice1::dump`](#namespacepractice1_1_1dump) | module - Dump utility of NFA.
`namespace `[`practice1::nfa`](#namespacepractice1_1_1nfa) | module - Implementation of [NFA](#classpractice1_1_1nfa_1_1NFA).

# namespace `practice1` 

Python Library - Solve for homework: 'Formal Languages, Practice 1, task 13'.

## Summary

 Members                        | Descriptions                                
--------------------------------|---------------------------------------------
`public def `[`solve`](#namespacepractice1_1a4f1e2327621575169836b24fad1c4cc0)`(istream,ostream)`            | Solution for the task.

## Members

#### `public def `[`solve`](#namespacepractice1_1a4f1e2327621575169836b24fad1c4cc0)`(istream,ostream)` 

Solution for the task.

Корректность: воспользуемся тем, что любая регулярка задаёт НКА. А значит если подслово может быть прочитано НКА, то оно принадлежит установленному языку. Более точно, переберем все подстроки данной нам строки и попытаемся их прочитать, длина наибольшей прочитанной строки будет ответом. Верность построения НКА доказывается самим алгоритмом построения.

# namespace `practice1::dump` 

module - Dump utility of NFA.

## Summary

 Members                        | Descriptions                                
--------------------------------|---------------------------------------------
`public def `[`__dump__`](#namespacepractice1_1_1dump_1ad9f715f29da831aa7643c91af5ebe458)`(nfa,filename)`            | Dump the information about NFA.
`private def `[`__get_transitions_count`](#namespacepractice1_1_1dump_1a48a26379315f5034651c9f7bb9bb4fe5)`(node)`            | Counts the number of possible transitions.
`public def `[`__print__`](#namespacepractice1_1_1dump_1ab26a8f699adf1b51bbb17f5d6b0f5286)`(nfa)`            | Dump NFA.
`public def `[`__print_brief__`](#namespacepractice1_1_1dump_1ae6922a078c8fb18193cfe597b9590312)`(node)`            | Print a summary of the NFA node.
`public def `[`__print_node__`](#namespacepractice1_1_1dump_1ade4c74aabe15dae245a2b47484ca9612)`(node)`            | Printing node of NFA.
`private def `[`_tree_remove`](#namespacepractice1_1_1dump_1a99dcf84e0b8fa8cb8f8c888ffc8f198f)`(str top)`            | Removes all files in the current directory.
`public str `[`make_new_state`](#namespacepractice1_1_1dump_1a8d3277da1b00286352f693cdb9c011a0)`(node)`            | Generate new name for id(node) in format: f'q + {id}'.

## Members

#### `public def `[`__dump__`](#namespacepractice1_1_1dump_1ad9f715f29da831aa7643c91af5ebe458)`(nfa,filename)` 

Dump the information about NFA.

#### Parameters
* `nfa` NFA 

* `filename` output file

#### `private def `[`__get_transitions_count`](#namespacepractice1_1_1dump_1a48a26379315f5034651c9f7bb9bb4fe5)`(node)` 

Counts the number of possible transitions.

#### Parameters
* `node` node that number of transitions is being searched for 

#### Returns
count: number of transitions

#### `public def `[`__print__`](#namespacepractice1_1_1dump_1ab26a8f699adf1b51bbb17f5d6b0f5286)`(nfa)` 

Dump NFA.

Make notes about nodes and their connections 
#### Parameters
* `nfa` nondeterministic finite automaton that need to be print

#### `public def `[`__print_brief__`](#namespacepractice1_1_1dump_1ae6922a078c8fb18193cfe597b9590312)`(node)` 

Print a summary of the NFA node.

Short output format: 'node.name node.final' 
#### Parameters
* `node` node the debugrmation about which should be output

#### `public def `[`__print_node__`](#namespacepractice1_1_1dump_1ade4c74aabe15dae245a2b47484ca9612)`(node)` 

Printing node of NFA.

Output the name of the node, its final and a list of neighbors with their number 
#### Parameters
* `node` printing node

#### `private def `[`_tree_remove`](#namespacepractice1_1_1dump_1a99dcf84e0b8fa8cb8f8c888ffc8f198f)`(str top)` 

Removes all files in the current directory.

#### Parameters
* `top` Name of initial directory.

#### `public str `[`make_new_state`](#namespacepractice1_1_1dump_1a8d3277da1b00286352f693cdb9c011a0)`(node)` 

Generate new name for id(node) in format: f'q + {id}'.

#### Parameters
* `node` node 

#### Returns
name: new name of node

# namespace `practice1::nfa` 

module - Implementation of [NFA](#classpractice1_1_1nfa_1_1NFA).

## Summary

 Members                        | Descriptions                                
--------------------------------|---------------------------------------------
`private list `[`_get_ways`](#namespacepractice1_1_1nfa_1a4d9a2e5db8da6340541e17cde0bc5680)`(`[`_Node`](#classpractice1_1_1nfa_1_1__Node)` state,str letter)`            | Returns a list of states that can be entered by a given letter.
`private bool `[`_is_letter`](#namespacepractice1_1_1nfa_1a12e43040f4837c23c481fc929939fed5)`(str symbol)`            | Checks for the presence of a character in the alphabet.
`private bool `[`_is_way_to`](#namespacepractice1_1_1nfa_1a44b82383fce3d09db5a6b4ee9e553c6b)`(`[`_Node`](#classpractice1_1_1nfa_1_1__Node)` state,str letter)`            | Checks for the presence letter in possible transitions.
`class `[`practice1::nfa::_CreateNFA`](#classpractice1_1_1nfa_1_1__CreateNFA) | Functor for creating [NFA](#classpractice1_1_1nfa_1_1NFA).
`class `[`practice1::nfa::_Node`](#classpractice1_1_1nfa_1_1__Node) | Section: Working with states of [NFA](#classpractice1_1_1nfa_1_1NFA).
`class `[`practice1::nfa::NFA`](#classpractice1_1_1nfa_1_1NFA) | Section: Working with [NFA](#classpractice1_1_1nfa_1_1NFA).

## Members

#### `private list `[`_get_ways`](#namespacepractice1_1_1nfa_1a4d9a2e5db8da6340541e17cde0bc5680)`(`[`_Node`](#classpractice1_1_1nfa_1_1__Node)` state,str letter)` 

Returns a list of states that can be entered by a given letter.

#### Parameters
* `state` state of [NFA](#classpractice1_1_1nfa_1_1NFA)

* `letter` letter from preset alphabet 

#### Returns
list list of states that can be entered by a given letter

#### `private bool `[`_is_letter`](#namespacepractice1_1_1nfa_1a12e43040f4837c23c481fc929939fed5)`(str symbol)` 

Checks for the presence of a character in the alphabet.

#### Parameters
* `symbol` user-supplied character 

#### Returns
True if symbol in alphabet 

#### Returns
False if symbol not in alphabet

#### `private bool `[`_is_way_to`](#namespacepractice1_1_1nfa_1a44b82383fce3d09db5a6b4ee9e553c6b)`(`[`_Node`](#classpractice1_1_1nfa_1_1__Node)` state,str letter)` 

Checks for the presence letter in possible transitions.

#### Parameters
* `state` state of [NFA](#classpractice1_1_1nfa_1_1NFA)

* `letter` letter from preset alphabet 

#### Returns
True if ways exist 

#### Returns
False if ways don't exist

# class `practice1::nfa::_CreateNFA` 

Functor for creating [NFA](#classpractice1_1_1nfa_1_1NFA).

## Summary

 Members                        | Descriptions                                
--------------------------------|---------------------------------------------
`public  `[`nodes`](#classpractice1_1_1nfa_1_1__CreateNFA_1a6da5270e48c8b5c2f0dbaa008af4df76) | 
`public  `[`stack`](#classpractice1_1_1nfa_1_1__CreateNFA_1a37d7c639a3adefa88200027e9f78ba3f) | 
`public def `[`__init__`](#classpractice1_1_1nfa_1_1__CreateNFA_1a62d114c8017936187a4b318c581e0bb3)`(self,reg_exp)` | 
`public def `[`reg_concatenation`](#classpractice1_1_1nfa_1_1__CreateNFA_1a5c3712c31bdf8318bd4b732d4e99014b)`(self)` | Regex concatenation This method takes the last two elements in stack and concatenates.
`public def `[`reg_iteration`](#classpractice1_1_1nfa_1_1__CreateNFA_1a377c78827ef6e6c6bfa1e88c880b6882)`(self)` | Regex iteration This method takes the last element and applies the Kleene star.
`public def `[`reg_or`](#classpractice1_1_1nfa_1_1__CreateNFA_1a57eb512c08bd3207c3a41667f054dc65)`(self)` | boolean 'or' for regular expressions This method takes the last two elements in stack and forks them into one block with the help of two additional states.

## Members

#### `public  `[`nodes`](#classpractice1_1_1nfa_1_1__CreateNFA_1a6da5270e48c8b5c2f0dbaa008af4df76) 

#### `public  `[`stack`](#classpractice1_1_1nfa_1_1__CreateNFA_1a37d7c639a3adefa88200027e9f78ba3f) 

#### `public def `[`__init__`](#classpractice1_1_1nfa_1_1__CreateNFA_1a62d114c8017936187a4b318c581e0bb3)`(self,reg_exp)` 

#### `public def `[`reg_concatenation`](#classpractice1_1_1nfa_1_1__CreateNFA_1a5c3712c31bdf8318bd4b732d4e99014b)`(self)` 

Regex concatenation This method takes the last two elements in stack and concatenates.

#### `public def `[`reg_iteration`](#classpractice1_1_1nfa_1_1__CreateNFA_1a377c78827ef6e6c6bfa1e88c880b6882)`(self)` 

Regex iteration This method takes the last element and applies the Kleene star.

#### `public def `[`reg_or`](#classpractice1_1_1nfa_1_1__CreateNFA_1a57eb512c08bd3207c3a41667f054dc65)`(self)` 

boolean 'or' for regular expressions This method takes the last two elements in stack and forks them into one block with the help of two additional states.

# class `practice1::nfa::_Node` 

Section: Working with states of [NFA](#classpractice1_1_1nfa_1_1NFA).

Node - state of NKA

## Summary

 Members                        | Descriptions                                
--------------------------------|---------------------------------------------
`public  `[`final`](#classpractice1_1_1nfa_1_1__Node_1a46a85338742bf5c446ee7a462d658889) | 
`public def `[`__init__`](#classpractice1_1_1nfa_1_1__Node_1ae8d7d57832bfb87f45bdc9b6e8bfc030)`(self,`[`transitions`](#classpractice1_1_1nfa_1_1__Node_1a2594171e7c2a90ab61e43e1bc68adaf7)`,`[`final`](#classpractice1_1_1nfa_1_1__Node_1af28a838c358ed1f4ae4ebd0b702ea078)`)` | 

## Members

#### `public  `[`final`](#classpractice1_1_1nfa_1_1__Node_1a46a85338742bf5c446ee7a462d658889) 

#### `public def `[`__init__`](#classpractice1_1_1nfa_1_1__Node_1ae8d7d57832bfb87f45bdc9b6e8bfc030)`(self,`[`transitions`](#classpractice1_1_1nfa_1_1__Node_1a2594171e7c2a90ab61e43e1bc68adaf7)`,`[`final`](#classpractice1_1_1nfa_1_1__Node_1af28a838c358ed1f4ae4ebd0b702ea078)`)` 

# class `practice1::nfa::NFA` 

Section: Working with [NFA](#classpractice1_1_1nfa_1_1NFA).

Nondeterministic finite automaton It consists of a list of states, in which, inside each state, all possible transitions to other states are stored, allowed by a regular expression specified by the user in reverse Polish notation.

## Summary

 Members                        | Descriptions                                
--------------------------------|---------------------------------------------
`public  `[`nodes`](#classpractice1_1_1nfa_1_1NFA_1a6da5270e48c8b5c2f0dbaa008af4df76) | 
`public  `[`state`](#classpractice1_1_1nfa_1_1NFA_1adc6e5733fc3c22f0a7b2914188c49c90) | 
`public def `[`__init__`](#classpractice1_1_1nfa_1_1NFA_1a1be0698cef9313432d31dd5028cd7654)`(self,str reg_exp)` | Initialize method from a regExp in reverse Polish notation.
`public bool `[`read`](#classpractice1_1_1nfa_1_1NFA_1a42f933055dd9fadc2a95f6f3484dc096)`(self,str string)` | Answers the question whether the string can be read by the [NFA](#classpractice1_1_1nfa_1_1NFA) This method uses the breadth-first search algorithm.

## Members

#### `public  `[`nodes`](#classpractice1_1_1nfa_1_1NFA_1a6da5270e48c8b5c2f0dbaa008af4df76) 

#### `public  `[`state`](#classpractice1_1_1nfa_1_1NFA_1adc6e5733fc3c22f0a7b2914188c49c90) 

#### `public def `[`__init__`](#classpractice1_1_1nfa_1_1NFA_1a1be0698cef9313432d31dd5028cd7654)`(self,str reg_exp)` 

Initialize method from a regExp in reverse Polish notation.

#### Parameters
* `reg_exp` regular expression given in reverse Polish notation

#### `public bool `[`read`](#classpractice1_1_1nfa_1_1NFA_1a42f933055dd9fadc2a95f6f3484dc096)`(self,str string)` 

Answers the question whether the string can be read by the [NFA](#classpractice1_1_1nfa_1_1NFA) This method uses the breadth-first search algorithm.

#### Parameters
* `string` the string passed by the user 

#### Returns
True if the string can be read by an automaton 

#### Returns
False if the string can't be read by an automaton

Generated by [Moxygen](https://sourcey.com/moxygen)