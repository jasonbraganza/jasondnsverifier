"""
Problem to solve: 

Take a list of domains (one per line) from a text file as input, find the IP address for the domain using the standard system level DNS, and then check against DoH answers from both cloudflare and google. and say if all answers match properly or not.

"""
import socket
import sys

import requests


def main():
    list_of_sites = get_list_of_sites()
    compare_list_with_providers(list_of_sites)


def get_list_of_sites():
    try:
        if sys.argv[1]:
            with open(f"{sys.argv[1]}") as list_to_process:
                site_list = [each_site.strip().lower() for each_site in list_to_process]
                return site_list
    except:
        print("Please give a text file of domains, one per line, to process.")


def compare_list_with_providers(some_list_to_process):
    for site in some_list_to_process:
        ip_local = local_lookup(site)
        ip_from_google = google_lookup(site)
        ip_from_cloudflare = cloudflare_lookup(site)
        if ip_local == ip_from_google and ip_local == ip_from_cloudflare:
            pass
        elif ip_local == ip_from_google and not ip_local == ip_from_cloudflare:
            print(
                f"{site}: Local dns lookup matches with Google, but not Cloudflare.\n"
            )
        elif ip_local == ip_from_cloudflare and not ip_local == ip_from_google:
            print(
                f"{site}: Local dns lookup matches with Cloudflare, but not Google.\n"
            )
        else:
            print(
                f"{site}: Local dns lookup does not match with either Google or Cloudflare.\n"
            )


def local_lookup(some_site):
    site_ip = socket.gethostbyname(some_site).strip()
    return site_ip


def google_lookup(some_site):
    google_lookup = requests.get(f"https://dns.google/resolve?name={some_site}")
    site_ip = google_lookup.json()["Answer"][0]["data"].strip()
    return site_ip


def cloudflare_lookup(some_site):
    cloudflare_url = f"https://cloudflare-dns.com/dns-query?name={some_site}&type=A&ct=application/dns-json"
    cloudflare_lookup = requests.get(cloudflare_url)
    site_ip = cloudflare_lookup.json()["Answer"][0]["data"].strip()
    return site_ip


if __name__ == "__main__":
    main()
