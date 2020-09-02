# Demultiplexing PacBio files

This repository is developed and maintained by Domenico Simone (domenico.simone@slu.se). It contains a script to demultiplex PacBio read files in order to get files for single samples which are suitable for submission to public databases (eg SRA).

## Getting the repository

```bash
git clone https://github.com/domenico-simone/demultiplex_pacbio.git
```

## Prerequisites

The demultiplexing script needs Python to be run (tested with Python > 3.4) and the Biopython library. If you don't have it, the easiest way to install it is with `pip`:

```bash
pip install biopython
```

## Demultiplexing read datasets

In order to demultiplex your datasets you will need to arrange input files like this:

- **the fastq file to be demultiplexed** has to be in the root folder of the git repo;
- **read mapping files** (_ie_, files with read IDs one per line) have to be in a subfolder of your choice **with a \*.txt extension**.

The demultiplexing script can be run as follows:

```bash
python demultiplex_pacbio.py <file_to_be_demultiplexed> <folder_with_mapping_files>
```

If everything goes right, you'll find in the same folder as the read mapping files your demultiplexed outputs. They will have the same name as the read mapping files, with the \*.txt extension replaced by a \*.fastq extension.

## Getting troubles?

Please open an issue `https://github.com/domenico-simone/demultiplex_pacbio/issues` (preferred) or contact me at `domenico.simone@slu.se`. Opening an issue is the preferred way since other people can more easily benefit from it!

**Happy demultiplexing!**
 