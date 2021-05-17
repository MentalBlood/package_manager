import main

default_build_function = lambda dependencies_data: dependencies_data

m = main.Manager()
m.addPackage('1', default_build_function, [])
m.addPackage('2', default_build_function, ['1'])
m.addPackage('3', default_build_function, ['1', '2'])
m.addPackage('4', default_build_function, ['3'])
m.rebuildPackage('4')
print(m.getData('4'))
print(m.getAllDependencies('4'))