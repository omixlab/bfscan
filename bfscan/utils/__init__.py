from Bio.Seq import Seq

def sequence_to_kmer(sequence, k):
    
    sequence = Seq(sequence).upper()
    c_rev_seq = sequence.reverse_complement()
    kmer_list = []
    
    base_index = 0
    for i in sequence:
        if (len(sequence) - base_index) >= k:
            kmer_list.append(sequence[base_index:(base_index+k)])
            kmer_list.append(c_rev_seq[base_index:(base_index+k)])
        base_index+=1
    
    return kmer_list
