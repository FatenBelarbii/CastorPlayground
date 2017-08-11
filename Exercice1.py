def print_kmers(seq,k):
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
print_kmers('GATTACA',4)
print_kmers("MISSISSIPPI",5)
print_kmers("MISSISSIPPI",3)
