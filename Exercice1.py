def print_kmers_frequency(seq,k):
	big_list=[]
	for i in range(len(seq)-k+1):
		big_list.append(seq[i:i+k])
	#print(big_list)
	counts = {}
	for s in big_list:
		if not (s in counts):
			counts[s] = 0
		counts[s] += 1
	print(counts)
print_kmers_frequency('GATTACA',4)
print_kmers_frequency("MISSISSIPPI",5)
print_kmers_frequency("MISSISSIPPI",3)

from Bio import SeqIO
for seq_record in SeqIO.parse("HBV_genotypes_sample_1.fa", "fasta"):
    print(seq_record.id)
    print(repr(seq_record.seq))
    print(len(seq_record))
