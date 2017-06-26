from setuptools import setup, find_packages

setup(name='pygments-hackasm-lexer',
      version='0.1',
      description='Pygments lexer for the Nand2Tetris Hack Assembler',
      packages = setuptools.find_packages(),
      url='https://github.com/cprieto/pygments_hack_asm',
      author='Cristian Prieto',
      author_email='me@cprieto.com',
      license='MIT',
      install_requires = ['pygments'],
      keywords = [
          'syntax highlighting',
          'pygments',
          'lexer',
          'hack',
          'assembler',
          'nand2tetris'],
      classifiers =[
          'Intended Audience :: Developers',
          'Operating System :: OS Independent',
          'Programming Language :: Python',
          'Programming Language :: Python :: 2',
          'Programming Language :: Python :: 3',
          'Topic :: Utilities',
          'License :: OSI Approved :: MIT License',
          'Environment :: Plugins'])

