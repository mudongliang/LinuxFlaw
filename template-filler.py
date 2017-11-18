#!/usr/local/bin/python3


import os
from shutil import copy

def create_file():
    cve = input("Insert CVE number: \n")
    exp_env = input("Experiment Environment (OS, etc.): \n")
    config = input("Install and configuration (link): \n")
    problems_config = input("Problems in Installation and Configuration: \n")
    trigger= input("How to trigger the vulnerability? (e.g. trigger method) \n")
    poc = input("Insert the PoC here or press enter to add file \n")
    if (poc==""):
        poc_file = input("Insert path to PoC file, if it exists (e.g. /usr/local/poc): \n")
    vuln_details = input("Vulnerability details and patch: \n")
    root_cause = input("Root cause: \n")
    stack_trace = input("Stack trace: \n")
    references = input("References: \n")

    if not os.path.exists("./"+cve):
        os.makedirs("./"+cve)
    f= open("./"+cve+"/README.md","w+")
    f.write("#CVE/EDB ID\n")
    f.write(cve+"\n")
    f.write("##Experiment Environment\n")
    f.write(exp_env+"\n")
    f.write("##INSTALL and Configuration\n")
    f.write(config+"\n")
    f.write("##Problems in Installation and Configuration\n")
    f.write(problems_config+"\n")
    f.write("##How to trigger vulnerability\n")
    f.write(trigger+"\n")
    if poc!="":
        f.write("##PoC\n")
        f.write(poc+"\n")
    else:
        f.write("##PoC\n")
        f.write("In folder\n")
        copy(poc_file,"./"+cve+"/")        
    f.write("##Vulnerability Details and Patch\n")
    f.write(vuln_details+"\n")
    f.write("##Root Cause\n")
    f.write(root_cause+"\n")
    f.write("##Stack Trace\n")
    f.write(stack_trace+"\n")
    f.write("##References\n")
    f.write(references)


def main():
    create_file()

if __name__ == "__main__": main()
