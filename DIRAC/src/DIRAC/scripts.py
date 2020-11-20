from collections import defaultdict
from importlib import metadata


def proxy_info():
    print("Called DIRAC.scripts.proxy_info")


def dms_get_file():
    print("Called DIRAC.scripts.dms_get_file")


def show_extensions():
    priorties = defaultdict(list)
    for entrypoint in metadata.entry_points()['dirac']:
        extension_name = entrypoint.module.split(".")[0]
        extension_metadata = entrypoint.load()()
        priorties[extension_metadata["priority"]].append(extension_name)
        print("Found extension", extension_name, "with metadata", extension_metadata)

    extensions = []
    for priority, extension_names in sorted(priorties.items()):
        if len(extension_names) != 1:
            print(
                f"WARNING: Found multiple extensions with priority "
                f"{priority} ({extension_names})"
            )
        # If multiple are passed, sort the extensions so things are deterministic at least
        extensions.extend(sorted(extension_names))
    print("Ranked extensions are:", ",".join(extensions))
