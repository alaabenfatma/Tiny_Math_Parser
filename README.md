# Tiny_Math_Parser
A 99-lines math expressions parser made from scratch. No package has been used.

## Usage

### Pre-conditions
This parser does not support variables.
The elements of the expression have to be seperated by a whitespace.

### Execution
You can feed the expression into the parser by passing it as an argument the moment of the execution of the script.

Sample:

```
python parser.py '5 + ( 1 + 2 * 1 )'
```
_output:_ 8.0

### Methodology

I did use the *recursive descent* method that is widely used for it being one of the most optimal ways of evaluating nested mathematical expressions.

The script is an implementation of the following grammar:

```
parse -> low_priority_terms_trigger

low_priority_terms_trigger -> high_prio_terms_trigger low_priority_terms

low_priority_terms -> + high_prio_terms_trigger low_priority_terms
    | - high_prio_terms_trigger low_priority_terms
    | epsilon

high_prio_terms_trigger -> FACTOR high_priority_terms

high_priority_terms -> * FACTOR high_priority_terms | 
    / FACTOR high_priority_terms | epsilon

FACTOR -> x | (parse)
```
