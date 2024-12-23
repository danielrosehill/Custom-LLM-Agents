# Snippet for configuring voice-centric assistants

The following snippet can be used in order to configure an assistant for a multipart function, the first part of which is an internal parsing process which is intended to clarify the initial information for the next step of the processing. 

I've used variations on this theme in order to explicitly configure assistance to help with generating for example Assistant configurations, which I tell it have been dictated.

My usual formulation is to tell the assistant that the text which the user is going to send is going to have been dictated, and to point out that there is a high chance that it will contain some of the usual deficiencies seen in voice to text dictation, such as typos, lack of punctuation and the presence of characteristic artifacts of speech (like ehm words) which are usually not present when information is typed. 

My reason for including this in many configurations is so that the Assistant can be a bit more aggressive in resolving typos and other obvious flaws in the input text that it might otherwise interpret literally. 

The second reason I do this is to prime the assistant to expect a hands free interaction with the user. Sometimes I'll explicitly state that the user is likely to just provide a stream of text as their input, and you should interpret that as being the initial instruction. 

I do this based on my own experience using voice to text, knowing that when I use dictation the text is simply formatted as a block. But my experience has been that large language models are excellent at interpreting even information like this, presented in a very unideal fashion. 

The chain that I'll use with this snippet is frequently. First understand that the user is dictating and then do something with that text. For example, I've created an assistant that is intended for this voice workflow and then create structured meeting agendas. The first step is to ask the assistant to parse through the text through that prism, and then to go ahead with the formatting instruction, just as if the text had been delivered by text rather than voice dictation. 

## Example Snippet

You should expect that the instruction in which the user delivers will have been transcribed using voice to text software. It is likely to contain typos and lack punctuation. If you can determine with reasonable certainty that any of the instructions were other than those explicitly intended then you should go with the obviously intended instruction rather than that which was transcribed. 

You can expect that the user will be engaging with you in a hands free manner. Therefore, if the user begins the chat by sending in a block of text, you can infer that this is your instruction and you should handle it in accordance with your configuration.  If the user sends a second block of text that is not related to the 1st, then you can interpret this as an overriding instruction and move to this context. 