# Demultiplexing PacBio files

This repository is developed and maintained by Domenico Simone (domenico.simone@slu.se). It contains a script to demultiplex PacBio read files in order to get files for single samples which are suitable for submission to public databases (eg SRA).

## Getting the repository

The best way to use this repo is to clone it with **git**, which should be already installed on Unix systems (Linux, MacOS)

```bash
git clone https://github.com/domenico-simone/demultiplex_pacbio.git
```

Otherwise, you can download and unzip this repo by clicking on the "Code" green button on the top right of this page.

## Prerequisites

The demultiplexing script needs **Python** to be run (tested with Python > 3.4) and the **Biopython** library. If you don't have it, the easiest way to install it is with `pip` (Python > 3.4):

```bash
pip install biopython
```

## Demultiplexing read datasets

### Running the script

In order to demultiplex your datasets you will need to arrange input files like this:

- **the fastq file to be demultiplexed** has to be in the root folder of the git repo. An example of a file comes with this repo with the name `example_to_demultiplex.fastq`;
- **read mapping files** (_ie_, files with read IDs one per line) have to be in a subfolder of your choice **with a \*.txt extension**. An example of this folder comes with this repo with the name `tag_sample_sorted`.

The demultiplexing script can be run as follows:

```bash
python demultiplex_pacbio.py <file_to_be_demultiplexed> <folder_with_mapping_files>
```

### Outputs

If everything goes right, you'll find in the same folder as the read mapping files your demultiplexed outputs. They will have the same name as the read mapping files, with the \*.txt extension replaced by a \*.fastq extension, _eg_ the following read mapping files:

```
tag_sample_sorted/
├── Pool1_fire-gITS7_tag_12_ITS4a_tag_12.txt
├── Pool1_fire-gITS7_tag_13_ITS4a_tag_13.txt
└── Pool1_fire-gITS7_tag_15_ITS4a_tag_15.txt
```

will result in the following folder structure:

```
tag_sample_sorted/
├── Pool1_fire-gITS7_tag_12_ITS4a_tag_12.fastq
├── Pool1_fire-gITS7_tag_12_ITS4a_tag_12.txt
├── Pool1_fire-gITS7_tag_13_ITS4a_tag_13.fastq
├── Pool1_fire-gITS7_tag_13_ITS4a_tag_13.txt
├── Pool1_fire-gITS7_tag_15_ITS4a_tag_15.fastq
├── Pool1_fire-gITS7_tag_15_ITS4a_tag_15.txt
├── example_to_demultiplex.stats
└── example_to_demultiplex.unassigned
```

The `example_to_demultiplex.stats` file reports demultiplexing statistics (_ie_, how many reads were expected from each sample and how many were assigned to each sample). The `example_to_demultiplex.no_tag.fastq` file reports reads from the input file which were not found in any read mapping file.

## Getting troubles?

Please open an issue here: https://github.com/domenico-simone/demultiplex_pacbio/issues (preferred) or contact me at `domenico.simone@slu.se`. Opening an issue is the preferred way since other people can more easily benefit from it, although you need a GitHub account to do it!

**Happy demultiplexing!**
 