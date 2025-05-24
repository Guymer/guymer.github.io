!["gmake" GitHub Action Status](https://github.com/Guymer/misc/actions/workflows/gmake.yaml/badge.svg) !["mypy" GitHub Action Status](https://github.com/Guymer/misc/actions/workflows/mypy.yaml/badge.svg) !["pylint" GitHub Action Status](https://github.com/Guymer/misc/actions/workflows/pylint.yaml/badge.svg) !["shellcheck" GitHub Action Status](https://github.com/Guymer/misc/actions/workflows/shellcheck.yaml/badge.svg)

This repository contains a few random little things that do not fit in anywhere else.

## Contents

* Configuration, Option & Settings Files
    * [my EditorConfig configuration](.editorconfig)
    * [my get_iplayer options](.get_iplayer/options)
    * [my Git configuration](.gitconfig)
    * [my GitHub funding](.github/FUNDING.yml)
    * [my SSH configuration](.ssh/config)
    * [my yt-dlp configuration](.config/yt-dlp/config)
* Run Control Files
    * [my BASH run control](.bashrc)
    * [my PyLint run control](.pylintrc)
    * [my ShellCheck run control](.shellcheckrc)
    * [my TCSH run control](.tcshrc)
    * [my Vim run control](.vimrc)
    * [my wget run control](.wgetrc)
    * [my ZSH run control](.zshrc)
* Git Files
    * [my Git ignore](.gitignore)
* BASH Scripts
    * [`commit` every Git repository](commit.sh)
    * [`diff` every Git repository](diff.sh)
    * [`pull` every Git repository](pull.sh)
    * [`push` every Git repository](push.sh)
    * [`update` every Git repository](update.sh)
    * [Print every Git branch](branch.sh)
    * [Print every Git remote](remote.sh)
    * [Print every insecure "http://" URL](grep.sh)
    * [Test every Python module](test.sh)
* Python Scripts
    * [Check that every function call within a module specifies all keyword arguments](checkAllKeywordArguments.py)
    * [Check functions calls for specific arguments](checkEverything.py)
    * [Check that every PyGuymer3 function call specifies all keyword arguments](checkPyGuymer3KeywordArguments.py)
    * [Check every README has links to its dependencies](check_READMEs.py)

## Dependencies

This collection requires the following Python modules to be installed and available in your `PYTHONPATH`.

* [pyguymer3](https://github.com/Guymer/PyGuymer3)
* [scipy](https://pypi.org/project/scipy/)
* [shapely](https://pypi.org/project/Shapely/)

## MatPlotLib Figure Sizes

The two "standard" 4K sizes are:

| Size | Aspect Ratio | Size Nickname | Aspect Ratio Nickname |
|---|---|---|---|
| 3,840 px × 2,160 px | 1.778…:1 = 16:9 = 4²:3² | 4K UHD | Wide Screen |
| 4,096 px × 2,160 px | 1.896…:1 | 4K DCI |  |

There is a third "standard" 4K-ish size with a height of 2,160 px:

| Size | Aspect Ratio | Size Nickname | Aspect Ratio Nickname |
|---|---|---|---|
| 5,120 px × 2,160 px | 2.370…:1 = 64∶27 = 4³:3³ | 5K Ultrawide | Ultrawide Screen |

Finally, there are four more "honourable mention" 4K-ish sizes with heights of 2,160 px (just because I like the idea of 4:3, followed by 4²:3², followed by 4³:3³, etc ...):

| Size | Aspect Ratio | Size Nickname | Aspect Ratio Nickname |
|---|---|---|---|
| 2,880 px × 2,160 px | 1.333…:1 = 4:3 |  | Full Screen |
| 3,240 px × 2,160 px | 1.5:1 = 3:2 |  | 35 mm Film |
| 3,456 px × 2,160 px | 1.6:1 = 16:10 |  |  |
| ~3,495 px × 2,160 px | 1.618…:1 |  | Golden Ratio |

These seven 4K-ish sizes equate to:

| Size (at 300 px/inch) | Aspect Ratio | Size Nickname | Aspect Ratio Nickname |
|---|---|---|---|
|  9.6    inches × 7.2 inches | 1.333…:1 = 4:3 |  | Full Screen |
| 10.8    inches × 7.2 inches | 1.5:1 = 3:2 |  | 35 mm Film |
| 11.52   inches × 7.2 inches | 1.6:1 = 16:10 |  |  |
| 11.650… inches × 7.2 inches | 1.618…:1 |  | Golden Ratio |
| 12.8    inches × 7.2 inches | 1.778…:1 = 16:9 = 4²:3² | 4K UHD | Wide Screen |
| 13.653… inches × 7.2 inches | 1.896…:1 | 4K DCI |  |
| 17.066… inches × 7.2 inches | 2.370…:1 = 64∶27 = 4³:3³ | 5K Ultrawide | Ultrawide Screen |

Given the recurring decimals in three of the seven 4K-ish sizes above, then I choose my personal 4K-ish MatPlotLib sizes (up to 4³:3³) to be:

| Size (at 300 px/inch) | Size | Aspect Ratio | Size Nickname | Aspect Ratio Nickname |
|---|---|---|---|---|
|  0.8 inches × 7.2 inches |   240 px × 2,160 px | 0.111…:1 |  |  |
|  1.6 inches × 7.2 inches |   480 px × 2,160 px | 0.222…:1 |  |  |
|  2.4 inches × 7.2 inches |   720 px × 2,160 px | 0.333…:1 |  |  |
|  3.2 inches × 7.2 inches |   960 px × 2,160 px | 0.444…:1 |  |  |
|  4.0 inches × 7.2 inches | 1,200 px × 2,160 px | 0.556…:1 |  |  |
|  4.8 inches × 7.2 inches | 1,440 px × 2,160 px | 0.667…:1 = 2:3 |  | 35 mm Film (portrait) |
|  5.6 inches × 7.2 inches | 1,680 px × 2,160 px | 0.778…:1 |  |  |
|  6.4 inches × 7.2 inches | 1,920 px × 2,160 px | 0.889…:1 |  |  |
|  7.2 inches × 7.2 inches | 2,160 px × 2,160 px | 1:1 |  | Square |
|  8.0 inches × 7.2 inches | 2,400 px × 2,160 px | 1.111…:1 |  |  |
|  8.8 inches × 7.2 inches | 2,640 px × 2,160 px | 1.222…:1 |  |  |
|  9.6 inches × 7.2 inches | 2,880 px × 2,160 px | 1.333…:1 = 4:3 |  | Full Screen |
| 10.4 inches × 7.2 inches | 3,120 px × 2,160 px | 1.444…:1 |  |  |
| 11.2 inches × 7.2 inches | 3,360 px × 2,160 px | 1.556…:1 |  |  |
| 12.0 inches × 7.2 inches | 3,600 px × 2,160 px | 1.667…:1 |  |  |
| 12.8 inches × 7.2 inches | 3,840 px × 2,160 px | 1.778…:1 = 16:9 = 4²:3² | 4K UHD | Wide Screen |
| 13.6 inches × 7.2 inches | 4,080 px × 2,160 px | 1.889…:1 |  |  |
| 14.4 inches × 7.2 inches | 4,320 px × 2,160 px | 2:1 |  |  |
| 15.2 inches × 7.2 inches | 4,560 px × 2,160 px | 2.111…:1 |  |  |
| 16.0 inches × 7.2 inches | 4,800 px × 2,160 px | 2.222…:1 |  |  |
| 16.8 inches × 7.2 inches | 5,040 px × 2,160 px | 2.333…:1 |  |  |
| 17.6 inches × 7.2 inches | 5,280 px × 2,160 px | 2.444…:1 |  |  |
| 18.4 inches × 7.2 inches | 5,520 px × 2,160 px | 2.555…:1 |  |  |

You may notice that the heights are spaced 0.8 inches apart. In summary:

* normal plots, and plots of a Robinson map with a horizontal colour bar and plots of an Orthographic map with a vertical colour bar, should use `figsize = (9.6, 7.2)`; and
* plots of a naked Robinson map, or plots of two axes side-by-side, should use `figsize = (12.8, 7.2)`.

See the following Wikipedia articles:

* [4K Resolution](https://en.wikipedia.org/wiki/4K_resolution)
* [Aspect Ratio](https://en.wikipedia.org/wiki/Aspect_ratio_(image))
* [Video Standards](https://commons.wikimedia.org/wiki/File:Vector_Video_Standards8.svg)
