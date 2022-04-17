
def aggregate_scores(year: str, block: str) -> str:

    from EventProcessor2017 import process_2017
    from EventProcessor2018 import process_2018
    from EventProcessor2019 import process_2019

    if year == '2017':

        return 'done'
        # do something
    elif year == '2018':

        return 'done'
        # do something else
    elif year == '2019':

        return 'done'
        # do something else else
    else:
        return "No Years to check"