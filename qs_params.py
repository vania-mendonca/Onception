tasks = ["WMT19", "WMT20_pSQM"]
mt_languages_19 = ["en-de", "fr-de", "de-cs", "gu-en", "lt-en"]
mt_languages_20 = ["en-de", "zh-en"]

query_strategies_params = dict.fromkeys(tasks, {})
query_strategies_params["WMT19"] = dict.fromkeys(mt_languages_19, {})
query_strategies_params["WMT20_pSQM"] = dict.fromkeys(mt_languages_20, {})

query_strategies_params["WMT19"]["en-de"] = {"EWAF": {"All": [], "NoDen": []},
                                    "EXP3": {"All": [], "NoDen": []}}
query_strategies_params["WMT19"]["fr-de"] = {"EWAF": {"All": [], "NoDen": []},
                                    "EXP3": {"All": [], "NoDen": []}}
query_strategies_params["WMT19"]["de-cs"] = {"EWAF": {"All": [], "NoDen": []},
                                    "EXP3": {"All": [], "NoDen": []}}
query_strategies_params["WMT19"]["gu-en"] = {"EWAF": {"All": [], "NoDen": [], " NoPrism": []},
                                    "EXP3": {"All": [], "NoDen": [], " NoPrism": []}}
query_strategies_params["WMT19"]["lt-en"] = {"EWAF": {"All": [], "NoDen": []},
                                    "EXP3": {"All": [], "NoDen": []}}

query_strategies_params["WMT20_pSQM"]["en-de"] = {"EWAF": {"All": [], "NoDen": []},
                                    "EXP3": {"All": [], "NoDen": []}}
query_strategies_params["WMT20_pSQM"]["zh-en"] = {"EWAF": {"All": [], "NoDen": []},
                                    "EXP3": {"All": [], "NoDen": []}}

################################################################################

query_strategies_params["WMT19"]["en-de"]["EWAF"]["All"] = [('Div', ('jac', 0.09)),
                                                   ('Div', ('BERT', 0.91)),
                                                   ('Den', ('jac', 0.05)),
                                                   ('Den', ('BERT', 0.92)),
                                                   ('QbC', ('jac', 0.63)),
                                                   ('QbC', ('BERT', 0.975)),
                                                   ('QbC', ('BLEU', 0.48)),
                                                   ('QEst', ('PRISM', -0.7)),
                                                   ('DivNg', ('3', 0.9)),
                                                   ('DenNg', ('3', 0.00035)),
                                                   ('random', None)]

query_strategies_params["WMT19"]["en-de"]["EWAF"]["NoDen"] = [('Div', ('jac', 0.09)),
                                                   ('Div', ('BERT', 0.91)),
                                                   ('QbC', ('jac', 0.63)),
                                                   ('QbC', ('BERT', 0.975)),
                                                   ('QbC', ('BLEU', 0.48)),
                                                   ('QEst', ('PRISM', -0.7)),
                                                   ('DivNg', ('3', 0.9)),
                                                   ('random', None)]

###

query_strategies_params["WMT19"]["en-de"]["EXP3"]["All"] = [('Div', ('jac', 0.09)),
                                                   ('Div', ('BERT', 0.91)),
                                                   ('Den', ('jac', 0.05)),
                                                   ('Den', ('BERT', 0.92)),
                                                   ('QbC', ('jac', 0.63)),
                                                   ('QbC', ('BERT', 0.975)),
                                                   ('QbC', ('BLEU', 0.48)),
                                                   ('QEst', ('PRISM', -0.7)),
                                                   ('DivNg', ('3', 0.9)),
                                                   ('DenNg', ('3', 0.00035)),
                                                   ('random', None)]

query_strategies_params["WMT19"]["en-de"]["EXP3"]["NoDen"] = [('Div', ('jac', 0.09)),
                                                   ('Div', ('BERT', 0.91)),
                                                   ('QbC', ('jac', 0.63)),
                                                   ('QbC', ('BERT', 0.975)),
                                                   ('QbC', ('BLEU', 0.48)),
                                                   ('QEst', ('PRISM', -0.7)),
                                                   ('DivNg', ('3', 0.9)),
                                                   ('random', None)]

################################################################################

query_strategies_params["WMT19"]["fr-de"]["EWAF"]["All"] = [('Div', ('jac', 0.06)),
                                                   ('Div', ('BERT', 0.9)),
                                                   ('Den', ('jac', 0.07)),
                                                   ('Den', ('BERT', 0.91)),
                                                   ('QbC', ('jac', 0.59)),
                                                   ('QbC', ('BERT', 0.969)),
                                                   ('QbC', ('BLEU', 0.4)),
                                                   ('QEst', ('PRISM', -0.89)),
                                                   ('DivNg', ('3', 0.88)),
                                                   ('DenNg', ('3', 0.00052)),
                                                   ('random', None)]

query_strategies_params["WMT19"]["fr-de"]["EWAF"]["NoDen"] = [('Div', ('jac', 0.06)),
                                                   ('Div', ('BERT', 0.9)),
                                                   ('QbC', ('jac', 0.59)),
                                                   ('QbC', ('BERT', 0.969)),
                                                   ('QbC', ('BLEU', 0.4)),
                                                   ('QEst', ('PRISM', -0.89)),
                                                   ('DivNg', ('3', 0.88)),
                                                   ('random', None)]

###

query_strategies_params["WMT19"]["fr-de"]["EXP3"]["All"] = [('Div', ('jac', 0.06)),
                                                   ('Div', ('BERT', 0.9)),
                                                   ('Den', ('jac', 0.07)),
                                                   ('Den', ('BERT', 0.91)),
                                                   ('QbC', ('jac', 0.59)),
                                                   ('QbC', ('BERT', 0.969)),
                                                   ('QbC', ('BLEU', 0.4)),
                                                   ('QEst', ('PRISM', -0.89)),
                                                   ('DivNg', ('3', 0.88)),
                                                   ('DenNg', ('3', 0.00052)),
                                                   ('random', None)]

query_strategies_params["WMT19"]["fr-de"]["EXP3"]["NoDen"] = [('Div', ('jac', 0.06)),
                                                   ('Div', ('BERT', 0.9)),
                                                   ('QbC', ('jac', 0.59)),
                                                   ('QbC', ('BERT', 0.969)),
                                                   ('QbC', ('BLEU', 0.4)),
                                                   ('QEst', ('PRISM', -0.89)),
                                                   ('DivNg', ('3', 0.88)),
                                                   ('random', None)]

################################################################################


query_strategies_params["WMT19"]["de-cs"]["EWAF"]["All"] = [('Div', ('jac', 0.03)),
                                                   ('Div', ('BERT', 0.9)),
                                                   ('Den', ('jac', 0.03)),
                                                   ('Den', ('BERT', 0.9)),
                                                   ('QbC', ('jac', 0.41)),
                                                   ('QbC', ('BERT', 0.962)),
                                                   ('QbC', ('BLEU', 0.28)),
                                                   ('QEst', ('PRISM', -1.33)),
                                                   ('DivNg', ('3', 0.95)),
                                                   ('DenNg', ('3', 0.00049)),
                                                   ('random', None)]

query_strategies_params["WMT19"]["de-cs"]["EWAF"]["NoDen"] = [('Div', ('jac', 0.03)),
                                                   ('Div', ('BERT', 0.9)),
                                                   ('QbC', ('jac', 0.41)),
                                                   ('QbC', ('BERT', 0.962)),
                                                   ('QbC', ('BLEU', 0.28)),
                                                   ('QEst', ('PRISM', -1.33)),
                                                   ('DivNg', ('3', 0.95)),
                                                   ('random', None)]

###

query_strategies_params["WMT19"]["de-cs"]["EXP3"]["All"] = [('Div', ('jac', 0.03)),
                                                   ('Div', ('BERT', 0.9)),
                                                   ('Den', ('jac', 0.03)),
                                                   ('Den', ('BERT', 0.9)),
                                                   ('QbC', ('jac', 0.41)),
                                                   ('QbC', ('BERT', 0.962)),
                                                   ('QbC', ('BLEU', 0.28)),
                                                   ('QEst', ('PRISM', -1.33)),
                                                   ('DivNg', ('3', 0.95)),
                                                   ('DenNg', ('3', 0.00049)),
                                                   ('random', None)]

query_strategies_params["WMT19"]["de-cs"]["EXP3"]["NoDen"] = [('Div', ('jac', 0.03)),
                                                   ('Div', ('BERT', 0.9)),
                                                   ('QbC', ('jac', 0.41)),
                                                   ('QbC', ('BERT', 0.962)),
                                                   ('QbC', ('BLEU', 0.28)),
                                                   ('QEst', ('PRISM', -1.33)),
                                                   ('DivNg', ('3', 0.95)),
                                                   ('random', None)]

################################################################################


query_strategies_params["WMT19"]["gu-en"]["EWAF"]["All"] = [('Div', ('jac', 0.02)),
                                                   ('Div', ('BERT', 0.95)),
                                                   ('Den', ('jac', 0.02)),
                                                   ('Den', ('BERT', 0.94)),
                                                   ('QbC', ('jac', 0.25)),
                                                   ('QbC', ('BERT', 0.948)),
                                                   ('QbC', ('BLEU', 0.14)),
                                                   ('QEst', ('PRISM', -4.74)),
                                                   ('DivNg', ('3', 0.96)),
                                                   ('DenNg', ('3', 0.00025)),
                                                   ('random', None)]

query_strategies_params["WMT19"]["gu-en"]["EWAF"]["NoDen"] = [('Div', ('jac', 0.02)),
                                                   ('Div', ('BERT', 0.95)),
                                                   ('QbC', ('jac', 0.25)),
                                                   ('QbC', ('BERT', 0.948)),
                                                   ('QbC', ('BLEU', 0.14)),
                                                   ('QEst', ('PRISM', -4.74)),
                                                   ('DivNg', ('3', 0.96)),
                                                   ('random', None)]

query_strategies_params["WMT19"]["gu-en"]["EWAF"]["NoPrism"] = [('Div', ('jac', 0.02)),
                                                   ('Div', ('BERT', 0.95)),
                                                   ('QbC', ('jac', 0.25)),
                                                   ('QbC', ('BERT', 0.948)),
                                                   ('QbC', ('BLEU', 0.14)),
                                                   ('DivNg', ('3', 0.96)),
                                                   ('random', None)]

###

query_strategies_params["WMT19"]["gu-en"]["EXP3"]["All"] = [('Div', ('jac', 0.02)),
                                                   ('Div', ('BERT', 0.95)),
                                                   ('Den', ('jac', 0.02)),
                                                   ('Den', ('BERT', 0.94)),
                                                   ('QbC', ('jac', 0.25)),
                                                   ('QbC', ('BERT', 0.948)),
                                                   ('QbC', ('BLEU', 0.14)),
                                                   ('QEst', ('PRISM', -4.74)),
                                                   ('DivNg', ('3', 0.96)),
                                                   ('DenNg', ('3', 0.00025)),
                                                   ('random', None)]

query_strategies_params["WMT19"]["gu-en"]["EXP3"]["NoDen"] = [('Div', ('jac', 0.02)),
                                                   ('Div', ('BERT', 0.95)),
                                                   ('QbC', ('jac', 0.25)),
                                                   ('QbC', ('BERT', 0.948)),
                                                   ('QbC', ('BLEU', 0.14)),
                                                   ('QEst', ('PRISM', -4.74)),
                                                   ('DivNg', ('3', 0.96)),
                                                   ('random', None)]

query_strategies_params["WMT19"]["gu-en"]["EXP3"]["NoPrism"] = [('Div', ('jac', 0.02)),
                                                   ('Div', ('BERT', 0.95)),
                                                   ('QbC', ('jac', 0.25)),
                                                   ('QbC', ('BERT', 0.948)),
                                                   ('QbC', ('BLEU', 0.14)),
                                                   ('DivNg', ('3', 0.96)),
                                                   ('random', None)]

################################################################################

query_strategies_params["WMT19"]["lt-en"]["EWAF"]["All"] = [('Div', ('jac', 0.003)),
                                                   ('Div', ('BERT', 0.91)),
                                                   ('Den', ('jac', 0.01)),
                                                   ('Den', ('BERT', 0.91)),
                                                   ('QbC', ('jac', 0.65)),
                                                   ('QbC', ('BERT', 0.983)),
                                                   ('QbC', ('BLEU', 0.41)),
                                                   ('QEst', ('PRISM', -1.16)),
                                                   ('DivNg', ('3', 0.99)),
                                                   ('DenNg', ('3', 0.0002)),
                                                   ('random', None)]

query_strategies_params["WMT19"]["lt-en"]["EWAF"]["NoDen"] = [('Div', ('jac', 0.003)),
                                                   ('Div', ('BERT', 0.91)),
                                                   ('QbC', ('jac', 0.65)),
                                                   ('QbC', ('BERT', 0.983)),
                                                   ('QbC', ('BLEU', 0.41)),
                                                   ('QEst', ('PRISM', -1.16)),
                                                   ('DivNg', ('3', 0.99)),
                                                   ('random', None)]

###

query_strategies_params["WMT19"]["lt-en"]["EXP3"]["All"] = [('Div', ('jac', 0.003)),
                                                   ('Div', ('BERT', 0.91)),
                                                   ('Den', ('jac', 0.01)),
                                                   ('Den', ('BERT', 0.91)),
                                                   ('QbC', ('jac', 0.65)),
                                                   ('QbC', ('BERT', 0.983)),
                                                   ('QbC', ('BLEU', 0.41)),
                                                   ('QEst', ('PRISM', -1.16)),
                                                   ('DivNg', ('3', 0.99)),
                                                   ('DenNg', ('3', 0.0002)),
                                                   ('random', None)]

query_strategies_params["WMT19"]["lt-en"]["EXP3"]["NoDen"] = [('Div', ('jac', 0.003)),
                                                   ('Div', ('BERT', 0.91)),
                                                   ('QbC', ('jac', 0.65)),
                                                   ('QbC', ('BERT', 0.983)),
                                                   ('QbC', ('BLEU', 0.41)),
                                                   ('QEst', ('PRISM', -1.16)),
                                                   ('DivNg', ('3', 0.99)),
                                                   ('random', None)]

################################################################################
################################################################################

query_strategies_params["WMT20_pSQM"]["en-de"]["EWAF"]["All"] = [('Div', ('jac', 0.09)),
                                                   ('Div', ('BERT', 0.94)),
                                                   ('Den', ('jac', 0.06)),
                                                   ('Den', ('BERT', 0.93)),
                                                   ('QbC', ('jac', 0.59)),
                                                   ('QbC', ('BERT', 0.983)),
                                                   ('QbC', ('BLEU', 0.45)),
                                                   ('QEst', ('PRISM', -0.76)),
                                                   ('DivNg', ('3', 0.88)),
                                                   ('DenNg', ('3', 0.00015)),
                                                   ('random', None)]

query_strategies_params["WMT20_pSQM"]["en-de"]["EWAF"]["NoDen"] = [('Div', ('jac', 0.09)),
                                                   ('Div', ('BERT', 0.94)),
                                                   ('QbC', ('jac', 0.59)),
                                                   ('QbC', ('BERT', 0.983)),
                                                   ('QbC', ('BLEU', 0.45)),
                                                   ('QEst', ('PRISM', -0.76)),
                                                   ('DivNg', ('3', 0.88)),
                                                   ('random', None)]
##

query_strategies_params["WMT20_pSQM"]["en-de"]["EXP3"]["All"] = [('Div', ('jac', 0.09)),
                                                   ('Div', ('BERT', 0.94)),
                                                   ('Den', ('jac', 0.06)),
                                                   ('Den', ('BERT', 0.93)),
                                                   ('QbC', ('jac', 0.59)),
                                                   ('QbC', ('BERT', 0.983)),
                                                   ('QbC', ('BLEU', 0.45)),
                                                   ('QEst', ('PRISM', -0.76)),
                                                   ('DivNg', ('3', 0.88)),
                                                   ('DenNg', ('3', 0.00015)),
                                                   ('random', None)]

query_strategies_params["WMT20_pSQM"]["en-de"]["EXP3"]["NoDen"] = [('Div', ('jac', 0.09)),
                                                   ('Div', ('BERT', 0.94)),
                                                   ('QbC', ('jac', 0.59)),
                                                   ('QbC', ('BERT', 0.983)),
                                                   ('QbC', ('BLEU', 0.45)),
                                                   ('QEst', ('PRISM', -0.76)),
                                                   ('DivNg', ('3', 0.88)),
                                                   ('random', None)]


################################################################################


query_strategies_params["WMT20_pSQM"]["zh-en"]["EWAF"]["All"] = [('Div', ('jac', 0.07)),
                                                   ('Div', ('BERT', 0.9)),
                                                   ('Den', ('jac', 0.07)),
                                                   ('Den', ('BERT', 0.89)),
                                                   ('QbC', ('jac', 0.75)),
                                                   ('QbC', ('BERT', 0.993)),
                                                   ('QbC', ('BLEU', 0.62)),
                                                   ('QEst', ('PRISM', -1.06)),
                                                   ('DivNg', ('3', 0.91)),
                                                   ('DenNg', ('3', 0.00025)),
                                                   ('random', None)]

query_strategies_params["WMT20_pSQM"]["zh-en"]["EWAF"]["NoDen"] = [('Div', ('jac', 0.07)),
                                                   ('Div', ('BERT', 0.9)),
                                                   ('QbC', ('jac', 0.75)),
                                                   ('QbC', ('BERT', 0.993)),
                                                   ('QbC', ('BLEU', 0.62)),
                                                   ('QEst', ('PRISM', -1.06)),
                                                   ('DivNg', ('3', 0.91)),
                                                   ('random', None)]
##

query_strategies_params["WMT20_pSQM"]["zh-en"]["EXP3"]["All"] = [('Div', ('jac', 0.07)),
                                                   ('Div', ('BERT', 0.9)),
                                                   ('Den', ('jac', 0.07)),
                                                   ('Den', ('BERT', 0.89)),
                                                   ('QbC', ('jac', 0.75)),
                                                   ('QbC', ('BERT', 0.993)),
                                                   ('QbC', ('BLEU', 0.62)),
                                                   ('QEst', ('PRISM', -1.06)),
                                                   ('DivNg', ('3', 0.91)),
                                                   ('DenNg', ('3', 0.00025)),
                                                   ('random', None)]

query_strategies_params["WMT20_pSQM"]["zh-en"]["EXP3"]["NoDen"] = [('Div', ('jac', 0.07)),
                                                   ('Div', ('BERT', 0.9)),
                                                   ('QbC', ('jac', 0.75)),
                                                   ('QbC', ('BERT', 0.993)),
                                                   ('QbC', ('BLEU', 0.62)),
                                                   ('QEst', ('PRISM', -1.06)),
                                                   ('DivNg', ('3', 0.91)),
                                                   ('random', None)]