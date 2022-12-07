# bfscan

BFScan is a tool to scan FASTA and FASTQ files using a combination of
k-mer composition, Bloom-filter and machine learning methods. 

## Example

### 1. Construction a collection of Bloom filters for targets organisms

```
$ bfscan-build-filters \
    -i \
        data/fasta/salmonella.fasta \
        data/fasta/listeria.fasta \
        data/fasta/campylobacter.fasta \
    -o data/filters/filter
```

### 2. Training a machine learning model

```
$ bfscan-build-model \
    -i \
        data/fasta/salmonella.fasta \
        data/fasta/listeria.fasta \
        data/fasta/campylobacter.fasta \
    -o data/models/model \
    -background data/fastq/metagenome.fastq \
    -r data/reports/classification_report.txt
```

### 3. Running the search

```
$ bfscan-search \
    -i \
        reads.fastq \
    -o data/results/filtered \
    -F fastq
``
