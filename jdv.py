"""
Problem to solve: 

Take a list of domains (one per line) from a text file as input, find the IP address for the domain using the standard system level DNS, and then check against DoH answers from both cloudflare and google. and say if all answers match properly or not.

"""
import socket
import sys

import requests


def main():
    list_of_sites = []
    get_list_of_sites()
    compare_list_with_providers(list_of_sites)


def get_list_of_sites():

    try:
        if sys.argv[1]:

            with open(f"{sys.argv[1]}") as list_to_process:
                for each_site in list_to_process:
                    # print(each_site)
                    list_of_sites.append(each_site)

    except:
        print("Please give a text file of domains, one per line, to process.")


def compare_list_with_providers(some_list_to_process):
    print(some_list_to_process)


if __name__ == "__main__":
    main()
