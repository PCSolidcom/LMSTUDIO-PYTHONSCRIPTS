# LMSTUDIO-PYTHONSCRIPTS
Scripts to submit prompts to LM Studio via Python script
Once you install LM Studio and run LM Studio, you can go to a command prompt and run this python script and the prompt response will print to screen.  
You can redirect the prompt output to a text file as well using the following format c:\> <Python script name.py> > <Text file output name.txt>, for example c:\> pythonpromptscript.py > lmstudioresponse.txt  (you can monitor the script status by going to LM STUDIO app and going to teh developer tab, and it will show the prompt is processing and a lot of details regarding loading and loading models and VRAM usage, etc.
- The model name, final token total, elapsed time, and tokens/second are listed after each prompt response.  Looks like this: "Model: qwen/qwen3-4b-thinking-2507  | Final tokens: 2531 | elapsed: 163.20s | tokens/sec: 15.51"
- SOUND: Also, this prompt has a short deep sound that plays once each prompt response has been completed.
- USE OF MSWord MERGE NOTE: I use old school method to generate this code using MSWord merge!  
-- I use an excel spreadsheet file with a list of all of the models I want to load and submit the prompts to.
-- Then I use another merge document to merge the model information into a list repeating the model data repeatedly into a list, listing the model name, model number,  model size, and model name,
-- THEN I just paste this merged data into a spreadsheet where I have all of my prompts I want to submit to each model.
-- THEN I merge the final document into this script template, merging the above model info and prompts into the script.
-- The final merge doc info contains the core section of the script, w/ the model name, model number, model size (in gb), prompt number, as well as the  prompt itself.
-- I've generated and submitted  over 100 prompts in a single script file this way with over 30 different models.  The main issues that have arisen is the the computer can run out of RAM and/or VRAM during some of these runs, depending on the prompt length and model settings w/i LM STUDIO.
Working on a more automated script that will pull the model names directly from lm studio using the LMS LM command, as well as the prompt input and output from text files, etc.
If you have any input about any of this, please feel free to send it!
Happy prompting!
Todd
