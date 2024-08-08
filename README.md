# Daniel Rosehill Open Source Custom GPT Library

## About This Repository

This repository contains links to custom GPTs that I have build on top of ChatGPT (*although increasingly I'm exploring the use of other GPTs including Claude*).

I am finding amazing utility in creating custom GPTs for specific purposes (commonly those related to my professional life). 

However, while it lacks the ability of custom GPTs to quickly store detailed contextual information, prompt engineering is often enough to quickly and dramatically accelerate the value yielded from working with GPTs.

The overarching objective is to create a sort of "fleet" of GPT agents to help me manage various aspects of my work and personal lives.

Like everything I open-source, I'm doing so to make a small contribution to the collective sum of human knowledge. If you'd like to use any of these GPTs for whatever reason, you have my full permission to do so.

## Storing Custom GPTs

In day-to-day use, I'm using a system I'm building on top of NocoDB for storing custom GPTs, a prompt library, and a record of GPT outputs.

If you're interested, I'm open-sourcing that project [here](https://github.com/danielrosehill/GPT-Management-System).

This repository operates on a bit of a lag but includes many of the custom GPTs that I use day-to-day.

## File Format

As a best practice, I'm sharing the configurations in `JSON` format.

I'm adding a file called `about.md` which describes the purpose of the individual GPTs.

And then grouping each of these two files into a folder named according to the purpose of the custom GPT.

 ## GPT Self-Optimisation: Snippets

 The ability to use GPT to self-correct its own configuration opens up quite incredible possibilities.

 I've bucketed a few snippets into a prompt snippets folder, but these ones are good enough for most use-cases:

 ### To optimise custom GPT configuration texts, consider running:

 ```
 Please optimise the following configuration script which is intended to create a custom GPT on the ChatGPT platform. 

Please return the optimised version of the configuration text. 
```

### To optimise individual prompts, consider running:

```
Please optimise this prompt so that it produces the most useful output:

[prompt]
```

## Notes On GPT URLs

At the time of writing, OpenAI does not commit to saving users' custom GPTs indefinitely. The current process is that the GPTs may be deactivated if the user changes paying tier. As I don't and can't commit to maintaining a paid subscription indefinitely, it's possible that the URLs will not resolve. The URLs for private GPTs are not shared.

## A Note About Gender Pronouns

To achieve effective outputs with GPTs, concise prompts and configuration texts are advised. In the interest of streamlining generation, I use 'he' as a pronoun to refer to the user. This is simply for pragmatic reasons and should not adversely affect the usability of the GPT for users who identify in other terms.

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
