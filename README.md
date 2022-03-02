# Pycar

Pycar is a project to build a car with micropython using ESP8266

This project was tested in:
* MacOSX Big Sur

## Requirements
* [pipenv](https://pypi.org/project/pipenv/)

## Prepare ESP8266 with micropython
* [Preparing ESP8266](PREPARE.md)

Setup config settings
```sh
cp .ampy.example .ampy
cp settings.example.json settings.json
```

Put files into ESP8266
```sh
(env)$ ampy put public
(env)$ ampy put utils
(env)$ ampy put settings.json
(env)$ ampy put main.py
```

Run dev mode
```sh
(env)$ ampy run main.py
```

## License

MIT License

    Copyright (c) 2022 Marcelo1180
    
    Permission is hereby granted, free of charge, to any person obtaining a copy
    of this software and associated documentation files (the "Software"), to deal
    in the Software without restriction, including without limitation the rights
    to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
    copies of the Software, and to permit persons to whom the Software is
    furnished to do so, subject to the following conditions:
    
    The above copyright notice and this permission notice shall be included in all
    copies or substantial portions of the Software.
    
    THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
    IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
    FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
    AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
    LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
    OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
    SOFTWARE.
