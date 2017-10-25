FUNCTIONALITY:

1. Displays the total count of functions in 'provide' section
2. Alerts when it sees a comment in provide section
3. Alerts when the recipe is not followed for functions
4. Alerts when the contract is missed for functions 
   (NOTE:- you will need check the recipe again after adding contract)

REQUIREMENTS: 

1. Code is written in 'Python', you will need to have it installed

2. You need to provide the filename in script ('file_path' variable):

file_path = r'<FULL PATH TO YOUR RACKET FILE>'
 
3. The provided functions should be mentioned in new lines in the following format:

(provide
 function-1
 function-2
 ...)

4. The definition of functions should be in one line in the following format:

(define (funtion-1 ...)
 ...)

5. Contracts in the below format are detected:

<func_name> : (...)

OR

<func_name> :
(...)

Else will prompt an error for the given fuction with the line number of its definition

EXAMPLES:

1. Total functions provided = 7
"lexer-token" missing statements -> ['GIVEN', 'RETURNS', 'EXAMPLE']

2. ;;lexer-token IS COMMENTED IN PROVIDE !!!
Total functions provided = 6
all functions are following the recipe correctly !!!!

3. Total functions provided = 18
Function 'initial-test' defined at line '1466' has an incorrect syntax or missing contract !!!, please check the rest of it's recipe too

4. Total functions provided = 7
all functions are following the recipe correctly !!!!
