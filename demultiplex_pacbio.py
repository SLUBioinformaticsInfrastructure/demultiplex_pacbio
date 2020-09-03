from Bio import SeqIO
from types import SimpleNamespace
import glob, os, sys

# For each fastq:
# 
# create dict of sequences
# iterate over fastq
# write sequences in proper files

def qual2ascii(list_of_phred):
    ascii = ''
    for i in list_of_phred:
        ascii += chr(i+33)
    return ascii

def usage():
    print("""
        USAGE:
        
        python demultiplex_pacbio.py <file_to_demultiplex> <folder_with_mapping_files>
    """)
    
if len(sys.argv) != 3:
    usage()
    sys.exit("Not enough arguments provided. Exit.\n")
    
file_to_demultiplex = sys.argv[1]
folder_with_mapping_files = sys.argv[2]

# outputs names from inputs
file_to_demultiplex_stats = os.path.join(folder_with_mapping_files, file_to_demultiplex.replace(".fastq", ".stats"))
file_to_demultiplex_non_tag = os.path.join(folder_with_mapping_files, file_to_demultiplex.replace(".fastq", ".no_tag.fastq"))

# dictionary of { readID : file.fastq }
D1 = {}
# dictionary of { sample : [number_of_seqs }
stats_dict = {}
D1_files = glob.glob("{folder_with_mapping_files}/*.txt".format(folder_with_mapping_files=folder_with_mapping_files))
print("\nRead mapping files:")
for f in D1_files:
    print(f)
#    stats_dict[f.replace(".txt", "")] = 0
    stats_dict[f.replace(".txt", "")] = SimpleNamespace(total=0, found=0)
    fhandle = open(f, 'r')
    for l in fhandle:
        l = l.strip()
        if l in D1:
            print("{l} already in dict".format(l))
        D1[l] = f.replace(".txt", ".fastq")
        stats_dict[f.replace(".txt", "")].total += 1

#print(len(stats_dict))
print("\nTotal read IDs in read mapping files: {}".format(len(D1)))

fastq = SeqIO.parse(file_to_demultiplex, 'fastq')
total = 0
tag = 0
non_tag = 0
non_tag_file = open(file_to_demultiplex_non_tag, 'w')
for entry in fastq:
    total += 1
    if entry.id in D1:
        outfile = D1[entry.id]
        if os.path.isfile(outfile):
            o = open(outfile, 'a')
            # write sequence
            _ = o.write("@{seqid}\n{seq}\n+\n{qual}\n".format(seqid = entry.id, 
                                                          seq = str(entry.seq),
                                                          qual = qual2ascii(entry._per_letter_annotations['phred_quality'])))
            o.close()
        else:
            o = open(outfile, 'w')
            # write sequence
            _ = o.write("@{seqid}\n{seq}\n+\n{qual}\n".format(seqid = entry.id, 
                                                          seq = str(entry.seq),
                                                          qual = qual2ascii(entry._per_letter_annotations['phred_quality'])))
            o.close()
        # stats_dict[D1[entry.id].replace(".fastq", "")] += 1
        stats_dict[D1[entry.id].replace(".fastq", "")].found += 1
        tag += 1
    else:
        #print("{} not linked to any tag")
        non_tag += 1
        _ = non_tag_file.write("@{seqid}\n{seq}\n+\n{qual}\n".format(seqid = entry.id, 
                                                      seq = str(entry.seq),
                                                      qual = qual2ascii(entry._per_letter_annotations['phred_quality'])))

stats_file = open(file_to_demultiplex_stats, 'w')
stats_file.write("sample\ttotal_reads\treads_found\n")
for read_mapping_file in stats_dict:
    _ = stats_file.write("{read_mapping_file}\t{total_reads}\t{assigned_reads}\n".format(read_mapping_file=read_mapping_file,
                                                                            total_reads=stats_dict[read_mapping_file].total,
                                                                            assigned_reads=stats_dict[read_mapping_file].found))
stats_file.close()

print("{} total sequences.".format(total))
print("{} sequences assigned to a tag.".format(tag))
print("{non_tag} sequences not linked to any tag. You can find them in file {file}".format(non_tag=non_tag,
                                                                                            file=file_to_demultiplex_non_tag))
print("\nPer-sample demultiplexing stats are provided in file {file}".format(file=file_to_demultiplex_stats))
print("")
