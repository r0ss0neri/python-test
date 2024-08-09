
from kywy.client.kawa_decorators import kawa_tool
import pandas as pd


@kawa_tool(
    inputs={'name': str},
    outputs={'gender': str},
    secrets={'open_ai_key': 'OPEN_AI_KEY'},
)
def execute(df: pd.DataFrame, open_ai_key: str) -> pd.DataFrame:
    open_ai_client = get_open_ai_client(open_ai_key)
    df['gender'] = df['name'].apply(lambda x: guess_gender(open_ai_client, x))
    return df


def get_open_ai_client(open_ai_key: str):
    return f'Some client, authenticated with {open_ai_key}'


def guess_gender(open_ai_client, name: str):
    return f'The guess using {open_ai_client} and {name}'
