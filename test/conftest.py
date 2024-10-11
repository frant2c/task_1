import pytest
import json

from src.controller import api_controller
from src.helper.file_reader import read_file
from src.model import Config
from src.helper.response_helper import get_data_from_html_response
from src.model.table_entries import TableEntries
from src.model.entry import Entry


@pytest.fixture
def get_popular_programming_languages_table(init_config) -> TableEntries:
    table = TableEntries()
    controller = api_controller.ApiController()

    response = controller.send_get_request(init_config.api_url)
    proceeded_response = get_data_from_html_response(
        response.text, init_config.table_name
    )
    for row in proceeded_response:
        entry = Entry.from_table_row(row)
        table.add_entry(entry)
    return table


@pytest.fixture
def init_config():
    j = json.loads(read_file("res/config.json"))
    return Config(**j)
