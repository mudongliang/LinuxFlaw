#! python

#sys.path.append('~/Dev/LinuxFlaw/')


import os
from shutil import copy
import openpyxl

def create_file(cv, ex, cf, prb, tr, po, vd, ro, st, ref, file_flag):
    cve = cv
    exp_env = ex
    config = cf
    problems_config = prb
    trigger= tr
    poc = po
    vuln_details = vd
    root_cause = ro
    stack_trace = st
    references = ref

    if not os.path.exists("./"+cve):
        os.makedirs("./"+cve)
    f= open("./"+cve+"/README.md","w+")
    f.write("# CVE/EDB ID\n")
    f.write(cve+"\n")
    f.write("## Experiment Environment\n")
    f.write(exp_env+"\n")
    f.write("## INSTALL and Configuration\n")
    f.write(config+"\n")
    f.write("## Problems in Installation and Configuration\n")
    f.write(problems_config+"\n")
    f.write("## How to trigger vulnerability\n")
    f.write(trigger+"\n")
    if file_flag==False:
        f.write("## PoC\n")
        f.write(poc+"\n")
    else:
        f.write("## PoC\n")
        f.write("In folder\n")
        copy(poc,"./"+cve+"/")
    f.write("## Vulnerability Details and Patch\n")
    f.write(vuln_details+"\n")
    f.write("## Root Cause\n")
    f.write(root_cause+"\n")
    f.write("## Stack Trace\n")
    f.write(stack_trace+"\n")
    f.write("## References\n")
    f.write(references)



def create_file_scratch():
    cve = input("Insert CVE number: \n")
    exp_env = input("Experiment Environment (OS, etc.): \n")
    config = input("Install and configuration (link): \n")
    problems_config = input("Problems in Installation and Configuration: \n")
    trigger= input("How to trigger the vulnerability? (e.g. trigger method) \n")
    poc = input("Insert the PoC here or press enter to add file \n")
    if (poc==""):
        poc_flag = True
        poc = input("Insert path to PoC file, if it exists (e.g. /usr/local/poc): \n")
    vuln_details = input("Vulnerability details and patch: \n")
    root_cause = input("Root cause: \n")
    stack_trace = input("Stack trace: \n")
    references = input("References: \n")

    create_file(cve, exp_env, config, problems_config, trigger,
     poc, vuln_details, root_cause, stack_trace, references, poc_flag)



def create_from_excel():

    ## Default Values
    exp_env= "Ubuntu 14.04"
    problems_config="n/a"
    vuln_details="n/a"
    root_cause="n/a"
    poc_flag=True


    wb = openpyxl.load_workbook('table.xlsx')
    sheet = wb.get_sheet_by_name('Sheet1')
    for row in range(2, sheet.max_row + 1):
        print("Name and Version\n")
        print (sheet['A' + str(row)].value)
        print (sheet['B' + str(row)].value)
        print (sheet['C' + str(row)].value)
        print("\n")
        cve = sheet['C' + str(row)].value
        poc="../files/"+ sheet['F'+str(row)].value
        references=sheet['H'+str(row)].value

        config = input("Install and configuration (link): \n")
        problems_config = input("Problems in Installation and Configuration: \n")
        trigger= input("How to trigger the vulnerability? (e.g. trigger method) \n")
        stack_trace = input("Stack trace: \n")

        print(cve+","+exp_env+","+config+","+problems_config+","+
        trigger+","+poc+","+vuln_details+","+root_cause+","+
        stack_trace+""+references)

        okay = input("Are these details good?(T/F)\n")
        if okay =="T":
            create_file(cve, exp_env, config, problems_config, trigger,
            poc, vuln_details, root_cause, stack_trace, references, poc_flag)
        else:
            continue
