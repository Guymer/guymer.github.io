#!/usr/bin/env python3

# Use the proper idiom in the main module ...
# NOTE: See https://docs.python.org/3.12/library/multiprocessing.html#the-spawn-and-forkserver-start-methods
if __name__ == "__main__":
    # Import standard modules ...
    import argparse
    import glob
    import os

    # Import special modules ...
    try:
        import pyguymer3
    except:
        raise Exception("\"pyguymer3\" is not installed; run \"pip install --user PyGuymer3\"") from None

    # **************************************************************************

    # Create argument parser and parse the arguments ...
    parser = argparse.ArgumentParser(
           allow_abbrev = False,
            description = "Make a dashboard of the SVG badges for all of the GitHub Actions on my public GitHub repositories.",
        formatter_class = argparse.ArgumentDefaultsHelpFormatter,
    )
    parser.add_argument(
        "--timeout",
        default = 60.0,
           help = "the timeout for any requests/subprocess calls (in seconds)",
           type = float,
    )
    args = parser.parse_args()

    # **************************************************************************

    # Open output file ...
    with open("docs/index.html", "wt", encoding = "utf-8") as fObj:
        # Write header ...
        fObj.write("<!DOCTYPE HTML>\n")
        fObj.write("<html lang=\"en-gb\" xmlns=\"http://www.w3.org/1999/xhtml\" xmlns:svg=\"http://www.w3.org/2000/svg\">\n")
        fObj.write("    <head>\n")
        fObj.write("        <link rel=\"canonical\" href=\"https://guymer.github.io/\"/>\n")
        fObj.write("        <link rel=\"license\" href=\"https://www.apache.org/licenses/LICENSE-2.0/\"/>\n")
        fObj.write("        <meta charset=\"utf-8\"/>\n")
        fObj.write("        <meta name=\"author\" content=\"Thomas Guymer\"/>\n")
        fObj.write(f'        <meta name=\"copyright\" content=\"© 2025 - {pyguymer3.now().strftime("%Y")} Thomas Guymer\"/>\n')
        fObj.write("        <meta name=\"description\" content=\"A dashboard of the SVG badges for all of the GitHub Actions on my public GitHub repositories\"/>\n")
        fObj.write("        <meta name=\"generator\" content=\"Python\"/>\n")
        fObj.write("        <meta name=\"robots\" content=\"index,follow\"/>\n")
        fObj.write("        <title>GitHub Actions Badges</title>\n")
        fObj.write("    </head>\n")
        fObj.write("    <body>\n")
        fObj.write("        <main>\n")
        fObj.write("            <article>\n")
        fObj.write("                <header>\n")
        fObj.write("                    <h1>GitHub Actions Badges</h1>\n")
        fObj.write("                </header>\n")

        # Start session ...
        with pyguymer3.start_session() as sess:
            # Loop over Git repositories ...
            for gName in sorted(glob.glob(f"{os.path.dirname(os.path.dirname(__file__))}/*/.git")):
                # Skip this Git repository if it is a submodule ...
                if not os.path.isdir(gName):
                    continue

                # Create short-hands and skip this Git repository if it is not
                # saved on GitHub ...
                dName = os.path.dirname(gName)
                gRemote = pyguymer3.git_remote(
                    dName,
                    timeout = args.timeout,
                )
                onGitHub = gRemote.startswith("git@github.com:")
                if not onGitHub:
                    print(f"\"{dName}\" is not saved on GitHub.")
                    continue

                # Create short-hands and skip this Git repository if it is not
                # public on GitHub ...
                gUrl = f'https://github.com/Guymer/{gRemote.removeprefix("git@github.com:Guymer/")}'.removesuffix(".git")
                gHeader = pyguymer3.download_header(
                    sess,
                    gUrl,
                    timeout = args.timeout,
                )
                if not gHeader:
                    print(f"\"{dName}\" is not public on GitHub.")
                    continue

                print(f"Writing SVG badges for \"{dName}\" ...")

                # Write data ...
                fObj.write(f"                <h2><a href=\"{gUrl}\" title=\"“{os.path.basename(dName)}” on GitHub\">{os.path.basename(dName)}</a></h2>\n")
                fObj.write("                <p>Badges:")
                for yName in sorted(glob.glob(f"{dName}/.github/workflows/*.yaml")):
                    fObj.write(f' <img src=\"{gUrl}/actions/{yName.removeprefix(f"{dName}/.github/")}/badge.svg\"/>')
                fObj.write("</p>\n")

        # Write footer ...
        fObj.write("            </article>\n")
        fObj.write("        </main>\n")
        fObj.write("    </body>\n")
        fObj.write("</html>\n")
