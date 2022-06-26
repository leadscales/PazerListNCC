import requests
import argparse
from src.parser import parser
from src.format import format

argparse_example = """
Example:
    python main.py -l pazer -o pazer.txt
"""

argparser = argparse.ArgumentParser(description="A tool to convert d3fc0n6's lists to valid NCC playerlists.", epilog=argparse_example)
argparser.add_argument("-l", "--list", help="The list to convert.", choices=["bot", "cheater", "tacobot", "pazer"], required=True)
argparser.add_argument("-o", "--output", help="The output file.", default="output.txt")
args = argparser.parse_args()

def main(list = args.list, output = args.output):
    url = parser.LISTS[list]
    response = requests.get(url)
    if response.status_code == 200:
        if list == "bot":
            ids = parser.parse_bot_list(response.text)
        elif list == "pazer":
            ids = parser.parse_pazer_list(response.text)
        else:
            ids = response.text.splitlines()
        formatted = format.format_ncc_list(ids)
        with open(output, "w") as f:
            f.write("\n".join(formatted))
    else:
        print(f"Error: {response.status_code}")

if __name__ == "__main__":
    try: 
        main()
    except KeyboardInterrupt:
        print("\nExiting...")
        exit()
    except Exception as e:
        print(e)
        exit()