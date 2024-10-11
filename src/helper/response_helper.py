from pyquery import PyQuery as pq


def get_programming_languages_table(response, table_name):
    d = pq(response)
    programming_languages_table = d("table")
    for table in programming_languages_table.items():
        caption = programming_languages_table.find("caption").text()
        if table_name in caption:
            return table


def get_data_from_html_response(response, table_name):
    table = get_programming_languages_table(response, table_name)
    rows = []
    for row in table.find("tbody").find("tr").items():
        row_data = [cell.text() for cell in row.find("td").items()]
        if len(row_data) == 0:
            continue
        rows.append(row_data)
    return rows
