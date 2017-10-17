FUNCTIONALITY:

1. Displays the count of functions in 'provide' section
2. Alerts when it sees a comment in provide section
3. Alerts when the recipe is not followed for functions

REQUIREMENTS: 

1. The provided functions should be mentioned in new lines in the following format:

(provide
 function-1
 function-2
 ...)

2. The definition of functions should be in one line in the following format:

(define (funtion-1 ...)
 ...)

EXAMPLES:

1. Total functions provided = 7
"lexer-token" missing statements -> ['GIVEN', 'RETURNS', 'EXAMPLE']

2. ;;lexer-token IS COMMENTED IN PROVIDE !!!
Total functions provided = 6
all functions are following the recipe correctly !!!!

3. Total functions provided = 7
all functions are following the recipe correctly !!!!


