# iconmeta2json

This script can generate search terms for CSS Icon Frameworks that follow the Font Awesome structure/

The purpose of this script was to generate metadata that can be uses for seraching icons in non Font Awesome Icon Projects like [Line Awesome](https://github.com/icons8/line-awesome)

This script depends on [requests](https://github.com/psf/requests) to download fresh [Font Awesome metadata](https://raw.githubusercontent.com/FortAwesome/Font-Awesome/master/metadata/icons.json) if none can be found locally.

It also includes the flit branch of [tinycss2 from Kozea](https://github.com/Kozea/tinycss2/tree/flit). I decided to do this because of the better documentation I found there.

## Usage

Simply execute this module with your Python 3 interpreter and add all CSS files you want to add to your search term index file:

For example:

```bash
python3 -m iconmeta2json ./lineawesome.css ./forkawesome.css
```

The output will look different from the original Icons.json file because my focus was searching, if you think I missed something important feel free to open an Issue.

**Note:** This script has only been tested with [Line Awesome](https://github.com/icons8/line-awesome) and [Fork Awesome](https://github.com/ForkAwesome/Fork-Awesome). If you want to use it with a different framework it might need some adjustments (see `IDENT_FILTER` in `__main__.py`). Also feel free to share those adjustments so everyone can benefit from serachable non Font Awesome Icons!