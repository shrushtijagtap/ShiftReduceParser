import pandas as pd

def parse(productions, input_str):
    stack = ""
    output_stack={}
    stack_actions={}
    input_string={}
    inp_counter=0
    out_counter=0
    act_counter=0

    l = []
    for p in productions:
        s = p[1]
        if s.find("|"):
            p[1] = p[1].split("|")
            for i in p[1]:
                l.append([p[0], i])
        else:
            l.append([p[0], p[1]])

    print("Modified Grammar is: ")
    print(l)

    n = len(l) #number of productions after string modification

    input_string[inp_counter]=input_str
    inp_counter=inp_counter+1
    output_stack[out_counter]=" "
    out_counter=out_counter+1
    stack_actions[act_counter]='Initialization'
    act_counter=act_counter+1

    loc = 0
    while loc < len(input_str):
        t1 = input_str.index(' ', loc)

        #append input string 
        str = input_str[t1:]
        input_string[inp_counter]=str
        inp_counter=inp_counter+1
        input_string[inp_counter]=str
        inp_counter=inp_counter+1

        temp = input_str[loc:t1]
        #append to stack
        output_stack[out_counter]=stack + temp
        out_counter=out_counter+1
        #append to action
        stack_actions[act_counter]='Shift'
        act_counter=act_counter+1

        loc = input_str.index(' ', loc) + 1
        for i in range(0, n):
            if temp == l[i][1]:
                temp = l[i][0]
                #append to action
                stack_actions[act_counter]='Reduce'
                act_counter=act_counter+1
                break

        stack = stack + temp
        #append to stack
        output_stack[out_counter]=stack
        out_counter=out_counter+1
        
        for i in range(0, n):
            if stack == l[i][1].strip():
                stack = l[i][0]
                #append to action
                stack_actions[act_counter]='Reduce'
                act_counter=act_counter+1
                break


    if stack == l[0][0]:
        stack_actions[act_counter]='Reduce'
        output_stack[out_counter]=l[0][0]
        output = 'Input String Accepted'
        print(output)
    else:
        output = 'Input String Rejected'
        print(output)

    final_dict={}
    final_dict['Stack']=output_stack
    final_dict['Input String']=input_string
    final_dict['Action']=stack_actions
    print(final_dict)

    df=pd.DataFrame.from_dict(final_dict)

    return output,df

#print(parse([['E', 'E+E'], ['E','a']], 'a + a '))