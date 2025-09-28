from saim.designation.manager import AcronymManager


def create_abstract_from_inverted(r_ind: dict[str, tuple[int, ...]], /) -> str:
    last_ind = 0
    for ind_v in r_ind.values():
        new_m = max(ind_v)
        last_ind = new_m if new_m > last_ind else last_ind
    reversed_abs = ["" for _ in range(0, last_ind + 1)]
    for key, ind_v in r_ind.items():
        for pos in ind_v:
            reversed_abs[pos] = key
    return " ".join(reversed_abs)


def get_ccno_from_abstract(abstract: str, /) -> set[str]:
    acronym_manager = AcronymManager("v0.9.3")
    res_ccno = acronym_manager.extract_all_valid_ccno_from_text(abstract)
    return set(
        ccno.designation
        for ccno in res_ccno if ccno.acr != ""
    )