import json
import xml.etree.ElementTree as ET


def analyze_sales(data):
    if isinstance(data, str):
        extension = data.split('.')[-1].lower()
        if extension == 'json':
            try:
                with open(data, 'r') as f:
                    data = json.load(f)
                    daily_sales = [item['value'] for item in data if 'value' in item]
            except (FileNotFoundError, json.JSONDecodeError) as e:
                raise ValueError(f"Error reading JSON file: {e}")
        elif extension == 'xml':
            try:
                tree = ET.parse(data)
                root = tree.getroot()
                daily_sales = [float(item.get('value', 0)) for item in root.iter('item')]
            except (ET.ParseError, FileNotFoundError) as e:
                raise ValueError(f"Error reading XML file: {e}")
        else:
            raise ValueError("Invalid file format")
    else:
        daily_sales = data

    daily_sales = [value for value in daily_sales if value > 0]

    if not daily_sales:
        return None, None, 0

    average = sum(daily_sales) / len(daily_sales)
    min_value = min(daily_sales)
    max_value = max(daily_sales)
    days_above_average = sum(1 for value in daily_sales if value > average)

    return min_value, max_value, days_above_average



if __name__ == "__main__":
    json_result = analyze_sales("sales_data.json")
    xml_result = analyze_sales("sales_data.xml")

    print("JSON Result:", json_result)
    print("XML Result:", xml_result)
