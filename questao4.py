def calculate_percentual(data):

    total = sum(data.values())

    percents = {}
    for state, value in data.items():
        percents[state] = (value / total) * 100
    return percents

sales = {
    "SP": 67836.43,
    "RJ": 36678.66,
    "MG": 29229.88,
    "ES": 27165.48,
    "Outros": 19849.53
}


if __name__ == "__main__":
    result = calculate_percentual(sales)
    for state, percent in result.items():
        print(f"O estado {state} represntou {percent:.2f}% do faturamento total da empresa")