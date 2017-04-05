from modulefinder import ModuleFinder
import os
from collections import Counter


def is_target(filename):
    if '__' in filename:
        # __file__や__init__.pyを除外
        return False
    if 'report' in filename:
        return False
    if os.path.splitext(filename)[1] != '.py':
        return False
    return True


def collect_files():
    root_dir = os.path.abspath(os.path.dirname(__file__))
    results = []
    for root, dirs, files in os.walk(root_dir):
        dirs[:] = [d for d in dirs if 'env' not in os.path.join(root, d)]
        targets = [os.path.join(root, f) for f in files if is_target(f)]
        results.extend(targets)
    return results


def main():
    files = collect_files()

    modules = []
    for f in files:
        finder = ModuleFinder()
        finder.run_script(f)

        for name, mod in finder.modules.items():
            if name == '__main__':
                continue
            if not mod.globalnames.keys():
                continue
            modules.append(name)

    c = Counter(modules)
    print(c.most_common())
    #=> [('ham_package.ham_module', 3), ('spam_package.spam_module', 3), ('eggs_package.eggs_module', 2)]


if __name__ == '__main__':
    main()