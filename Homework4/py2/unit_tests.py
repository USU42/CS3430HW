#!/usr/bin/python

################################################
# module: unit_tests.py
# author: vladimir kulyukin
# Py2 unit tests for HW04, S18
# bugs to vladimir dot kulyukin at usu dot edu
################################################

from __future__ import division
import __future__
from HuffmanTree import HuffmanTree
from HuffmanTreeNode import HuffmanTreeNode
from BinHuffmanTree import BinHuffmanTree
from CharFreqMap import CharFreqMap

ht_nodes = [HuffmanTreeNode(symbols=set([kv[0]]), weight=kv[1])
                for kv in [('A', 8), ('B', 3), ('C', 1), ('D', 1),
                           ('E', 1), ('F', 1), ('G', 1), ('H', 1)]]

txt0 = 'AABCCDEFG'
txt1 = 'AABBBBHHHFFGGGDDDDEEEECCCCCCCCDDDDDHHHHHAAAAAA'
## Change the value of work_dir to the directory where
## you save the files moby_dick_ch01.txt, moby_dick_ch01.txt,
## test_txt0.txt, and test_txt1.txt.
work_dir = '/home/vladimir/teaching/CS3430/S18/hw/hw04/data/'

def unit_test_00():
    hnodes = [HuffmanTreeNode(symbols=set([kv[0]]), weight=kv[1])
                for kv in [('A', 4), ('B', 3), ('C', 1), ('D', 1)]]
    ht = HuffmanTree.fromListOfHuffmanTreeNodes(hnodes)
    if ht is None:
        print 'NONE'
    print(str(ht.getRoot()))
    print(str(ht.getRoot().getLeftChild()))
    print(str(ht.getRoot().getRightChild()))
    print(str(ht.getRoot().getRightChild().getLeftChild()))
    print(str(ht.getRoot().getRightChild().getLeftChild().getLeftChild()))
    print(str(ht.getRoot().getRightChild().getLeftChild().getRightChild()))
    print(str(ht.getRoot().getRightChild().getRightChild()))
    
def unit_test_01():    
    ht = HuffmanTree.fromListOfHuffmanTreeNodes(ht_nodes)
    for s in ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']:
        print(s + ' --> ' + ht.encodeSymbol(s))
    enc0 = ht.encodeText(txt0)
    enc1 = ht.encodeText(txt1)
    dec0 = ht.decode(enc0)
    dec1 = ht.decode(enc1)
    assert dec0 == txt0
    assert dec1 == txt1
    print('Assertions passed!')

def unit_test_02():
    ht = HuffmanTree.fromListOfHuffmanTreeNodes(ht_nodes)
    bht = BinHuffmanTree(root=ht.getRoot())
    bin_enc0, num_bytes0, pad_bits0 = bht.encodeText(txt0)
    bin_enc1, num_bytes1, pad_bits1 = bht.encodeText(txt1)
    print(bin_enc0, pad_bits0)
    print(bin_enc1, pad_bits1)
    dec0 = bht.decode(bin_enc0, pad_bits0)
    dec1 = bht.decode(bin_enc1, pad_bits1)
    assert dec0 == txt0
    assert dec1 == txt1
    print('Assertions passed!')

def unit_test_03():
    ht = HuffmanTree.fromListOfHuffmanTreeNodes(ht_nodes)
    bht = BinHuffmanTree(root=ht.getRoot())
    with open(work_dir + 'test_txt0.txt', 'w') as of:
        of.write(txt0)
        of.flush()
    bht.encodeTextToFile(txt0, work_dir + 'test_txt0')
    with open(work_dir + 'test_txt1.txt', 'w') as of:
        of.write(txt1)
        of.flush()
    bht.encodeTextToFile(txt1, work_dir + 'test_txt1')
    dec0 = bht.decodeTextFromFile(work_dir + 'test_txt0')
    dec1 = bht.decodeTextFromFile(work_dir + 'test_txt1')
    assert txt0 == dec0
    assert txt1 == dec1
    print('Assertions passed!')

def unit_test_04():
    cfm1 = CharFreqMap.computeCharFreqMap(work_dir + 'moby_dick_ch01.txt')
    nodes = HuffmanTree.freqMapToListOfHuffmanTreeNodes(cfm1)
    ht = HuffmanTree.fromListOfHuffmanTreeNodes(nodes)
    bht = BinHuffmanTree(root=ht.getRoot())
    bht.encodeTextFromFileToFile(work_dir + 'moby_dick_ch01.txt',
                                 work_dir + 'moby_dick_ch01')
    with open(work_dir + 'moby_dick_ch01.txt', 'r') as inf:
        data = inf.read()
        dec0 = bht.decodeTextFromFile(work_dir + 'moby_dick_ch01')
        assert dec0 == data
        print('Assertion passed!')

def unit_test_05():
    cfm2 = CharFreqMap.computeCharFreqMap(work_dir + 'moby_dick_ch02.txt')
    nodes = HuffmanTree.freqMapToListOfHuffmanTreeNodes(cfm2)
    ht = HuffmanTree.fromListOfHuffmanTreeNodes(nodes)
    bht = BinHuffmanTree(root=ht.getRoot())
    bht.encodeTextFromFileToFile(work_dir + 'moby_dick_ch02.txt',
                                 work_dir + 'moby_dick_ch02')
    with open(work_dir + 'moby_dick_ch02.txt', 'r') as inf:
        data = inf.read()
        dec0 = bht.decodeTextFromFile(work_dir + 'moby_dick_ch02')
        assert dec0 == data
        print('Assertion passed!')
    
def unit_test_06():
    cfm = CharFreqMap.computeCharFreqMap(work_dir + 'moby_dick_ch01.txt')
    nodes = HuffmanTree.freqMapToListOfHuffmanTreeNodes(cfm)
    ht = HuffmanTree.fromListOfHuffmanTreeNodes(nodes)
    bht = BinHuffmanTree(root=ht.getRoot())
    bht.persist(work_dir + 'moby_dick_ch01_bht.bin')

def unit_test_07():
    cfm = CharFreqMap.computeCharFreqMap(work_dir + 'moby_dick_ch02.txt')
    nodes = HuffmanTree.freqMapToListOfHuffmanTreeNodes(cfm)
    ht = HuffmanTree.fromListOfHuffmanTreeNodes(nodes)
    bht = BinHuffmanTree(root=ht.getRoot())
    bht.persist(work_dir + 'moby_dick_ch02_bht.bin')

def unit_test_08():
    bht01 = BinHuffmanTree.load(work_dir + 'moby_dick_ch01_bht.bin')
    bht02 = BinHuffmanTree.load(work_dir + 'moby_dick_ch02_bht.bin')
    with open(work_dir + 'moby_dick_ch01.txt', 'r') as inf:
        data = inf.read()
        dec01 = bht01.decodeTextFromFile(work_dir + 'moby_dick_ch01')
        assert dec01 == data
        print('Assertion passed!')
    with open(work_dir + 'moby_dick_ch02.txt', 'r') as inf:
        data = inf.read()
        dec02 = bht02.decodeTextFromFile(work_dir + 'moby_dick_ch02')
        assert dec02 == data
        print('Assertion passed!')


    
    
