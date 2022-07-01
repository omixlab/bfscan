from Bio import SeqIO
import pickle
import argparse
import bfscan
import tqdm

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-i', '--input', required=True, help='Input fasta file')
    parser.add_argument('-f', '--filter', required=True, help='Bloom filter file')
    parser.add_argument('-o', '--output', required=True)
    parser.add_argument('-t', '--threshold', type=float, default=0.9, help='Threshold')
    arguments = parser.parse_args()

    reader = open(arguments.input)
    sequences = SeqIO.parse(reader, 'fasta')
    bloomfilters = pickle.load(open(arguments.filter, 'rb'))

    output_writers = {bloomfilter:open(arguments.output+bloomfilter+'.fasta', 'w') for bloomfilter in bloomfilters}
    for sequence in sequences:
            kmers = utils.sequence_to_kmer(sequence.seq, arguments.k_size)
            hits = {}
            for bloomfilter in bloomfilters:
                kmer_hits = 0
                for kmer in tqdm(kmers):
                    if kmer in bloomfilters[bloomfilter]:
                        kmer_hits+=1
                hit_rate = kmer_hits/len(kmers)
                if hit_rate >= arguments.threshold:
                    output_writers[bloomfilter].write(sequence.format('fasta'))
    for writer in output_writers:
        output_writers[writer].close()


if __name__ == '__main__':
    main()



