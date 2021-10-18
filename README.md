# Summary

 Members                        | Descriptions                                
--------------------------------|---------------------------------------------
`namespace `[`FormalLangPractice1task13`](#namespaceFormalLangPractice1task13) | Python Library to solve homework: 'Formal Languages, Practice 1, task 13'.
`namespace `[`FormalLangPractice1task13::dump`](#namespaceFormalLangPractice1task13_1_1dump) | 
`namespace `[`FormalLangPractice1task13::nfa`](#namespaceFormalLangPractice1task13_1_1nfa) | Python Library to solve homework: 'Formal Languages, Practice 1, task 13'.

# namespace `FormalLangPractice1task13` 

Python Library to solve homework: 'Formal Languages, Practice 1, task 13'.

## Summary

 Members                        | Descriptions                                
--------------------------------|---------------------------------------------
`public def `[`solve`](#namespaceFormalLangPractice1task13_1a98803c3026e9b391bfb50f8b984deff7)`(istream,ostream)`            | Solution for the task Корректность: воспользуемся тем, что любая регулярка задаёт НКА.

## Members

#### `public def `[`solve`](#namespaceFormalLangPractice1task13_1a98803c3026e9b391bfb50f8b984deff7)`(istream,ostream)` 

Solution for the task Корректность: воспользуемся тем, что любая регулярка задаёт НКА.

А значит если подслово может быть прочитано НКА, то оно принадлежит установленному языку. Более точно, переберем все подстроки данной нам строки и попытаемся их прочитать, длина наибольшей прочитанной строки будет ответом. Верность построения НКА доказывается самим алгоритмом построения.

# namespace `FormalLangPractice1task13::dump` 

## Summary

 Members                        | Descriptions                                
--------------------------------|---------------------------------------------
`public def `[`__dump_stack__`](#namespaceFormalLangPractice1task13_1_1dump_1acc1a8e78078dde929a37b6d6535c5563)`(nfa,filename)`            | 
`public def `[`__print__`](#namespaceFormalLangPractice1task13_1_1dump_1ac7997ed8b833e1fbd2d7631c70cb9032)`(nfa)`            | 
`public def `[`__print_brief__`](#namespaceFormalLangPractice1task13_1_1dump_1a5d8bf0ad59557c62aabb22f21ef39017)`(node)`            | 
`public def `[`__print_node__`](#namespaceFormalLangPractice1task13_1_1dump_1a129f222ba493ae164ae721f5974d7d31)`(node)`            | 
`private def `[`_tree_remove`](#namespaceFormalLangPractice1task13_1_1dump_1a5ba975f792a466a1124874bcc01d52d2)`(str top)`            | Removes all files in the current directory.
`public def `[`get_transitions_size`](#namespaceFormalLangPractice1task13_1_1dump_1afb8c29eac02bfcda391bbb3f4b60c251)`(node)`            | 
`public def `[`make_new_state`](#namespaceFormalLangPractice1task13_1_1dump_1a590bbd4db11eab36b8ad441dfb6feb3c)`(num)`            | 

## Members

#### `public def `[`__dump_stack__`](#namespaceFormalLangPractice1task13_1_1dump_1acc1a8e78078dde929a37b6d6535c5563)`(nfa,filename)` 

#### `public def `[`__print__`](#namespaceFormalLangPractice1task13_1_1dump_1ac7997ed8b833e1fbd2d7631c70cb9032)`(nfa)` 

#### `public def `[`__print_brief__`](#namespaceFormalLangPractice1task13_1_1dump_1a5d8bf0ad59557c62aabb22f21ef39017)`(node)` 

#### `public def `[`__print_node__`](#namespaceFormalLangPractice1task13_1_1dump_1a129f222ba493ae164ae721f5974d7d31)`(node)` 

#### `private def `[`_tree_remove`](#namespaceFormalLangPractice1task13_1_1dump_1a5ba975f792a466a1124874bcc01d52d2)`(str top)` 

Removes all files in the current directory.

#### Parameters
* `top` Name of initial directory.

#### `public def `[`get_transitions_size`](#namespaceFormalLangPractice1task13_1_1dump_1afb8c29eac02bfcda391bbb3f4b60c251)`(node)` 

#### `public def `[`make_new_state`](#namespaceFormalLangPractice1task13_1_1dump_1a590bbd4db11eab36b8ad441dfb6feb3c)`(num)` 

# namespace `FormalLangPractice1task13::nfa` 

Python Library to solve homework: 'Formal Languages, Practice 1, task 13'.

## Summary

 Members                        | Descriptions                                
--------------------------------|---------------------------------------------
`private list `[`_get_ways`](#namespaceFormalLangPractice1task13_1_1nfa_1a72d7acfb55cee262f711b476ccc62a21)`(`[`_Node`](#classFormalLangPractice1task13_1_1nfa_1_1__Node)` state,str letter)`            | Returns a list of states that can be entered by a given letter.
`private bool `[`_is_letter`](#namespaceFormalLangPractice1task13_1_1nfa_1a79b03dc91927f5d8a7a7b578a3693f4f)`(str symbol)`            | Checks for the presence of a character in the alphabet.
`private bool `[`_is_way_to`](#namespaceFormalLangPractice1task13_1_1nfa_1a3515f301665012841b004380bd49e2ea)`(`[`_Node`](#classFormalLangPractice1task13_1_1nfa_1_1__Node)` state,str letter)`            | Checks for the presence letter in possible transitions.
`class `[`FormalLangPractice1task13::nfa::_CreateNFA`](#classFormalLangPractice1task13_1_1nfa_1_1__CreateNFA) | Functor for creating [NFA](#classFormalLangPractice1task13_1_1nfa_1_1NFA).
`class `[`FormalLangPractice1task13::nfa::_Node`](#classFormalLangPractice1task13_1_1nfa_1_1__Node) | Section: Working with states of [NFA](#classFormalLangPractice1task13_1_1nfa_1_1NFA).
`class `[`FormalLangPractice1task13::nfa::NFA`](#classFormalLangPractice1task13_1_1nfa_1_1NFA) | Section: Working with [NFA](#classFormalLangPractice1task13_1_1nfa_1_1NFA).

## Members

#### `private list `[`_get_ways`](#namespaceFormalLangPractice1task13_1_1nfa_1a72d7acfb55cee262f711b476ccc62a21)`(`[`_Node`](#classFormalLangPractice1task13_1_1nfa_1_1__Node)` state,str letter)` 

Returns a list of states that can be entered by a given letter.

#### Parameters
* `state` state of [NFA](#classFormalLangPractice1task13_1_1nfa_1_1NFA)

* `letter` letter from preset alphabet 

#### Returns
list list of states that can be entered by a given letter

#### `private bool `[`_is_letter`](#namespaceFormalLangPractice1task13_1_1nfa_1a79b03dc91927f5d8a7a7b578a3693f4f)`(str symbol)` 

Checks for the presence of a character in the alphabet.

#### Parameters
* `symbol` user-supplied character 

#### Returns
True if symbol in alphabet 

#### Returns
False if symbol not in alphabet

#### `private bool `[`_is_way_to`](#namespaceFormalLangPractice1task13_1_1nfa_1a3515f301665012841b004380bd49e2ea)`(`[`_Node`](#classFormalLangPractice1task13_1_1nfa_1_1__Node)` state,str letter)` 

Checks for the presence letter in possible transitions.

#### Parameters
* `state` state of [NFA](#classFormalLangPractice1task13_1_1nfa_1_1NFA)

* `letter` letter from preset alphabet 

#### Returns
True if ways exist 

#### Returns
False if ways don't exist

# class `FormalLangPractice1task13::nfa::_CreateNFA` 

Functor for creating [NFA](#classFormalLangPractice1task13_1_1nfa_1_1NFA).

## Summary

 Members                        | Descriptions                                
--------------------------------|---------------------------------------------
`public  `[`nodes`](#classFormalLangPractice1task13_1_1nfa_1_1__CreateNFA_1a6da5270e48c8b5c2f0dbaa008af4df76) | 
`public  `[`stack`](#classFormalLangPractice1task13_1_1nfa_1_1__CreateNFA_1a37d7c639a3adefa88200027e9f78ba3f) | 
`public def `[`__init__`](#classFormalLangPractice1task13_1_1nfa_1_1__CreateNFA_1a62d114c8017936187a4b318c581e0bb3)`(self,reg_exp)` | 
`public def `[`reg_concatenation`](#classFormalLangPractice1task13_1_1nfa_1_1__CreateNFA_1a5c3712c31bdf8318bd4b732d4e99014b)`(self)` | Regex concatenation This method takes the last two elements in stack and concatenates.
`public def `[`reg_iteration`](#classFormalLangPractice1task13_1_1nfa_1_1__CreateNFA_1a377c78827ef6e6c6bfa1e88c880b6882)`(self)` | Regex iteration This method takes the last element and applies the Kleene star.
`public def `[`reg_or`](#classFormalLangPractice1task13_1_1nfa_1_1__CreateNFA_1a57eb512c08bd3207c3a41667f054dc65)`(self)` | boolean 'or' for regular expressions This method takes the last two elements in stack and forks them into one block with the help of two additional states.

## Members

#### `public  `[`nodes`](#classFormalLangPractice1task13_1_1nfa_1_1__CreateNFA_1a6da5270e48c8b5c2f0dbaa008af4df76) 

#### `public  `[`stack`](#classFormalLangPractice1task13_1_1nfa_1_1__CreateNFA_1a37d7c639a3adefa88200027e9f78ba3f) 

#### `public def `[`__init__`](#classFormalLangPractice1task13_1_1nfa_1_1__CreateNFA_1a62d114c8017936187a4b318c581e0bb3)`(self,reg_exp)` 

#### `public def `[`reg_concatenation`](#classFormalLangPractice1task13_1_1nfa_1_1__CreateNFA_1a5c3712c31bdf8318bd4b732d4e99014b)`(self)` 

Regex concatenation This method takes the last two elements in stack and concatenates.

#### `public def `[`reg_iteration`](#classFormalLangPractice1task13_1_1nfa_1_1__CreateNFA_1a377c78827ef6e6c6bfa1e88c880b6882)`(self)` 

Regex iteration This method takes the last element and applies the Kleene star.

#### `public def `[`reg_or`](#classFormalLangPractice1task13_1_1nfa_1_1__CreateNFA_1a57eb512c08bd3207c3a41667f054dc65)`(self)` 

boolean 'or' for regular expressions This method takes the last two elements in stack and forks them into one block with the help of two additional states.

# class `FormalLangPractice1task13::nfa::_Node` 

Section: Working with states of [NFA](#classFormalLangPractice1task13_1_1nfa_1_1NFA).

Node - state of NKA

## Summary

 Members                        | Descriptions                                
--------------------------------|---------------------------------------------
`public  `[`final`](#classFormalLangPractice1task13_1_1nfa_1_1__Node_1a46a85338742bf5c446ee7a462d658889) | 
`public def `[`__init__`](#classFormalLangPractice1task13_1_1nfa_1_1__Node_1ae8d7d57832bfb87f45bdc9b6e8bfc030)`(self,`[`transitions`](#classFormalLangPractice1task13_1_1nfa_1_1__Node_1a2594171e7c2a90ab61e43e1bc68adaf7)`,`[`final`](#classFormalLangPractice1task13_1_1nfa_1_1__Node_1af28a838c358ed1f4ae4ebd0b702ea078)`)` | 

## Members

#### `public  `[`final`](#classFormalLangPractice1task13_1_1nfa_1_1__Node_1a46a85338742bf5c446ee7a462d658889) 

#### `public def `[`__init__`](#classFormalLangPractice1task13_1_1nfa_1_1__Node_1ae8d7d57832bfb87f45bdc9b6e8bfc030)`(self,`[`transitions`](#classFormalLangPractice1task13_1_1nfa_1_1__Node_1a2594171e7c2a90ab61e43e1bc68adaf7)`,`[`final`](#classFormalLangPractice1task13_1_1nfa_1_1__Node_1af28a838c358ed1f4ae4ebd0b702ea078)`)` 

# class `FormalLangPractice1task13::nfa::NFA` 

Section: Working with [NFA](#classFormalLangPractice1task13_1_1nfa_1_1NFA).

Nondeterministic finite automaton It consists of a list of states, in which, inside each state, all possible transitions to other states are stored, allowed by a regular expression specified by the user in reverse Polish notation.

## Summary

 Members                        | Descriptions                                
--------------------------------|---------------------------------------------
`public  `[`nodes`](#classFormalLangPractice1task13_1_1nfa_1_1NFA_1a6da5270e48c8b5c2f0dbaa008af4df76) | 
`public  `[`state`](#classFormalLangPractice1task13_1_1nfa_1_1NFA_1adc6e5733fc3c22f0a7b2914188c49c90) | 
`public def `[`__init__`](#classFormalLangPractice1task13_1_1nfa_1_1NFA_1a1be0698cef9313432d31dd5028cd7654)`(self,str reg_exp)` | Initialize method from a regExp in reverse Polish notation.
`public bool `[`read`](#classFormalLangPractice1task13_1_1nfa_1_1NFA_1a42f933055dd9fadc2a95f6f3484dc096)`(self,str string)` | Answers the question whether the string can be read by the [NFA](#classFormalLangPractice1task13_1_1nfa_1_1NFA) This method uses the breadth-first search algorithm.

## Members

#### `public  `[`nodes`](#classFormalLangPractice1task13_1_1nfa_1_1NFA_1a6da5270e48c8b5c2f0dbaa008af4df76) 

#### `public  `[`state`](#classFormalLangPractice1task13_1_1nfa_1_1NFA_1adc6e5733fc3c22f0a7b2914188c49c90) 

#### `public def `[`__init__`](#classFormalLangPractice1task13_1_1nfa_1_1NFA_1a1be0698cef9313432d31dd5028cd7654)`(self,str reg_exp)` 

Initialize method from a regExp in reverse Polish notation.

#### Parameters
* `reg_exp` regular expression given in reverse Polish notation

#### `public bool `[`read`](#classFormalLangPractice1task13_1_1nfa_1_1NFA_1a42f933055dd9fadc2a95f6f3484dc096)`(self,str string)` 

Answers the question whether the string can be read by the [NFA](#classFormalLangPractice1task13_1_1nfa_1_1NFA) This method uses the breadth-first search algorithm.

#### Parameters
* `string` the string passed by the user 

#### Returns
True if the string can be read by an automaton 

#### Returns
False if the string can't be read by an automaton

Generated by [Moxygen](https://sourcey.com/moxygen)