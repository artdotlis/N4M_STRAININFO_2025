import requests
from typing import Iterable
from n4m_straininfo_2025.tips.si_ids_4 import get_si_ids_for_ccnos
from n4m_straininfo_2025.tips.taxa_3 import get_e_limosum_from_abstract


STRAIN = "https://api.straininfo.dsmz.de/v2/data/strain/min/"


def get_matched_strains() -> Iterable[tuple[int, str, str]]:
    taxa = get_e_limosum_from_abstract()
    si_ids = get_si_ids_for_ccnos()
    res = requests.get(STRAIN + ",".join(str(si_id) for si_id in si_ids))
    if res.status_code == 200:
        for strain in res.json():
            if strain["strain"]["taxon"]["name"] in taxa:
                yield (
                    strain["strain"]["siID"], 
                    ",".join(
                        dep["designation"]
                        for dep in strain["strain"]["relation"]["deposit"]
                    ),
                    strain["strain"]["taxon"]["name"] 
                )


if __name__ == "__main__":
    for line in get_matched_strains():
        print("STRAIN:")
        print("\n\t".join(str(ele) for ele in line))
