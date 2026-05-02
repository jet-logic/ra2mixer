#!/usr/bin/python3

import json
from pathlib import Path
from tempfile import gettempdir
from unittest import TestCase, main
from subprocess import run

ref_mix = "tests/test.mix"

class Test(TestCase):
    def test_4(self):
        run(["python","-m","ra2mixer","l", ref_mix])

    def test_5(self):
        from string import ascii_lowercase, ascii_uppercase, punctuation
        m1 = Path("/tmp/test.mix")
        file_map={
            "ascii.lowercase":ascii_lowercase.encode(),
            "ascii.uppercase":ascii_uppercase.encode(),
            "punctuation":punctuation.encode(),
        }
        tmp = Path(gettempdir())
        mix = tmp/"my.mix"
        mixr = Path(ref_mix)
        files = []
        for k,v in file_map.items():
            p=(tmp/k)
            p.write_bytes(v)
            files.append(str(p))
        print(files)
        run(["python","-m","ra2mixer","c", str(mix), *files])
        run(["python","-m","ra2mixer","l", str(mix)])
        self.assertEqual(mixr.stat().st_size, mix.stat().st_size)
        self.assertEqual(mixr.read_bytes(), mix.read_bytes())


if __name__ == "__main__":
    main()
