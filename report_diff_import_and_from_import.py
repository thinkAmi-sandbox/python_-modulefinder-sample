from modulefinder import ModuleFinder

def diff_import_fromimport():
    files = ['from_import.py', 'import.py']

    for f in files:
        print('='*10)
        print('filename:{}'.format(f))
        # ModuleFinderオブジェクトは、ファイルごとに生成する
        finder = ModuleFinder()
        finder.run_script(f)
        for name, mod in finder.modules.items():
            print('-'*10)
            print('name:{}'.format(name))
            print('modules:{}'.format(','.join(list(mod.globalnames.keys()))))


if __name__ == '__main__':
    diff_import_fromimport()