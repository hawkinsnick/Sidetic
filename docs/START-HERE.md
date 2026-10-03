# Start researching Sidetic

1. [Download the AI starter](../ai-skill/Research-Starter.txt). If it opens as text, save the file.
2. Attach it to an AI assistant that can read text files.
3. Copy this message:

> Use the uploaded Sidetic research instructions. Confirm which files you can actually read. My question is [your question]. Tell me which evidence files I should supply next, then distinguish source readings, interpretations and unknowns. Cite record identifiers and source locators. Do not invent translations.

For a source-based question, [download this repository](https://github.com/hawkinsnick/Sidetic/archive/refs/heads/main.zip) and extract it. Upload `analysis/current-status.json`, `data/reference/records.json`, and `research/source-register.json`; add raw evidence from `data/upstream/ediana/response.json` when an exact source assertion needs checking. The index is a directory, not inscription evidence. A GitHub link does not establish that your assistant can read it.

Useful first question: Which records mention my chosen edition identifier, and where can I verify the reading in the captured source?

Save the repository commit, record ID, source URL, response row pointers and your question with any result. Cite eDiAna and the relevant edition, as well as this repository version for the digital processing. See [methods](METHODS.md) and [rights](../DATA-LICENSE-MATRIX.md).

This initial release supports examination of an attributed digital reference layer. Primary-edition/object verification and independent scholarly review remain outstanding. Updates on GitHub do not refresh files you already uploaded.
