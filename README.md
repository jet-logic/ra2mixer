Create, list .mix files of Command & Conquer: Red Alert 2 / Command & Conquer: Yuri's Revenge. Once installed, you can invoke it as a standalone command or via the Python module:

```bash
ra2mixer <command> [options]
# or
python -m ra2mixer <command> [options]
```

### 📖 Available Commands

```bash
$ python -m ra2mixer -h
usage: ra2mix [-h] {list,l,extract,x,create,c} ...

List, extract, create MIX files

positional arguments:
  {list,l,extract,x,create,c}
    list (l)            list files of MIX file
    extract (x)         extract files of MIX file
    create (c)          create MIX file from files

options:
  -h, --help            show this help message and exit
```

| Command   | Description                                  |
| --------- | -------------------------------------------- |
| `list`    | View contents of a `.mix` archive            |
| `extract` | Extract all files from a `.mix` archive      |
| `create`  | Pack files/folders into a new `.mix` archive |

### 🔍 List Contents

```bash
$ python -m ra2mixer list -h
usage: ra2mix list [-h] [--sort-by-offset {ascending,descending,a,d}] mix_files [mix_files ...]

positional arguments:
  mix_files             path to the .mix files

options:
  -h, --help            show this help message and exit
  --sort-by-offset {ascending,descending,a,d}
                        Sort entries by offset
```

```bash
# Basic file listing
ra2mixer list game.mix
```

### 📦 Extract Archive

```bash
$ python -m ra2mixer extract -h
usage: ra2mix extract [-h] [-d DIR] mix_files [mix_files ...]

positional arguments:
  mix_files   path to the .mix files

options:
  -h, --help  show this help message and exit
  -d DIR      extract files into DIR
```

```bash
# Extract to a specific folder
ra2mixer extract game.mix -d output/
```

### 🛠️ Create Archive

```bash
$ python -m ra2mixer create -h
usage: ra2mix create [-h] [--no-names-db] [--game GAME] mix_file files [files ...]

positional arguments:
  mix_file       the mix file to create
  files          files to include

options:
  -h, --help     show this help message and exit
  --no-names-db  Dont add 'local mix database.dat'
  --game GAME    which game TD, RA, TS, DUNE2, DUNE2000, RA2, RA2_YR, RG, GR, GR_ZH, EBFD, NOX, BFME, BFME2, TW, TS_FS, UNKNOWN
```

```bash
# Pack all files from a directory
ra2mixer create new.mix assets/

# Pack specific files
ra2mixer create new.mix rules.ini art.ini audio01.wav
```
