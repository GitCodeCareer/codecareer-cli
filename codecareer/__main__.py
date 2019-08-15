import platform
from argparse import ArgumentParser, RawDescriptionHelpFormatter
from codecareer.generate import Generate

module_name = "CodeCareer CLI"
__version__ = "1.0.0"

def main():
    version_string = f"{module_name}\n" + \
                     f"Version: {__version__}\n" + \
                     f"Python:  {platform.python_version()}"

    parser = ArgumentParser(formatter_class=RawDescriptionHelpFormatter,
                            description=f"{module_name} (Version {__version__})"
                            )
    parser.add_argument("--version",
                        action="version", version=version_string,
                        help="Display version information and dependencies."
                        )

    args = parser.parse_args()
    Generate(args)


if __name__ == "__main__":
    main()