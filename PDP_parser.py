file_path = r'<FULL PATH TO YOUR RACKET FILE>'
file = open(file_path,'r')
functions = []
comments = []
contracts = []
incorrect_count = 0


def function_parse(func_comments, items_boolean):

    for comm in func_comments:
        if comm.find('GIVEN') > 0 and not items_boolean[0]:
            items_boolean[0] = True
        if comm.find('RETURNS') > 0 and not items_boolean [1]:
            items_boolean[1] = True
        if comm.find('EXAMPLE') > 0 and not items_boolean[2]:
            items_boolean[2] = True
        if comm.find('STRATEGY') > 0 and not items_boolean[3]:
            items_boolean[3] = True
    return items_boolean


for line in file:
    if line.find('(provide') >= 0:
        while line.find(')') == -1:
            line = file.readline()
            if line.find(')') >= 0:
                break
            if line.find(';') >= 0:
                print(line.lstrip().rstrip() + " IS COMMENTED IN PROVIDE !!!")
                continue
            functions.append(line.lstrip().rstrip())
        str1 = line.lstrip()
        functions.append(str1.replace(')', '').rstrip())
        break
print("Total functions provided =", functions.__len__())

functions = []

for line in file:
    if (line.find('->') >= 0) and (line.find('-fn') < 0):
        con_str = line.split(':')
        contracts.append(con_str[0].replace(';; ', '').rstrip().lstrip())
    if line.find('(define (') >= 0:
        if line.find('-fn') >= 0:
            continue
        defined_func = line.split()
        functions.append(defined_func[1].replace('(', ''))

file.seek(0)

for func_name in functions:
    if not (func_name in contracts):
        incorrect_count += 1
        print('{0} function is missing contract (or a typo) !!!, '
              'please check the rest of it\'s recipe too'.format(func_name))

for line in file:
    for func_name in functions:
            if line.find(';; '+func_name+' :') >= 0:
                while line.find('(define') == -1:
                    comments.append(line.rstrip())
                    line = file.readline()
                items_boolean = [False, False, False, False]
                items_boolean = function_parse(comments, items_boolean)
                comments = []
                not_defined = []
                if not items_boolean[0]:
                    not_defined.append('GIVEN')
                if not items_boolean[1]:
                    not_defined.append('RETURNS')
                if not items_boolean[2]:
                    not_defined.append('EXAMPLE')
                if not items_boolean[3]:
                    not_defined.append('STRATEGY')
                if not_defined.__len__() != 0:
                    incorrect_count += 1
                    print('\"{0}\" missing statements -> {1}'.format(func_name, not_defined))

if incorrect_count == 0:
    print('all functions are following the recipe correctly !!!!')