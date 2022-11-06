# Onception

Active Learning with Expert Advice for Real World Machine Translation


### Data

We use the test sets from the [WMT'19 News Translation shared task](http://statmt.org/wmt19/translation-task.html) and the [WMT'20 News Translation shared task](https://github.com/google/wmt-mqm-human-evaluation) (the latter annotated with pSQM scores).

On the test sets from WMT'19, the files `ad-seg-scores-src-mt.csv` for each language pair `src-mt` (where `src` is the source language and `mt` is the translation language) are under different subfolders of "[human evaluation data](https://www.computing.dcu.ie/~ygraham/newstest2019-humaneval.tar.gz)" (depending on the languages), and should be gathered under the same directory when running the `Preprocessing-AnyLang` notebook. 

In the `datasets/` folder, we provide the Comet scores for each pair of segment ID (`sid`) and competing system on WMT'19.

For WMT'20, the files `psqm_newstest2020_ende.tsv` and `psqm_newstest2020_zhen.tsv` provided [here](https://github.com/google/wmt-mqm-human-evaluation/tree/main/newstest2020) should be run over `data_processing_20_2/DataProcessing_pSQM.ipynb`, and the outputs copied to the `datasets/WMT20_pSQM` folder. 

### How to run

For embedding extraction:
- Download the desired BERT model (we used English and Multilingual Base Cased on our experiments)
- Install *BERT as a service* from [hanxiao/bert-as-service](https://github.com/hanxiao/bert-as-service) and run its server on a Python >= 3.5 environment with Tensorflow >= 1.10
- Run `Data Processing_embeddings.ipynb`

For the remaining code:
- Run `pip install -r requirements.txt` on a Python 3.x environment

To obtain Prism scores:
- Get `prism.py` and the model from [thompsonb/prism](https://github.com/thompsonb/prism)
- Run `PRISM.ipynb`

Experiments: 
- Baseline (without active learning): run `mt_ol.ipynb` (requires Jupyter Notebook or similar)
- Onception: run `Onception.ipynb`
- Individual active learning query strategies: 

```
> mt_ol_al.py --qs=<query_strategy> --sm=<similarity_measure> --ts=<threshold> --alg=<online_algorithm> --rw=<reward_func> --task=<task> --src=<src_lang> --mt=<mt_lang> --run=<num_no>
```

### How to cite

If you use this code, please cite the following articles:

- **Onception/Active Learning:** Mendonça, V., Rei, R., Coheur, L. Sardinha, A. (2021), **Onception: Active Learning with Expert Advice for Real World Machine Translation**, [arXiv:2203.04507](https://arxiv.org/abs/2203.04507)

- **Baseline:** Mendonça, V., Rei, R., Coheur, L., Sardinha, A., Santos, A. L. (2021). **Online Learning Meets Machine Translation Evaluation: Finding the Best Systems with the Least Human Effort**. *Proceedings of the 59th Annual Meeting of the Association for Computational Linguistics and the 11th International Joint Conference on Natural Language Processing (Volume 1: Long Papers)*, 3105–3117. [10.18653/v1/2021.acl-long.242](https://doi.org/10.18653/v1/2021.acl-long.242)