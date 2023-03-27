#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
import getopt
import urllib.parse
import base64
import subprocess
import os

def usage():
    print("""Usage: youzaicoding.py [-h] [-a e|d] [--utf8|gbk] [""]
  -h          Show help message
  -u -e|-d    Encode(-e) or decode(-d) a URL
  -b -e|-d    Encode(-e) or decode(-d) a base64
  -n -e|-d    Encode(-e) or decode(-d) a unicode
  -a -e|-d    Encode(-e) or decode(-d) a ascii 
  --UTF8      Output using UTF-8 encoding (default)
  --GBK       Output using GBK encoding
  """)
    #sys.exit()

def url_encode_decode(mode, content):
    if mode == 'd':
        # 对衔接内容进行URL解码
        print(f"URL decoding: {urllib.parse.unquote(content)}")
    elif mode == 'e':
        # 对衔接内容进行URL编码
        print(f"URL encoding: {urllib.parse.quote(content)}")
    else:
        print(f"Invalid argument: -u{mode}", file=sys.stderr)
        sys.exit(1)

def base64_encode_decode(mode, content,encoding):
    if mode == 'd':
        # 对衔接内容进行base64解码
        print(f"Base64 decoding: {base64.b64decode(content).decode(encoding)}")
    elif mode == 'e':
        # 对衔接内容进行base64编码
        print(f"Base64 encoding: {base64.b64encode(content.encode(encoding)).decode(encoding)}")
    else:
        print(f"Invalid argument: -b{mode}", file=sys.stderr)
        sys.exit(1)

def unicode_encode_decode(mode, content,encoding):
    if mode == 'd':
        # 对衔接内容进行unicode解码
        print(f"unicode decoding:{content.encode(encoding).decode('unicode_escape')}")
    elif mode == 'e':
        # 对衔接内容进行unicode编码
        print(f"unicode encoding:{content.encode('unicode_escape').decode(encoding)}")
    else:
        print(f"Invalid argument: -n{mode}",file=sys.stderr)
        sys.exit(1)

def ascii_encode_decode(mode, content):
    if mode == 'd':
        # 对衔接内容进行ASCII解码
         # 解码 ASCII 编码
        decoded = ""
        codes = content.split()
        for code in codes:
            decoded += chr(int(code))
        print(f"ASCII decoding: {decoded}")
    elif mode == 'e':
        # 对衔接内容进行ASCII编码
        encoded = " ".join(str(ord(c)) for c in content)
        print(f"ASCII encoding: {encoded}")
    else:
        print(f"Invalid argument: -a{mode}", file=sys.stderr)
        sys.exit(1)


def main(argv):
    encoding = 'UTF-8'
    try:
        opts, args = getopt.getopt(argv, "hu:e:d:b:n:a:",["utf8","gbk"])
    except getopt.GetoptError as err:
        print(f"{str(err)}", file=sys.stderr)
        usage()

    for opt, arg in opts:
        if opt == '-h':
            usage()
        elif opt == '-u':
            url_encode_decode(arg, args[0],encoding)
        elif opt == '-b':
            base64_encode_decode(arg, args[0], encoding)
        elif opt == '-n':
            unicode_encode_decode(arg, args[0],encoding)
        elif opt == '-a':
            ascii_encode_decode(arg, args[0],encoding)
        elif opt == "--utf8":
            encoding = 'UTF-8'
        elif opt == "--gbk":
            encoding = 'GBK'
        else:
            print(f"Invalid option: {opt}", file=sys.stderr)
            usage()

    if len(opts) == 0:
        usage()

if __name__ == "__main__":
    if len(sys.argv) == 1 and os.isatty(sys.stdin.fileno()):
        usage()
        subprocess.call(['cmd', '/k', 'python', sys.argv[0]])
        sys.exit()
    main(sys.argv[1:])
