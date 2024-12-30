# Daniel Rosehill Open Source Custom LLM Configuration Library

[![View on GitHub](https://img.shields.io/badge/View%20on-GitHub-181717?logo=github&logoColor=white)](https://github.com/danielrosehill/Custom-LLM-Agents)

This repository contains configuration files for large language model (LLM) assistants.

When I began this repository, most of the assistants were deployed onto the custom GPT platform. 

My approach to AI is to remain vendor agnostic whenever possible. So most of these have since been moved over to Hugging Face Chat. If the assistant has been set up on Hugging Face, then the link in the index will resolve to it.  

These assistants are pretty wide ranging. Some are tools I've created for my own personal uses. In other cases, they were created for clients or jobs. My experience working with assistants changes and grows over time much as their capabilities evolve. So any of the configurations really just reflect my current understanding for how to maximize the utility of these tools. I'm very interested in leveraging voice with these assistants, so that will be an increasing focus in the future.

## JSON Index

This badge links to the JSON index for the assistants, which is built dynamically whenever I push the repository. It can be used to provide a list of all the assistants in this repository to tools like "wizard" agents who guide to specific tools.

[![JSON Index](https://img.shields.io/badge/JSON%20Index-blue)](https://raw.githubusercontent.com/danielrosehill/Custom-LLM-Agents/refs/heads/main/assistants_index.json)


## Structure 
 
The GitHub link in the index simply opens the markdown file for that index configuration page. This is where I share the configuration as I've written it. Sometimes I'll include the iterations as I make them. 

I share these assistants on the hope that they might be useful to others!

![Sloth making a new LLM](images/banner.webp)

## Index
| Creation Date | Assistant Name | Repo Link | Use Now |
|---------------|----------------|-----------|---------|
| Dec 23 (2024) | A Day In GPT Land | [![View on GitHub](https://img.shields.io/badge/View%20on-GitHub-black?style=for-the-badge&logo=github&logoColor=white)](ai-related/a-day-in-gpt-land.md) | [![View on Hugging Face](https://img.shields.io/badge/View%20on-Hugging%20Face-ff9b34?style=for-the-badge&logo=huggingface&logoColor=white)](https://hf.co/chat/assistant/675b7e9621499ff25259eabb) |
| Dec 23 (2024) | AI Career Ideation Tool | [![View on GitHub](https://img.shields.io/badge/View%20on-GitHub-black?style=for-the-badge&logo=github&logoColor=white)](ai-related/ai-career-ideator.md) | [![View on Hugging Face](https://img.shields.io/badge/View%20on-Hugging%20Face-ff9b34?style=for-the-badge&logo=huggingface&logoColor=white)](https://hf.co/chat/assistant/6701df91cb513bb057ded417) |
| Dec 23 (2024) | AI Tech Advisor | [![View on GitHub](https://img.shields.io/badge/View%20on-GitHub-black?style=for-the-badge&logo=github&logoColor=white)](ai-related/ai-tech-advisor.md) | [![View on Hugging Face](https://img.shields.io/badge/View%20on-Hugging%20Face-ff9b34?style=for-the-badge&logo=huggingface&logoColor=white)](https://hf.co/chat/assistant/6701df2bcb513bb057ded3a8) |
| Dec 23 (2024) | Acronym To Organisation | [![View on GitHub](https://img.shields.io/badge/View%20on-GitHub-black?style=for-the-badge&logo=github&logoColor=white)](utilities/acronym_to_organisation.md) | [![View on Hugging Face](https://img.shields.io/badge/View%20on-Hugging%20Face-ff9b34?style=for-the-badge&logo=huggingface&logoColor=white)](https://hf.co/chat/assistant/67698cab384ae3573032b658) |
| Dec 23 (2024) | Agenda Creation Assistant | [![View on GitHub](https://img.shields.io/badge/View%20on-GitHub-black?style=for-the-badge&logo=github&logoColor=white)](professional/meeting-organisers/agenda-assistant-v2.md) | [![View on Hugging Face](https://img.shields.io/badge/View%20on-Hugging%20Face-ff9b34?style=for-the-badge&logo=huggingface&logoColor=white)](https://hf.co/chat/assistant/6768a5297eba7923b7af64f6) |
| Dec 23 (2024) | Airport Food Finder | [![View on GitHub](https://img.shields.io/badge/View%20on-GitHub-black?style=for-the-badge&logo=github&logoColor=white)](travel/airport-food-options.md) | [![View on Hugging Face](https://img.shields.io/badge/View%20on-Hugging%20Face-ff9b34?style=for-the-badge&logo=huggingface&logoColor=white)](https://hf.co/chat/assistant/6769980a6f424cd438c4fdd3) |
| Dec 29 (2024) | Aliexpress Product Finder | [![View on GitHub](https://img.shields.io/badge/View%20on-GitHub-black?style=for-the-badge&logo=github&logoColor=white)](shopping/aliexpress-finder.md) |  |
| Dec 13 (2024) | Assistant Team Manager | [![View on GitHub](https://img.shields.io/badge/View%20on-GitHub-black?style=for-the-badge&logo=github&logoColor=white)](llms/agent-fleets/assistant-team-manager.md) | [![View on Hugging Face](https://img.shields.io/badge/View%20on-Hugging%20Face-ff9b34?style=for-the-badge&logo=huggingface&logoColor=white)](https://hf.co/chat/assistant/675b82b18892019207cd0533) |
| Dec 23 (2024) | Automate My Workflow | [![View on GitHub](https://img.shields.io/badge/View%20on-GitHub-black?style=for-the-badge&logo=github&logoColor=white)](productivity/automation/automate-my-workflow.md) | [![View on Hugging Face](https://img.shields.io/badge/View%20on-Hugging%20Face-ff9b34?style=for-the-badge&logo=huggingface&logoColor=white)](https://hf.co/chat/assistant/67579ee97ab12b601c7fd9fd) |
| Dec 23 (2024) | BLUF Email Reformatter | [![View on GitHub](https://img.shields.io/badge/View%20on-GitHub-black?style=for-the-badge&logo=github&logoColor=white)](writing/email-assistants/bluf-email-generator.md) | [![View on Hugging Face](https://img.shields.io/badge/View%20on-Hugging%20Face-ff9b34?style=for-the-badge&logo=huggingface&logoColor=white)](https://hf.co/chat/assistant/6768d60a802ca8f9d4600557) |
| Dec 30 (2024) | Background Briefer (General Purpose) | [![View on GitHub](https://img.shields.io/badge/View%20on-GitHub-black?style=for-the-badge&logo=github&logoColor=white)](utilities/background-briefer.md) | [![View on Hugging Face](https://img.shields.io/badge/View%20on-Hugging%20Face-ff9b34?style=for-the-badge&logo=huggingface&logoColor=white)](https://hf.co/chat/assistant/6772b26a3e564ef7e918c6f9) |
| Dec 23 (2024) | Backoffice Development Copilot | [![View on GitHub](https://img.shields.io/badge/View%20on-GitHub-black?style=for-the-badge&logo=github&logoColor=white)](development/backoffice-development-copilot.md) |  |
| Dec 23 (2024) | Backoffice LLM Agent Ideation Tool | [![View on GitHub](https://img.shields.io/badge/View%20on-GitHub-black?style=for-the-badge&logo=github&logoColor=white)](development/backoffice-gpt-creation-assistant.md) |  |
| Dec 23 (2024) | Backup Coach | [![View on GitHub](https://img.shields.io/badge/View%20on-GitHub-black?style=for-the-badge&logo=github&logoColor=white)](tech-general/backup-coach.md) | [![View on Hugging Face](https://img.shields.io/badge/View%20on-Hugging%20Face-ff9b34?style=for-the-badge&logo=huggingface&logoColor=white)](https://hf.co/chat/assistant/6701e064b41b0e86f9d5acdd) |
| Dec 23 (2024) | Backup Evaluation Assistant | [![View on GitHub](https://img.shields.io/badge/View%20on-GitHub-black?style=for-the-badge&logo=github&logoColor=white)](tech-general/backup-evaluation-assistant.md) | [![View on Hugging Face](https://img.shields.io/badge/View%20on-Hugging%20Face-ff9b34?style=for-the-badge&logo=huggingface&logoColor=white)](https://hf.co/chat/assistant/67699879480189a47ff7374f) |
| Dec 23 (2024) | Bad Jokes Generation Assistant | [![View on GitHub](https://img.shields.io/badge/View%20on-GitHub-black?style=for-the-badge&logo=github&logoColor=white)](for-fun/bad-jokes-galore.md) | [![View on Hugging Face](https://img.shields.io/badge/View%20on-Hugging%20Face-ff9b34?style=for-the-badge&logo=huggingface&logoColor=white)](https://hf.co/chat/assistant/674d41dfcf1f9846ac2d50e0) |
| Dec 23 (2024) | Beer Tap Identifier (Vision) | [![View on GitHub](https://img.shields.io/badge/View%20on-GitHub-black?style=for-the-badge&logo=github&logoColor=white)](food-and-drink/beer-tap-identifier.md) | [![View on Hugging Face](https://img.shields.io/badge/View%20on-Hugging%20Face-ff9b34?style=for-the-badge&logo=huggingface&logoColor=white)](https://hf.co/chat/assistant/674d41200a1ac006d7354790) |
| Dec 23 (2024) | Boss Update Batcher | [![View on GitHub](https://img.shields.io/badge/View%20on-GitHub-black?style=for-the-badge&logo=github&logoColor=white)](productivity/boss-update-batcher.md) | [![View on Hugging Face](https://img.shields.io/badge/View%20on-Hugging%20Face-ff9b34?style=for-the-badge&logo=huggingface&logoColor=white)](https://hf.co/chat/assistant/67579f6a2526a3ccbf0c76ac) |
| Dec 23 (2024) | Brainstorming Assistant | [![View on GitHub](https://img.shields.io/badge/View%20on-GitHub-black?style=for-the-badge&logo=github&logoColor=white)](productivity/brainstorming/brainstorming-assistant.md) | [![View on Hugging Face](https://img.shields.io/badge/View%20on-Hugging%20Face-ff9b34?style=for-the-badge&logo=huggingface&logoColor=white)](https://hf.co/chat/assistant/6769978f384ae3573032b7d2) |
| Dec 23 (2024) | Brainstorming Coach | [![View on GitHub](https://img.shields.io/badge/View%20on-GitHub-black?style=for-the-badge&logo=github&logoColor=white)](productivity/brainstorming/brainstorming-coach.md) | [![View on Hugging Face](https://img.shields.io/badge/View%20on-Hugging%20Face-ff9b34?style=for-the-badge&logo=huggingface&logoColor=white)](https://hf.co/chat/assistant/676998ca0efd1a5bae6fddd7) |
| Dec 23 (2024) | Brand Reliability Checker | [![View on GitHub](https://img.shields.io/badge/View%20on-GitHub-black?style=for-the-badge&logo=github&logoColor=white)](research/purchasing/brand-reliability-checker.md) | [![View on Hugging Face](https://img.shields.io/badge/View%20on-Hugging%20Face-ff9b34?style=for-the-badge&logo=huggingface&logoColor=white)](https://hf.co/chat/assistant/6769991f83d3037536d6cdf4) |
| Dec 23 (2024) | Brief Writing Assistant | [![View on GitHub](https://img.shields.io/badge/View%20on-GitHub-black?style=for-the-badge&logo=github&logoColor=white)](writing/brief-generator.md) | [![View on Hugging Face](https://img.shields.io/badge/View%20on-Hugging%20Face-ff9b34?style=for-the-badge&logo=huggingface&logoColor=white)](https://hf.co/chat/assistant/676999c853155b6690e871f2) |
| Dec 23 (2024) | Broken Link Retrieval Helper | [![View on GitHub](https://img.shields.io/badge/View%20on-GitHub-black?style=for-the-badge&logo=github&logoColor=white)](utilities/broken-link-helper.md) | [![View on Hugging Face](https://img.shields.io/badge/View%20on-Hugging%20Face-ff9b34?style=for-the-badge&logo=huggingface&logoColor=white)](https://hf.co/chat/assistant/6757a04fca07b5d6830df541) |
| Dec 23 (2024) | Business Continuity Advisor | [![View on GitHub](https://img.shields.io/badge/View%20on-GitHub-black?style=for-the-badge&logo=github&logoColor=white)](preparedness/business-continuity/business-continuity-advisor.md) | [![View on Hugging Face](https://img.shields.io/badge/View%20on-Hugging%20Face-ff9b34?style=for-the-badge&logo=huggingface&logoColor=white)](https://hf.co/chat/assistant/675b07eeb36bc6d22c25ee37) |
| Dec 23 (2024) | CSV Taxonomy Generator | [![View on GitHub](https://img.shields.io/badge/View%20on-GitHub-black?style=for-the-badge&logo=github&logoColor=white)](data/taxonomies/csv-taxonomy-generator.md) | [![View on Hugging Face](https://img.shields.io/badge/View%20on-Hugging%20Face-ff9b34?style=for-the-badge&logo=huggingface&logoColor=white)](https://hf.co/chat/assistant/67699d9753155b6690e8726d) |
| Dec 23 (2024) | CSV To Markdown Reformatting Assistant | [![View on GitHub](https://img.shields.io/badge/View%20on-GitHub-black?style=for-the-badge&logo=github&logoColor=white)](data/data-formatting/csv-to-markdown-reformatter.md) | [![View on Hugging Face](https://img.shields.io/badge/View%20on-Hugging%20Face-ff9b34?style=for-the-badge&logo=huggingface&logoColor=white)](https://hf.co/chat/assistant/67699ded6f424cd438c4fe97) |
| Dec 23 (2024) | CV/Resume Hole-Picker | [![View on GitHub](https://img.shields.io/badge/View%20on-GitHub-black?style=for-the-badge&logo=github&logoColor=white)](career/job-hunt-helpers/resume-hole-picker.md) | [![View on Hugging Face](https://img.shields.io/badge/View%20on-Hugging%20Face-ff9b34?style=for-the-badge&logo=huggingface&logoColor=white)](https://hf.co/chat/assistant/6768aceb6f424cd438c4e0d0) |
| Dec 23 (2024) | Career Pivot Ideation Coach | [![View on GitHub](https://img.shields.io/badge/View%20on-GitHub-black?style=for-the-badge&logo=github&logoColor=white)](career/career-pivot-ideator.md) | [![View on Hugging Face](https://img.shields.io/badge/View%20on-Hugging%20Face-ff9b34?style=for-the-badge&logo=huggingface&logoColor=white)](https://hf.co/chat/assistant/67697e1714a1a002763381ab) |
| Dec 27 (2024) | Catalog Image Recommendation Bot | [![View on GitHub](https://img.shields.io/badge/View%20on-GitHub-black?style=for-the-badge&logo=github&logoColor=white)](shopping/image-recommender.md) | [![View on Hugging Face](https://img.shields.io/badge/View%20on-Hugging%20Face-ff9b34?style=for-the-badge&logo=huggingface&logoColor=white)](https://hf.co/chat/assistant/676ebd5f6d5e4d03120d1ce1) |
| Dec 29 (2024) | Code Generation Prompt Formatted (From Voice) | [![View on GitHub](https://img.shields.io/badge/View%20on-GitHub-black?style=for-the-badge&logo=github&logoColor=white)](prompt-eng/voice-prompting/voice-prompt-for-software.md) | [![View on Hugging Face](https://img.shields.io/badge/View%20on-Hugging%20Face-ff9b34?style=for-the-badge&logo=huggingface&logoColor=white)](https://hf.co/chat/assistant/6770988da7bef1c4ff8c41ee) |
| Dec 23 (2024) | Company Exploration Tool (Topic To Copmany) | [![View on GitHub](https://img.shields.io/badge/View%20on-GitHub-black?style=for-the-badge&logo=github&logoColor=white)](career/company-explorer.md) | [![View on Hugging Face](https://img.shields.io/badge/View%20on-Hugging%20Face-ff9b34?style=for-the-badge&logo=huggingface&logoColor=white)](https://hf.co/chat/assistant/6768fa2ba465d8e1f2841d02) |
| Dec 24 (2024) | Company Hiring Researcher | [![View on GitHub](https://img.shields.io/badge/View%20on-GitHub-black?style=for-the-badge&logo=github&logoColor=white)](research/career-and-job-hunting/company-hiring-researcher.md) | [![View on Hugging Face](https://img.shields.io/badge/View%20on-Hugging%20Face-ff9b34?style=for-the-badge&logo=huggingface&logoColor=white)](https://hf.co/chat/assistant/676ab339589078e4a21a332f) |
| Dec 23 (2024) | Company News Retrieval Assistant | [![View on GitHub](https://img.shields.io/badge/View%20on-GitHub-black?style=for-the-badge&logo=github&logoColor=white)](research/company-news-retriever.md) | [![View on Hugging Face](https://img.shields.io/badge/View%20on-Hugging%20Face-ff9b34?style=for-the-badge&logo=huggingface&logoColor=white)](https://hf.co/chat/assistant/6769775b53155b6690e86d5c) |
| Dec 23 (2024) | Company Remote Job Researcher | [![View on GitHub](https://img.shields.io/badge/View%20on-GitHub-black?style=for-the-badge&logo=github&logoColor=white)](career/job-hunt-helpers/company-remote-info.md) | [![View on Hugging Face](https://img.shields.io/badge/View%20on-Hugging%20Face-ff9b34?style=for-the-badge&logo=huggingface&logoColor=white)](https://hf.co/chat/assistant/6768a3b54d6ce65716485c94) |
| Dec 23 (2024) | Company Screener / Red Flag Identification Assistant | [![View on GitHub](https://img.shields.io/badge/View%20on-GitHub-black?style=for-the-badge&logo=github&logoColor=white)](career/job-hunt-helpers/company-screener.md) | [![View on Hugging Face](https://img.shields.io/badge/View%20on-Hugging%20Face-ff9b34?style=for-the-badge&logo=huggingface&logoColor=white)](https://hf.co/chat/assistant/6768ae79384ae35730329bd9) |
| Dec 17 (2024) | Company background research helper | [![View on GitHub](https://img.shields.io/badge/View%20on-GitHub-black?style=for-the-badge&logo=github&logoColor=white)](research/career-and-job-hunting/company-backgrounder.md) | [![View on Hugging Face](https://img.shields.io/badge/View%20on-Hugging%20Face-ff9b34?style=for-the-badge&logo=huggingface&logoColor=white)](https://hf.co/chat/assistant/675b722cb491864d969872db) |
| Dec 23 (2024) | Competitive Landscape Analysis Assistant | [![View on GitHub](https://img.shields.io/badge/View%20on-GitHub-black?style=for-the-badge&logo=github&logoColor=white)](career/job-hunt-helpers/competitive-landscape-mapper.md) | [![View on Hugging Face](https://img.shields.io/badge/View%20on-Hugging%20Face-ff9b34?style=for-the-badge&logo=huggingface&logoColor=white)](https://hf.co/chat/assistant/6768b9091936c35ab02be05a) |
| Dec 18 (2024) | Config Text For Config Text Generation Assistant (!) | [![View on GitHub](https://img.shields.io/badge/View%20on-GitHub-black?style=for-the-badge&logo=github&logoColor=white)](llm-tools/config-test-creator.md) | [![View on Hugging Face](https://img.shields.io/badge/View%20on-Hugging%20Face-ff9b34?style=for-the-badge&logo=huggingface&logoColor=white)](https://hf.co/chat/assistant/6762c852203d2dc056b1e4fa) |
| Dec 18 (2024) | Context Data Development Helper | [![View on GitHub](https://img.shields.io/badge/View%20on-GitHub-black?style=for-the-badge&logo=github&logoColor=white)](llm-tools/context/context-data-ideator.md) | [![View on Hugging Face](https://img.shields.io/badge/View%20on-Hugging%20Face-ff9b34?style=for-the-badge&logo=huggingface&logoColor=white)](https://hf.co/chat/assistant/6762d5b9bb93201f4b42bcbd) |
| Dec 23 (2024) | Context Data Extraction Tool | [![View on GitHub](https://img.shields.io/badge/View%20on-GitHub-black?style=for-the-badge&logo=github&logoColor=white)](llm-tools/context/context-data-extractor.md) | [![View on Hugging Face](https://img.shields.io/badge/View%20on-Hugging%20Face-ff9b34?style=for-the-badge&logo=huggingface&logoColor=white)](https://hf.co/chat/assistant/6769775b53155b6690e86d5c) |
| Dec 23 (2024) | Context Generation Assistant (Voice Workflow) | [![View on GitHub](https://img.shields.io/badge/View%20on-GitHub-black?style=for-the-badge&logo=github&logoColor=white)](llm-tools/voice-helpers/voice-context-data-helper.md) | [![View on Hugging Face](https://img.shields.io/badge/View%20on-Hugging%20Face-ff9b34?style=for-the-badge&logo=huggingface&logoColor=white)](https://hf.co/chat/assistant/6768d07954c6d31d32d3786e) |
| Dec 18 (2024) | Contextual Data Generation Assistant | [![View on GitHub](https://img.shields.io/badge/View%20on-GitHub-black?style=for-the-badge&logo=github&logoColor=white)](llm-tools/context/context-snippet-generator.md) | [![View on Hugging Face](https://img.shields.io/badge/View%20on-Hugging%20Face-ff9b34?style=for-the-badge&logo=huggingface&logoColor=white)](https://hf.co/chat/assistant/67624b04c43bc16e05331a06) |
| Dec 24 (2024) | Cornelius The Sloth | [![View on GitHub](https://img.shields.io/badge/View%20on-GitHub-black?style=for-the-badge&logo=github&logoColor=white)](for-fun/corn-the-sloth.md) | [![View on Hugging Face](https://img.shields.io/badge/View%20on-Hugging%20Face-ff9b34?style=for-the-badge&logo=huggingface&logoColor=white)](https://hf.co/chat/assistant/676abda472e9b857f61628db) |
| Dec 23 (2024) | Custom GPT To Hugging Face Chat Conversion Utility | [![View on GitHub](https://img.shields.io/badge/View%20on-GitHub-black?style=for-the-badge&logo=github&logoColor=white)](utilities/chatgpt-to-hf-chat.md) | [![View on Hugging Face](https://img.shields.io/badge/View%20on-Hugging%20Face-ff9b34?style=for-the-badge&logo=huggingface&logoColor=white)](https://hf.co/chat/assistant/675b0744903247ce54987b69) |
| Dec 23 (2024) | Daily Schedule Manager | [![View on GitHub](https://img.shields.io/badge/View%20on-GitHub-black?style=for-the-badge&logo=github&logoColor=white)](organisation/workflow-planners/daily-schedule-manager.md) | [![View on Hugging Face](https://img.shields.io/badge/View%20on-Hugging%20Face-ff9b34?style=for-the-badge&logo=huggingface&logoColor=white)](https://hf.co/chat/assistant/67699d17685abc1df63adefc) |
| Dec 23 (2024) | Daniel's Email Optimiser | [![View on GitHub](https://img.shields.io/badge/View%20on-GitHub-black?style=for-the-badge&logo=github&logoColor=white)](writing/email-assistants/email-optimiser.md) | [![View on Hugging Face](https://img.shields.io/badge/View%20on-Hugging%20Face-ff9b34?style=for-the-badge&logo=huggingface&logoColor=white)](https://hf.co/chat/assistant/67699c8f45672804f8d00840) |
| Dec 23 (2024) | Data Organisation Sidekick | [![View on GitHub](https://img.shields.io/badge/View%20on-GitHub-black?style=for-the-badge&logo=github&logoColor=white)](data/data-organisation/data-organisation-genie.md) |  |
| Dec 23 (2024) | Data Relationship Utility | [![View on GitHub](https://img.shields.io/badge/View%20on-GitHub-black?style=for-the-badge&logo=github&logoColor=white)](data/data-utilities/data-relationships-utility.md) |  |
| Dec 23 (2024) | Data Visualisation & Storytelling Guide | [![View on GitHub](https://img.shields.io/badge/View%20on-GitHub-black?style=for-the-badge&logo=github&logoColor=white)](data/data-visualisation/data-visualisation-and-storytelling-guide.md) | [![View on Hugging Face](https://img.shields.io/badge/View%20on-Hugging%20Face-ff9b34?style=for-the-badge&logo=huggingface&logoColor=white)](https://hf.co/chat/assistant/675b7afc21499ff25259e9c2) |
| Dec 23 (2024) | Data Visualisation Ideator (Alternatives Suggester) | [![View on GitHub](https://img.shields.io/badge/View%20on-GitHub-black?style=for-the-badge&logo=github&logoColor=white)](data/data-visualisation/data-vis-ideator.md) | [![View on Hugging Face](https://img.shields.io/badge/View%20on-Hugging%20Face-ff9b34?style=for-the-badge&logo=huggingface&logoColor=white)](https://hf.co/chat/assistant/6769b4923055fc7410147914) |
| Nov 26 (2024) | Databases Are Better Than Spreadsheets | [![View on GitHub](https://img.shields.io/badge/View%20on-GitHub-black?style=for-the-badge&logo=github&logoColor=white)](data/education/databases-are-better-than-spreadsheets.md) |  |
| Dec 14 (2024) | Decluttering | [![View on GitHub](https://img.shields.io/badge/View%20on-GitHub-black?style=for-the-badge&logo=github&logoColor=white)](helpers/decluttering.md) | [![View on Hugging Face](https://img.shields.io/badge/View%20on-Hugging%20Face-ff9b34?style=for-the-badge&logo=huggingface&logoColor=white)](https://hf.co/chat/assistant/675d552a074837b9c77190a9) |
| Dec 23 (2024) | Dictated Text Fixer | [![View on GitHub](https://img.shields.io/badge/View%20on-GitHub-black?style=for-the-badge&logo=github&logoColor=white)](voice/dictated-text-fixer.md) | [![View on Hugging Face](https://img.shields.io/badge/View%20on-Hugging%20Face-ff9b34?style=for-the-badge&logo=huggingface&logoColor=white)](https://hf.co/chat/assistant/675d323cd74aa23d31f4fd78) |
| Nov 26 (2024) | Disaster Debrief Assistant | [![View on GitHub](https://img.shields.io/badge/View%20on-GitHub-black?style=for-the-badge&logo=github&logoColor=white)](preparedness/disaster-debrief-assistant.md) |  |
| Nov 26 (2024) | Disaster Preparedness Expert | [![View on GitHub](https://img.shields.io/badge/View%20on-GitHub-black?style=for-the-badge&logo=github&logoColor=white)](preparedness/disaster-preparedness-expert.md) |  |
| Nov 26 (2024) | Disaster Scenario Ideator | [![View on GitHub](https://img.shields.io/badge/View%20on-GitHub-black?style=for-the-badge&logo=github&logoColor=white)](preparedness/disaster-scenario-ideator.md) |  |
| Nov 26 (2024) | Do We Need This Meeting | [![View on GitHub](https://img.shields.io/badge/View%20on-GitHub-black?style=for-the-badge&logo=github&logoColor=white)](productivity/do-we-need-this-meeting.md) |  |
| Dec 23 (2024) | Docker Compose Analysis Tool | [![View on GitHub](https://img.shields.io/badge/View%20on-GitHub-black?style=for-the-badge&logo=github&logoColor=white)](utilities/docker-compose-analyser.md) | [![View on Hugging Face](https://img.shields.io/badge/View%20on-Hugging%20Face-ff9b34?style=for-the-badge&logo=huggingface&logoColor=white)](https://hf.co/chat/assistant/675b05578892019207cce14a) |
| Dec 23 (2024) | Document Anonymisation Tool | [![View on GitHub](https://img.shields.io/badge/View%20on-GitHub-black?style=for-the-badge&logo=github&logoColor=white)](writing/anonimisation/doc-anon-tool.md) | [![View on Hugging Face](https://img.shields.io/badge/View%20on-Hugging%20Face-ff9b34?style=for-the-badge&logo=huggingface&logoColor=white)](https://hf.co/chat/assistant/6760b39606189c9ac0656dd6) |
| Dec 23 (2024) | Document Stats & Numbers Miner | [![View on GitHub](https://img.shields.io/badge/View%20on-GitHub-black?style=for-the-badge&logo=github&logoColor=white)](data/data-mining/document-stats-and-numbers-miner.md) | [![View on Hugging Face](https://img.shields.io/badge/View%20on-Hugging%20Face-ff9b34?style=for-the-badge&logo=huggingface&logoColor=white)](https://hf.co/chat/assistant/67699a6b83d3037536d6ce24) |
| Dec 12 (2024) | Document Table Finder | [![View on GitHub](https://img.shields.io/badge/View%20on-GitHub-black?style=for-the-badge&logo=github&logoColor=white)](data/data-discovery/document-table-finder.md) | [![View on Hugging Face](https://img.shields.io/badge/View%20on-Hugging%20Face-ff9b34?style=for-the-badge&logo=huggingface&logoColor=white)](https://hf.co/chat/assistant/6757a52e2526a3ccbf0c7ac5) |
| Dec 23 (2024) | Dummy Data Generator - CSV | [![View on GitHub](https://img.shields.io/badge/View%20on-GitHub-black?style=for-the-badge&logo=github&logoColor=white)](data/data-utilities/dummy--csv-data-generator.md) | [![View on Hugging Face](https://img.shields.io/badge/View%20on-Hugging%20Face-ff9b34?style=for-the-badge&logo=huggingface&logoColor=white)](https://hf.co/chat/assistant/67699ac945672804f8d00806) |
| Nov 26 (2024) | Dummy Tech Project Ideator | [![View on GitHub](https://img.shields.io/badge/View%20on-GitHub-black?style=for-the-badge&logo=github&logoColor=white)](data/data-utilities/dummy-tech-project-ideator.md) |  |
| Dec 12 (2024) | Eco Ninja V3 - Sustsainability Data Retrieval Genie | [![View on GitHub](https://img.shields.io/badge/View%20on-GitHub-black?style=for-the-badge&logo=github&logoColor=white)](sustainability/econinja/eco-ninja-v3.md) | [![View on Hugging Face](https://img.shields.io/badge/View%20on-Hugging%20Face-ff9b34?style=for-the-badge&logo=huggingface&logoColor=white)](https://hf.co/chat/assistant/674dfb83203be059afb0da43) |
| Nov 26 (2024) | Email Disaster | [![View on GitHub](https://img.shields.io/badge/View%20on-GitHub-black?style=for-the-badge&logo=github&logoColor=white)](for-fun/email-disaster.md) |  |
| Dec 23 (2024) | Email Shortener | [![View on GitHub](https://img.shields.io/badge/View%20on-GitHub-black?style=for-the-badge&logo=github&logoColor=white)](writing/email-assistants/email-shortener.md) | [![View on Hugging Face](https://img.shields.io/badge/View%20on-Hugging%20Face-ff9b34?style=for-the-badge&logo=huggingface&logoColor=white)](https://hf.co/chat/assistant/67696e6bc8c3abc5c7a8ec14) |
| Dec 24 (2024) | Email Thread Reader | [![View on GitHub](https://img.shields.io/badge/View%20on-GitHub-black?style=for-the-badge&logo=github&logoColor=white)](professional/email-thread-reader.md) | [![View on Hugging Face](https://img.shields.io/badge/View%20on-Hugging%20Face-ff9b34?style=for-the-badge&logo=huggingface&logoColor=white)](https://hf.co/chat/assistant/676aaddd9aa1f60df34a30e5) |
| Nov 26 (2024) | Emergency Shelter Finding Guidance | [![View on GitHub](https://img.shields.io/badge/View%20on-GitHub-black?style=for-the-badge&logo=github&logoColor=white)](preparedness/emergency-shelter-finding-guidance.md) |  |
| Nov 26 (2024) | Example Output | [![View on GitHub](https://img.shields.io/badge/View%20on-GitHub-black?style=for-the-badge&logo=github&logoColor=white)](sustainability/data-discovery/ghg-emissions-data.md) |  |
| Nov 26 (2024) | Find A Bar Near Me | [![View on GitHub](https://img.shields.io/badge/View%20on-GitHub-black?style=for-the-badge&logo=github&logoColor=white)](travel/find-a-bar-near-me.md) |  |
| Dec 23 (2024) | Find Me A License | [![View on GitHub](https://img.shields.io/badge/View%20on-GitHub-black?style=for-the-badge&logo=github&logoColor=white)](utilities/find-a-license.md) | [![View on Hugging Face](https://img.shields.io/badge/View%20on-Hugging%20Face-ff9b34?style=for-the-badge&logo=huggingface&logoColor=white)](https://hf.co/chat/assistant/6769ae205ea5dbac8674c55d) |
| Nov 26 (2024) | Find Me Compatible Hardware | [![View on GitHub](https://img.shields.io/badge/View%20on-GitHub-black?style=for-the-badge&logo=github&logoColor=white)](research/purchasing/find-me-compatible-hardware.md) |  |
| Dec 23 (2024) | Find Me Guinness! | [![View on GitHub](https://img.shields.io/badge/View%20on-GitHub-black?style=for-the-badge&logo=github&logoColor=white)](travel/find-me-a-guinness.md) |  |
| Dec 23 (2024) | Freeform Writing Converter | [![View on GitHub](https://img.shields.io/badge/View%20on-GitHub-black?style=for-the-badge&logo=github&logoColor=white)](writing/freeform-text-handlers/freeform-converter.md) | [![View on Hugging Face](https://img.shields.io/badge/View%20on-Hugging%20Face-ff9b34?style=for-the-badge&logo=huggingface&logoColor=white)](https://hf.co/chat/assistant/670cfcba1f325eee148c7c19) |
| Dec 24 (2024) | GHG Emissions Discovery Assistant | [![View on GitHub](https://img.shields.io/badge/View%20on-GitHub-black?style=for-the-badge&logo=github&logoColor=white)](sustainability/sustainability-reports/ghg-report-finder-v2.md) | [![View on Hugging Face](https://img.shields.io/badge/View%20on-Hugging%20Face-ff9b34?style=for-the-badge&logo=huggingface&logoColor=white)](https://hf.co/chat/assistant/676afd4089e2b65a406900b8) |
| Dec 24 (2024) | GHG Emissions Report Analyst | [![View on GitHub](https://img.shields.io/badge/View%20on-GitHub-black?style=for-the-badge&logo=github&logoColor=white)](sustainability/emissions-report-analyst.md) | [![View on Hugging Face](https://img.shields.io/badge/View%20on-Hugging%20Face-ff9b34?style=for-the-badge&logo=huggingface&logoColor=white)](https://hf.co/chat/assistant/676aacc8f48cb11efe7f02ea) |
| Nov 26 (2024) | Gaslighting Guardian | [![View on GitHub](https://img.shields.io/badge/View%20on-GitHub-black?style=for-the-badge&logo=github&logoColor=white)](health/mental-health/gaslighting-guardian.md) |  |
| Dec 23 (2024) | General Purpose Personal Assistant | [![View on GitHub](https://img.shields.io/badge/View%20on-GitHub-black?style=for-the-badge&logo=github&logoColor=white)](rag-enabled/general-personal-assistant.md) |  |
| Nov 26 (2024) | Geopolitical Brief Generator | [![View on GitHub](https://img.shields.io/badge/View%20on-GitHub-black?style=for-the-badge&logo=github&logoColor=white)](geopolitics/brief-generators/geopolitical-brief-generator.md) |  |
| Dec 13 (2024) | Geopolitical Relationship Briefer | [![View on GitHub](https://img.shields.io/badge/View%20on-GitHub-black?style=for-the-badge&logo=github&logoColor=white)](geopolitics/brief-generators/relations-briefer.md) | [![View on Hugging Face](https://img.shields.io/badge/View%20on-Hugging%20Face-ff9b34?style=for-the-badge&logo=huggingface&logoColor=white)](https://hf.co/chat/assistant/675b88ebc00f90d9bde73d4b) |
| Dec 12 (2024) | Geopolitical Scenario Simulator | [![View on GitHub](https://img.shields.io/badge/View%20on-GitHub-black?style=for-the-badge&logo=github&logoColor=white)](geopolitics/simulators/geopolitical-scenario-simulator.md) | [![View on Hugging Face](https://img.shields.io/badge/View%20on-Hugging%20Face-ff9b34?style=for-the-badge&logo=huggingface&logoColor=white)](https://hf.co/chat/assistant/6757a6b19370b67839010745) |
| Dec 23 (2024) | Gifted Adult Helper | [![View on GitHub](https://img.shields.io/badge/View%20on-GitHub-black?style=for-the-badge&logo=github&logoColor=white)](health/mental-health/gifted-adult-helper.md) |  |
| Dec 30 (2024) | Gmail Search String Generator | [![View on GitHub](https://img.shields.io/badge/View%20on-GitHub-black?style=for-the-badge&logo=github&logoColor=white)](utilities/gmail-search-string-generator.md) | [![View on Hugging Face](https://img.shields.io/badge/View%20on-Hugging%20Face-ff9b34?style=for-the-badge&logo=huggingface&logoColor=white)](https://hf.co/chat/assistant/6772affe64316d25463cfce2) |
| Dec 17 (2024) | Go Sell Yourself! | [![View on GitHub](https://img.shields.io/badge/View%20on-GitHub-black?style=for-the-badge&logo=github&logoColor=white)](career/go-sell-yourself.md) | [![View on Hugging Face](https://img.shields.io/badge/View%20on-Hugging%20Face-ff9b34?style=for-the-badge&logo=huggingface&logoColor=white)](https://hf.co/chat/assistant/6761ea0c90f63f7b682335b1) |
| Nov 26 (2024) | Gpt Prompt Chaining Coach | [![View on GitHub](https://img.shields.io/badge/View%20on-GitHub-black?style=for-the-badge&logo=github&logoColor=white)](prompt-eng/coaches/gpt-prompt-chaining-coach.md) |  |
| Nov 26 (2024) | Gpt Usage Coach | [![View on GitHub](https://img.shields.io/badge/View%20on-GitHub-black?style=for-the-badge&logo=github&logoColor=white)](llms/ideation/gpt-usage-coach.md) |  |
| Nov 26 (2024) | Graph Database Stack Assistant | [![View on GitHub](https://img.shields.io/badge/View%20on-GitHub-black?style=for-the-badge&logo=github&logoColor=white)](data/graph-databases/graph-database-stack-assistant.md) |  |
| Dec 23 (2024) | Grow With My Job | [![View on GitHub](https://img.shields.io/badge/View%20on-GitHub-black?style=for-the-badge&logo=github&logoColor=white)](career/grow-with-my-job.md) | [![View on Hugging Face](https://img.shields.io/badge/View%20on-Hugging%20Face-ff9b34?style=for-the-badge&logo=huggingface&logoColor=white)](https://hf.co/chat/assistant/67697fa57c53eb44ca9008d5) |
| Dec 12 (2024) | Grumpy Llm | [![View on GitHub](https://img.shields.io/badge/View%20on-GitHub-black?style=for-the-badge&logo=github&logoColor=white)](for-fun/grumpy-llm.md) | [![View on Hugging Face](https://img.shields.io/badge/View%20on-Hugging%20Face-ff9b34?style=for-the-badge&logo=huggingface&logoColor=white)](https://hf.co/chat/assistant/6757b7b9a55bdf54377f9b68) |
| Nov 26 (2024) | Help Me Remember That | [![View on GitHub](https://img.shields.io/badge/View%20on-GitHub-black?style=for-the-badge&logo=github&logoColor=white)](organisation/help-me-remember-that.md) |  |
| Nov 26 (2024) | If We Don't Change... | [![View on GitHub](https://img.shields.io/badge/View%20on-GitHub-black?style=for-the-badge&logo=github&logoColor=white)](sustainability/if-we-don't-change....md) |  |
| Dec 13 (2024) | Image Gen Advisor | [![View on GitHub](https://img.shields.io/badge/View%20on-GitHub-black?style=for-the-badge&logo=github&logoColor=white)](llm-tools/image-gen-advisor.md) | [![View on Hugging Face](https://img.shields.io/badge/View%20on-Hugging%20Face-ff9b34?style=for-the-badge&logo=huggingface&logoColor=white)](https://hf.co/chat/assistant/675b78e88892019207cd01ec) |
| Dec 23 (2024) | Image To SQL Query | [![View on GitHub](https://img.shields.io/badge/View%20on-GitHub-black?style=for-the-badge&logo=github&logoColor=white)](data/sql-helpers/image_to_sql_query.md) |  |
| Dec 24 (2024) | Impact bond research assistant | [![View on GitHub](https://img.shields.io/badge/View%20on-GitHub-black?style=for-the-badge&logo=github&logoColor=white)](sustainability/impact-bond-researcher.md) |  |
| Nov 26 (2024) | Improve My Gpt Prompt | [![View on GitHub](https://img.shields.io/badge/View%20on-GitHub-black?style=for-the-badge&logo=github&logoColor=white)](prompt-eng/utilities/improve-my-gpt-prompt.md) |  |
| Nov 26 (2024) | Improve My Script | [![View on GitHub](https://img.shields.io/badge/View%20on-GitHub-black?style=for-the-badge&logo=github&logoColor=white)](development/improve-my-script.md) |  |
| Nov 26 (2024) | In Flight Wifi | [![View on GitHub](https://img.shields.io/badge/View%20on-GitHub-black?style=for-the-badge&logo=github&logoColor=white)](travel/in-flight-wifi.md) |  |
| Nov 26 (2024) | Indian And Nepalese Restaurant Finder | [![View on GitHub](https://img.shields.io/badge/View%20on-GitHub-black?style=for-the-badge&logo=github&logoColor=white)](food-and-drink/indian-and-nepalese-restaurant-finder.md) |  |
| Dec 14 (2024) | Inventory Helper | [![View on GitHub](https://img.shields.io/badge/View%20on-GitHub-black?style=for-the-badge&logo=github&logoColor=white)](organisation/inventory-helper.md) | [![View on Hugging Face](https://img.shields.io/badge/View%20on-Hugging%20Face-ff9b34?style=for-the-badge&logo=huggingface&logoColor=white)](https://hf.co/chat/assistant/675db20e1cb94b2f5a99c110) |
| Dec 12 (2024) | Israel Price Comparison Helper | [![View on GitHub](https://img.shields.io/badge/View%20on-GitHub-black?style=for-the-badge&logo=github&logoColor=white)](shopping/israel-price-comparison-helper.md) | [![View on Hugging Face](https://img.shields.io/badge/View%20on-Hugging%20Face-ff9b34?style=for-the-badge&logo=huggingface&logoColor=white)](https://hf.co/chat/assistant/675b336841cdb0f48acc55cc) |
| Dec 30 (2024) | Israel Shopping Assistant 2 (Price Comparison) | [![View on GitHub](https://img.shields.io/badge/View%20on-GitHub-black?style=for-the-badge&logo=github&logoColor=white)](shopping/israel-shopping-assistant-2.md) | [![View on Hugging Face](https://img.shields.io/badge/View%20on-Hugging%20Face-ff9b34?style=for-the-badge&logo=huggingface&logoColor=white)](https://hf.co/chat/assistant/67729919ce8d9eb5d4da1a2f) |
| Dec 23 (2024) | Israel Sitreps | [![View on GitHub](https://img.shields.io/badge/View%20on-GitHub-black?style=for-the-badge&logo=github&logoColor=white)](geopolitics/brief-generators/sitrep/israel-sitreps.md) |  |
| Dec 12 (2024) | Israel Tech Shopping | [![View on GitHub](https://img.shields.io/badge/View%20on-GitHub-black?style=for-the-badge&logo=github&logoColor=white)](shopping/israel-tech-shopping.md) | [![View on Hugging Face](https://img.shields.io/badge/View%20on-Hugging%20Face-ff9b34?style=for-the-badge&logo=huggingface&logoColor=white)](https://hf.co/chat/assistant/675b2727fbc7dfcdaa9f8e7b) |
| Nov 26 (2024) | Iterative Gpt Suggester | [![View on GitHub](https://img.shields.io/badge/View%20on-GitHub-black?style=for-the-badge&logo=github&logoColor=white)](llms/iterative-gpt-suggester.md) |  |
| Dec 23 (2024) | JSON Natural Language Schema Definition Utility | [![View on GitHub](https://img.shields.io/badge/View%20on-GitHub-black?style=for-the-badge&logo=github&logoColor=white)](data/schema-builders/json.md) | [![View on Hugging Face](https://img.shields.io/badge/View%20on-Hugging%20Face-ff9b34?style=for-the-badge&logo=huggingface&logoColor=white)](https://hf.co/chat/assistant/6769932014a1a00276338470) |
| Dec 23 (2024) | Job Interview Brief Creator | [![View on GitHub](https://img.shields.io/badge/View%20on-GitHub-black?style=for-the-badge&logo=github&logoColor=white)](career/job-hunt-helpers/interview-preparation-helper.md) | [![View on Hugging Face](https://img.shields.io/badge/View%20on-Hugging%20Face-ff9b34?style=for-the-badge&logo=huggingface&logoColor=white)](https://hf.co/chat/assistant/6768b2c72fb5aa29a08237c9) |
| Dec 23 (2024) | Job Performance Coach | [![View on GitHub](https://img.shields.io/badge/View%20on-GitHub-black?style=for-the-badge&logo=github&logoColor=white)](career/job-performance-coach.md) | [![View on Hugging Face](https://img.shields.io/badge/View%20on-Hugging%20Face-ff9b34?style=for-the-badge&logo=huggingface&logoColor=white)](https://hf.co/chat/assistant/676980cfc9f2e60f896faab1) |
| Dec 23 (2024) | Job Search Accountability Partner | [![View on GitHub](https://img.shields.io/badge/View%20on-GitHub-black?style=for-the-badge&logo=github&logoColor=white)](career/job-hunt-helpers/job-search-accountability-partner.md) | [![View on Hugging Face](https://img.shields.io/badge/View%20on-Hugging%20Face-ff9b34?style=for-the-badge&logo=huggingface&logoColor=white)](https://hf.co/chat/assistant/6768a9d54144bd429bbd84a3) |
| Dec 23 (2024) | Just The Code, Please! | [![View on GitHub](https://img.shields.io/badge/View%20on-GitHub-black?style=for-the-badge&logo=github&logoColor=white)](code-gen/just-code-please.md) | [![View on Hugging Face](https://img.shields.io/badge/View%20on-Hugging%20Face-ff9b34?style=for-the-badge&logo=huggingface&logoColor=white)](https://hf.co/chat/assistant/6769a897c39cd38c060cf1db) |
| Dec 29 (2024) | Just The Python, Please (For OpenSUSE Tumbleweed) | [![View on GitHub](https://img.shields.io/badge/View%20on-GitHub-black?style=for-the-badge&logo=github&logoColor=white)](code-gen/just-code-python.md) | [![View on Hugging Face](https://img.shields.io/badge/View%20on-Hugging%20Face-ff9b34?style=for-the-badge&logo=huggingface&logoColor=white)](https://hf.co/chat/assistant/67709be13272931e503e67a9) |
| Dec 29 (2024) | Just The Python, Please (Linux) | [![View on GitHub](https://img.shields.io/badge/View%20on-GitHub-black?style=for-the-badge&logo=github&logoColor=white)](code-gen/just-code-python-for-linux.md) | [![View on Hugging Face](https://img.shields.io/badge/View%20on-Hugging%20Face-ff9b34?style=for-the-badge&logo=huggingface&logoColor=white)](https://hf.co/chat/assistant/67709cb49d17134d370f01d9) |
| Nov 26 (2024) | Keep Me On Time | [![View on GitHub](https://img.shields.io/badge/View%20on-GitHub-black?style=for-the-badge&logo=github&logoColor=white)](organisation/time-management/keep-me-on-time.md) |  |
| Dec 24 (2024) | LLM API Assistant | [![View on GitHub](https://img.shields.io/badge/View%20on-GitHub-black?style=for-the-badge&logo=github&logoColor=white)](llm-tools/llm-api-guide.md) | [![View on Hugging Face](https://img.shields.io/badge/View%20on-Hugging%20Face-ff9b34?style=for-the-badge&logo=huggingface&logoColor=white)](https://hf.co/chat/assistant/676a9047657f53b58a920b52) |
| Dec 23 (2024) | LLM Approach Advisory Tool | [![View on GitHub](https://img.shields.io/badge/View%20on-GitHub-black?style=for-the-badge&logo=github&logoColor=white)](llm-tools/llm-approach-advisor.md) | [![View on Hugging Face](https://img.shields.io/badge/View%20on-Hugging%20Face-ff9b34?style=for-the-badge&logo=huggingface&logoColor=white)](https://hf.co/chat/assistant/676974f97c53eb44ca900776) |
| Dec 23 (2024) | LLM Assistant Configuration Generator | [![View on GitHub](https://img.shields.io/badge/View%20on-GitHub-black?style=for-the-badge&logo=github&logoColor=white)](utilities/assistant-configuration-generator.md) | [![View on Hugging Face](https://img.shields.io/badge/View%20on-Hugging%20Face-ff9b34?style=for-the-badge&logo=huggingface&logoColor=white)](https://hf.co/chat/assistant/6769acce952e0760fd6c8626) |
| Dec 23 (2024) | LLM Augmentation Guide | [![View on GitHub](https://img.shields.io/badge/View%20on-GitHub-black?style=for-the-badge&logo=github&logoColor=white)](llm-tools/llm-augmentation-guide.md) | [![View on Hugging Face](https://img.shields.io/badge/View%20on-Hugging%20Face-ff9b34?style=for-the-badge&logo=huggingface&logoColor=white)](https://hf.co/chat/assistant/6769a552685abc1df63ae00e) |
| Dec 12 (2024) | LLM Background Assistant (Researcher) | [![View on GitHub](https://img.shields.io/badge/View%20on-GitHub-black?style=for-the-badge&logo=github&logoColor=white)](llms/llm-background-assistant.md) | [![View on Hugging Face](https://img.shields.io/badge/View%20on-Hugging%20Face-ff9b34?style=for-the-badge&logo=huggingface&logoColor=white)](https://hf.co/chat/assistant/674d4458a845eb960e0794b3) |
| Dec 23 (2024) | LLM Test Lab (Evaluation Tool) | [![View on GitHub](https://img.shields.io/badge/View%20on-GitHub-black?style=for-the-badge&logo=github&logoColor=white)](llms/evaluation/gpt-test-bench.md) |  |
| Dec 12 (2024) | LLM Use-Case Ideation Bot | [![View on GitHub](https://img.shields.io/badge/View%20on-GitHub-black?style=for-the-badge&logo=github&logoColor=white)](llms/llm-use-case-ideation-bot.md) | [![View on Hugging Face](https://img.shields.io/badge/View%20on-Hugging%20Face-ff9b34?style=for-the-badge&logo=huggingface&logoColor=white)](https://hf.co/chat/assistant/6757b54b097c39b938f2d199) |
| Dec 12 (2024) | LLMs People And Orgs | [![View on GitHub](https://img.shields.io/badge/View%20on-GitHub-black?style=for-the-badge&logo=github&logoColor=white)](llms/llms-people-and-orgs.md) | [![View on Hugging Face](https://img.shields.io/badge/View%20on-Hugging%20Face-ff9b34?style=for-the-badge&logo=huggingface&logoColor=white)](https://hf.co/chat/assistant/6757b68c0ff27103bd871481) |
| Nov 26 (2024) | Late Night Venues | [![View on GitHub](https://img.shields.io/badge/View%20on-GitHub-black?style=for-the-badge&logo=github&logoColor=white)](travel/late-night-venues.md) |  |
| Nov 26 (2024) | Let's Automate This | [![View on GitHub](https://img.shields.io/badge/View%20on-GitHub-black?style=for-the-badge&logo=github&logoColor=white)](productivity/automation/let's-automate-this.md) |  |
| Nov 26 (2024) | Let's Work Remotely! | [![View on GitHub](https://img.shields.io/badge/View%20on-GitHub-black?style=for-the-badge&logo=github&logoColor=white)](productivity/let's-work-remotely!.md) |  |
| Dec 23 (2024) | Life Is A Musical | [![View on GitHub](https://img.shields.io/badge/View%20on-GitHub-black?style=for-the-badge&logo=github&logoColor=white)](for-fun/life-is-a-musical.md) |  |
| Dec 24 (2024) | Linux hardware finder | [![View on GitHub](https://img.shields.io/badge/View%20on-GitHub-black?style=for-the-badge&logo=github&logoColor=white)](shopping/linux-hardware-finder.md) | [![View on Hugging Face](https://img.shields.io/badge/View%20on-Hugging%20Face-ff9b34?style=for-the-badge&logo=huggingface&logoColor=white)](https://hf.co/chat/assistant/676ab15072e9b857f61625da) |
| Dec 12 (2024) | Llm Output Judge | [![View on GitHub](https://img.shields.io/badge/View%20on-GitHub-black?style=for-the-badge&logo=github&logoColor=white)](llms/llm-output-judge.md) | [![View on Hugging Face](https://img.shields.io/badge/View%20on-Hugging%20Face-ff9b34?style=for-the-badge&logo=huggingface&logoColor=white)](https://hf.co/chat/assistant/6757a73c7ab12b601c7fdfa7) |
| Nov 26 (2024) | Location Based Threat Briefer | [![View on GitHub](https://img.shields.io/badge/View%20on-GitHub-black?style=for-the-badge&logo=github&logoColor=white)](preparedness/location-based-threat-briefer.md) |  |
| Nov 26 (2024) | Lousy Pun Joke Generator | [![View on GitHub](https://img.shields.io/badge/View%20on-GitHub-black?style=for-the-badge&logo=github&logoColor=white)](for-fun/lousy-pun-joke-generator.md) |  |
| Nov 26 (2024) | Low Fat Food Options | [![View on GitHub](https://img.shields.io/badge/View%20on-GitHub-black?style=for-the-badge&logo=github&logoColor=white)](health/low-fat-food-options.md) |  |
| Nov 26 (2024) | Luggage Allowance Helper | [![View on GitHub](https://img.shields.io/badge/View%20on-GitHub-black?style=for-the-badge&logo=github&logoColor=white)](travel/luggage-allowance-helper.md) |  |
| Nov 26 (2024) | Media Interview Coach | [![View on GitHub](https://img.shields.io/badge/View%20on-GitHub-black?style=for-the-badge&logo=github&logoColor=white)](professional/pr-and-comms/media-interview-coach.md) |  |
| Dec 24 (2024) | Media Monitoring Assistant | [![View on GitHub](https://img.shields.io/badge/View%20on-GitHub-black?style=for-the-badge&logo=github&logoColor=white)](professional/pr-and-comms/media-monitoring-helper.md) | [![View on Hugging Face](https://img.shields.io/badge/View%20on-Hugging%20Face-ff9b34?style=for-the-badge&logo=huggingface&logoColor=white)](https://hf.co/chat/assistant/676aaed072e9b857f6162534) |
| Nov 26 (2024) | Media Monitoring Brief Assistant | [![View on GitHub](https://img.shields.io/badge/View%20on-GitHub-black?style=for-the-badge&logo=github&logoColor=white)](professional/pr-and-comms/media-monitoring-brief-assistant.md) |  |
| Nov 26 (2024) | Media Opportunity Screener | [![View on GitHub](https://img.shields.io/badge/View%20on-GitHub-black?style=for-the-badge&logo=github&logoColor=white)](professional/pr-and-comms/media-opportunity-screener.md) |  |
| Dec 23 (2024) | Media Outreach Assistant | [![View on GitHub](https://img.shields.io/badge/View%20on-GitHub-black?style=for-the-badge&logo=github&logoColor=white)](professional/pr-and-comms/media-outreach-assistant.md) |  |
| Dec 23 (2024) | Media Source Background Checker | [![View on GitHub](https://img.shields.io/badge/View%20on-GitHub-black?style=for-the-badge&logo=github&logoColor=white)](research/media-source-background-checker.md) | [![View on Hugging Face](https://img.shields.io/badge/View%20on-Hugging%20Face-ff9b34?style=for-the-badge&logo=huggingface&logoColor=white)](https://hf.co/chat/assistant/6769b2f6952e0760fd6c86f2) |
| Dec 23 (2024) | Medieval Text Generation Assistant | [![View on GitHub](https://img.shields.io/badge/View%20on-GitHub-black?style=for-the-badge&logo=github&logoColor=white)](writing/jokes/medieval-english-text-generator.md) |  |
| Nov 26 (2024) | Meeting Agenda Assistant | [![View on GitHub](https://img.shields.io/badge/View%20on-GitHub-black?style=for-the-badge&logo=github&logoColor=white)](professional/meeting-organisers/meeting-agenda-assistant.md) |  |
| Dec 23 (2024) | Meeting Minutes Creator (V2) | [![View on GitHub](https://img.shields.io/badge/View%20on-GitHub-black?style=for-the-badge&logo=github&logoColor=white)](professional/meeting-organisers/minutes-creator-v2.md) | [![View on Hugging Face](https://img.shields.io/badge/View%20on-Hugging%20Face-ff9b34?style=for-the-badge&logo=huggingface&logoColor=white)](https://hf.co/chat/assistant/6768a645802ca8f9d460007e) |
| Nov 26 (2024) | Meeting Minutes Recorder | [![View on GitHub](https://img.shields.io/badge/View%20on-GitHub-black?style=for-the-badge&logo=github&logoColor=white)](professional/meeting-organisers/meeting-minutes-recorder.md) |  |
| Dec 23 (2024) | Meeting Preparation Assistant (Participant Researcher) | [![View on GitHub](https://img.shields.io/badge/View%20on-GitHub-black?style=for-the-badge&logo=github&logoColor=white)](professional/meeting-organisers/meeting-briefer.md) | [![View on Hugging Face](https://img.shields.io/badge/View%20on-Hugging%20Face-ff9b34?style=for-the-badge&logo=huggingface&logoColor=white)](https://hf.co/chat/assistant/6768b0d4c39cd38c060cd37f) |
| Dec 31 (2024) | Microphone Purchasing Assistant | [![View on GitHub](https://img.shields.io/badge/View%20on-GitHub-black?style=for-the-badge&logo=github&logoColor=white)](shopping/microphone-finder.md) | [![View on Hugging Face](https://img.shields.io/badge/View%20on-Hugging%20Face-ff9b34?style=for-the-badge&logo=huggingface&logoColor=white)](https://hf.co/chat/assistant/6773305f34099d98d008e9e6) |
| Dec 12 (2024) | Monetised emissions data retrieval genie (Eco Ninja 3) | [![View on GitHub](https://img.shields.io/badge/View%20on-GitHub-black?style=for-the-badge&logo=github&logoColor=white)](data/data-discovery/eco-ninja3.md) | [![View on Hugging Face](https://img.shields.io/badge/View%20on-Hugging%20Face-ff9b34?style=for-the-badge&logo=huggingface&logoColor=white)](https://hf.co/chat/assistant/674dfb83203be059afb0da43) |
| Dec 17 (2024) | Narcissistic & Emotional Abuse: Gaslighting Recognition Coach | [![View on GitHub](https://img.shields.io/badge/View%20on-GitHub-black?style=for-the-badge&logo=github&logoColor=white)](health/mental-health/degaslighting-trainer.md) | [![View on Hugging Face](https://img.shields.io/badge/View%20on-Hugging%20Face-ff9b34?style=for-the-badge&logo=huggingface&logoColor=white)](https://hf.co/chat/assistant/676194d0848a28b678962395) |
| Dec 23 (2024) | Natural Language Schema Definition Utility: CSV | [![View on GitHub](https://img.shields.io/badge/View%20on-GitHub-black?style=for-the-badge&logo=github&logoColor=white)](data/schema-builders/csv.md) | [![View on Hugging Face](https://img.shields.io/badge/View%20on-Hugging%20Face-ff9b34?style=for-the-badge&logo=huggingface&logoColor=white)](https://hf.co/chat/assistant/67698f01c9f2e60f896fac8a) |
| Dec 23 (2024) | Natural Language Schema Definition Utility: MongoDB | [![View on GitHub](https://img.shields.io/badge/View%20on-GitHub-black?style=for-the-badge&logo=github&logoColor=white)](data/schema-builders/mongodb.md) | [![View on Hugging Face](https://img.shields.io/badge/View%20on-Hugging%20Face-ff9b34?style=for-the-badge&logo=huggingface&logoColor=white)](https://hf.co/chat/assistant/67698faa28f7b8f9319e1523) |
| Dec 23 (2024) | Natural Language Schema Definition Utility: MySQL | [![View on GitHub](https://img.shields.io/badge/View%20on-GitHub-black?style=for-the-badge&logo=github&logoColor=white)](data/schema-builders/mysql.md) | [![View on Hugging Face](https://img.shields.io/badge/View%20on-Hugging%20Face-ff9b34?style=for-the-badge&logo=huggingface&logoColor=white)](https://hf.co/chat/assistant/6769927e7c53eb44ca900b39) |
| Dec 23 (2024) | Natural Language Schema Definition Utility: Neo4J | [![View on GitHub](https://img.shields.io/badge/View%20on-GitHub-black?style=for-the-badge&logo=github&logoColor=white)](data/schema-builders/neo4j.md) | [![View on Hugging Face](https://img.shields.io/badge/View%20on-Hugging%20Face-ff9b34?style=for-the-badge&logo=huggingface&logoColor=white)](https://hf.co/chat/assistant/67699150d36d646a09336576) |
| Dec 23 (2024) | Natural Language Schema Definition Utility: PostgreSQL | [![View on GitHub](https://img.shields.io/badge/View%20on-GitHub-black?style=for-the-badge&logo=github&logoColor=white)](data/schema-builders/postgres.md) | [![View on Hugging Face](https://img.shields.io/badge/View%20on-Hugging%20Face-ff9b34?style=for-the-badge&logo=huggingface&logoColor=white)](https://hf.co/chat/assistant/676990b9d36d646a09336559) |
| Dec 23 (2024) | Natural Language Schema Definition Utility: SQLite | [![View on GitHub](https://img.shields.io/badge/View%20on-GitHub-black?style=for-the-badge&logo=github&logoColor=white)](data/schema-builders/sqlite.md) | [![View on Hugging Face](https://img.shields.io/badge/View%20on-Hugging%20Face-ff9b34?style=for-the-badge&logo=huggingface&logoColor=white)](https://hf.co/chat/assistant/676992ce1936c35ab02bfa0f) |
| Nov 26 (2024) | New Statistics Locator | [![View on GitHub](https://img.shields.io/badge/View%20on-GitHub-black?style=for-the-badge&logo=github&logoColor=white)](data/data-discovery/new-statistics-locator.md) |  |
| Dec 12 (2024) | Open Data Finder | [![View on GitHub](https://img.shields.io/badge/View%20on-GitHub-black?style=for-the-badge&logo=github&logoColor=white)](data/data-discovery/open-data-finder.md) | [![View on Hugging Face](https://img.shields.io/badge/View%20on-Hugging%20Face-ff9b34?style=for-the-badge&logo=huggingface&logoColor=white)](https://hf.co/chat/assistant/6757ae28097c39b938f2cd7d) |
| Nov 26 (2024) | Opportunities For Comment Pr Assistant | [![View on GitHub](https://img.shields.io/badge/View%20on-GitHub-black?style=for-the-badge&logo=github&logoColor=white)](professional/pr-and-comms/opportunities-for-comment-pr-assistant.md) |  |
| Nov 26 (2024) | Organisation Relationship Finder | [![View on GitHub](https://img.shields.io/badge/View%20on-GitHub-black?style=for-the-badge&logo=github&logoColor=white)](data/data-utilities/organisation-relationship-finder.md) |  |
| Nov 26 (2024) | Personal Conspiracy Theory Generator | [![View on GitHub](https://img.shields.io/badge/View%20on-GitHub-black?style=for-the-badge&logo=github&logoColor=white)](for-fun/personal-conspiracy-theory-generator.md) |  |
| Dec 14 (2024) | Pick An Approach | [![View on GitHub](https://img.shields.io/badge/View%20on-GitHub-black?style=for-the-badge&logo=github&logoColor=white)](llm-tools/pick-an-approach.md) |  |
| Dec 23 (2024) | Postgres Taxonomy Building Assistant | [![View on GitHub](https://img.shields.io/badge/View%20on-GitHub-black?style=for-the-badge&logo=github&logoColor=white)](data/taxonomies/postgres_taxonomy_builder.md) |  |
| Nov 26 (2024) | Preparedness Advisor | [![View on GitHub](https://img.shields.io/badge/View%20on-GitHub-black?style=for-the-badge&logo=github&logoColor=white)](preparedness/preparedness-advisor.md) |  |
| Nov 26 (2024) | Preparedness Brief Creator | [![View on GitHub](https://img.shields.io/badge/View%20on-GitHub-black?style=for-the-badge&logo=github&logoColor=white)](preparedness/preparedness-brief-creator.md) |  |
| Nov 26 (2024) | Preparedness Partner | [![View on GitHub](https://img.shields.io/badge/View%20on-GitHub-black?style=for-the-badge&logo=github&logoColor=white)](preparedness/preparedness-partner.md) |  |
| Dec 23 (2024) | Process Improvement Helper (Tech Oriented) | [![View on GitHub](https://img.shields.io/badge/View%20on-GitHub-black?style=for-the-badge&logo=github&logoColor=white)](productivity/process-improvement.md) | [![View on Hugging Face](https://img.shields.io/badge/View%20on-Hugging%20Face-ff9b34?style=for-the-badge&logo=huggingface&logoColor=white)](https://hf.co/chat/assistant/6769730fc8c3abc5c7a8ecb0) |
| Dec 23 (2024) | Prompt Analyst | [![View on GitHub](https://img.shields.io/badge/View%20on-GitHub-black?style=for-the-badge&logo=github&logoColor=white)](prompt-eng/prompt-analyst.md) | [![View on Hugging Face](https://img.shields.io/badge/View%20on-Hugging%20Face-ff9b34?style=for-the-badge&logo=huggingface&logoColor=white)](https://hf.co/chat/assistant/6769a3553055fc74101476db) |
| Dec 12 (2024) | Prompt Eng Analyser | [![View on GitHub](https://img.shields.io/badge/View%20on-GitHub-black?style=for-the-badge&logo=github&logoColor=white)](llm-tools/prompt-eng-analyser.md) | [![View on Hugging Face](https://img.shields.io/badge/View%20on-Hugging%20Face-ff9b34?style=for-the-badge&logo=huggingface&logoColor=white)](https://hf.co/chat/assistant/675b0992d19467d49184081a) |
| Dec 23 (2024) | Prompt Engineering Digest | [![View on GitHub](https://img.shields.io/badge/View%20on-GitHub-black?style=for-the-badge&logo=github&logoColor=white)](prompt-eng/news-digest/prompt-engineering-digest.md) |  |
| Dec 23 (2024) | Prompt Example Addition Tool | [![View on GitHub](https://img.shields.io/badge/View%20on-GitHub-black?style=for-the-badge&logo=github&logoColor=white)](prompt-eng/add-examples.md) | [![View on Hugging Face](https://img.shields.io/badge/View%20on-Hugging%20Face-ff9b34?style=for-the-badge&logo=huggingface&logoColor=white)](https://hf.co/chat/assistant/6769a67bd36d646a09336831) |
| Dec 24 (2024) | Prompt Length Guide | [![View on GitHub](https://img.shields.io/badge/View%20on-GitHub-black?style=for-the-badge&logo=github&logoColor=white)](prompt-eng/prompt-length-guide.md) | [![View on Hugging Face](https://img.shields.io/badge/View%20on-Hugging%20Face-ff9b34?style=for-the-badge&logo=huggingface&logoColor=white)](https://hf.co/chat/assistant/676ac19c72105fc97b441f05) |
| Nov 26 (2024) | Prompt Shortener | [![View on GitHub](https://img.shields.io/badge/View%20on-GitHub-black?style=for-the-badge&logo=github&logoColor=white)](prompt-eng/utilities/prompt-shortener.md) |  |
| Dec 12 (2024) | Prompt To Llm | [![View on GitHub](https://img.shields.io/badge/View%20on-GitHub-black?style=for-the-badge&logo=github&logoColor=white)](llm-tools/prompt-to-llm.md) | [![View on Hugging Face](https://img.shields.io/badge/View%20on-Hugging%20Face-ff9b34?style=for-the-badge&logo=huggingface&logoColor=white)](https://hf.co/chat/assistant/674d7fd13b64184e69e89508) |
| Dec 24 (2024) | Prompt Tokenisation Estimator | [![View on GitHub](https://img.shields.io/badge/View%20on-GitHub-black?style=for-the-badge&logo=github&logoColor=white)](prompt-eng/token-estimator.md) | [![View on Hugging Face](https://img.shields.io/badge/View%20on-Hugging%20Face-ff9b34?style=for-the-badge&logo=huggingface&logoColor=white)](https://hf.co/chat/assistant/676ac05090f98bff93e023ed) |
| Nov 26 (2024) | Pub Agenda Generator | [![View on GitHub](https://img.shields.io/badge/View%20on-GitHub-black?style=for-the-badge&logo=github&logoColor=white)](for-fun/pub-agenda-generator.md) |  |
| Nov 26 (2024) | Pub Crawl Creator | [![View on GitHub](https://img.shields.io/badge/View%20on-GitHub-black?style=for-the-badge&logo=github&logoColor=white)](for-fun/pub-crawl-creator.md) |  |
| Dec 23 (2024) | Purpose | [![View on GitHub](https://img.shields.io/badge/View%20on-GitHub-black?style=for-the-badge&logo=github&logoColor=white)](ai-related/ai-could-help-here.md) |  |
| Dec 23 (2024) | Python GUI Generation Assistant | [![View on GitHub](https://img.shields.io/badge/View%20on-GitHub-black?style=for-the-badge&logo=github&logoColor=white)](code-gen/python-generator.md) | [![View on Hugging Face](https://img.shields.io/badge/View%20on-Hugging%20Face-ff9b34?style=for-the-badge&logo=huggingface&logoColor=white)](https://hf.co/chat/assistant/6769aa11c39cd38c060cf20a) |
| Nov 26 (2024) | Quick Email Template Generator | [![View on GitHub](https://img.shields.io/badge/View%20on-GitHub-black?style=for-the-badge&logo=github&logoColor=white)](writing/quick-email-template-generator.md) |  |
| Dec 23 (2024) | Quick Statistic Checker | [![View on GitHub](https://img.shields.io/badge/View%20on-GitHub-black?style=for-the-badge&logo=github&logoColor=white)](research/stat-checker.md) | [![View on Hugging Face](https://img.shields.io/badge/View%20on-Hugging%20Face-ff9b34?style=for-the-badge&logo=huggingface&logoColor=white)](https://hf.co/chat/assistant/6769b1543f41e5999813ad25) |
| Dec 17 (2024) | Random AI Assistant Ideator | [![View on GitHub](https://img.shields.io/badge/View%20on-GitHub-black?style=for-the-badge&logo=github&logoColor=white)](ideation/random-ai-assistant-ideator.md) | [![View on Hugging Face](https://img.shields.io/badge/View%20on-Hugging%20Face-ff9b34?style=for-the-badge&logo=huggingface&logoColor=white)](https://hf.co/chat/assistant/67618e14c43bc16e0532ffd7) |
| Nov 26 (2024) | Random Gpt Suggestion Tool | [![View on GitHub](https://img.shields.io/badge/View%20on-GitHub-black?style=for-the-badge&logo=github&logoColor=white)](llms/random-gpt-suggestion-tool.md) |  |
| Nov 26 (2024) | Recent Documentary Finder | [![View on GitHub](https://img.shields.io/badge/View%20on-GitHub-black?style=for-the-badge&logo=github&logoColor=white)](for-fun/recent-documentary-finder.md) |  |
| Nov 26 (2024) | Recent Report Finder | [![View on GitHub](https://img.shields.io/badge/View%20on-GitHub-black?style=for-the-badge&logo=github&logoColor=white)](sustainability/sustainability-reports/recent-report-finder.md) |  |
| Nov 26 (2024) | Regulation And Policy Comparison Assistant | [![View on GitHub](https://img.shields.io/badge/View%20on-GitHub-black?style=for-the-badge&logo=github&logoColor=white)](research/policy-analysis/regulation-and-policy-comparison-assistant.md) |  |
| Dec 24 (2024) | Remote Friendly Company Finder | [![View on GitHub](https://img.shields.io/badge/View%20on-GitHub-black?style=for-the-badge&logo=github&logoColor=white)](research/career-and-job-hunting/remote-friendly-finder.md) | [![View on Hugging Face](https://img.shields.io/badge/View%20on-Hugging%20Face-ff9b34?style=for-the-badge&logo=huggingface&logoColor=white)](https://hf.co/chat/assistant/676ab52d90f98bff93e020dd) |
| Dec 17 (2024) | Remote Job Identification Tool | [![View on GitHub](https://img.shields.io/badge/View%20on-GitHub-black?style=for-the-badge&logo=github&logoColor=white)](research/career-and-job-hunting/remote-job-profiler.md) | [![View on Hugging Face](https://img.shields.io/badge/View%20on-Hugging%20Face-ff9b34?style=for-the-badge&logo=huggingface&logoColor=white)](https://hf.co/chat/assistant/67618ba28956d493cd64a50e) |
| Dec 24 (2024) | Report Summariser | [![View on GitHub](https://img.shields.io/badge/View%20on-GitHub-black?style=for-the-badge&logo=github&logoColor=white)](research/summarisers/report-summariser.md) | [![View on Hugging Face](https://img.shields.io/badge/View%20on-Hugging%20Face-ff9b34?style=for-the-badge&logo=huggingface&logoColor=white)](https://hf.co/chat/assistant/676aaa9990f98bff93e01dab) |
| Nov 26 (2024) | Research With Python Tutorials Generator | [![View on GitHub](https://img.shields.io/badge/View%20on-GitHub-black?style=for-the-badge&logo=github&logoColor=white)](research/research-with-python-tutorials-generator.md) |  |
| Dec 13 (2024) | Ridiculous Sloth Photo Generator | [![View on GitHub](https://img.shields.io/badge/View%20on-GitHub-black?style=for-the-badge&logo=github&logoColor=white)](image-generation/sloth-guys.md) | [![View on Hugging Face](https://img.shields.io/badge/View%20on-Hugging%20Face-ff9b34?style=for-the-badge&logo=huggingface&logoColor=white)](https://hf.co/chat/assistant/675b750321499ff25259e817) |
| Nov 26 (2024) | Ruggedized Product Finder | [![View on GitHub](https://img.shields.io/badge/View%20on-GitHub-black?style=for-the-badge&logo=github&logoColor=white)](research/purchasing/ruggedized-product-finder.md) |  |
| Dec 23 (2024) | SITREP Creator (General) | [![View on GitHub](https://img.shields.io/badge/View%20on-GitHub-black?style=for-the-badge&logo=github&logoColor=white)](geopolitics/brief-generators/sitrep/sitrep-maker-general.md) | [![View on Hugging Face](https://img.shields.io/badge/View%20on-Hugging%20Face-ff9b34?style=for-the-badge&logo=huggingface&logoColor=white)](https://hf.co/chat/assistant/674d466ea845eb960e079530) |
| Dec 23 (2024) | SQL Data Relationship Helper | [![View on GitHub](https://img.shields.io/badge/View%20on-GitHub-black?style=for-the-badge&logo=github&logoColor=white)](data/sql-helpers/sql-data-relationship-helper.md) |  |
| Dec 23 (2024) | SQL Schema Genie | [![View on GitHub](https://img.shields.io/badge/View%20on-GitHub-black?style=for-the-badge&logo=github&logoColor=white)](data/sql-helpers/schema-genie.md) |  |
| Dec 23 (2024) | Salary Research Sidekick | [![View on GitHub](https://img.shields.io/badge/View%20on-GitHub-black?style=for-the-badge&logo=github&logoColor=white)](career/job-hunt-helpers/salary-research-sidekick.md) | [![View on Hugging Face](https://img.shields.io/badge/View%20on-Hugging%20Face-ff9b34?style=for-the-badge&logo=huggingface&logoColor=white)](https://hf.co/chat/assistant/6768b4b7c8c3abc5c7a8d60a) |
| Nov 26 (2024) | Self Hosted Tech Finder | [![View on GitHub](https://img.shields.io/badge/View%20on-GitHub-black?style=for-the-badge&logo=github&logoColor=white)](tech-general/self-hosted-tech-finder.md) |  |
| Dec 23 (2024) | Sensory Processing Support Assistance Tool | [![View on GitHub](https://img.shields.io/badge/View%20on-GitHub-black?style=for-the-badge&logo=github&logoColor=white)](health/mental-health/sensory-support-gpt.md) |  |
| Dec 24 (2024) | Sloth Metaphor Explainer | [![View on GitHub](https://img.shields.io/badge/View%20on-GitHub-black?style=for-the-badge&logo=github&logoColor=white)](for-fun/sloth-metaphor-explainer.md) | [![View on Hugging Face](https://img.shields.io/badge/View%20on-Hugging%20Face-ff9b34?style=for-the-badge&logo=huggingface&logoColor=white)](https://hf.co/chat/assistant/676ab7d57d4a0c8650556475) |
| Dec 23 (2024) | Snippet for configuring voice-centric assistants | [![View on GitHub](https://img.shields.io/badge/View%20on-GitHub-black?style=for-the-badge&logo=github&logoColor=white)](snippets/voice-preface.md) |  |
| Dec 13 (2024) | Spot The Llm | [![View on GitHub](https://img.shields.io/badge/View%20on-GitHub-black?style=for-the-badge&logo=github&logoColor=white)](llm-tools/spot-the-llm.md) | [![View on Hugging Face](https://img.shields.io/badge/View%20on-Hugging%20Face-ff9b34?style=for-the-badge&logo=huggingface&logoColor=white)](https://hf.co/chat/assistant/675c5c9b7b4e71b47969538e) |
| Dec 23 (2024) | Stack Research Prompt | [![View on GitHub](https://img.shields.io/badge/View%20on-GitHub-black?style=for-the-badge&logo=github&logoColor=white)](llm-tools/prompt-creation-assistants/stack-research-prompt.md) | [![View on Hugging Face](https://img.shields.io/badge/View%20on-Hugging%20Face-ff9b34?style=for-the-badge&logo=huggingface&logoColor=white)](https://hf.co/chat/assistant/6759f22de2c6caf4b22afa82) |
| Dec 24 (2024) | Sustainability Data Gathering Assistant | [![View on GitHub](https://img.shields.io/badge/View%20on-GitHub-black?style=for-the-badge&logo=github&logoColor=white)](sustainability/data-discovery/sustainability-data.md) | [![View on Hugging Face](https://img.shields.io/badge/View%20on-Hugging%20Face-ff9b34?style=for-the-badge&logo=huggingface&logoColor=white)](https://hf.co/chat/assistant/676aff1371e0f0e07689ad1e) |
| Dec 24 (2024) | Sustainability Linked Bonds And Loans Research Assistant | [![View on GitHub](https://img.shields.io/badge/View%20on-GitHub-black?style=for-the-badge&logo=github&logoColor=white)](sustainability/slbs-and-slls.md) | [![View on Hugging Face](https://img.shields.io/badge/View%20on-Hugging%20Face-ff9b34?style=for-the-badge&logo=huggingface&logoColor=white)](https://hf.co/chat/assistant/676aa8e2f5594e37952a01c3) |
| Dec 24 (2024) | Sustainability News Digest (Finance) | [![View on GitHub](https://img.shields.io/badge/View%20on-GitHub-black?style=for-the-badge&logo=github&logoColor=white)](sustainability/recent-news-digest.md) | [![View on Hugging Face](https://img.shields.io/badge/View%20on-Hugging%20Face-ff9b34?style=for-the-badge&logo=huggingface&logoColor=white)](https://hf.co/chat/assistant/676aafaf589078e4a21a322f) |
| Dec 24 (2024) | Sustainability Regulation Guide | [![View on GitHub](https://img.shields.io/badge/View%20on-GitHub-black?style=for-the-badge&logo=github&logoColor=white)](sustainability/sustainability-regulation.md) | [![View on Hugging Face](https://img.shields.io/badge/View%20on-Hugging%20Face-ff9b34?style=for-the-badge&logo=huggingface&logoColor=white)](https://hf.co/chat/assistant/676abf0ccfc381aec6cba726) |
| Nov 26 (2024) | Sustainability Report Finder | [![View on GitHub](https://img.shields.io/badge/View%20on-GitHub-black?style=for-the-badge&logo=github&logoColor=white)](sustainability/sustainability-reports/sustainability-report-finder.md) |  |
| Nov 26 (2024) | Sustainable Living Advisor | [![View on GitHub](https://img.shields.io/badge/View%20on-GitHub-black?style=for-the-badge&logo=github&logoColor=white)](sustainability/advisory/sustainable-living-advisor.md) |  |
| Dec 20 (2024) | Synthetic Data Generation Assistant | [![View on GitHub](https://img.shields.io/badge/View%20on-GitHub-black?style=for-the-badge&logo=github&logoColor=white)](cybersecurity/synthetic-pii-creator.md) | [![View on Hugging Face](https://img.shields.io/badge/View%20on-Hugging%20Face-ff9b34?style=for-the-badge&logo=huggingface&logoColor=white)](https://hf.co/chat/assistant/676582eb67886299fb855408) |
| Dec 25 (2024) | TL:DR Email Rewriter | [![View on GitHub](https://img.shields.io/badge/View%20on-GitHub-black?style=for-the-badge&logo=github&logoColor=white)](writing/email-assistants/tldr-email-rewriter.md) | [![View on Hugging Face](https://img.shields.io/badge/View%20on-Hugging%20Face-ff9b34?style=for-the-badge&logo=huggingface&logoColor=white)](https://hf.co/chat/assistant/676c5569238681ef0d823bb3) |
| Nov 26 (2024) | Taxonomy And Category Builder | [![View on GitHub](https://img.shields.io/badge/View%20on-GitHub-black?style=for-the-badge&logo=github&logoColor=white)](data/taxonomies/taxonomy-and-category-builder.md) |  |
| Dec 12 (2024) | Taxonomy Ideation Wizard | [![View on GitHub](https://img.shields.io/badge/View%20on-GitHub-black?style=for-the-badge&logo=github&logoColor=white)](data/taxonomies/taxonomy-ideation-tool.md) | [![View on Hugging Face](https://img.shields.io/badge/View%20on-Hugging%20Face-ff9b34?style=for-the-badge&logo=huggingface&logoColor=white)](https://hf.co/chat/assistant/6701e018cb513bb057ded466) |
| Dec 23 (2024) | Tech Courses and Certs ... Advisory Tool | [![View on GitHub](https://img.shields.io/badge/View%20on-GitHub-black?style=for-the-badge&logo=github&logoColor=white)](research/courses-and-certs.md) | [![View on Hugging Face](https://img.shields.io/badge/View%20on-Hugging%20Face-ff9b34?style=for-the-badge&logo=huggingface&logoColor=white)](https://hf.co/chat/assistant/676983f0b6426161b4ba2caf) |
| Nov 26 (2024) | Tech Improvement Guide | [![View on GitHub](https://img.shields.io/badge/View%20on-GitHub-black?style=for-the-badge&logo=github&logoColor=white)](tech-general/tech-improvement-guide.md) |  |
| Nov 26 (2024) | Tech Product Finder | [![View on GitHub](https://img.shields.io/badge/View%20on-GitHub-black?style=for-the-badge&logo=github&logoColor=white)](research/tech-product-finder.md) |  |
| Dec 23 (2024) | Tech Stack Evaluation Assistant | [![View on GitHub](https://img.shields.io/badge/View%20on-GitHub-black?style=for-the-badge&logo=github&logoColor=white)](research/tech-spec-assistant.md) | [![View on Hugging Face](https://img.shields.io/badge/View%20on-Hugging%20Face-ff9b34?style=for-the-badge&logo=huggingface&logoColor=white)](https://hf.co/chat/assistant/6768c7c97baf7ae121bfcf7a) |
| Nov 26 (2024) | Tech Stack Optimizer | [![View on GitHub](https://img.shields.io/badge/View%20on-GitHub-black?style=for-the-badge&logo=github&logoColor=white)](tech-general/tech-stack-optimizer.md) |  |
| Nov 26 (2024) | Text Fixer (british_english) | [![View on GitHub](https://img.shields.io/badge/View%20on-GitHub-black?style=for-the-badge&logo=github&logoColor=white)](writing/text-fixer-(british_english).md) |  |
| Dec 23 (2024) | Text To Video Prompt | [![View on GitHub](https://img.shields.io/badge/View%20on-GitHub-black?style=for-the-badge&logo=github&logoColor=white)](llm-tools/prompt-creation-assistants/text-to-video-prompt.md) | [![View on Hugging Face](https://img.shields.io/badge/View%20on-Hugging%20Face-ff9b34?style=for-the-badge&logo=huggingface&logoColor=white)](https://hf.co/chat/assistant/6759ecd6692d209d580976fe) |
| Nov 26 (2024) | The Checklist Pro | [![View on GitHub](https://img.shields.io/badge/View%20on-GitHub-black?style=for-the-badge&logo=github&logoColor=white)](organisation/the-checklist-pro.md) |  |
| Dec 23 (2024) | The Creativity Coach | [![View on GitHub](https://img.shields.io/badge/View%20on-GitHub-black?style=for-the-badge&logo=github&logoColor=white)](health/mental-health/the-creativity-coach.md) | [![View on Hugging Face](https://img.shields.io/badge/View%20on-Hugging%20Face-ff9b34?style=for-the-badge&logo=huggingface&logoColor=white)](https://hf.co/chat/assistant/6769a1b63055fc74101476a5) |
| Nov 26 (2024) | The Database Matchmaker | [![View on GitHub](https://img.shields.io/badge/View%20on-GitHub-black?style=for-the-badge&logo=github&logoColor=white)](data/data-architecture/the-database-matchmaker.md) |  |
| Dec 23 (2024) | The Fake Wine Buff | [![View on GitHub](https://img.shields.io/badge/View%20on-GitHub-black?style=for-the-badge&logo=github&logoColor=white)](for-fun/the-fake-wine-buff.md) |  |
| Dec 12 (2024) | The Llm Mimic | [![View on GitHub](https://img.shields.io/badge/View%20on-GitHub-black?style=for-the-badge&logo=github&logoColor=white)](llms/the-llm-mimic.md) | [![View on Hugging Face](https://img.shields.io/badge/View%20on-Hugging%20Face-ff9b34?style=for-the-badge&logo=huggingface&logoColor=white)](https://hf.co/chat/assistant/6757b29b0eb722654f51ac6c) |
| Dec 24 (2024) | The Night Time Forager | [![View on GitHub](https://img.shields.io/badge/View%20on-GitHub-black?style=for-the-badge&logo=github&logoColor=white)](food-and-drink/the-night-time-forager.md) | [![View on Hugging Face](https://img.shields.io/badge/View%20on-Hugging%20Face-ff9b34?style=for-the-badge&logo=huggingface&logoColor=white)](https://hf.co/chat/assistant/676ab9fe7d4a0c865055650a) |
| Dec 23 (2024) | The Postgres Expert | [![View on GitHub](https://img.shields.io/badge/View%20on-GitHub-black?style=for-the-badge&logo=github&logoColor=white)](data/postgres/postgresql-expert.md) |  |
| Dec 12 (2024) | The Postgres Schema Genie | [![View on GitHub](https://img.shields.io/badge/View%20on-GitHub-black?style=for-the-badge&logo=github&logoColor=white)](data/postgres/postgres-schema-coach.md) | [![View on Hugging Face](https://img.shields.io/badge/View%20on-Hugging%20Face-ff9b34?style=for-the-badge&logo=huggingface&logoColor=white)](https://hf.co/chat/assistant/6701e0c3b41b0e86f9d5ad2e) |
| Nov 26 (2024) | The Professional Skeptic | [![View on GitHub](https://img.shields.io/badge/View%20on-GitHub-black?style=for-the-badge&logo=github&logoColor=white)](research/the-professional-skeptic.md) |  |
| Nov 26 (2024) | The Sunrise Riser Sleeping Hours Suggester | [![View on GitHub](https://img.shields.io/badge/View%20on-GitHub-black?style=for-the-badge&logo=github&logoColor=white)](health/the-sunrise-riser-sleeping-hours-suggester.md) |  |
| Nov 26 (2024) | Topic To Subreddit | [![View on GitHub](https://img.shields.io/badge/View%20on-GitHub-black?style=for-the-badge&logo=github&logoColor=white)](research/topic-to-subreddit.md) |  |
| Dec 15 (2024) | Toxic Email Parser | [![View on GitHub](https://img.shields.io/badge/View%20on-GitHub-black?style=for-the-badge&logo=github&logoColor=white)](health/mental-health/toxic-email-parser.md) | [![View on Hugging Face](https://img.shields.io/badge/View%20on-Hugging%20Face-ff9b34?style=for-the-badge&logo=huggingface&logoColor=white)](https://hf.co/chat/assistant/675ecf4241db734868f0c1e0) |
| Nov 26 (2024) | Travel Prep Pro | [![View on GitHub](https://img.shields.io/badge/View%20on-GitHub-black?style=for-the-badge&logo=github&logoColor=white)](travel/travel-prep-pro.md) |  |
| Dec 23 (2024) | True Story Movie & Documentary Finder | [![View on GitHub](https://img.shields.io/badge/View%20on-GitHub-black?style=for-the-badge&logo=github&logoColor=white)](entertainment/true-story-movie-recommender.md) | [![View on Hugging Face](https://img.shields.io/badge/View%20on-Hugging%20Face-ff9b34?style=for-the-badge&logo=huggingface&logoColor=white)](https://hf.co/chat/assistant/67699f75890c7f9b0d6d903a) |
| Dec 23 (2024) | Tumbleweed Troubleshooter (KDE Plasma) | [![View on GitHub](https://img.shields.io/badge/View%20on-GitHub-black?style=for-the-badge&logo=github&logoColor=white)](tech-support/tumbleweed-helper.md) | [![View on Hugging Face](https://img.shields.io/badge/View%20on-Hugging%20Face-ff9b34?style=for-the-badge&logo=huggingface&logoColor=white)](https://hf.co/chat/assistant/6769aaf3384ae3573032ba71) |
| Dec 23 (2024) | Typo Master | [![View on GitHub](https://img.shields.io/badge/View%20on-GitHub-black?style=for-the-badge&logo=github&logoColor=white)](writing/jokes/typo-master.md) |  |
| Dec 23 (2024) | UI Improvement Tool (Python/Bash) | [![View on GitHub](https://img.shields.io/badge/View%20on-GitHub-black?style=for-the-badge&logo=github&logoColor=white)](code-gen/ui-improver.md) | [![View on Hugging Face](https://img.shields.io/badge/View%20on-Hugging%20Face-ff9b34?style=for-the-badge&logo=huggingface&logoColor=white)](https://hf.co/chat/assistant/6769a774890c7f9b0d6d913e) |
| Dec 23 (2024) | VS Code -> Markdown Formatter | [![View on GitHub](https://img.shields.io/badge/View%20on-GitHub-black?style=for-the-badge&logo=github&logoColor=white)](text-formatting/vscode-to-markdown.md) |  |
| Nov 26 (2024) | Vacation Doomsday Prepper | [![View on GitHub](https://img.shields.io/badge/View%20on-GitHub-black?style=for-the-badge&logo=github&logoColor=white)](for-fun/vacation-doomsday-prepper.md) |  |
| Dec 12 (2024) | View on Hugging Face Markdown badge generator | [![View on GitHub](https://img.shields.io/badge/View%20on-GitHub-black?style=for-the-badge&logo=github&logoColor=white)](utilities/view-on-hf-badges.md) | [![View on Hugging Face](https://img.shields.io/badge/View%20on-Hugging%20Face-ff9b34?style=for-the-badge&logo=huggingface&logoColor=white)](https://hf.co/chat/assistant/6759f095fa3a18005bba7d2e) |
| Dec 23 (2024) | Voice Assistant Configuration Helper | [![View on GitHub](https://img.shields.io/badge/View%20on-GitHub-black?style=for-the-badge&logo=github&logoColor=white)](llm-tools/voice-helpers/voice-config-helper.md) | [![View on Hugging Face](https://img.shields.io/badge/View%20on-Hugging%20Face-ff9b34?style=for-the-badge&logo=huggingface&logoColor=white)](https://hf.co/chat/assistant/6768a167612c984fd47e5024) |
| Nov 26 (2024) | Voice Mode Mentor | [![View on GitHub](https://img.shields.io/badge/View%20on-GitHub-black?style=for-the-badge&logo=github&logoColor=white)](productivity/voice-mode/voice-mode-mentor.md) |  |
| Dec 23 (2024) | Voice Note Journalling Assistant | [![View on GitHub](https://img.shields.io/badge/View%20on-GitHub-black?style=for-the-badge&logo=github&logoColor=white)](writing/voice-note-helper.md) | [![View on Hugging Face](https://img.shields.io/badge/View%20on-Hugging%20Face-ff9b34?style=for-the-badge&logo=huggingface&logoColor=white)](https://hf.co/chat/assistant/67697bd73f41e5999813a5dc) |
| Dec 23 (2024) | Voice Prompt Refiner | [![View on GitHub](https://img.shields.io/badge/View%20on-GitHub-black?style=for-the-badge&logo=github&logoColor=white)](llm-tools/voice-helpers/voice-prompt-refiner.md) | [![View on Hugging Face](https://img.shields.io/badge/View%20on-Hugging%20Face-ff9b34?style=for-the-badge&logo=huggingface&logoColor=white)](https://hf.co/chat/assistant/6759efc2fa3a18005bba7cee) |
| Dec 12 (2024) | Voice To Text | [![View on GitHub](https://img.shields.io/badge/View%20on-GitHub-black?style=for-the-badge&logo=github&logoColor=white)](shopping/voice-to-text.md) | [![View on Hugging Face](https://img.shields.io/badge/View%20on-Hugging%20Face-ff9b34?style=for-the-badge&logo=huggingface&logoColor=white)](https://hf.co/chat/assistant/675b0be7be9adaf5257b7f94) |
| Dec 23 (2024) | Weekly Work Planner | [![View on GitHub](https://img.shields.io/badge/View%20on-GitHub-black?style=for-the-badge&logo=github&logoColor=white)](organisation/workflow-planners/weekly-work-planner.md) |  |
| Nov 26 (2024) | Weekly Workflow Planning Assistant | [![View on GitHub](https://img.shields.io/badge/View%20on-GitHub-black?style=for-the-badge&logo=github&logoColor=white)](organisation/workflow-planners/weekly-workflow-planning-assistant.md) |  |
| Dec 23 (2024) | What's At This Domain? | [![View on GitHub](https://img.shields.io/badge/View%20on-GitHub-black?style=for-the-badge&logo=github&logoColor=white)](utilities/what's-at-this-domain.md) |  |
| Nov 26 (2024) | Who's This Person | [![View on GitHub](https://img.shields.io/badge/View%20on-GitHub-black?style=for-the-badge&logo=github&logoColor=white)](utilities/who's-this-person.md) |  |
| Dec 23 (2024) | Workspace Ergonomics Assistant (Vision Required) | [![View on GitHub](https://img.shields.io/badge/View%20on-GitHub-black?style=for-the-badge&logo=github&logoColor=white)](utilities/ergonomic-evaulation-assistant.md) | [![View on Hugging Face](https://img.shields.io/badge/View%20on-Hugging%20Face-ff9b34?style=for-the-badge&logo=huggingface&logoColor=white)](https://hf.co/chat/assistant/6768bae1cfb5f6f6033e63f9) |
| Nov 26 (2024) | Worst Eats Guide | [![View on GitHub](https://img.shields.io/badge/View%20on-GitHub-black?style=for-the-badge&logo=github&logoColor=white)](food-and-drink/worst-eats-guide.md) |  |
| Dec 23 (2024) | Ye Olde Text Converter | [![View on GitHub](https://img.shields.io/badge/View%20on-GitHub-black?style=for-the-badge&logo=github&logoColor=white)](writing/jokes/ye-olde-text-converter.md) |  |

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
 
A quick note about the use of pronouns in these configuration texts. 

When rising configuration text for large language model assistants it is extremely important to be as precise and non confusing as possible. 

Gender politics are, of course, highly topical these days. But even before that was the case, it would be odd to simply assume a gender in a chatbot. 

For the vast majority of interactions, however, I expect that the chat bot is going to be interacting with the user in the second person ie addressing it as "you". Therefore, in the interest of minimizing the possibility for confusion when writing configurations, I identified the user was the pronoun "he" while fully knowing And appreciating that the user the assistant will likely be helping may be a "he", a "she", or somebody identifying by another gender pronoun. Sometimes I will use "the user" rather than he. Generally, however, my choice of words is decided by whatever seems most natural when I'm drafting that particular configuration. 

Please understand that the configuration texts are worded thusly solely for this reason/

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

## Total Count

| Metric                  | Count |
|-------------------------|-------|
| Total Assistants        | 204 |
| Total on Hugging Face   | 80 |

## Total Count

| Metric | Count |
|-------------------------|-------|
| Total Assistants | 209 |
| Total on Hugging Face | 90 |

## Total Count

| Metric | Count |
|-------------------------|-------|
| Total Assistants | 209 |
| Total on Hugging Face | 90 |

## Total Count

| Metric | Count |
|-------------------------|-------|
| Total Assistants | 207 |
| Total on Hugging Face | 90 |

## Total Count

| Metric | Count |
|-------------------------|-------|
| Total Assistants | 207 |
| Total on Hugging Face | 90 |

## Total Count

| Metric | Count |
|-------------------------|-------|
| Total Assistants | 207 |
| Total on Hugging Face | 95 |

## Total Count

| Metric | Count |
|-------------------------|-------|
| Total Assistants | 207 |
| Total on Hugging Face | 95 |

## Total Count

| Metric | Count |
|-------------------------|-------|
| Total Assistants | 207 |
| Total on Hugging Face | 98 |

## Total Count

| Metric | Count |
|-------------------------|-------|
| Total Assistants | 207 |
| Total on Hugging Face | 99 |

## Total Count

| Metric | Count |
|-------------------------|-------|
| Total Assistants | 206 |
| Total on Hugging Face | 103 |

## Total Count

| Metric | Count |
|-------------------------|-------|
| Total Assistants | 206 |
| Total on Hugging Face | 104 |

## Total Count

| Metric | Count |
|-------------------------|-------|
| Total Assistants | 207 |
| Total on Hugging Face | 105 |

## Total Count

| Metric | Count |
|-------------------------|-------|
| Total Assistants | 211 |
| Total on Hugging Face | 109 |

## Total Count

| Metric | Count |
|-------------------------|-------|
| Total Assistants | 213 |
| Total on Hugging Face | 111 |

## Total Count

| Metric | Count |
|-------------------------|-------|
| Total Assistants | 214 |
| Total on Hugging Face | 112 |

## Total Count

| Metric | Count |
|-------------------------|-------|
| Total Assistants | 215 |
| Total on Hugging Face | 113 |

## Total Count

| Metric | Count |
|-------------------------|-------|
| Total Assistants | 215 |
| Total on Hugging Face | 113 |

## Total Count

| Metric | Count |
|-------------------------|-------|
| Total Assistants | 218 |
| Total on Hugging Face | 114 |

## Total Count

| Metric | Count |
|-------------------------|-------|
| Total Assistants | 219 |
| Total on Hugging Face | 115 |

## Total Count

| Metric | Count |
|-------------------------|-------|
| Total Assistants | 219 |
| Total on Hugging Face | 115 |

## Total Count

| Metric | Count |
|-------------------------|-------|
| Total Assistants | 220 |
| Total on Hugging Face | 116 |

## Total Count

| Metric | Count |
|-------------------------|-------|
| Total Assistants | 221 |
| Total on Hugging Face | 117 |

## Total Count

| Metric | Count |
|-------------------------|-------|
| Total Assistants | 221 |
| Total on Hugging Face | 118 |

## Total Count

| Metric | Count |
|-------------------------|-------|
| Total Assistants | 222 |
| Total on Hugging Face | 120 |

## Total Count

| Metric | Count |
|-------------------------|-------|
| Total Assistants | 225 |
| Total on Hugging Face | 124 |

## Total Count

| Metric | Count |
|-------------------------|-------|
| Total Assistants | 226 |
| Total on Hugging Face | 125 |

## Total Count

| Metric | Count |
|-------------------------|-------|
| Total Assistants | 228 |
| Total on Hugging Face | 127 |

## Total Count

| Metric | Count |
|-------------------------|-------|
| Total Assistants | 230 |
| Total on Hugging Face | 129 |

## Total Count

| Metric | Count |
|-------------------------|-------|
| Total Assistants | 231 |
| Total on Hugging Face | 130 |

## Total Count

| Metric | Count |
|-------------------------|-------|
| Total Assistants | 233 |
| Total on Hugging Face | 132 |

## Total Count

| Metric | Count |
|-------------------------|-------|
| Total Assistants | 234 |
| Total on Hugging Face | 132 |

## Total Count

| Metric | Count |
|-------------------------|-------|
| Total Assistants | 235 |
| Total on Hugging Face | 134 |

## Total Count

| Metric | Count |
|-------------------------|-------|
| Total Assistants | 236 |
| Total on Hugging Face | 135 |

## Total Count

| Metric | Count |
|-------------------------|-------|
| Total Assistants | 237 |
| Total on Hugging Face | 136 |

## Total Count

| Metric | Count |
|-------------------------|-------|
| Total Assistants | 238 |
| Total on Hugging Face | 137 |

## Total Count

| Metric | Count |
|-------------------------|-------|
| Total Assistants | 240 |
| Total on Hugging Face | 139 |

## Total Count

| Metric | Count |
|-------------------------|-------|
| Total Assistants | 242 |
| Total on Hugging Face | 140 |

## Total Count

| Metric | Count |
|-------------------------|-------|
| Total Assistants | 243 |
| Total on Hugging Face | 141 |

## Total Count

| Metric | Count |
|-------------------------|-------|
| Total Assistants | 244 |
| Total on Hugging Face | 142 |

## Total Count

| Metric | Count |
|-------------------------|-------|
| Total Assistants | 245 |
| Total on Hugging Face | 143 |

