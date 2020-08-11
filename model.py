from docproduct.predictor import RetreiveQADoc

pretrained_path = 'model_artifacts/BioBertFolder/biobert_v1.0_pubmed_pmc/'
bert_ffn_weight_file = 'model_artifacts/newFolder/models/bertffn_crossentropy/bertffn'
embedding_file = 'model_artifacts/Float16EmbeddingsExpanded5-27-19.pkl'

doc = RetreiveQADoc(pretrained_path=pretrained_path,
                    ffn_weight_file=None,
                    bert_ffn_weight_file=bert_ffn_weight_file,
                    embedding_file=embedding_file)


def get_predictor():
    return doc
