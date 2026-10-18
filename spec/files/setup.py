from setuptools import setup
import os

setup(name='giki',
	version='0.1pre',
	description='a Git-based wiki',
	author='Adam Brenecki',
	author_email='adam@brenecki.id.au',
	url='',
	packages=['.'.join(i[0].split(os.sep))
		for i in os.walk('giki')
		if '__init__.py' in i[2]],
	install_requires=[
		'dulwich==1.2.9',
		'jinja2==3.1.6',
		'Werkzeug==3.1.9',
		# formatters
		'markdown2==2.4.0',
		'docutils==0.9.1',
		'textile==2.1.5',
	],
	extras_require = {
		'test':  [
			'nose==1.1.2',
			'WebTest==1.4.0',
		],
		'faster_markdown':  [
			'misaka==1.0.2',
		],
	},
	entry_points = {
    'console_scripts':
        ['giki = giki.cli:main'],
	},
)
