import json
import xml.etree.ElementTree as ET
from typing import Union, List, Tuple


def analyze_sales(data: Union[str, List[Union[int, float]]]) -> Tuple[float, float, int]:
    """
    Analisa dados de vendas a partir de um arquivo JSON/XML ou uma lista de valores.

    Args:
        data (Union[str, List[Union[int, float]]]): Caminho do arquivo JSON/XML ou lista de valores de vendas.

    Returns:
        Tuple[float, float, int]: Uma tupla contendo:
            - Valor mínimo de venda
            - Valor máximo de venda
            - Número de dias com vendas acima da média

    Raises:
        ValueError: Se houver erro na leitura do arquivo ou formato inválido.
    """
    if isinstance(data, str):
        extension = data.split('.')[-1].lower()
        if extension == 'json':
            try:
                with open(data, 'r') as f:
                    json_data = json.load(f)
                    daily_sales = [float(item['valor']) for item in json_data if 'valor' in item]
            except (FileNotFoundError, json.JSONDecodeError) as e:
                raise ValueError(f"Erro ao ler o arquivo JSON: {e}") from e
        elif extension == 'xml':
            try:
                tree = ET.parse(data)
                root = tree.getroot()
                daily_sales = [
                    float(valor.text)
                    for item in root.findall('row')
                    if (valor := item.find('valor')) is not None and valor.text is not None
                ]
            except (ET.ParseError, FileNotFoundError) as e:
                raise ValueError(f"Erro ao ler o arquivo XML: {e}") from e
        else:
            raise ValueError("Formato de arquivo inválido")
    else:
        daily_sales = [float(value) for value in data]

    # Filtra valores positivos
    daily_sales = [value for value in daily_sales if value > 0]

    if not daily_sales:
        return 0.0, 0.0, 0

    average = sum(daily_sales) / len(daily_sales)
    min_value = min(daily_sales)
    max_value = max(daily_sales)

    # Conta dias acima da média
    days_above_average = sum(1 for value in daily_sales if value > average)

    return min_value, max_value, days_above_average



if __name__ == "__main__":
    try:
        json_result = analyze_sales("sales.json")
        xml_result = analyze_sales("sales.xml")

        print(f"JSON Result: {json_result}")
        print(f"XML Result: {xml_result}")
    except ValueError as e:
        print(f"Erro: {e}")
