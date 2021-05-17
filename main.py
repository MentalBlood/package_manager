class Manager:
	def __init__(self):
		self.packages = {}

	def addPackage(self, name, build_function, dependencies):
		new_package = {
			'name': name,
			'build_function': build_function,
			'dependencies': dependencies,
			'data': None
		}
		self.packages[name] = new_package

	def getAllDependencies_(self, name, dependencies, dependencies_in_order):
		for d in self.packages[name]['dependencies']:
			self.getAllDependencies_(d, dependencies, dependencies_in_order)
			if not (d in dependencies):
				dependencies[d] = True
				dependencies_in_order.append(d)

	def getAllDependencies(self, name):
		result = []
		self.getAllDependencies_(name, {}, result)
		return result

	def getData(self, name):
		return self.packages[name]['data']

	def rebuildPackage_(self, name):
		package = self.packages[name]
		dependencies_data = {
			d: self.packages[d]['data']
			for d in package['dependencies']
		}
		package['data'] = package['build_function'](dependencies_data)

	def rebuildPackage(self, name):
		package = self.packages[name]
		dependencies = self.getAllDependencies(name)
		for d in dependencies:
			self.rebuildPackage_(d)
		dependencies_data = {
			d: self.packages[d]['data']
			for d in package['dependencies']
		}
		package['data'] = package['build_function'](dependencies_data)