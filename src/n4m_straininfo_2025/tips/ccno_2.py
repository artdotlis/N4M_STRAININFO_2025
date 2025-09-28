from n4m_straininfo_2025.lib.helper import get_ccno_from_abstract
from n4m_straininfo_2025.tips.abstract_1 import get_abstract_from_open_alex

if __name__ == "__main__":
    print(get_ccno_from_abstract(get_abstract_from_open_alex()))
