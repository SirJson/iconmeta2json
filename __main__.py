import json
import argparse
import requests
from pprint import pformat
from typing import Dict, List
from pathlib import Path
import tinycss2
import tinycss2.ast
from metaparser import Icon, icons_from_dict
from tinycss2.ast import IdentToken, StringToken

SCRIPT_PATH = Path(__file__).absolute()
SCRIPT_HOME = Path('/'.join(SCRIPT_PATH.parts[:len(SCRIPT_PATH.parts) - 1]))
SEARCH_DATA = SCRIPT_HOME / "data/icons.fa.json"
FA_META_SRC = "https://raw.githubusercontent.com/FortAwesome/Font-Awesome/master/metadata/icons.json"

IDENT_FILTER = [
    "active",
    "focus",


    # Font Awesome specific
    "fa",
    "fa-lg",
    "fa-2x",
    "fa-3x",
    "fa-4x",
    "fa-5x",
    "fa-fw",
    "fa-ul",
    "fa-ul",
    "fa-li",
    "fa-li.fa-lg",
    "fa-border",
    "fa-pull-left",
    "fa-pull-right",
    "fa.fa-pull-left",
    "fa.fa-pull-right",
    "fa-flip-horizontal",
    "fa-flip-vertical",
    "fa-rotate-180",
    "fa-rotate-270",
    "fa-rotate-90"
    "fa.pull-left",
    "fa.pull-right",
    "fa-spin",
    "fa-pulse",
    "fa-stack",
    "fa-stack-1x",
    "fa-stack-2x",
    "fa-inverse",


    # Line Awesome specific
    "la",
    "la-lg",
    "la-1x",
    "la-2x",
    "la-3x",
    "la-4x",
    "la-5x",
    "la-6x",
    "la-7x",
    "la-8x",
    "la-9x",
    "la-10x",
    "la-fw",
    "la-ul",
    "la-li",
    "la-li.fa-lg",
    "la-border",
    "la-pull-left",
    "la-pull-right",
    "la.fa-pull-left",
    "la.fa-pull-right",
    "la-flip-horizontal",
    "la-flip-vertical",
    "la-rotate-180",
    "la-rotate-270",
    "la-rotate-90"
    "la.pull-left",
    "la.pull-right",
    "la-spin",
    "la-pulse",
    "la-stack",
    "la-stack-1x",
    "la-stack-2x",
    "la-inverse",
    "la-xs",
    "la-sm",
    "la-rotate-90",
    "la-flip-both",

    # v5 Modifier
    "fas",
    "fab",
    "far",
    "las",
    "lab",
    "lar",
    "lal",
    "lad",

    "root",
    "flip-both",
    "pull-right",
    "pull-left",
    "sr-only-focusable",
    "sr-only",
    "li"
]


def parse_icon_sheet(sheet: str) -> list:
    icons = []
    with open(sheet, 'r') as stylesheet:
        css = tinycss2.parse_stylesheet(
            stylesheet.read(), True, True)
        for rule in css:
            iconset = list(filter(lambda x: type(
                x) is IdentToken and x.value not in IDENT_FILTER, rule.prelude))
            if len(iconset) <= 0:
                continue

            unichar: List[str] = list(map(lambda y: y.value, filter(
                lambda x: type(x) is StringToken, rule.content)))
            if(len(unichar) <= 0):
                print(f'\t!! {pformat(iconset)} has no content')
                continue
            if unichar[0][0].isupper():
                continue
            icons.append({"name": iconset[0].value, "content": unichar[0]})
    return icons


def run():
    masterlist = []
    fa_meta: Dict[str, Icon] = {}
    fa_charmap: Dict[str, str] = {}
    output: Dict[str, dict] = {}
    parser = argparse.ArgumentParser(prog="iconmeta2json")
    parser.add_argument('css_sheet', nargs='+')
    args = parser.parse_args()

    if not SEARCH_DATA.exists():
        print("Downloading latest metadata from Font Awesome")
        response = requests.get(FA_META_SRC, allow_redirects=True)
        with open(SEARCH_DATA,"w") as newmeta:
            newmeta.write(response.content.decode('utf-8'))

    with open(SEARCH_DATA) as template:
        fa_meta = icons_from_dict(json.loads(template.read()))

    fa_transform = map(
        lambda kv: {'name': kv[0], 'content': kv[1].unicode}, fa_meta.items())

    for v in fa_transform:
        fa_charmap[chr(int(v['content'], base=16))] = v['name']

    for sheet in args.css_sheet:
        print("> Parsing " + sheet)
        masterlist.extend(list(map(lambda z: {'name': z['name'].replace(
            'fa-', '').replace('la-', ''), 'content': z['content']}, parse_icon_sheet(sheet))))

    for icon in masterlist:
        if icon['name'] in output.keys():
            # We already have an icon with the same name so we skip that
            continue
        if icon['name'] in fa_meta.keys():
            output[icon['name']] = {'character': icon['content'],
                                    'searchterms': fa_meta[icon['name']].search.terms}
        elif icon['content'] in fa_charmap.keys():
            output[icon['name']] = {'character': icon['content'],
                                    'searchterms': fa_meta[fa_charmap[icon['content']]].search.terms}
        else:
            print(" - No search terms defined for: " + icon['name'])
            output[icon['name']] = {
                'character': icon['content'], 'searchterms': []}
        if not icon['name'] in output[icon['name']]['searchterms']:
            output[icon['name']]['searchterms'].append(icon['name'])

    with open("icons.json", "w") as newindex:
        newindex.write(json.dumps(output, sort_keys=True, indent=4))

run()
