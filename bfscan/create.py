import argparse
from Bio import SeqIO
from bfscan import utils
from bloom_filter2 import BloomFilter
import pickle
from tqdm import tqdm 

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-i', '--input', nargs='*', metavar='FASTAFILE', required=True, help='Input fasta file')
    parser.add_argument('-k', '--k-size', type=int, default=7, help='Input k size')
    parser.add_argument('-o', '--output', required=True)
    parser.add_argument('-m', '--max-elements', type=int, default=100000, help='Input max elements')
    parser.add_argument('-e', '--error', type=float, delfault=0.001, help ='Input error rate') 
    arguments = parser.parse_args()

    bloomfilters = {}
    for file in arguments.input:
        print(file)
        #pegar o basename do arquivo
        bloomfilters[file] = BloomFilter(arguments.max_elements, arguments.error)  
        reader = open(file)
        sequences = SeqIO.parse(reader, 'fasta')
        for sequence in sequences:
            kmers = utils.sequence_to_kmer(sequence.seq, arguments.k_size)
            for kmer in tqdm(kmers):
                bloomfilters[file].add(kmer)
    with open(arguments.output, 'wb') as writer: 
        writer.write(pickle.dumps(bloomfilters))

if __name__ == '__main__':
    main()
    



