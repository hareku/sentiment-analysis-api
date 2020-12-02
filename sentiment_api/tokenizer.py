import sentencepiece as spm
sp = spm.SentencePieceProcessor(model_file='./models/wiki-ja.model')

def tokenize(text):
    return sp.encode(text, out_type=str)

def get_vocab():
    vocab_n = sp.get_piece_size()
    vocab = [sp.id_to_piece(i) for i in range(vocab_n)]
    return vocab
