# Identifying Identifiers
### Harnessing StrainInfo’s tools to find and resolve strain designations in literature and metadata

## Hands-on

1. **Get abstract for DOI: 10.1093/femsle/fnad030**  
   - Use the **OpenAlex API** and **requests** to fetch the abstract.  
   - **OpenAlex API** - https://api.openalex.org/works/https://doi.org/10.1093/femsle/fnad030
   - Use the function **`create_abstract_from_inverted`** in `lib.helper` to process the response.
   - (Alternative): You can simply copy the abstract directly from [DOI: 10.1093/femsle/fnad030](https://doi.org/10.1093/femsle/fnad030).


2. **Find all culture collection numbers in the abstract**  
   - Extract culture collection numbers from the abstract using the function **`get_ccno_from_abstract`** in `lib.helper`.
   - (Optional): Try creating a **RegEx** pattern to extract culture collection numbers with the Acronym-Number structure (**DSM 72**).

3. **Find *Eubacterium limosum* in the abstract**  
   - Search for occurrences of **`Eubacterium limosum`** within the abstract text.
   - (Recommended): Use a simple string search approach, or refer to `tips.taxa_3`
  
4. **Find all strains in StrainInfo with the same CCNos found in the previous task**
   - Use the **StrainInfo API** to search for all matching strain IDs (`SI-ID`).
   - Documentation: [StrainInfo API](https://straininfo.dsmz.de/service)

5. **Check if the strains overlap with detected taxonomy**
   - Use the **StrainInfo API** to retrieve information about the strain.
   - Compare each strain's taxonomy with the detected taxonomy.
   - Print the following for each matched strain:
     - **SI-ID**
     - **Strain designation**
     - **Taxonomy**


## Resources

1. **Implement your solution**  
   The main implementation file for the solution can be found here:  
   `src/n4m_straininfo_2025/main.py`

2. **Recommended functions to use**  
   To save time, refer to the recommended functions in the library folder:  
   `src/n4m_straininfo_2025/lib`

3. **Tips for each step**  
   Helpful tips for each step are provided here (spoiler alert!):  
   `src/n4m_straininfo_2025/tips`

4. **StrainInfo API**  
   Access the StrainInfo API documentation for detailed information on how to interact with it:  
   [StrainInfo API](https://straininfo.dsmz.de/service)

5. **OpenAlex**  
   To fetch the abstract you could use OpenAlex API or directly copy the abstract from the webpage. Replace `{DOI}` with the desired DOI:  
   [OpenAlex API](https://api.openalex.org/works/https://doi.org/{DOI})


## Install - Linux

1. **Run `git clone https://github.com/artdotlis/N4M_STRAININFO_2025.git`** to download the repository.
2. **Run `make install`** to install dependencies and set up the environment.
3. **Run `make activate`** to activate the installation.


## Install - Windows/Linux/Mac

1. **Run `git clone https://github.com/artdotlis/N4M_STRAININFO_2025.git`** to download the repository.
2. **Run `python -m venv .venv`** to set up the environment.
3. Activate environment
   - Windows - **Run `.\.venv\Scripts\activate`**
   - Linux/Mac - **Run `source .venv/bin/activate`**
4. **Run `pip install .`** to install dependencies.


## Uninstall

1. **Run `make uninstall`** to remove everything from your system.


## Dependencies

1. git
2. python >= 3.13
3. Requests - `pip install requests`
4. SAIM - `pip install saim@git+https://github.com/LeibnizDSMZ/saim.git@v0.9.1`
5. CAFI - `pip install cafi@git+https://github.com/LeibnizDSMZ/cafi.git@v0.9.3`

---

## Best practices - API

- Retry on failure
- Schema checks - `pydantic`
- Timeout - respect the requests per second limits imposed by APIs
- Cache responses - `requests-cache`
- Thread-/Process-based parallelism or asynchronous calls
- Data license
- (Optional) robots.txt


## Issue - CCNo

**Complexity escalation**:

- Maintainability
- Performance
- High resource consumption

**Best practices**

- Use number as anchor - `(\d+(?:\D\d+)*)` 123-1.42
- Look left to search for an acronym and prefix
- (Optional) Look right to search for suffix

-> Requires knowledge about acronyms - CAFI


## Issue - Taxonomy

- Knowledge about taxonomy
- Search word-by-word


## Issue - False positives

**Found**
- ATCC 8486
- Eubacterium limosum
  
**Could these be false positives?**
- Verify with StrainInfo API


## Best practices - StrainInfo API

- Bundle requests - make one request instead of multiple


## Best practices - Verification

- Links reduce false positives