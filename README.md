# Nand2Tetris Hack Assembler

[Pygments](http://pygments.org/) lexer for [Nand2Tetris Hack Assembler](http://www.nand2tetris.org/chapters/chapter%2004.pdf) language.

Part of the languages used/developed in the [Building a Modern Computer from First Principles](http://www.nand2tetris.org/) book.

## Usage

The name of the lexer is `hack_asm` so you can call it from `pygmentize` like this:

```
pygmentize -l hack_asm -f html -O full test.asm 
```

The recognize extension is `.asm` but it is as well used by many other lexers (like, you know, other assemblers), so I recommend passing directly the lexer name.

## Installation

The lexer is available in PyPI, just install using `pip`:

```
pip install pygments-hackasm-lexer
```

And start using it.
