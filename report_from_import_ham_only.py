from modulefinder import ModuleFinder

def print_type_dir():
    finder = ModuleFinder()
    finder.run_script('from_import.py')
    print('dir ModuleFinder: {}'.format(dir(finder)))
    """
    dir ModuleFinder: ['__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__',
     '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', 
     '__init_subclass__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', 
     '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', 
     '__weakref__', '_add_badmodule', '_safe_import_hook', 'add_module', 'any_missing', 
     'any_missing_maybe', 'badmodules', 'debug', 'determine_parent', 'ensure_fromlist', 
     'excludes', 'find_all_submodules', 'find_head_package', 'find_module', 'import_hook', 
     'import_module', 'indent', 'load_file', 'load_module', 'load_package', 'load_tail', 
     'modules', 'msg', 'msgin', 'msgout', 'path', 'processed_paths', 'replace_paths', 
     'replace_paths_in_code', 'report', 'run_script', 'scan_code', 'scan_opcodes']
    """

    for name, mod in finder.modules.items():
        print('type:{}'.format(type(mod)))
        #=> type:<class 'modulefinder.Module'>
        print('dir Module object:{}'.format(dir(mod)))
        """
        dir:['__class__', '__code__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', 
        '__file__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', 
        '__init_subclass__', '__le__', '__lt__', '__module__', '__name__', '__ne__', '__new__', 
        '__path__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', 
        '__str__', '__subclasshook__', '__weakref__', 'globalnames', 'starimports']
        """
        return


def print_attr():
    finder = ModuleFinder()
    finder.run_script('from_import_ham_only.py')

    for name, mod in finder.modules.items():
        print('-'*10)
        print('name:{}'.format(name))
        print('globalnames:{}'.format(mod.globalnames))
        print('modules:{}'.format(','.join(list(mod.globalnames.keys()))))
        print('starimports:{}'.format(mod.starimports))

    print('bad modules:{}'.format(','.join(finder.badmodules.keys())))
    """
    ----------
    name:__main__
    globalnames:{'ham': 1}
    modules:ham
    starimports:{}
    ----------
    name:ham_package
    globalnames:{}
    modules:
    starimports:{}
    ----------
    name:ham_package.ham_module
    globalnames:{'ham': 1}
    modules:ham
    starimports:{}
    bad modules:
    """

def usage_mistakes():
    files = ['from_import_spam_only.py', 'from_import_ham_only.py']
    # ModuleFinderオブジェクトを使いまわす
    finder = ModuleFinder()

    for f in files:
        finder.run_script(f)
        for name, mod in finder.modules.items():
            print('-'*10)
            print('file:{}'.format(f))
            print('name:{}'.format(name))
            print('modules:{}'.format(','.join(list(mod.globalnames.keys()))))
            """ModuleFinderオブジェクトを使いまわすと、誤った結果になる
            ----------
            file:from_import_spam_only.py
            name:__main__
            modules:spam
            ----------
            file:from_import_spam_only.py
            name:spam_package
            modules:
            ----------
            file:from_import_spam_only.py
            name:spam_package.spam_module
            modules:spam
            ----------
            file:from_import_ham_only.py
            name:__main__
            modules:spam,ham                  <= hamだけなのにspamがいる
            ----------
            file:from_import_ham_only.py
            name:spam_package
            modules:
            ----------
            file:from_import_ham_only.py
            name:spam_package.spam_module
            modules:spam
            ----------
            file:from_import_ham_only.py
            name:ham_package
            modules:
            ----------
            file:from_import_ham_only.py
            name:ham_package.ham_module
            modules:ham
            """


def usage_files():
    files = ['from_import_spam_only.py', 'from_import_ham_only.py']

    for f in files:
        # ModuleFinderオブジェクトは、ファイルごとに生成する
        finder = ModuleFinder()
        finder.run_script(f)
        for name, mod in finder.modules.items():
            print('-'*10)
            print('file:{}'.format(f))
            print('name:{}'.format(name))
            print('modules:{}'.format(','.join(list(mod.globalnames.keys()))))
            """
            ----------
            file:from_import_spam_only.py
            name:__main__
            modules:spam
            ----------
            file:from_import_spam_only.py
            name:spam_package
            modules:
            ----------
            file:from_import_spam_only.py
            name:spam_package.spam_module
            modules:spam
            ----------
            file:from_import_ham_only.py
            name:__main__
            modules:ham                  <= hamだけになった
            ----------
            file:from_import_ham_only.py
            name:ham_package
            modules:
            ----------
            file:from_import_ham_only.py
            name:ham_package.ham_module
            modules:ham
            """


if __name__ == '__main__':
    print_type_dir()
    print_attr()
    usage_mistakes()
    usage_files()
    