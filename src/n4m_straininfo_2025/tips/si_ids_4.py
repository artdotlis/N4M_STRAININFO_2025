import requests
from n4m_straininfo_2025.lib.helper import get_ccno_from_abstract
from n4m_straininfo_2025.tips.abstract_1 import get_abstract_from_open_alex

SI_IDS = "https://api.straininfo.dsmz.de/v2/search/strain/cc_no/"


def get_si_ids_for_ccnos() -> set[str]:
    ccnos = get_ccno_from_abstract(get_abstract_from_open_alex())
    res = requests.get(SI_IDS + ",".join(ccnos))
    if res.status_code == 200:
        return set(res.json())
    return set()


if __name__ == "__main__":
    print(get_si_ids_for_ccnos())
