import requests
from n4m_straininfo_2025.lib.helper import create_abstract_from_inverted


OPEN_ALEX = "https://api.openalex.org/works/https://doi.org/10.1093/femsle/fnad030"


def get_abstract_from_open_alex() -> str:
    res = requests.get(OPEN_ALEX)
    if res.status_code == 200:
        return create_abstract_from_inverted(res.json()["abstract_inverted_index"])
    return ""


if __name__ == "__main__":
    print(get_abstract_from_open_alex())
