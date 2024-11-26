# Daniel Rosehill Open Source Custom LLM Configuration Library

[![View on GitHub](https://img.shields.io/badge/View%20on-GitHub-181717?logo=github&logoColor=white)](https://github.com/danielrosehill/Custom-LLM-Agents)

![Sloth making a new LLM](images/banner.webp)
 
## Individual LLM Agent Configurations

```
LLM Name
- about.md
- Config
-- config.md
-- config.json
```

- The `LLM Name` is the LLM's name.
- `about.md` provides a little bit of information about the custom LLM's intended purpose
- `config` houses configuration files provided in markdown and JSON format (the latter for machine-readibility and portability)

## About This Repository

This repository contains links to custom LLMs that I have build on top of ChatGPT (*although increasingly I'm exploring the use of other LLMs including Claude*).

I am finding amazing utility in creating custom LLMs for specific purposes (commonly those related to my professional life). 

However, while it lacks the ability of custom LLMs to quickly store detailed contextual information, prompt engineering is often enough to quickly and dramatically accelerate the value yielded from working with LLMs.

The overarching objective is to create a sort of "fleet" of LLM agents to help me manage various aspects of my work and personal lives.

Like everything I open-source, I'm doing so to make a small contribution to the collective sum of human knowledge. If you'd like to use any of these LLMs for whatever reason, you have my full permission to do so.

## File Formats

LLMs are organised into folders describing their purpose.

- LLMName/
  - Config/
    - config.txt
    - config.json
  - about.md
  
In this setup:

- `config.txt` is a text file containing the LLM configuration
- `config.json` is a JSON file containing the LLM configuration
- `about.md` is a markdown document describing the purpose of the LLM and providing other details intended for a human reader

You can use `JSON` directly in ChatLLM's custom LLM editor to effectively recreate any of these LLMs.

## Pronouns

For simplicity I use "he" when I need to refer to the user in a configuration text.

## Author

Daniel Rosehill  
(public at danielrosehill dot com)

## Licensing

All my GitHub repositories are licensed under [Creative Commons Attribution 4.0 International](https://creativecommons.org/licenses/by/4.0/).

### Summary of the License
The Creative Commons Attribution 4.0 International (CC BY 4.0) license allows others to:
- **Share**: Copy and redistribute the material in any medium or format.
- **Adapt**: Remix, transform, and build upon the material for any purpose, even commercially.

The licensor cannot revoke these freedoms as long as you follow the license terms.

#### License Terms
- **Attribution**: You must give appropriate credit, provide a link to the license, and indicate if changes were made. You may do so in any reasonable manner, but not in any way that suggests the licensor endorses you or your use.
- **No additional restrictions**: You may not apply legal terms or technological measures that legally restrict others from doing anything the license permits.

For the full legal code, please visit the [Creative Commons website](https://creativecommons.org/licenses/by/4.0/legalcode).
