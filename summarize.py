
import pandas



dirname="/mnt/chr7/data/julia/kallisto_stats/"

for k in [13,17,21]:
    filename=dirname+"6685_04-06-2015_depl_kallisto_21_out_stats.txt"

    names=['kmers1', 'kmers2', 'contigs1', 'contigs2', 'contigs1+2', 
	'tu1', 'tu2', 'tu1+2', 'ti1', 'ti2', 'ti1+2']
    data = pandas.read_csv(filename, sep='\t', names=names)

    #unmapped = data[data["ti1+2"] == 0]

    #print k, "unmapped / all", float(len(unmapped.index)) / len(data.index)
    #print k, "out of it unmapped due to conflict", float(sum(unmapped["tu1+2"]>0))/len(unmapped.index)
    print "k, mapped, unmapped (no kmers), unmapped (conflicts)"
    n=float(len(data.index))
    zerok = len(data[(data["ti1+2"] == 0) & (data[(data["kmers1"] == 0) & (data[(data["kmers2"] == 0)])
    confl = len(data[(data["ti1+2"] == 0) & (data[(data["tu1+2"] > 0)])
    print k, len(data[data["ti1+2"] > 0])/n, zerok/n, confl/n

