import re
from typing import Final, Iterable
from n4m_straininfo_2025.tips.abstract_1 import get_abstract_from_open_alex

GEN_RE: Final[re.Pattern[str]] = re.compile(r"(\b[A-Z][a-z]+\b)")
SPE_RE: Final[re.Pattern[str]] = re.compile(r"^\s([a-z]+)")


def search_regex(text: str, /) -> Iterable[tuple[int, str]]:
    for sea in re.finditer(GEN_RE, text):
        res = sea.group(1)
        if isinstance(res, str) and res != "":
            yield sea.start(), res


def get_spe_name(spe_s: set[str] | None, gen: str, pos: int, full: str, /) -> str:
    if spe_s is None:
        return gen
    spe_m = SPE_RE.match(full[pos + len(gen) :])
    if spe_m is not None and spe_m.group(1) in spe_s:
        return f"{gen} {spe_m.group(1)}"
    return gen


def extract_taxa(tax_man: dict[str, set[str] | None], abstract: str, /,) -> Iterable[str]:
    if abstract != "":
        for pos_start, match in search_regex(abstract):
            if (gid := match.lower()) in tax_man:
                yield get_spe_name(tax_man[gid], match, pos_start, abstract)


def get_e_limosum_from_abstract() -> set[str]:
    return set(
        extract_taxa({"eubacterium": {"limosum"}}, get_abstract_from_open_alex())
    )


if __name__ == "__main__":
    print(get_e_limosum_from_abstract())
