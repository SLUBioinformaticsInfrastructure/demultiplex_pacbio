from Bio import SeqIO
import glob, os

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

D1 = {}
D1_files = glob.glob("tag_sample_sorted/Pool1*")
for f in D1_files:
    fhandle = open(f, 'r')
    for l in fhandle:
        l = l.strip()
        D1[l] = f.replace(".txt", ".fastq")

fastq = SeqIO.parse("ps_034_001.ccs.fastq", 'fastq')
tag = 0
non_tag = 0
for entry in fastq:
    try:
        outfile = D1[entry.id]
        tag += 1
        if os.path.isfile(outfile):
            o = open(outfile, 'a')
            # write sequence
            o.write("@{seqid}\n{seq}\n+\n{qual}\n".format(seqid = entry.id, 
                                                          seq = str(entry.seq),
                                                          qual = qual2ascii(entry._per_letter_annotations['phred_quality'])))
            o.close()
        else:
            o = open(outfile, 'w')
            # write sequence
            o.write("@{seqid}\n{seq}\n+\n{qual}\n".format(seqid = entry.id, 
                                                          seq = str(entry.seq),
                                                          qual = qual2ascii(entry._per_letter_annotations['phred_quality'])))
            o.close()
    except:
        #print("{} not linked to any tag")
        non_tag += 1

print("{} sequences assigned to a tag.".format(tag))
print("{} sequences not linked to any tag.".format(non_tag))
