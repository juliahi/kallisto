
import pandas
import random
from Bio import SeqIO


dirname="/mnt/chr7/data/julia/kallisto_stats/"

for k in [13,21,25]:
    
    name="6685_04-06-2015_depl"
    filename=dirname+name+("_kallisto_%d_out_stats.txt"%k)

    names=['kmers1', 'kmers2', 'contigs1', 'contigs2', 'contigs1+2', 
	'tu1', 'tu2', 'tu1+2', 'ti1', 'ti2', 'ti1+2']
    data = pandas.read_csv(filename, sep='\t', names=names)

    #unmapped = data[data["ti1+2"] == 0]

    #print k, "unmapped / all", float(len(unmapped.index)) / len(data.index)
    #print k, "out of it unmapped due to conflict", float(sum(unmapped["tu1+2"]>0))/len(unmapped.index)
    n=float(len(data.index))

    
    selected = []

    N = 10
    types = []
    zerokmers = data[(data["kmers1"] == 0) & (data["kmers2"] == 0)].index.tolist()
    if len(zerokmers) > N:
    	selected += random.sample(zerokmers,N) 
        types += ["zero kmers"]*N
    conflicts = data[(data["ti1+2"] == 0) & (data["tu1+2"] > 0)]
    #selected += random.sample(conflicts,N)
    selected += data[(data["ti1+2"] == 0)].nlargest(N,"tu1+2").index.tolist()
    types += ["conficts"]*N
    
    nonunique = data[(data["ti1+2"] > 0)]
    #selected += random.sample(nonunique,10) 
    selected += data.nlargest(N,"ti1+2").index.tolist()
    types += ["non-unique"]*N

    with open(dirname+name+"_%d_selected.fasta"%k, "w+") as output:
        datadir = "/mnt/chr4/mikrobiomy-2/Wyniki_sekwencjonowania/demultiplexed/"
        records = list(SeqIO.parse(datadir+name+"_1.fq", "fastq"))
        for idx,typ in zip(selected,types): 
            records[idx].name += (' '+typ)
            SeqIO.write([records[idx]], output, "fasta")

    print selected 
    print "k, mapped, unmapped (no kmers), unmapped (conflicts), nonuniquelly mapped"
    print k, len(data[data["ti1+2"] > 0])/n, len(zerokmers)/n, len(conflicts)/n, len(nonunique)/n
    
    
     
    
