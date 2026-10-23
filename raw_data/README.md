# Raw data

This folder held the emission reduction spreadsheets and monitoring reports that the values in
`methodology_data.xlsx` were transcribed from. The files are not included in this repository: they
are third-party registry documents, some of them contain personal data of project participants, and
the registries do not grant a licence to redistribute them. All of them can be downloaded from the
public registry pages listed below.

To rerun `extract_non_empty_cells.ipynb` or `extract_raw_filesize.ipynb`, download the files into
one subfolder per project, named as in the table, and prefix each file with its monitoring period,
`MP<n>_<original file name>` (e.g. `MP3_...xlsx`). The number `<n>` matches the `monitoring_period`
variable in `methodology_data.xlsx`. PDFs are ignored by the extraction notebooks.

Gold Standard registry URLs use the registry's internal record number, not the GS ID: for example,
GS10812 is at `projects/details/2769`.

| Folder | Registry | Project | Country | Registry page |
|---|---|---|---|---|
| `CDM_2898` | CDM PoA 2898 | Sichuan Rural Poor-Household Biogas Development Programme, CPA SCHHBG-2010-01 | CN | [CDM](https://cdm.unfccc.int/ProgrammeOfActivities/poa_db/5BGM96VOK3ATN4JPR70XSWIQ8CZH2F/view?cp=1) |
| `VCM_GS1239` | Gold Standard PoA GS1239 (GS1288) | same project as `CDM_2898` | CN | [GS PoA](https://registry.goldstandard.org/projects/details/148), [GS project](https://registry.goldstandard.org/projects/details/166), [documents](https://assurance-platform.goldstandard.org/project-documents/GS1288) |
| `CDM_4058` | CDM 4058 | Kolar Biogas Project | IN | [CDM](https://cdm.unfccc.int/Projects/DB/SGS-UKL1287587238.03/view) |
| `CDM_5415` | CDM 5415 | Biogas Support Program - Nepal Activity-3 | NP | [CDM](https://cdm.unfccc.int/Projects/DB/RWTUV1321009660.45/view) |
| `CDM_5416` | CDM 5416 | Biogas Support Program - Nepal Activity-4 | NP | [CDM](https://cdm.unfccc.int/Projects/DB/RWTUV1321020993.82/view) |
| `CDM_8275` | CDM 8275 | Micro Scale Biogas CDM Project of WORD | IN | [CDM](https://cdm.unfccc.int/Projects/DB/TUEV-RHEIN1353294073.62/view) |
| `CDM_9572` | CDM PoA 9572 | Nepal Biogas Support Program-PoA | NP | [CDM](https://cdm.unfccc.int/ProgrammeOfActivities/poa_db/7BSCYZMH2U05TWXFJKELND18PRQ96O/view), [issuance](https://cdm.unfccc.int/PoAIssuance/iss_db/poaiss339237849/view) |
| `VCM_GS4265` | Gold Standard GS4265 | WWF Biogas Nepal II | NP | [GS](https://registry.goldstandard.org/projects/details/730) |
| `VCM_GS10710` | Gold Standard GS10710 (PoA GS10655) | Promotion of clean cooking solutions in rural India by Infosys, VPA 1 | IN | [GS](https://registry.goldstandard.org/projects/details/2668) |
| `VCM_GS10812` | Gold Standard GS10812 | same project as `CDM_5415` | NP | [GS](https://registry.goldstandard.org/projects/details/2769) |
| `VCM_GS10813` | Gold Standard GS10813 | same project as `CDM_5416` | NP | [GS](https://registry.goldstandard.org/projects/details/2770) |
| `VCM_GS11394 (INCOMPLETE)` | Gold Standard GS11394 | India Dairy Biogas Program | IN | [GS](https://registry.goldstandard.org/projects/details/3415) |
| `VCM_GS11568` | Gold Standard GS11568 | Biodigesters program for a low-carbon livestock sector in Vietnam (BioLive) | VN | [GS](https://registry.goldstandard.org/projects/details/3660) |
| `VCM_GS11722` | Gold Standard GS11722 (PoA GS10655) | Promotion of clean cooking solutions in rural India by Infosys, VPA 2 | IN | [GS](https://registry.goldstandard.org/projects/details/3853) |

The full list of screened projects, with the reason each was included or excluded, is in the sheets
`CDM Projects Selection` and `GS Projects Selection` of `methodology_data.xlsx`.

## Notes on individual projects

- Three projects are registered with both the CDM and the Gold Standard: CDM PoA 2898 / GS1239,
  CDM 5415 / GS10812 and CDM 5416 / GS10813. The 14 folders therefore cover 11 projects.
- `VCM_GS1239`: the documents for monitoring periods 9 and 10 were missing from the Gold Standard
  registry, and Gold Standard staff could not provide them. The issued VER numbers were available,
  and the values for MP9 and MP10 were interpolated from MP8 and MP11.
- `VCM_GS11394 (INCOMPLETE)`: the folder held the project design document, a verification report
  and the validated ER spreadsheet, but no per-period monitoring files.
