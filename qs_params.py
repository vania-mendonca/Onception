mt_languages = ["en-de", "fr-de", "de-cs", "gu-en", "lt-en"]

query_strategies_params = dict.fromkeys(mt_languages, {})

query_strategies_params["en-de"] = {"EWAF": {"All": [], "NoDen": []},
                                    "EXP3": {"All": [], "NoDen": []}}
query_strategies_params["fr-de"] = {"EWAF": {"All": [], "NoDen": []},
                                    "EXP3": {"All": [], "NoDen": []}}
query_strategies_params["de-cs"] = {"EWAF": {"All": [], "NoDen": []},
                                    "EXP3": {"All": [], "NoDen": []}}
query_strategies_params["gu-en"] = {"EWAF": {"All": [], "NoDen": [], " NoPrism": []},
                                    "EXP3": {"All": [], "NoDen": [], " NoPrism": []}}
query_strategies_params["lt-en"] = {"EWAF": {"All": [], "NoDen": []},
                                    "EXP3": {"All": [], "NoDen": []}}

################################################################################

query_strategies_params["en-de"]["EWAF"]["All"] = [('Div', ('jac', 0.6)),
                                                   ('Div', ('BERT', 0.93)),
                                                   ('Den', ('jac', 0.55)),
                                                   ('Den', ('BERT', 0.92)),
                                                   ('QbC', ('jac', 0.85)),
                                                   ('QbC', ('BERT', 0.955)),
                                                   ('QbC', ('BLEU', 0.55)),
                                                   ('QEst', ('PRISM', -1)),
                                                   ('DivNg', ('3', 0.6)),
                                                   ('DenNg', ('3', 0.00003)),
                                                   ('random', None)]

query_strategies_params["en-de"]["EWAF"]["NoDen"] = [('Div', ('jac', 0.6)),
                                                   ('Div', ('BERT', 0.93)),
                                                   ('QbC', ('jac', 0.85)),
                                                   ('QbC', ('BERT', 0.955)),
                                                   ('QbC', ('BLEU', 0.55)),
                                                   ('QEst', ('PRISM', -1)),
                                                   ('DivNg', ('3', 0.6)),
                                                   ('random', None)]

###

query_strategies_params["en-de"]["EXP3"]["All"] = [('Div', ('jac', 0.6)),
                                                   ('Div', ('BERT', 0.925)),
                                                   ('Den', ('jac', 0.6)),
                                                   ('Den', ('BERT', 0.925)),
                                                   ('QbC', ('jac', 0.85)),
                                                   ('QbC', ('BERT', 0.955)),
                                                   ('QbC', ('BLEU', 0.45)),
                                                   ('QEst', ('PRISM', -0.25)),
                                                   ('DivNg', ('3', 0.6)),
                                                   ('DenNg', ('3', 0.00004)),
                                                   ('random', None)]

query_strategies_params["en-de"]["EXP3"]["NoDen"] = [('Div', ('jac', 0.6)),
                                                   ('Div', ('BERT', 0.925)),
                                                   ('QbC', ('jac', 0.85)),
                                                   ('QbC', ('BERT', 0.955)),
                                                   ('QbC', ('BLEU', 0.45)),
                                                   ('QEst', ('PRISM', -0.25)),
                                                   ('DivNg', ('3', 0.6)),
                                                   ('random', None)]

################################################################################

query_strategies_params["fr-de"]["EWAF"]["All"] = [('Div', ('jac', 0.65)),
                                                   ('Div', ('BERT', 0.875)),
                                                   ('Den', ('jac', 0.55)),
                                                   ('Den', ('BERT', 0.875)),
                                                   ('QbC', ('jac', 0.75)),
                                                   ('QbC', ('BERT', 0.96)),
                                                   ('QbC', ('BLEU', 0.4)),
                                                   ('QEst', ('PRISM', -1)),
                                                   ('DivNg', ('3', 0.55)),
                                                   ('DenNg', ('3', 0.00005)),
                                                   ('random', None)]

query_strategies_params["fr-de"]["EWAF"]["NoDen"] = [('Div', ('jac', 0.65)),
                                                   ('Div', ('BERT', 0.875)),
                                                   ('QbC', ('jac', 0.75)),
                                                   ('QbC', ('BERT', 0.96)),
                                                   ('QbC', ('BLEU', 0.4)),
                                                   ('QEst', ('PRISM', -1)),
                                                   ('DivNg', ('3', 0.55)),
                                                   ('random', None)]

###


query_strategies_params["fr-de"]["EXP3"]["All"] = [('Div', ('jac', 0.5)),
                                                   ('Div', ('BERT', 0.875)),
                                                   ('Den', ('jac', 0.5)),
                                                   ('Den', ('BERT', 0.875)),
                                                   ('QbC', ('jac', 0.8)),
                                                   ('QbC', ('BERT', 0.965)),
                                                   ('QbC', ('BLEU', 0.35)),
                                                   ('QEst', ('PRISM', -1.5)),
                                                   ('DivNg', ('3', 0.4)),
                                                   ('DenNg', ('3', 0.00004)),
                                                   ('random', None)]

query_strategies_params["fr-de"]["EXP3"]["NoDen"] = [('Div', ('jac', 0.5)),
                                                   ('Div', ('BERT', 0.875)),
                                                   ('QbC', ('jac', 0.8)),
                                                   ('QbC', ('BERT', 0.965)),
                                                   ('QbC', ('BLEU', 0.35)),
                                                   ('QEst', ('PRISM', -1.5)),
                                                   ('DivNg', ('3', 0.4)),
                                                   ('random', None)]

################################################################################


query_strategies_params["de-cs"]["EWAF"]["All"] = [('Div', ('jac', 0.45)),
                                                   ('Div', ('BERT', 0.9)),
                                                   ('Den', ('jac', 0.5)),
                                                   ('Den', ('BERT', 0.9)),
                                                   ('QbC', ('jac', 0.75)),
                                                   ('QbC', ('BERT', 0.96)),
                                                   ('QbC', ('BLEU', 0.3)),
                                                   ('QEst', ('PRISM', -1.5)),
                                                   ('DivNg', ('3', 0.7)),
                                                   ('DenNg', ('3', 0.0001)),
                                                   ('random', None)]

query_strategies_params["de-cs"]["EWAF"]["NoDen"] = [('Div', ('jac', 0.45)),
                                                   ('Div', ('BERT', 0.9)),
                                                   ('QbC', ('jac', 0.75)),
                                                   ('QbC', ('BERT', 0.96)),
                                                   ('QbC', ('BLEU', 0.3)),
                                                   ('QEst', ('PRISM', -1.5)),
                                                   ('DivNg', ('3', 0.7)),
                                                   ('random', None)]

###

query_strategies_params["de-cs"]["EXP3"]["All"] = [('Div', ('jac', 0.55)),
                                                   ('Div', ('BERT', 0.9)),
                                                   ('Den', ('jac', 0.6)),
                                                   ('Den', ('BERT', 0.9)),
                                                   ('QbC', ('jac', 0.8)),
                                                   ('QbC', ('BERT', 0.955)),
                                                   ('QbC', ('BLEU', 0.25)),
                                                   ('QEst', ('PRISM', -1.5)),
                                                   ('DivNg', ('3', 0.7)),
                                                   ('DenNg', ('3', 0.000075)),
                                                   ('random', None)]

query_strategies_params["de-cs"]["EXP3"]["NoDen"] = [('Div', ('jac', 0.55)),
                                                   ('Div', ('BERT', 0.9)),
                                                   ('QbC', ('jac', 0.8)),
                                                   ('QbC', ('BERT', 0.955)),
                                                   ('QbC', ('BLEU', 0.25)),
                                                   ('QEst', ('PRISM', -1.5)),
                                                   ('DivNg', ('3', 0.7)),
                                                   ('random', None)]

################################################################################


query_strategies_params["gu-en"]["EWAF"]["All"] = [('Div', ('jac', 0.55)),
                                                   ('Div', ('BERT', 0.95)),
                                                   ('Den', ('jac', 0.4)),
                                                   ('Den', ('BERT', 0.9)),
                                                   ('QbC', ('jac', 0.75)),
                                                   ('QbC', ('BERT', 0.95)),
                                                   ('QbC', ('BLEU', 0.15)),
                                                   ('QEst', ('PRISM', -6)),
                                                   ('DivNg', ('3', 0.65)),
                                                   ('DenNg', ('3', 0.00005)),
                                                   ('random', None)]

query_strategies_params["gu-en"]["EWAF"]["NoDen"] = [('Div', ('jac', 0.55)),
                                                   ('Div', ('BERT', 0.95)),
                                                   ('QbC', ('jac', 0.75)),
                                                   ('QbC', ('BERT', 0.95)),
                                                   ('QbC', ('BLEU', 0.15)),
                                                   ('QEst', ('PRISM', -6)),
                                                   ('DivNg', ('3', 0.65)),
                                                   ('random', None)]

query_strategies_params["gu-en"]["EWAF"]["NoPrism"] = [('Div', ('jac', 0.55)),
                                                   ('Div', ('BERT', 0.95)),
                                                   ('QbC', ('jac', 0.75)),
                                                   ('QbC', ('BERT', 0.95)),
                                                   ('QbC', ('BLEU', 0.15)),
                                                   ('DivNg', ('3', 0.65)),
                                                   ('random', None)]

###

query_strategies_params["gu-en"]["EXP3"]["All"] = [('Div', ('jac', 0.55)),
                                                   ('Div', ('BERT', 0.9)),
                                                   ('Den', ('jac', 0.55)),
                                                   ('Den', ('BERT', 0.9)),
                                                   ('QbC', ('jac', 0.8)),
                                                   ('QbC', ('BERT', 0.955)),
                                                   ('QbC', ('BLEU', 0.15)),
                                                   ('QEst', ('PRISM', -4.5)),
                                                   ('DivNg', ('3', 0.6)),
                                                   ('DenNg', ('3', 0.000075)),
                                                   ('random', None)]

query_strategies_params["gu-en"]["EXP3"]["NoDen"] = [('Div', ('jac', 0.55)),
                                                   ('Div', ('BERT', 0.9)),
                                                   ('QbC', ('jac', 0.8)),
                                                   ('QbC', ('BERT', 0.955)),
                                                   ('QbC', ('BLEU', 0.15)),
                                                   ('QEst', ('PRISM', -4.5)),
                                                   ('DivNg', ('3', 0.6)),
                                                   ('random', None)]

query_strategies_params["gu-en"]["EXP3"]["NoPrism"] = [('Div', ('jac', 0.55)),
                                                   ('Div', ('BERT', 0.9)),
                                                   ('QbC', ('jac', 0.8)),
                                                   ('QbC', ('BERT', 0.955)),
                                                   ('QbC', ('BLEU', 0.15)),
                                                   ('DivNg', ('3', 0.6)),
                                                   ('random', None)]

################################################################################

query_strategies_params["lt-en"]["EWAF"]["All"] = [('Div', ('jac', 0.45)),
                                                   ('Div', ('BERT', 0.9)),
                                                   ('Den', ('jac', 0.6)),
                                                   ('Den', ('BERT', 0.925)),
                                                   ('QbC', ('jac', 0.8)),
                                                   ('QbC', ('BERT', 0.955)),
                                                   ('QbC', ('BLEU', 0.3)),
                                                   ('QEst', ('PRISM', -1.5)),
                                                   ('DivNg', ('3', 0.75)),
                                                   ('DenNg', ('3', 0.000075)),
                                                   ('random', None)]

query_strategies_params["lt-en"]["EWAF"]["NoDen"] = [('Div', ('jac', 0.45)),
                                                   ('Div', ('BERT', 0.9)),
                                                   ('QbC', ('jac', 0.8)),
                                                   ('QbC', ('BERT', 0.955)),
                                                   ('QbC', ('BLEU', 0.3)),
                                                   ('QEst', ('PRISM', -1.5)),
                                                   ('DivNg', ('3', 0.75)),
                                                   ('random', None)]

###

query_strategies_params["lt-en"]["EXP3"]["All"] = [('Div', ('jac', 0.55)),
                                                   ('Div', ('BERT', 0.875)),
                                                   ('Den', ('jac', 0.45)),
                                                   ('Den', ('BERT', 0.9)),
                                                   ('QbC', ('jac', 0.8)),
                                                   ('QbC', ('BERT', 0.955)),
                                                   ('QbC', ('BLEU', 0.25)),
                                                   ('QEst', ('PRISM', -1.25)),
                                                   ('DivNg', ('3', 0.9)),
                                                   ('DenNg', ('3', 0.00005)),
                                                   ('random', None)]

query_strategies_params["lt-en"]["EXP3"]["NoDen"] = [('Div', ('jac', 0.55)),
                                                   ('Div', ('BERT', 0.875)),
                                                   ('QbC', ('jac', 0.8)),
                                                   ('QbC', ('BERT', 0.955)),
                                                   ('QbC', ('BLEU', 0.25)),
                                                   ('QEst', ('PRISM', -1.25)),
                                                   ('DivNg', ('3', 0.9)),
                                                   ('random', None)]
