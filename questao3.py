import json
import xml.etree.ElementTree as ET
from typing import Union, List, Tuple


def analyze_sales(data: Union[str, List[float]]) -> Tuple[float, float, int]:
    """
    Analisa dados de vendas a partir de um arquivo JSON/XML ou uma lista de valores.

    Args:
        data (Union[str, List[float]]): Caminho do arquivo JSON/XML ou lista de valores de vendas.

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
                    data = json.load(f)
                    daily_sales = [item['valor'] for item in data if 'valor' in item]
            except (FileNotFoundError, json.JSONDecodeError) as e:
                raise ValueError(f"Erro ao ler o arquivo JSON: {e}") from e
        elif extension == 'xml':
            try:
                tree = ET.parse(data)
                root = tree.getroot()
                daily_sales = [float(item.find('valor').text) for item in root.findall('row')]
            except (ET.ParseError, FileNotFoundError) as e:
                raise ValueError(f"Erro ao ler o arquivo XML: {e}") from e
        else:
            raise ValueError("Formato de arquivo inválido")
    else:
        daily_sales = data

    # Filtra valores positivos
    daily_sales = [value for value in daily_sales if value > 0]

    if not daily_sales:
        return None, None, 0

    try:
        average = sum(daily_sales) / len(daily_sales)
        min_value = min(daily_sales)
        max_value = max(daily_sales)
    except ZeroDivisionError:
        return None, None, 0

    # Conta dias acima da média
    days_above_average = sum(bool(value > average) for value in daily_sales)

    return min_value, max_value, days_above_average



if __name__ == "__main__":
    try:
        json_result = analyze_sales("sales.json")
        xml_result = analyze_sales("sales.xml")

        print(f"JSON Result: {json_result}")
        print(f"XML Result: {xml_result}")
    except ValueError as e:
        print(f"Erro: {e}")
